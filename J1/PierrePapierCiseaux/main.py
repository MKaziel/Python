import random

def alea():
    rdm = random.randint(1,3);
    return rdm

def verif_coup(coup_joueur: int):
    if coup_joueur == 1:
        return 1
    elif coup_joueur == 2:
        return 2
    elif coup_joueur == 3:
        return 3
    else: 
        return -1

def resultat_tour(coup_joueur, coup_ordi):
    if coup_joueur == 1:
        if coup_ordi == 1:
            return 0
        elif coup_ordi == 2:
            return 2
        else :
            return 1
    elif coup_joueur == 2:
        if coup_ordi == 1:
            return 1
        elif coup_ordi == 2:
            return 0
        else :
            return 2
    elif coup_joueur == 3 :
        if coup_ordi == 1:
            return 2
        elif coup_ordi == 2:
            return 1
        else :
            return 0
    else :
        return -1

def game():
    compteur_joueur = 0
    compteur_oridnateur = 0
    game=1
    cpt = 0

    print("Bienvenu dans le jeux du Pierre Papier Ciseaux !\n")

    while(game==1):
        cpt +=1
        ordi = alea()
        joueur=input("Veuillez entrez votre choix ( 1: Pierre, 2: Papier, 3: Ciseaux ) :")

        if(joueur.isdigit()):
            if verif_coup(int(joueur)) != -1 :
                resultat = resultat_tour(int(joueur),ordi)
            
            if resultat == 1:
                print("Vous gagnez !")
                compteur_joueur += 1
            elif resultat == 2:
                print("l'ordianteur gagne.")
                compteur_oridnateur += 1
            elif resultat == 0 :
                print("C'est un match nul !")
            else :
                raise ValueError(f"Des données non attendu on été fournise.\nCoup Joeur : {joueur} | Coup Ordinateur : {ordi}")
        else:
            print("\nVeuillez renseignez un nombre comme précisé dans la consigne.\n")

        if cpt == 5 :
            print(f"Voici les scores : Vous [{compteur_joueur}] | l'ordinateur[{compteur_oridnateur}]")
            continu = input("Voulez vous continuer ? (y or n) :")
            if continu == "n":
                game = 0
            else :
                cpt = 0
    print("Fin de la partie")

game()