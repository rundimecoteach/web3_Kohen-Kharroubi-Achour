import os
import json
import subprocess
from test_eval import *
import os.path
from os import path

fileOutput = ""


langues = {}
langues["Greek"] = []
langues["English"] = []
langues["Polish"] = []
langues["Russian"] = []
langues["Chinese"] = []
sites = {}

print('script starts...')

with open("doc_lg.json") as json_file:
    data = json.load(json_file)
    for file in data:
        # recuperation de langue et nom de site
        langue = data[file]
        lien = (file.split("_"))[1]

        #que les fichiers trouvés dans le JSON et CleanScrapeBS
        if path.exists("CleanScrapeBS/"+file) :
            open("CleanScrapeBS/"+file,"r",encoding="utf8").read()


            if lien not in langues[langue]:
                langues[langue].append(lien)

            if lien not in sites:
                values = {}
                values["F"] = 0
                values["R"] = 0
                values["P"] = 0
                values["nbPages"] = 0
                sites[lien]=[]
                sites[lien].append(values)


            # calculs F, R et P
            result = evaluate("CleanScrapeBS/"+file,"clean/"+file)

            sites[lien][0]['F'] = sites[lien][0]['F']+result["f-score"]
            sites[lien][0]['R'] = sites[lien][0]['R']+result["recall"]
            sites[lien][0]['P'] = sites[lien][0]['P']+result["precision"]
            sites[lien][0]['nbPages'] = sites[lien][0]['nbPages']+1 #increment du nb de pages pour le site:

# sauvegarder les données dans un fichier JSON
data={}
counter = 0
for langue in langues:
    data[langue]=[]
    counter = 0
    for lien in langues[langue]:
        data[langue].append([lien])
        data[langue][counter].append({
            "F":(sites[lien][0]['F']/sites[lien][0]['nbPages']), #moyenne F
            "R" :(sites[lien][0]['R']/sites[lien][0]['nbPages']), #moyenne R
            "P":(sites[lien][0]['P']/sites[lien][0]['nbPages']) #moyenne P
        })
        counter = counter+1

#sauvegarde des resultats dans un nouveau fichier JSON
with open("FileLinks.json","w") as res:
    json.dump(data,res)


print('script ends...')
