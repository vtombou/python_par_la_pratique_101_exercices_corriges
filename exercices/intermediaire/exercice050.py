arret, compt = "n", -1

while(arret=="n"):
    compt+=1
    print(f"Le compteur est maintenant à {compt}")
    arret = input("Voulez vous arrêtez ? o/n ").lower()