from bs4 import BeautifulSoup
import os

#parcours des fichiers html
for filename in os.listdir("html"):
    print(filename)
    try:
        file = open("html/"+filename,"r", encoding="utf8") 
        soup = BeautifulSoup(file.read(), 'html.parser') #creation objet BS avec contenu du fichier

        #on enleve le contenu des balises script contenant du code js
        for script in soup.find_all('script', src=False):
            script.decompose()

        #creation du fichier de sortie
        output = open("CleanScrapeBS"+"/"+filename,"w",encoding="utf8")
        for i in soup.find_all(recursive = False):
            #on enleve les lignes vides
            items = ' '.join(i.text.split())
            if items != '' :      	
                output.write("\n<p>"+items+"</p>")
        
    except UnicodeDecodeError:
        print("encoding utf8 : "+filename)
