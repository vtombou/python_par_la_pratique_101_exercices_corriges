liste = ["Pierre", "Marie", "Julie", "Adrien", "Julie"]
nom_a_chercher = "Julie"
nouveau_nom = "Julien"

i_elt_a_remplacer = [i for i, nom in enumerate(liste) if nom == nom_a_chercher]
for i in i_elt_a_remplacer:
    liste[i]=nouveau_nom
print(liste)

#Solution formateur
liste = [x.replace(nom_a_chercher, nouveau_nom) for x in liste]
print(liste)