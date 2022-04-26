from deep_translator import GoogleTranslator
import pandas as pd

def make_translation_list(length):
    with open("ko_words.txt",mode="r",encoding="utf8") as ko_file:
        ko_lines_list = ko_file.readlines()
        ko_en_list = ["korean","english"]
        for line in ko_lines_list[0:length]:
            korean_word = line.split()[0]
            english_word = GoogleTranslator(source='ko', target='en').translate(text=f'{korean_word}')
            line_list = [korean_word,english_word]

            ko_en_list.append(line_list)

        df = pd.DataFrame(ko_en_list,columns=["Korean","English"])
        df.to_csv('ko_en_list.csv', index=False) 