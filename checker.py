import hashlib
import urllib.request

def verifier_fuite(mot_de_passe):
    empreinte = hashlib.sha1(mot_de_passe.encode("utf-8")).hexdigest().upper()
    debut = empreinte[:5]
    fin = empreinte[5:]

    url = f"https://api.pwnedpasswords.com/range/{debut}"
    requete = urllib.request.Request(url, headers={"User-Agent": "password-checker"})
    with urllib.request.urlopen(requete) as reponse:
        texte = reponse.read().decode("utf-8")

    for ligne in texte.splitlines():
        suffixe, nombre = ligne.split(":")
        if suffixe == fin:
            return int(nombre)
    return 0


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

print("Recherche dans les fuites de données...")
fuites = verifier_fuite(mot_de_passe)
if fuites > 0:
    print(f"Ce mot de passe apparaît {fuites} fois dans des fuites ! Ne l'utilisez pas !")
else:
    print("Ce mot de passe n'a pas été trouvé dans les fuites de données connues.")

      