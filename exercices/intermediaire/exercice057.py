nombre = 52039480394023
string_nb = str(nombre)
list_nb = [i for i in string_nb]
list_nb.reverse()
list_mil, i = [], 0
while i < len(list_nb):
    list_mil.append(list_nb[i])
    i+=1
    if i%3 == 0 :
        list_mil.append(",")

list_mil.reverse()
list_mil = "".join(list_mil)
print(list_mil)