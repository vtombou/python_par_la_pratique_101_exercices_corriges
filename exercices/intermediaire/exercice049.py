nombres = [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 7, 8, 9, 10]
new_nombres = []
for i in nombres:
    if i not in new_nombres:
        new_nombres.append(i)

print(new_nombres)
