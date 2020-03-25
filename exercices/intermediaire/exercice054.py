# Longueur maximale à afficher
n = 8
symbole = '*'
for i in range(1, 16):
    if i <= n :
        print(symbole*i)
    else:
        print(symbole*(2*n -i))


#Solution formateur
nombres = list(range(1, n+1)) + list(range(n-1, 0, -1))
for i in nombres:
    print(symbole*i)