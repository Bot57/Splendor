from typing import List, Any

from composants import *
from composants import PileJeton, Pioche

global joueurs, pioche_n1, pioche_n2, pioche_n3, pioches, nb_joueur
global rouge, vert, bleu, noir, blanc, jaune, jetons
pile_nobles = []
pioche_n1, pioche_n2, pioche_n3 = Pioche(1), Pioche(2), Pioche(3)
global joueurs = []



# Je comprend pas pourquoi je ne peux pas inclures ces variables dans initialisation()


def initialisation():
	"""
	- Définition du nombre de joueur
	- Définition des joueurs
	- Mélange et distribution des nobles
	- Mise en place des jetons
	- Affichage du jeu en place
	"""
	pioche_n1, pioche_n2, pioche_n3 = Pioche(1), Pioche(2), Pioche(3)
	while nb_joueur != [2, 3, 4]:
		nb_joueur: int = int(input("Quel est le nombre de joueur ? 2, 3 ou 4 ?"))
		if nb_joueur != [2, 3, 4]:
			print("Le nombre de joueur indiqué ne correspond pas.")

	joueur1 = Joueur(input("Quel est le pseudo du joueur 1 ?"))
	joueurs.extend([joueur1])
	joueur2 = Joueur(input("Quel est le pseudo du joueur 2 ?"))
	joueurs.extend([joueur2])
	if nb_joueur >= 3:
		joueur3 = Joueur(input("Quel est le pseudo du joueur 3 ?"))
		joueurs.extend([joueur3])
	if nb_joueur == 4:
		joueur4 = Joueur(input("Quel est le pseudo du joueur 4 ?"))
		joueurs.extend([joueur4])

	init_nobles(nb_joueur)
	rouge, vert, bleu, noir, blanc, jaune = PileJeton("Rouge", nb_joueur), PileJeton("Vert", nb_joueur), PileJeton(
		"Bleu", nb_joueur), PileJeton("Noir", nb_joueur), PileJeton("Blanc", nb_joueur), PileJeton("Jaune", nb_joueur),
	jetons = {"rouge": rouge, "vert": vert, "bleu": bleu, "noir": noir, "blanc": blanc, "jaune": jaune}
	pioches = {"1": pioche_n1, "2": pioche_n2, "3": pioche_n3}
	afficher_jeu()


def init_nobles(nj):
	"""
	- Défini les cartes de nobles
	- Mélanges les nobles
	- Distribut les nobles en fonctions du nombre de joueurs
	:param nj: nombre de joueurs
	"""
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
	"""
	Affiche les nobles et les cartes disponibles
	:param p1: pioche niveau 1
	:param p2: pioche niveau 2
	:param p3: pioche niveau 3
	"""
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

	return False


def pioche3jetons(joueur):
	"""
	Pioche de 3 jetons de couleurs différentes
	:param joueur: Joueur qui pioche les jetons
	"""

	def piocherjeton(joueurbis, tour, interdit=[], compteur=0):
		"""
		Pioche d'un jeton
		:param joueurbis: Joueur qui pioche le jeton
		:param compteur: Permet de vérifier si l'action est finie
		:param tour: Indique quel jeton est pioché (première, deuxième ou troisième)
		:param interdit: Contient les couleurs déjà piochées
		:return: La couleur du jeton pioché
		"""
		while compteur == 0:
			couleur: str = input(f"""Quel jeton voulez vous en {tour}? (indiquez "annuler" pour annuler)
			Jeton disponibles:
			- rouge: {rouge.nb_jetons}
			- vert: {vert.nb_jetons} 
			- bleu: {bleu.nb_jetons}
			- noir: {noir.nb_jetons}
			- blanc: {blanc.nb_jetons}""")
			if couleur == "annuler":
				return False # utilisé pour indiquer que l'action n'est pas validé et reproposer les acions possible
			elif couleur not in jetons:
				print("Votre saisie est incorrect !\nVeuillez indiquez l'une des couleurs suivantes:")
				continue
			elif jetons[couleur].nb_jetons == 0:
				print("Il n'y a plus de jeton de cette couleur disponible\nVeuillez choisir une couleur disponible :")
				continue
			elif couleur in interdit:
				print(
					f"Vous avez déjà piocher un jeton {couleur}, vous ne pouvez pas en piocher un deuxième identique !")
			else:
				joueurbis.jetons[couleur] += 1
				jetons[couleur].nb_jetons -= 1
				compteur += 1
		return couleur

	couleur1 = piocherjeton(joueur, "premier")
	if couleur1 == False:
		return False
	couleur2 = piocherjeton(joueur, "second", [couleur1])
	if couleur2 == False:
		return False
	couleur3 = piocherjeton(joueur, "troisième", [couleur1, couleur2])
	if couleur3 == False:
		return False

	print(f"Vous avez choisi un jeton {couleur1}, {couleur2} et {couleur3}."
		  f"Vous avez maintenant {joueur.jetons['rouge']} rouge(s), {joueur.jetons['vert']} vert(s), "
		  f"{joueur.jetons['bleu']} bleu(s), {joueur.jetons['noir']} noir(s) et {joueur.jetons['blanc']} blanc(s)")
	return True


def pioche2jetons(joueur, compteur=0):
	"""
	Pioche de 2 jetons de même couleurs
	:param compteur: Permet de vérifier si l'action est fini
	:param joueur: Joueur qui pioche les jetons
	:return: True si action terminé, False si action non aboutie
	"""
	while compteur == 0:
		double_couleur: str = input(f"""Quel jeton voulez vous en double? (indiquez "annuler" pour annuler)
		Jeton disponibles:
		- rouge: {rouge.nb_jetons}
		- vert: {vert.nb_jetons} 
		- bleu: {bleu.nb_jetons}
		- noir: {noir.nb_jetons}
		- blanc: {blanc.nb_jetons}""")

		if double_couleur == "annuler":
			return False # utilisé pour indiquer que l'action n'est pas validé et reproposer les acions possible
		elif double_couleur not in jetons:
			print("Votre saisie est incorrect !\nVeuillez indiquez l'une des couleurs suivantes:")
			continue
		elif jetons[double_couleur].nb_jetons < 4:
			print("Cette action n'est pas possible si il y a moins de 4 jetons de cette couleur disponibles\n"
				  "Veuillez choisir une couleur disponible :")
			continue
		else:
			joueur.jetons[double_couleur] += 2
			jetons[double_couleur].nb_jetons -= 2
			compteur += 1
	print(f"Vous avez choisi 2 jetons {double_couleur}."
		  f"Vous avez maintenant {joueur.jetons['rouge']} rouge(s), {joueur.jetons['vert']} vert(s), "
		  f"{joueur.jetons['bleu']} bleu(s), {joueur.jetons['noir']} noir(s) et {joueur.jetons['blanc']} blanc(s)")
	return True


def choisir_carte(joueur):
	"""
	Le joueur choisi une carte et l'achète si il le peut
	:param joueur: Joueur qui pioche les jetons
	:return: True si action terminé, False si action non aboutie
	"""
	global utiliseJaune, couleurChoisi

	def check_jetons(joueurbis, carte, check = 0):
		"""
		On check si le joueur a les jetons pour acheter la carte selectionné
		:param carte:
		:param joueurbis:
		:return: True si le joueur a assez de jeton, sinon False
		"""
		return (joueurbis.jetons["rouge"] + joueurbis.bonus["rouge"]) >= carte.rouge and \
			   (joueurbis.jetons["vert"] + joueurbis.bonus["vert"]) >= carte.vert and \
			   (joueurbis.jetons["bleu"] + joueurbis.bonus["bleu"]) >= carte.bleu and \
			   (joueurbis.jetons["noir"] + joueurbis.bonus["noir"]) >= carte.noir and \
			   (joueurbis.jetons["blanc"] + joueurbis.bonus["blanc"]) >= carte.blanc

	pioche = pioches[input("De quel niveau est la carte que vous souhaitez ? (1, 2 ou 3?)")]
	numero = int(input("Quel est le numéro de la carte que vous souhaitez? (1, 2, 3 ou 4?)"))
	carteChoisie = pioche.cartes_visibles[numero - 1]
	if joueur.jetons["jaune"] > 0:
		utiliseJaune = input("Voulez vous utiliser un jeton jaune ? (O/N)")
		if utiliseJaune == "O":
			while check == 0:
				couleurChoisi = input("Quelle est la couleur que vous voulez que votre jeton jaune représente ? \n"
									"rouge, vert, bleu, noir ou blanc ?")
				if couleurChoisi not in jetons:
					print("Votre saisie est incorrect !")
					continue
				else:
					print(f"Vous avez choisi la couleur {couleurChoisi}")
					joueur.jetons[couleurChoisi] += 1
					check = 1
	else:
		utiliseJaune = "N"

	if check_jetons(joueur, carteChoisie):
		joueur.achete_carte(pioche, numero)
		if utiliseJaune == "O":
			joueur.jetons["jaune"] -= 1
		return True  # utilisé pour dire que l'action est validé
	else:
		print("Vous n'avez pas les jetons nécéssaires pour cette carte.")
		if utiliseJaune == "O":
			joueur.jetons[couleurChoisi] -= 1
		return False  # utilisé pour indiquer que l'action n'est pas validé et reproposer les acions possible


def afficher_main(joueur):
	"""
	Affiche la main du joueur:
	- Cartes achetés
	- Nombre de points gagnés
	"""
	joueur.voir_main()
	return False
