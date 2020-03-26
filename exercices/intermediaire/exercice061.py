import os

def remonter_dossier(dossier, niveau):
    while(niveau > 0):
        niveau-=1
        dossier = os.path.dirname(dossier)
    
    return dossier

dossier = "/Users/Thibh/Desktop/Dossier_01/Tutoriel/Udemy"
print(remonter_dossier(dossier, 3))