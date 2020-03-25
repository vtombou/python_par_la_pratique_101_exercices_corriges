"""Acceder à une variable d'environnement
"""

import os

env_home = os.environ.get("HOME")
print(env_home)