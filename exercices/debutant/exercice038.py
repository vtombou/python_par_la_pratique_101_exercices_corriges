a = 4
b = 6
c = 2

ens = {a,b,c}
min_1 = min(ens)
ens.discard(min_1)
min_2 = min(ens)
ens.discard(min_2)
min_3 = min(ens)

print("Les nombres dans l'ordre sont {}, {} et {}".format(min_1, min_2, min_3))

#Solution Formateur, very nice 
a1 = min(a, b, c)
a3 = max(a, b, c)
a2 = (a + b + c) - a1 - a3
 
print("Les nombres dans l'ordre sont {}, {} et {}".format(a1, a2, a3))