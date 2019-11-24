# -*- coding: utf-8 -*-
import json
import justext
import os
import sys

langue = ""

with open("doc_lg.json") as json_file:
    data = json.load(json_file)
    for filename in data: 

        #extraction de la langue dans le fichier trouvé
        langue = data[filename] 

        if langue == "Chinese": #le chinois n'est pas supporté par justext
            langue = "English"
        
        if os.path.exists("../html/"+filename):
            # print(filename+" : "+langue)
            file = open("../html/"+filename,"r")

            if file != None:
                file = file.read()
                paragraphs = justext.justext(file,justext.get_stoplist(langue))
                f = open("out/"+filename, "w+")

                for paragraph in paragraphs:   
                        f.write(paragraph.text)
                        # print(paragraph.text)
                f.close()