"""Remplacer un mot dans un autre
"""
phrase = "Bonjour tout le monde."
phrase = phrase.split()
phrase[0] = "Bonsoir"
nouvelle_phrase = " ".join(phrase)

print(nouvelle_phrase)