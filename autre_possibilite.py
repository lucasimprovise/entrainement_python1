import random

niveau = int(input("Quel niveau de difficulté pour jeu? 1,2,3"))

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

print(jarre)