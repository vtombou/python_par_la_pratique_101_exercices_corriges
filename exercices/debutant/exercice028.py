"""Récuperer l'extension d'un fichier
"""

import os

fichier = "C:/Python36/python.exe"
extension = os.path.splitext(fichier)[-1].split(".")[-1]
print(extension)