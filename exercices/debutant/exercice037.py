"""Calculer l'âge d'un chien
"""
continue_ = "c"
while(continue_!="q"):
    age = input("Entrez l'âge du chien : ")
    if age.isdigit() :
        age = int(age)
        if age < 0 :
            print("Vous devez entrer un âge positif.")
        elif age < 2 :
            age_human = age*10.5
            print(f"L'âge du chien en âge humain est {age_human}")
        else:
            age_human = 21 + (age-2)*4
            print(f"L'âge du chien en âge humain est {age_human}")
    else :
        continue_=age.lower()