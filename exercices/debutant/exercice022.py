"""Récuperer une valeur dans un dictionnaire
"""

employes = {"01": {"identite": {"prenom": "Pierre", "nom": "Dupont"}}}
prenom = employes.get("01").get("identite").get("prenom")
print(prenom)