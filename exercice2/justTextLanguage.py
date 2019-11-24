import justext
import os
import langid
import sys


#correspondance des langues avec leur code ISO
langues = {}
langues["el"] = "Greek"
langues["en"] = "English"
langues["ru"] = "Russian"
langues["pl"] = "Polish"
langues["zh"] = "English"
langFile = ""


for filename in os.listdir("../html"):
    try:
        file = open("../html/"+filename,"r",encoding="utf8").read()
        #detection de la langue avec langid
        lang = langid.classify(file) 

        langFile = langues[lang[0]] 
        if langFile :
            print(filename+" "+langFile)
            paragraphs = justext.justext(file,justext.get_stoplist(langFile))
            f = open("out/"+filename, "w",encoding="utf8")        
            for paragraph in paragraphs:
                # if not paragraph.is_boilerplate:   
                f.write(paragraph.text)
            f.close()
    except UnicodeDecodeError:
        print("file not utf8 : "+filename)
