import hashlib
import json
import urllib.request
import urllib.error
import urllib.parse
from getpass import getpass


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


def analyser_mot_de_passe():
    print("=== Vérificateur de mot de passe ===")
    mot_de_passe = getpass("Entre ton mot de passe : ")
    longueur = len(mot_de_passe)

    # Vérifier les types de caractères
    a_majuscule = any(c.isupper() for c in mot_de_passe)
    a_minuscule = any(c.islower() for c in mot_de_passe)
    a_chiffre = any(c.isdigit() for c in mot_de_passe)
    a_symbole = any(not c.isalnum() for c in mot_de_passe)

    # Calculer la note
    score = 0
    if longueur >= 12:
        score += 1
    if a_majuscule:
        score += 1
    if a_minuscule:
        score += 1
    if a_chiffre:
        score += 1
    if a_symbole:
        score += 1

    # Afficher le résultat
    print(f"Longueur : {longueur} caractères")
    print(f"Note : {score}/5")

    if score <= 2:
        print("Verdict : FAIBLE ❌")
    elif score <= 4:
        print("Verdict : MOYEN ⚠️")
    else:
        print("Verdict : FORT ✅")

    # Conseils
    if longueur < 12:
        print("💡 Conseil : utilise au moins 12 caractères.")
    if not a_symbole:
        print("💡 Conseil : ajoute un symbole (! @ # ...).")

    # Vérifier les fuites
    print("Recherche dans les fuites de données...")
    fuites = verifier_fuite(mot_de_passe)
    if fuites > 0:
        print(f"🚨 Ce mot de passe apparaît {fuites} fois dans des fuites ! Ne l'utilise pas.")
    else:
        print("✅ Ce mot de passe n'a pas été trouvé dans les fuites connues.")


def appeler_api(url):
    requete = urllib.request.Request(url, headers={"User-Agent": "password-checker"})
    try:
        with urllib.request.urlopen(requete, timeout=10) as reponse:
            return json.loads(reponse.read().decode("utf-8"))
    except urllib.error.HTTPError as erreur:
        if erreur.code == 404:
            return {}
        raise


def source_xposedornot(email):
    donnees = appeler_api("https://api.xposedornot.com/v1/check-email/" + urllib.parse.quote(email))
    fuites = donnees.get("breaches", [])
    if fuites and isinstance(fuites[0], list):
        fuites = fuites[0]
    return fuites


def source_leakcheck(email):
    donnees = appeler_api("https://leakcheck.io/api/public?check=" + urllib.parse.quote(email))
    fuites = []
    for source in donnees.get("sources", []):
        fuites.append(source["name"])
    return fuites


SOURCES = {
    "XposedOrNot": source_xposedornot,
    "LeakCheck": source_leakcheck,
}


def analyser_email():
    print("=== Vérificateur d'email ===")
    email = input("Entre ton adresse email : ").strip()

    if "@" not in email or "." not in email.split("@")[-1]:
        print("❌ Ce n'est pas une adresse email valide.")
        return

    print("Recherche dans les fuites de données...")
    resultats = {}
    for nom_source, fonction in SOURCES.items():
        try:
            fuites = fonction(email)
        except Exception as erreur:
            print(f"   ⚠️ {nom_source} : indisponible ({erreur})")
            continue
        print(f"   ✔ {nom_source} : {len(fuites)} fuite(s)")
        for fuite in fuites:
            if fuite not in resultats:
                resultats[fuite] = []
            resultats[fuite].append(nom_source)

    print()
    if resultats:
        print(f"🚨 {len(resultats)} fuite(s) trouvée(s) :")
        for fuite, sources in resultats.items():
            print(f"   - {fuite}  ({', '.join(sources)})")
        print("💡 Conseil : change le mot de passe des sites concernés et active la double authentification.")
    else:
        print("✅ Cette adresse n'a pas été trouvée dans les fuites connues.")


while True:
    print()
    print("=== MENU ===")
    print("1. Vérifier un mot de passe")
    print("2. Vérifier un email")
    print("3. Quitter")
    choix = input("Ton choix : ")

    if choix == "1":
        analyser_mot_de_passe()
    elif choix == "2":
        analyser_email()
    elif choix == "3":
        print("À bientôt !")
        break
    else:
        print("Choix invalide, tape 1, 2 ou 3.")
    