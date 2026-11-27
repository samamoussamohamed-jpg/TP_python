Partie A — Installation.
1. uv --version
 uv 0.13.9 (x86_64-unknown-linux-gnu)
2. uv python list --only-installed 
cpython-3.14.4-linux-x86_64-gnu    /usr/bin/python3.14
cpython-3.14.4-linux-x86_64-gnu    /usr/bin/python3 -> python3.14

PARTIE B — MODE INTERACTIF
1. Calculs
   Nombre de secondes dans une année de 365 jours :
       >>> 365 * 24 * 60 * 60
       31536000
   Quotient et reste de 2027 divisé par 12 :
       >>> 2027 // 12
       168
       >>> 2027 % 12
       11
   Valeur de 2 puissance 64 
       >>> 2 ** 64
       18446744073709551616
2. La valeur de 2 puissance 64 aurait-elle tenu dans un unsigned long de 64 bits en C ?
   Non. Un entier non signé de 64 bits peut représenter les valeurs de
   0 à 2^64 - 1, soit jusqu'à 18446744073709551615.
3. Erreur 
>>> print("As-Salamou Aleykoum !)
  File "<python-input-0>", line 1
    print("As-Salamou Aleykoum !)
          ^
SyntaxError: unterminated string literal (detected at line 1)

Partie D — Provoquer des erreurs.
1. SyntaxError
SyntaxError: expected ':'
2. IndentationError
IndentationError: expected an indented block after 'if' statement on line 11
3. NameError
NameError: name 'moyene' is not defined. Did you mean: 'moyenne'?,  line 9