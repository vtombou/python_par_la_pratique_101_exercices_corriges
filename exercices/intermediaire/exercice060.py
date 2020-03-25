import string

list_employes = ["Vincent", "Jospain", "Yannick", "Carine", "Georges", "Paul", "Julien", "Rose", "Martin", "Sami", "Thierry"]
alphabet = string.ascii_lowercase
milieu = int(len(alphabet)/2)
alphabet_a_m = alphabet[:milieu]
alphabet_n_z = alphabet[milieu:]

employes_a_m, employes_n_z = [], []
for employe in list_employes:
    if employe[0].lower() in alphabet_a_m:
        employes_a_m.append(employe)
    elif employe[0].lower() in alphabet_n_z:
        employes_n_z.append(employe)

print("Employés de A à M:", ", ".join(sorted(employes_a_m)))
print("Employés de N à Z:", ", ".join(sorted(employes_n_z)))