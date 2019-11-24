import glob
import math
import sys

def stats():
    nbFile = 0
    moyennLigne = 0
    nbligne = 0
    ecartTypeLigne = 0
    Ligne = []
    chemin = sys.argv[1]
    for name in glob.glob(chemin+"/*"):
        print(name)
        nbFile+=1
        file = open(name, "r")
        data = file.read()
        number_of_characters = len(data)
        count = 0
        for line in open(name).readlines(  ): count += 1
        print('Le nombre de lignes par fichier', count)
        print('Le nombre de characters par fichier', number_of_characters)
        nbligne+=count
        Ligne.append(count)

    moyennLigne = nbligne/nbFile

    for ligne in Ligne:
        ecartTypeLigne = ecartTypeLigne + pow(ligne-moyennLigne,2)

    ecartTypeLigne = ecartTypeLigne * (1/(nbFile-1))
    ecartTypeLigne = math.sqrt(ecartTypeLigne)

    print("nbLignes : {0}".format(nbligne))
    print("moyennLigne : {0}".format(moyennLigne))
    print("EcartTypeLignes : {0}".format(ecartTypeLigne))
    print('Le nombre de fichiers :', nbFile)
    print('La moyenne de lignes par fichier :', moyennLigne)

if __name__ == "__main__":
    stats()
    