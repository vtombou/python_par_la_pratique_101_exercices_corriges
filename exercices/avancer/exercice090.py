def replace(phrase, mot_a_remplacer, nouveau_mot):
    mots = phrase.split()
    for indice, mot in enumerate(mots) :
        if mot_a_remplacer in mot:
            i = 0
            while i < len(mot):
                try:
                    s = len(mot_a_remplacer) + i
                    if mot[i:s] == mot_a_remplacer :
                        mot = mot[:i] + nouveau_mot + mot[s:]
                        i+= len(mot_a_remplacer)
                        mots[indice] = mot
                    else:
                        i+=1
                except IndexError:
                    print("Out")
                    
        
    return " ".join(mots)

print(replace("bonjour bonjour, mon bon petit", "bon", "soir") )

#Solution Formateur
"""
def replace(phrase, mot_a_remplacer, nouveau_mot):
    while mot_a_remplacer in phrase:
        debut = phrase.index(mot_a_remplacer)
        fin = debut + len(mot_a_remplacer)
 
        phrase = list(phrase)
        phrase[debut:fin] = list(nouveau_mot)
        phrase = "".join(phrase)
 
    return phrase
 
phrase = replace("Mon nom est Bond, James Bond.", "Bond", "Tuche")
"""