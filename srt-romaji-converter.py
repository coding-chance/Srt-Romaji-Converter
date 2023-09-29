import pysrt
import os
import sys
import datetime
import cutlet
import argparse
from os.path import expanduser

dt_now = datetime.datetime.now()
formatted_time = dt_now.strftime('%Y%m%d_%H%M%S')


# Accept flag
parser = argparse.ArgumentParser(description='Process command line arguments.')
parser.add_argument('-i', '--input', nargs = '*', help='input file path')
args = parser.parse_args()
home_dir = expanduser("~")
project_root_dir = os.path.dirname(os.path.realpath(__file__))
if args.input:
    input_dir_list = args.input[0].split("/")
    input_srtname = input_dir_list.pop()
    input_dir = "/".join(input_dir_list)
    print(f"input_dir: {input_dir}")
    print(f"argument input was found \n -> inputdir: {input_dir}\n -> input_srtname: {input_srtname}")
else:
    input_dir = f"{project_root_dir}/input"
    # Get file name of srt file (ignore files starting with "." like ".DS_Store")
    file_names = os.listdir(input_dir)
    for file in os.listdir(input_dir):
        if not file.startswith('.') and os.path.isfile(os.path.join(input_dir, file)):
            input_srtname = file
    print(f"argument input wasn't found\n -> input_dir: {input_dir}\n -> input_srtname: {input_srtname}")

# Extract text data from srt file
subs = pysrt.open(f"{input_dir}/{input_srtname}")
jp_texts = []
for sub in subs:
    jp_texts.append(sub.text)

# Extract text from txt file
f = open(f"{input_dir}/{input_srtname}", 'r')
subtitle_lines = f.readlines()

# Convert jp_texts to romaji
romaji_converter = cutlet.Cutlet()
romaji_converter.use_foreign_spelling = False

romaji_wordlist = []
for jp_word in jp_texts:
    romaji = romaji_converter.romaji(jp_word)
    romaji_wordlist.append(romaji)

# Convert romaji to original phonetic
complete_phonetics = []
convert_necessity_flag = False
for phonetic in romaji_wordlist:
    replaced_phonetic = phonetic
    # Check if phonetic needs to be converted and convert phonetics
    if phonetic.find('i') != -1 or phonetic.find('e') != -1 or phonetic.find('ch') != -1 or phonetic.find('r') != -1:
        replaced_phonetic = phonetic.replace("watakushi", "watashï").replace("Watakushi", "Watashï").replace("Nippon", "Nihon").replace("i", "ï").replace("I", "Ï").replace("e", "é").replace("E", "É").replace("ch", "tch").replace("Ch", "Tch").replace("r", "l").replace("R", "L")
    complete_phonetics.append(replaced_phonetic)

# Display original sentences and romaji
for index, phonetic in enumerate(complete_phonetics):
    print(f"{jp_texts[index]}")
    print(f"{phonetic}\n")
    

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
output_file_path = f'{project_root_dir}/output/romaji-{input_srtname.split(".")[0]}-{formatted_time}.srt'
with open(output_file_path, 'x') as f:
    f.writelines(outputs)

# Show generated file location
print(f"Romaji conversion process completed. Open the file at\n\n{output_file_path}\n")