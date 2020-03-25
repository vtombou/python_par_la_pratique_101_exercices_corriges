import string
alphabet = string.ascii_lowercase
list_alphabet = [i for i in alphabet]
dic_alphabet = {}
for i, a in enumerate(list_alphabet):
    dic_alphabet[i+1] = a

print(dic_alphabet)