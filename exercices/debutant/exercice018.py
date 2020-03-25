"""Récuperer un élément sur deux dans une liste
"""

ma_liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
liste_final = [ma_liste[i] for i in range(0, len(ma_liste), 2)]
print(liste_final)

#Solution cours
ma_liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(ma_liste[::2])