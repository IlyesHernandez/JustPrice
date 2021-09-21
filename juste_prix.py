from random import randint

win = False
version = '1.0.0'

print(f'Bienvenue sur le jeux du juste prix.')
print(f'Nous somme à la version {version} du jeux !')
print('================================')
print('Les régle du jeux :')
print('Le but du jeux est très simple, il faut trouvé le bon nombre. Bien sur un systeme de difficulté est fait.\nPour la difficulté facile c\'est un nombre entre 0 et 50 qui est générés.\nPour la difficulté moyenne c\'est un nombre entre 0 et 150 qui est générés.\nPour la difficulté difficile c\'est un nombre entre 0 et 250 qui est générés.\nPour la difficulté impossible c\'est un nombre entre 0 et 350 qui est généré.')

print("Les difficulté que vous souhaitait ? (facile, moyen, difficile, impossible)")
difficulty = input()

if difficulty == "facile":
    numbers = randint(0, 50)
    play = True
    while play == True:
        print("Trouve le nombre !")
        number_user = int(input())
        if int(number_user) == int(numbers):
            print("Vous venez de trouvé le résultat !")
            play = False
            win = True
        elif numbers > number_user:
            print("Plus grand !")
        elif numbers < number_user:
            print("Plus petit")
        else:
            pass

elif difficulty == "moyen":
    numbers = randint(0, 150)
    play = True
    while play == True:
        print("Trouve le nombre !")
        number_user = int(input())
        if int(number_user) == int(numbers):
            print("Vous venez de trouvé le résultat !")
            play = False
            win = True
        elif numbers > number_user:
            print("Plus grand !")
        elif numbers < number_user:
            print("Plus petit")
        else:
            pass
elif difficulty == "difficile":
    numbers = randint(0, 250)
    play = True
    while play == True:
        print("Trouve le nombre !")
        number_user = int(input())
        if int(number_user) == int(numbers):
            print("Vous venez de trouvé le résultat !")
            play = False
            win = True
        elif numbers > number_user:
            print("Plus grand !")
        elif numbers < number_user:
            print("Plus petit")
        else:
           pass
elif difficulty == "impossible":
    numbers = randint(0, 350)
    play = True
    while play == True:
        print("Trouve le nombre !")
        number_user = int(input())
        if int(number_user) == int(numbers):
            print("Vous venez de trouvé le résultat !")
            play = False
            win = True
        elif numbers > number_user:
            print("Plus grand !")
        elif numbers < number_user:
            print("Plus petit")
        else:
            pass
else:
    print("Veuiller séléctioner la bonne difficulté")

if win == True:
    print("Vous avez gagné !")
else:
    print("Vous avez perdu !")
