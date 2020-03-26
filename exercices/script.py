import os

CURR_DIR = os.path.dirname(__file__)
DOC = os.path.join(CURR_DIR, "avancer")
os.makedirs(DOC, exist_ok=True)

for i in range(83, 102):
    fichier = "exercice{:03d}.py".format(i)
    DOC_fichier = os.path.join(DOC, fichier)
    with open(DOC_fichier, "w", encoding="utf-8"):
        pass