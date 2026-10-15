# 🔐 Password Checker

Outil en ligne de commande, écrit en Python, qui évalue la force d'un mot de passe et vérifie s'il a déjà fuité sur internet.

## Fonctionnalités

- Note de force sur 5 (longueur, majuscules, minuscules, chiffres, symboles)
- Verdict : faible, moyen ou fort, avec des conseils
- Vérification des fuites via l'API **Have I Been Pwned**
- Saisie masquée du mot de passe

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