from composants import *

pile_nobles = []


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
	               range(nj+1)]


def afficher_jeu(p1, p2, p3):
	print("Nobles disponibles :")
	for i, n in enumerate(pile_nobles):
		print(f"Noble {i+1} --> {n}")

	print("------------------------------------------------")

	print("Cartes niveau 3 disponibles :")
	for i, n in enumerate(p3.cartes_visibles):
		print(f"Carte 1.{i+1} --> {n}")

	print("------------------------------------------------")

	print("Cartes niveau 2 disponibles :")
	for i, n in enumerate(p2.cartes_visibles):
		print(f"Carte 2.{i + 1} --> {n}")

	print("------------------------------------------------")

	print("Cartes niveau 1 disponibles :")
	for i, n in enumerate(p1.cartes_visibles):
		print(f"Carte 3.{i + 1} --> {n}")


nb_joueur = int(input("Quel est le nombre de joueur ?"))
init_nobles(nb_joueur)
pioche_n3 = Pioche(3)
pioche_n2 = Pioche(2)
pioche_n1 = Pioche(1)
bot = Joueur("Bot")
afficher_jeu(pioche_n1, pioche_n2, pioche_n3)
bot.voir_main()
bot.achete_carte(pioche_n3, 3)
bot.voir_main()
afficher_jeu(pioche_n1, pioche_n2, pioche_n3)
bot.voir_main()
