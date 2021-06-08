import random

print("Bienvenue dans le jeu des jarres !")

#Compteur de clés
cle = 0

#Création de la boucle du jeu
while cle !=3:
    print("Vous disposez de 5 jarres devant vous. Choisis 1, 2, 3, 4 ou 5")

    #Choix aléatoire de la jarre qui fait perdre le joueur
    snake = random.randint(1,5) #On va chercher un nombre random entre 1 et 5

    # Demande au joueur de mettre une valeur et met en pause le programme (input renvoie une chaîne de caractère)
    reponse = int(input()) # le int permet de transformer la valeur en nombre

    print ("Le joueur a mis la jarre n°", reponse)


    #Verification

    if reponse != snake: #gagné
        print("La chance ! Tu as obtenu une clé ! le serpent était dans la jar")
        cle += 1
        print("Tu as actuellement", cle,"sur 3 clés")

    else:
        print("Perdu ! Un serpent était là!", snake)
        cle -= 1
        

        # Si le joueur n'a pas de clé
        if cle > 0:
            cle -= 1
            print("Tu as actuellement", cle,"sur 3 clés")
            print("Tu as actuellement", cle,"sur 3 clés")

print("T'es devenu le meilleur mon gars !")

