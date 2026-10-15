print ("=== Vérificateur de mot de passe ===")
mot_de_passe = input("Entre ton mot de passe :")
longueur = len(mot_de_passe)
print(f"Ton mot de passe contient {longueur} caractères.")


if longueur < 8:
    print("Trop court X")
elif longueur < 12:
    print("Correct, ! mais peut mieux fair !")
else: 
    print("Bonne longueur !")


a_majuscule = any(c.isupper() for c in mot_de_passe)
a_minuscule = any(c.islower() for c in mot_de_passe)
a_chiffre = any(c.isdigit() for c in mot_de_passe)
a_symbole = any(not c.isalnum() for c in mot_de_passe)

print(f"Majuscule : {a_majuscule}")
print(f"Minuscule :{a_minuscule}")
print(f"Chiffre : {a_chiffre}")
print(f"symbole : {a_symbole}")

score = 0
if longueur >= 12:
    score += 1
if a_majuscule :
    score += 1
if a_minuscule :
    score += 1 
if a_chiffre :
    score += 1 
if a_symbole :
    score += 1 

print(f"Longueur : {longueur} caractères")
print(f"Note : {score}/5")

if score <= 2:
    print("Verdict : Faible")
elif score <= 4:
    print("Verdict : Moyen")
else:
    print("Verdict : Fort")

if longueur < 12:
    print("Conseil : utilise au moins 12 caractères.")
if not a_symbole:
    print("Conseil: ajoute un symbole (! @ # ...)")