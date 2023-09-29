# Srt Romaji Converter
This python script converts Japanse subtitle file (srt) into romaji (phonetics with alphabet).
Please utilize this script when you need to check the pronounciation of Japanese text.
The generated romaji subtitle file is useful especially for those who haven't mastered Japanese characters.

<br>

![demo-gif](https://github.com/coding-chance/Wanna-Basket/blob/master/image/romaji-srt-converter.gif?raw=true)

<br>

## Prerequisites
To run this script, `Python` needs to be installed on your computer.
If you have not already installed `Python` on your computer, please visit [Doanload Page (Python Official Website)](https://www.python.org/downloads/) to downlaod `Python` for your own computer operating system.

<br>

## Installation & setup

1. Click green `Code` button on this page (github) and click on `Donwload ZIP`
2. Place the downloaded zip file to where you want to save the file, and unzip it
3. Open command line tool ( command prompt or terminal ), and change the directory to the folder where you saved the downloaded code
4. Run `pip install -r requirements.txt` at the root directory of this project

<br>

If `git` is installed on your computer, you can install it as follows
1. Open command line tool (terminal)
2. Navigate to the directory where you want to save the script
3. Run `git clone https://github.com/coding-chance/Easy-Japanese-Extractor`
4. Run `pip install -r requirements.txt`

<br>

## Usage
1. Put your srt file to `input` folder (*Do not put any other file in the folder)
2. Change directory to the root directory of this project(`srt-romaji-converter`) on your teminal
3. Run `python srt-romaji-converter.py`
4. The converted srt file will be saved in `output` folder

If you specify file path to the source srt file with `--input (-i)` flag, the script refers to srt file directly so you don't need to place the srt file under `input` folder. How to specify the file when the the script is executed is as follows.
`python srt-romaji-converter.py --input "file/path/to/subtitle.srt"`

<br>

## Notices 
### for Japanese Teachers
This script generates romaji subtitle using French characters so it contains specific letters like "ï" or "é". This is intended to uniquely denote a correct pronunciation.
In addition, some notations are written differently from the Japanese standard romaji to indicate proper pronunciation. (e.g. R -> L, ch -> tch)

<br>

### for Japanese Learners
Japanese is very hard to master but it got way easier to acquire Japanese skill thanks to the diverse resource, the help of technology. I beliieve now is a great moment to start learning Japanese. I am actually a professional Japanese teacher and I wrote this script to help my students. I hope this script helps you and if you wish, I can share with you lots of learning tips and strategies. Never hesitate to contact me to find out the secret of Japanese learning technics.