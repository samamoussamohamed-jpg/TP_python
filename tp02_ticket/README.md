Partie D — Questions.
1. Si l’on saisit 850,5 pour le prix

ValueError: invalid literal for int() with base 10: '850,5'

2. Le programme s'arrete a la ligne 8 car sans le int, quqntite est une chaine de charactere. Alos Brut sera la multiplication d'une chaine de charactere par l'entier du prix donc brut sera aussi une chaine de charactere.Et remise est arrondi avec round qui ne prend des characteres, d'ou son arret a cette ligne 8.

TypeError: can't multiply sequence by non-int of type 'float'

3. Modifiez l’affichage pour que les montants soient présentés avec une espace comme
séparateur de milliers.

brut2 = f"{brut:,}".replace(",", " ")
print(f"{'Montant brut :':<18}{brut2:>11} FCFA")