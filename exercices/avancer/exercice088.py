def bubble_sort(liste) :
    for i in range(len(liste) -1):
        for j in range(i+1, len(liste)):
            if liste[i] > liste[j] :
                per = liste[i]
                liste[i] = liste[j]
                liste[j] = per

    return liste

l = [40,16,80,2,90]
print(bubble_sort(l))