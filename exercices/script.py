import os

CURR_DIR = os.path.dirname(__file__)
DOC = os.path.join(CURR_DIR, "intermediaire")
os.makedirs(DOC, exist_ok=True)

for i in range(47, 83):
    fichier = f"exercice0{i}.py"
    DOC_fichier = os.path.join(DOC, fichier)
    with open(DOC_fichier, "w", encoding="utf-8"):
        pass