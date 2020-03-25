import random

mot = "Bonjour"
list_string = list(mot)
random.shuffle(list_string)
mot="".join(list_string).capitalize()
print(mot)