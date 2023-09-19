import pykakasi
import pysrt
import os
import sys
import datetime

dt_now = datetime.datetime.now()
formatted_time = dt_now.strftime('%Y%m%d_%H%M%S')

# Get file name of srt file
input_dir = "input"
file_names = os.listdir(input_dir)
input_srtname = file_names[0]

# Extract text data from srt file
subs = pysrt.open(f"input/{input_srtname}")
# print(subs)
jp_texts = []
for sub in subs:
    jp_texts.append(sub.text)

# Extract text from txt file
f = open(f"input/{input_srtname}", 'r')
subtitle_lines = f.readlines()

# Convert jp_texts to romaji
kks = pykakasi.kakasi()
romaji_wordlist = []
for jp_word in jp_texts:
    romaji = kks.convert(jp_word)[0]['hepburn']
    romaji_wordlist.append(romaji)

# Convert romaji to original phonetic
complete_phonetics = []
convert_necessity_flag = False
for phonetic in romaji_wordlist:
    replaced_phonetic = phonetic
    # Check if phonetic needs to be converted and convert phonetics
    if phonetic.find('i') != -1 or phonetic.find('e') != -1 or phonetic.find('ch') != -1 or phonetic.find('r') != -1:
        replaced_phonetic = phonetic.replace("i", "ï").replace("e", "é").replace("ch", "tch").replace("r", "l")
        # print(f"Phonetic replaced: {phonetic} -> {replaced_phonetic}")
    complete_phonetics.append(replaced_phonetic)

outputs = []
for index, line in enumerate(subtitle_lines):
    if index == 2 or index % 4 == 2 and index > 2:
        # print(f"index({index})の剰余演算: {index%4} ({complete_phonetics[0]})")
        outputs.append(f"{complete_phonetics[0]}\n")
        complete_phonetics.pop(0)
    else:
        outputs.append(line)
f.close()

# ファイルを srt 形式で出力
with open(f'output/romaji-{input_srtname.split(".")[0]}-{formatted_time}.srt', 'x') as f:
    f.writelines(outputs)