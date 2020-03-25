employes = {}
liste = [10, 2329, 5, "Pierre", 203, "Marie", 867, "Adrien"]
id = 0
for elt in liste:
    if type(elt) == str:
      id+=1
      new_id = f"id-0{id}"
      employes[new_id] = elt

print(employes)