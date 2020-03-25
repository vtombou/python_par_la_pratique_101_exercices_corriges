"""Ordonner une chiane de caractère
"""

chaine = "Pierre, Julien, Anne, Marie, Lucien"
chaine = chaine.split(", ")
chaine = sorted(chaine)
chaine = ", ".join(chaine)
print(chaine)