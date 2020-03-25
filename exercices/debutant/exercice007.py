"""Vérifier si la variable est d'un certain type
"""

prenom = "Pierre"
 
if type(prenom) == str:
    print("La variable est une chaîne de caractères")
 
prenom = 0
 
if isinstance(prenom, str):
    print("La variable est une chaîne de caractères")