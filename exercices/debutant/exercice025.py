"""Trouver l'erreur de syntaxe
"""
liste = [1, 1, 4, 3, 3, 2, 6, 7, 7, 9, 2]    
resultat = [i*(i+1%(i*5)) for i in sorted(list(set(liste)))]
if __name__ == "__main__":
    print(resultat)