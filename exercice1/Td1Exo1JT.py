#!/usr/bin/python   
# -*- coding: utf-8 -*-
import requests
import justext
import glob
from langdetect import detect
import os
import math

def lang_detect(argse):
   switch ={
       "el": "Greek",
       "ru": "Russian",
       "hr": "Croitian",
       "ko": "Korean",
       "pl": "Polish",
       "en": "English",
       "nl": "Dutch",
       "sw": "Swahili",
       "zh_TW": "English",
       "zh-cn": "English",
       "zh": "English",
       "no": "English",
       "da": "Danish",
       "bg": "Bulgarian",
       "fi": "Finnish",
       "lv": "Latvian",
       "sl": "Slovenian",
       "vi": "Vietnamese",
       "mk": "Macedonian",
       "it": "Italian",
       "sv": "Swedish",
       "de": "German",
       "sq": "Albanian"
   }
   return switch.get(argse, "English") 

def read_write_JT():
    for name in glob.glob("html/*"):
        file=open(name, 'r',encoding="utf-8")
        print(name)
        #Detection de langue
        chaine =file.read()
        chaine_JT = justext.justext(chaine, frozenset(), 99, 100, 0.1, 0.32, 0.2, 200, True)[0].text
        chaine_JT
        if len(chaine_JT)<50:
            chaine_JT=chaine
        lang = detect(chaine_JT)
        # print(lang)
        # print(type(lang))
        filename = "CleanScrapeJT/CLEAN_"+name.split("/")[1]
        cleanFile = open(filename, "w+")
        # print(name)
        paragraphs = justext.justext(chaine, justext.get_stoplist(lang_detect(lang)))
        for paragraph in paragraphs:
            if not paragraph.is_boilerplate:
                cleanFile.write(paragraph.text)
        cleanFile.close()
        file.close()

if __name__ == "__main__":
    read_write_JT()