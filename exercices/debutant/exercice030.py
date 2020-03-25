"""Calculer le temps d'execution d'un script
"""
from time import time

start = time()
_ = [i for i in range(9999999)]
print(f"Temps d'exécution {time() - start}s")