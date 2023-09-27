import pysrt
import os
import sys
import datetime
import cutlet

dt_now = datetime.datetime.now()
formatted_time = dt_now.strftime('%Y%m%d_%H%M%S')

# Get file name of srt file (ignore files starting with "." like ".DS_Store")
input_dir = "input"
file_names = os.listdir(input_dir)
input_srtname = ""
for file in os.listdir(input_dir):
    if not file.startswith('.') and os.path.isfile(os.path.join(input_dir, file)):
        input_srtname = file
        # print(input_srtname)


# Extract text data from srt file
subs = pysrt.open(f"input/{input_srtname}")
jp_texts = []
for sub in subs:
    jp_texts.append(sub.text)

# Extract text from txt file
f = open(f"input/{input_srtname}", 'r')
subtitle_lines = f.readlines()

# Convert jp_texts to romaji
romaji_converter = cutlet.Cutlet()
romaji_converter.use_foreign_spelling = False

romaji_wordlist = []
for jp_word in jp_texts:
    # romaji = kks.convert(jp_word)[0]['hepburn']
    romaji = romaji_converter.romaji(jp_word)
    romaji_wordlist.append(romaji)

# Convert romaji to original phonetic
complete_phonetics = []
convert_necessity_flag = False
for phonetic in romaji_wordlist:
    replaced_phonetic = phonetic
    # Check if phonetic needs to be converted and convert phonetics
    if phonetic.find('i') != -1 or phonetic.find('e') != -1 or phonetic.find('ch') != -1 or phonetic.find('r') != -1:
        replaced_phonetic = phonetic.replace("watakushi", "watashi").replace("Nippon", "Nihon").replace("i", "ï").replace("I", "Ï").replace("e", "é").replace("E", "É").replace("ch", "tch").replace("Ch", "Tch").replace("r", "l").replace("R", "L")
    complete_phonetics.append(replaced_phonetic)

# Display original sentences and romaji
for index, phonetic in enumerate(complete_phonetics):
    print(f"{jp_texts[index]}")
    print(f"{phonetic}")
    print()
    

# Put together original text and romaji as srt format
outputs = []
for index, line in enumerate(subtitle_lines):
    if index == 2 or index % 4 == 2 and index > 2:
        outputs.append(f"{complete_phonetics[0]}\n")
        complete_phonetics.pop(0)
    else:
        outputs.append(line)

    # if there's no element in complete_phonetics, break the for loop
    if len(complete_phonetics) == 0:
        break
f.close()


# Save file as srt
with open(f'output/romaji-{input_srtname.split(".")[0]}-{formatted_time}.srt', 'x') as f:
    f.writelines(outputs)