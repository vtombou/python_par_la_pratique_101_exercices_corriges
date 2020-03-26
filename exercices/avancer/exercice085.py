import os
import string
 
directory = os.path.dirname(__file__)
alphabet_dir = os.path.join(directory, "alphabet")
 
for lettre in string.ascii_uppercase:
    lettre_dir = os.path.join(alphabet_dir, lettre)
    if not os.path.isdir(lettre_dir):
        os.makedirs(lettre_dir)