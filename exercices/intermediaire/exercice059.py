def somme(a, b):
    min_, max_ = min(a,b), max(a,b) +1
    liste_nombre = [i for i in range(min_, max_)]
    return sum(liste_nombre)

print(somme(2, 6))