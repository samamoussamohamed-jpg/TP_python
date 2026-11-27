BOUTIQUE = "ALIMENTATION AL BARAKA"
TAUX_REMISE = 0.05
TAUX_REMISE2 = 0.1
nb_articles = 0
brut = 0
frais = 0
client = input("Nom du client : ").strip().title()
while True:
    article = input("Article : ").strip().upper()
    if article == "":
        break
    prix = int(input("Prix unitaire en FCFA : "))
    quantite = int(input("Quantité : "))
    if prix <= 0 or quantite <= 0:
        print("Erreur : les valeurs saisies doivent être positives.")
        continue
    Total = prix * quantite 
    brut += Total
    nb_articles += 1
    print(f"{'Article:':<6}{article} {'Quantité:':>4}{quantite} {'Prix:':>6}{prix} {'Total:':>6}{Total}")
brut2 = f"{brut:,}".replace(",", " ")
if brut >= 50000:
    remise = round(brut * TAUX_REMISE2) # avec round() la remise est arrondie en un entier#
elif brut >= 20000:
    remise = round(brut * TAUX_REMISE) # avec round() la remise est arrondie en un entier#
else:
    remise = 0
net = brut - remise
if nb_articles > 0:
    while True:
        mode = input("Paiement (E espèces, M mobile, C crédit) : ").strip().upper()
        if mode in ("E", "M", "C"):
            break
    match mode:
        case "E":
            pass
        case "M":
            frais = round(net * 0.01)
        case "C":
            print("Montant inscrit au cahier du client.")
net_a_payer = net + frais
print("=" * 36)
print(f"{BOUTIQUE:^36}")
print("=" * 36)
print(f"Client : {client}")
print("-" * 36)
print(f"{'Nombre d articles :':<18}{nb_articles:>11}")
print(f"{'Montant brut :':<18}{brut2:>11} FCFA")
print(f"{'Remise :':<18}{remise:>11} FCFA")
print(f"{'Frais :':<18}{frais:>11} FCFA")
print("-" * 36)
print(f"{'NET À PAYER :':<18}{net_a_payer:>11} FCFA")
print("=" * 36)
print(f"{'Jazakoumoullahou Khayran !':^36}")