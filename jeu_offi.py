import random

print("Bienvenue dans le jeu des jarres !")

#choix de la difficulté
niveau =int(input("Fait ton choix 1:Facile, 2:Moyen, 3:Difficile"))

#Compteur de clés
trousseau = 0

#Création de la boucle du jeu
while trousseau !=3:
    print("Vous disposez de 5 jarres devant vous. Choisis 1, 2, 3, 4 ou 5")

    #On genere les serpents par rapport au niveau
    serpent = ['S'] * niveau

    #On regarde dans combien de jarre il n'y a pas de serpent
    difference = 5 - niveau

    #on genere autant de jarre que la difference
    cle = ['K'] * difference

    #On additionne les jarres normal et avec des serpents
    jarre = serpent + cle

    #On melange les jarres
    random.shuffle(jarre)

    # Demande au joueur de mettre une valeur et met en pause le programme (input renvoie une chaîne de caractère)
    reponse = int(input()) # le int permet de transformer la valeur en nombre

    print ("Le joueur a mis la jarre n°", reponse)
    

    #Verification

    if jarre[reponse-1] : #gagné
        print("La chance ! Tu as obtenu une clé ! le serpent était dans la jar", jarre)
        trousseau += 1
        print("Tu as actuellement", trousseau,"sur 3 clés")

    else:
        print("Perdu ! Un serpent était là!")
        trousseau -= 1
        

        # Si le joueur n'a pas de clé
        if trousseau > 0:
            trousseau -= 1
            print("Tu as actuellement", trousseau,"sur 3 clés")
            print("Tu as actuellement", trousseau,"sur 3 clés")

print("T'es devenu le meilleur mon gars !")
 
