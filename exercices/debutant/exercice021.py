"""Trier une liste de tuples
"""

liste = [("Harry Potter", 5), ("Wall-E", 3), ("Blade Runner", 4)]

liste.sort(key=lambda tuple: tuple[1])

print(liste)