import os

def clear_function():
    clear = lambda: os.system('cls')
    clear()

def verification_char(lettre : str, mot : str):
    if lettre in mot:
        return 1
    else :
        return 0

def nb_char(lettre : str, mot : str):
    cpt=0
    for char in mot:
        if char == lettre :
            cpt += 1

    return cpt

def verif_mot(tab_lettre, mot):
    cpt_lettre = 0

    for lettre in tab_lettre :
        cpt_lettre += nb_char(lettre,mot)
    
    return cpt_lettre

def game():
    mot = ""
    lettre_trouver = []
    j2=""
    length = 0
    vie=6
    game = 1

    print("Bienvenu sur le jeu du pendu !")

    
    j2 = input("Avez-vous deux joueurs ? ( Y or N ) : ")

    if j2 == "Y":
        mot = input("Joueur 1, Choisissez un mot : ").lower()
        length = len(mot)
        clear_function()
    
    while(vie != 0 and game != 0) :
        print("Joueur 2, c'est à vous maintenant ! Essayer de devinez le mot.")
        print(f"Voici un indice : longueur = {length}.\nListe des lettres trouvé {lettre_trouver}")

        lettre = input("\nVeuillez entre une lettre : ")
        
        if isinstance(lettre,str) and len(lettre) == 1 :
            if verification_char(lettre,mot) == 1:
                print(f"Bien vue\nLa lettre {lettre} est présente : {nb_char(lettre,mot)} de fois dans le mot\n")
                lettre_trouver += lettre

                if verif_mot(lettre_trouver,mot) == length :
                    print(f"Bravo vous avez trouvé le mot ! Celui-ci était : {mot}\nIl vous restait {vie} nb de vie(s)")
                    game = 0
            else : 
                vie -= 1
                print(f"Loupé, la lettre {lettre} ne se trouve pas dans le mot ! Vous perdez une vie, il vous en reste {vie}")
        else :
            print("veuillez entrez une seule lettre. Faites bien attention à ne pas mettre d'espaces")
    if vie == 0 : print("\nVous n'avez plus de vie ! Vous avez perdu ...\n")
    print("\nMerci d'avoir joué ! A la prochaine.\n")
game()