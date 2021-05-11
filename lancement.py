from composants import *

pile_nobles = []
pioche_n1, pioche_n2, pioche_n3 = Pioche(1), Pioche(2), Pioche(3)


def initialisation():
	global pioche_n1, pioche_n2, pioche_n3
	global rouge, vert, bleu, noir, blanc, jaune
	nb_joueur = int(input("Quel est le nombre de joueur ?"))
	init_nobles(nb_joueur)
	rouge, vert, bleu, noir, blanc, jaune = PileJeton("Rouge", nb_joueur), PileJeton("Vert", nb_joueur), PileJeton(
		"Bleu", nb_joueur), PileJeton("Noir", nb_joueur), PileJeton("Blanc", nb_joueur), PileJeton("Jaune", nb_joueur),
	afficher_jeu()


def init_nobles(nj):
	nobles = [(3, 0, 0, 0, 4, 4),
	          (3, 0, 3, 0, 3, 3),
	          (3, 3, 3, 0, 3, 0),
	          (3, 0, 3, 3, 0, 3),
	          (3, 0, 0, 3, 3, 3),
	          (3, 4, 4, 0, 0, 0),
	          (3, 0, 0, 4, 0, 4),
	          (3, 4, 0, 0, 4, 0),
	          (3, 0, 4, 4, 0, 0),
	          (3, 3, 3, 3, 0, 0)]

	shuffle(nobles)
	global pile_nobles
	pile_nobles = [Noble(nobles[i][0], nobles[i][1], nobles[i][2], nobles[i][3], nobles[i][4], nobles[i][5]) for i in
	               range(nj + 1)]


def afficher_jeu(p1=pioche_n1, p2=pioche_n2, p3=pioche_n3):
	global pioche_n1, pioche_n2, pioche_n3
	print("Nobles disponibles :")
	for i, n in enumerate(pile_nobles):
		print(f"Noble {i + 1} --> {n}")

	print("------------------------------------------------")

	print("Cartes niveau 3 disponibles :")
	for i, n in enumerate(p3.cartes_visibles):
		print(f"Carte 1.{i + 1} --> {n}")

	print("------------------------------------------------")

	print("Cartes niveau 2 disponibles :")
	for i, n in enumerate(p2.cartes_visibles):
		print(f"Carte 2.{i + 1} --> {n}")

	print("------------------------------------------------")

	print("Cartes niveau 1 disponibles :")
	for i, n in enumerate(p1.cartes_visibles):
		print(f"Carte 3.{i + 1} --> {n}")


def pioche3jetons(joueur):
	secu = 0
	while secu == 0:
		couleur1 = input("Quel jeton voulez vous en premier?\n"
		                 f"Jeton disponibles --> rouge: {rouge.nb_jetons} / vert: {vert.nb_jetons} / bleu: "
		                 f"{bleu.nb_jetons} / noir: {noir.nb_jetons} / blanc: {blanc.nb_jetons}")
		if couleur1 not in ["rouge", "vert", "bleu", "noir", "blanc"]:
			print("Votre saisie est incorrect !\n Veuillez indiquez l'une des couleurs suivantes"
			      f"Jeton disponibles --> rouge: {rouge.nb_jetons} / vert: {vert.nb_jetons} / bleu: {bleu.nb_jetons} / \n"
			      f"noir: {noir.nb_jetons} / blanc: {blanc.nb_jetons}")
			continue
		joueur.jetons[couleur1] += 1
		secu += 1
		if couleur1 == "rouge":
			rouge.nb_jetons -= 1
		elif couleur1 == "vert":
			vert.nb_jetons -= 1
		elif couleur1 == "bleu":
			bleu.nb_jetons -= 1
		elif couleur1 == "noir":
			noir.nb_jetons -= 1
		elif couleur1 == "blanc":
			blanc.nb_jetons -= 1


initialisation()
bot = Joueur("Bot")
afficher_jeu()
bot.achete_carte(pioche_n3, 3)
afficher_jeu(pioche_n1, pioche_n2, pioche_n3)
pioche3jetons(bot)
bot.voir_main()
