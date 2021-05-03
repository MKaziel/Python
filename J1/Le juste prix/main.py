import random

def initiate_random():
    rdm = random.randint(500,10000);

    if rdm < 800 :
        print("\nNous avons dans le panier un nouveau gadget connecté ! Essayez de devinez son prix !\n")
    elif rdm < 2000 :
        print("\nNous avons dans le panier un joli Smartphone ! Essayez de devinez son prix !\n")
    elif rdm < 5000 :
        print("\nNous avons dans le panier un assortiment d'outil et de meubles essentiels pour la cuisine ! A combien estimez-vous le prix de ce panier ?!\n")
    elif rdm < 10000:
        print("\nNous avons dans le panier un assortiment d'outil, gadget ainsi qu'une voiture citadine ! A combien estimez-vous le prix de ce panier ?!\n")

    return rdm


def question_prix(prix, proposition):
    if proposition < prix :
        print("Votre proposition est inférieur au prix !")
    elif proposition > prix :
        print("Votre propostion est supérieur au prix !")
    else :
        print("Félicitation ! Vous avez devinez le prix !")
    
    ecart=0
    if proposition > prix :
        ecart = proposition - prix
    else :
        ecart = prix - proposition
    return ecart

def game():
    
    score = 1000
    game = 1

    print("Bonjour et bienvenue sur la plateau du Juste Prix !\n" +
        "Dans ce jeu vous aller devoir deviner le prix d'un ou plusieurs article qui se trouve dans un panier.\n" +
        "Voici les règles : Vous avez un total de 1000 points qui représentes votre score, plus l'écart est grand avec le prix du panier plus vous perdez de points.\n"+
        "Si vous trouvez le bon prix vous gagnez le panier ! Plutôt simple non ? Alors c'est parti !\n \n")

    prix = initiate_random()

    while(game == 1) :
        print(f"\nVoici votre score: {score}\n")
        print("Quelle est votre proposition?")
        proposition = input("Entrez le montant : ")

        ecart = question_prix(prix, int(proposition))

        if ecart == 0:
            game = 0
        elif ecart > 1000 :
            score -= 100
        elif ecart > 500 :
            score -= 50
        else :
            score -= 25

    print(f"Ceci conclu votre parti ! Votre score était de : {score} ! Nous vous remercions et espérons vous revoir très prochainement.")

game()