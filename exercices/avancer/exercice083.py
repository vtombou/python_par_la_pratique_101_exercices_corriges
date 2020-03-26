def isdigit(nombre):
    if type(nombre) == str :
        for char in nombre :
            try:
                n = int(char)
            except ValueError :
                return False
        return True
    return False

print(isdigit("1854274"))

#Autre posibilité
"""
def isdigit(nombre):
    nombre = nombre.strip("'")
    try:
        nombre = int(nombre)
    except ValueError :
        return False
    else:
        return True

print(isdigit("1854274"))
"""