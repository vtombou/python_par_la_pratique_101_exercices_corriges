from datetime import datetime

age = 25
mois_de_naissance = 10

year = datetime.today().year
month = datetime.today().month

year_born = year - age -1 if month < mois_de_naissance else year - age
print(year_born)