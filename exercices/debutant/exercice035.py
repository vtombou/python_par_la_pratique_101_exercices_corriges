nombre = 2938.48872
decimales = 3

print("Nombre tronqué: " + str( f"%.{decimales}f"%nombre))


print("Nombre tronqué: {nombre:.{decimales}f}".format(nombre=nombre, decimales=decimales))