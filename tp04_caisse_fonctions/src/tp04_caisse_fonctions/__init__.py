BOUTIQUE = "ALIMENTATION AL BARAKA"
def taux_remise(brut: int) -> float:
    """Renvoie le taux de remise en fonction du montant brut."""
    if brut >= 50000:
        return 0.1
    elif brut >= 20000:
        return 0.05
    else:
        return 0.0
def remise(brut: int) -> int:
    """Renvoie le montant de la remise en fonction du montant brut."""
    return round(brut * taux_remise(brut))
def frais(net: int, mode: str) -> int:
    """Renvoie le montant des frais en fonction du mode de paiement."""
    if mode == "M":
        return round(net * 0.01)
    return 0  
def montant(valeur: int) -> str:
    """Renvoie le montant formaté avec des espaces comme séparateurs de milliers."""
    return f"{valeur:,}".replace(",", " ")
def saisir_entier_positif(message: str) -> int:
    """Demande à l'utilisateur de saisir un entier positif et le renvoie."""
    while True:
        try:
            valeur = int(input(message))
        except ValueError:
            print("Erreur : veuillez saisir un nombre entier.")
            continue
        if valeur > 0:
            return valeur
        print("Erreur : la valeur saisie doit être positive.")
def saisir_mode_paiement() -> str:
    """Demande à l'utilisateur de saisir un mode de paiement valide et le renvoie."""
    while True:
        mode = input("Paiement (E espèces, M mobile, C crédit) : ").strip().upper()
        if mode in ("E", "M", "C"):
            return mode
        print("Erreur : mode de paiement non valide.")
def afficher_ligne(article: str, quantite: int, prix: int) -> None:
    """Affiche une ligne d'article."""
    print(f"Article : {article}")
    print(f"{'Quantité :':<18}{quantite:>11}")
    print(f"{'Prix unitaire :':<18}{montant(prix):>11} FCFA")
    print(f"{'Total :':<18}{montant(quantite * prix):>11} FCFA")
def afficher_recapitulatif(client: str, nb_articles: int, brut: int,
                           remise_accordee: int, frais_payes: int,
                           net_a_payer: int) -> None:
    """Affiche le récapitulatif de la transaction."""
    print("=" * 36)
    print(f"{BOUTIQUE:^36}")
    print("=" * 36)
    print(f"Client : {client}")
    print("-" * 36)
    print(f"{'Nombre d articles :':<18}{nb_articles:>11}")
    print(f"{'Montant brut :':<18}{montant(brut):>11} FCFA")
    print(f"{'Remise :':<18}{montant(remise_accordee):>11} FCFA")
    print(f"{'Frais :':<18}{montant(frais_payes):>11} FCFA")
    print("-" * 36)
    print(f"{'NET À PAYER :':<18}{montant(net_a_payer):>11} FCFA")
    print("=" * 36)
    print(f"{'Jazakoumoullahou Khayran !':^36}")
def main() -> None:
    client = input("Nom du client : ").strip().title()
    nb_articles = 0
    brut = 0
    while True:
        article = input("Article : ").strip().upper()
        if article == "":
            break
        prix = saisir_entier_positif("Prix unitaire en FCFA : ")
        quantite = saisir_entier_positif("Quantité : ")
        brut += prix * quantite
        nb_articles += 1
        afficher_ligne(article, quantite, prix)
    remise_accordee = remise(brut)
    net = brut - remise_accordee
    frais_payes = 0
    if nb_articles > 0:
        mode = saisir_mode_paiement()
        frais_payes = frais(net, mode)
        if mode == "C":
            print("Montant inscrit au cahier du client.")
    net_a_payer = net + frais_payes
    afficher_recapitulatif(client, nb_articles, brut,
                           remise_accordee, frais_payes, net_a_payer)
if __name__ == "__main__":
    main()