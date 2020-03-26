def recuperer_item(liste, indice):
    if abs(indice)>=0 and abs(indice)<len(liste):
        return liste[indice]
    elif indice < 0 and abs(indice) == len(liste):
        return liste[indice]
    else :
        return "Index {i} hors de la liste".format(i=indice)

liste = ["Julien", "Marie", "Pierre"]

print(recuperer_item(liste, 0))
print(recuperer_item(liste, 5))
print(recuperer_item(liste, -13))