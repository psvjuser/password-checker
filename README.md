# 🔐 Password Checker

Outil en ligne de commande, écrit en Python, qui évalue la force d'un mot de passe et vérifie s'il a déjà fuité sur internet.

## Fonctionnalités

**Mot de passe**
- Note de force sur 5 (longueur, majuscules, minuscules, chiffres, symboles)
- Verdict : faible, moyen ou fort, avec des conseils
- Vérification des fuites via **Have I Been Pwned** (k-anonymat)
- Saisie masquée

**Email**
- Recherche dans plusieurs bases de fuites : **XposedOrNot** et **LeakCheck**
- Fusion des résultats sans doublons, avec la source de chaque fuite
- Si une source est indisponible, les autres continuent

## ⚠️ Utilisation responsable

Contrairement au mot de passe, l'adresse email est envoyée en entier aux services de vérification. N'utilise cet outil que sur **tes propres adresses**.

## Installation

Il faut Python 3. Aucune bibliothèque à installer.

```
git clone https://github.com/psvjuser/password-checker.git
cd password-checker
python checker.py
```

## Comment le mot de passe reste secret (k-anonymat)

Le mot de passe n'est **jamais envoyé** sur internet :

1. Il est transformé en empreinte SHA-1 (40 caractères, impossible à inverser).
2. Seuls les **5 premiers caractères** de l'empreinte sont envoyés à Have I Been Pwned.
3. Le site renvoie toutes les empreintes connues qui commencent pareil.
4. La comparaison se fait **en local**, sur ton ordinateur.

Le site ne peut donc pas savoir quel mot de passe a été testé.

## Ce que j'ai appris

Python (variables, conditions, boucles, fonctions), le hachage SHA-1, l'appel à une API web, et Git/GitHub.

## Licence

MIT