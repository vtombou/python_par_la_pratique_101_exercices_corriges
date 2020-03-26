import os
from glob import glob

CURR_DIR = os.path.dirname(__file__)
DIR_FICHIERS = os.path.join(CURR_DIR, "**", "*.py")
mot_a_chercher = "logging"

fichiers = glob(DIR_FICHIERS, recursive=True)
fichiers_trouves = []

for filename in fichiers :
    with open(filename,"r") as f :
        contenu_fichier = f.read()
        if mot_a_chercher in contenu_fichier :
            fichiers_trouves.append(filename)

print(fichiers_trouves)