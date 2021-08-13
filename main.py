from actions import *
from checking import *
from composants import *


def lancement_partie():
	print("Bienvenue !\nVous venez de lancez une partie de Splendor !")
	nj = init_nb_joueur()
	game = Partie(nj)
	game.joueurs.extend(init_joueurs(nj))
	game.jetons.update(init_jetons(nj))
	afficher_jeu(game)

	# test
	game.joueurs[0].jetons["rouge"] += 2
	game.joueurs[0].jetons["vert"] += 2
	game.joueurs[0].jetons["bleu"] += 2
	game.joueurs[0].jetons["noir"] += 2
	game.joueurs[0].jetons["blanc"] += 2
	game.joueurs[0].jetons["jaune"] += 2
	reserver_carte(game, 0)
	jouer_carte_reserve(game, 0)

	test = input("ok?")
	afficher_main(game, 0)
	afficher_jeu(game)
	print(test)

	while True:
		for joueur in range(game.joueurs):
			while not choix:
				choix = int(input(f"""{game.joueurs[joueur].name} doit choisir une action parmi les suivantes :
				- (1) piocher 2 jetons
				- (2) piocher 3 jetons
				- (3) choisir une carte
				- (4) reserver une carte
	            - (5) jouer une carte réservée
				- (6) afficher sa main
				- (7) afficher le jeu"""))

				if choix == 1:
					choix = pioche2jetons(game, joueur)
				elif choix == 2:
					choix = pioche3jetons(game, joueur)
				elif choix == 3:
					choix = acheter_carte(game, joueur)
				elif choix == 4:
					choix = reserver_carte(game, joueur)
				elif choix == 5:
					choix = afficher_main(game, joueur)
				elif choix == 6:
					choix = afficher_jeu
				else:
					print(f"Le choix de {game.joueurs[joueur].name} n'est pas valide.")

			check_nb_jetons(game, joueur)
			check_noble(game, joueur)
			if check_point(game, joueur):
				firstone = game.joueurs.pop(joueur)
				fin = True
				break
		if fin:
			break

	for joueur in range(game.joueurs):
		while not choix:
			choix = int(input(f"""{game.joueurs[joueur].name} doit choisir une action parmi les suivantes :
							- (1) piocher 2 jetons
							- (2) piocher 3 jetons
							- (3) choisir une carte
							- (4) reserver une carte
				            - (5) jouer une carte réservée
							- (6) afficher sa main
							- (7) afficher le jeu"""))

			if choix == 1:
				choix = pioche2jetons(game, joueur)
			elif choix == 2:
				choix = pioche3jetons(game, joueur)
			elif choix == 3:
				choix = acheter_carte(game, joueur)
			elif choix == 4:
				choix = reserver_carte(game, joueur)
			elif choix == 5:
				choix = afficher_main(game, joueur)
			elif choix == 6:
				choix = afficher_jeu
			else:
				print(f"Le choix de {game.joueurs[joueur].name} n'est pas valide.")

		check_nb_jetons(game, joueur)
		check_noble(game, joueur)

		print("La partie est finie")


	# 		joueur i choisi une action parmi :
	#           - pioche2jetons()
	#           - pioche3jetons()
	#           - choisir_carte()
	#           - reserver_carte()
	#           - afficher_main()
	#           si il choisit afficher_main, reproposer les actions
	#       après le choix d'action, contrôle :
	#           - du nombre de jetons : si > 10, le joueur doit en défausser
	#           - de l'acquisition d'un noble si mérité
	#           - du nombre de points : si >= 15, enclenche le dernier tour


lancement_partie()
