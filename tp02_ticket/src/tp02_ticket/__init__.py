BOUTIQUE = "ALIMENTATION AL BARAKA"
TAUX_REMISE = 0.05
client = input("Nom du client : ").strip().title()
article = input("Article : ").strip().upper()
prix = int(input("Prix unitaire en FCFA : "))
quantite = int(input("Quantité : "))
brut = prix * quantite
brut2 = f"{brut:,}".replace(",", " ")
remise = round(brut * TAUX_REMISE) # avec round() la remise est arrondie en un entier#
net = brut - remise
print("=" * 36)
print(f"{BOUTIQUE:^36}")
print("=" * 36)
print(f"Client : {client}")
print("-" * 36)
print(f"Article : {article}")
print(f"{'Prix unitaire :':<18}{prix:>11} FCFA")
print(f"{'Quantité :':<18}{quantite:>11}")
print(f"{'Montant brut :':<18}{brut2:>11} FCFA")
print(f"{'Remise (5 %) :':<18}{remise:>11} FCFA")
print("-" * 36)
print(f"{'NET À PAYER :':<18}{net:>11} FCFA")
print("=" * 36)
print(f"{'Jazakoumoullahou Khayran !':^36}")