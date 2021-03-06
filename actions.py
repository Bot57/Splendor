from composants import *


def init_nb_joueur():
	nj = 0
	while nj not in [2, 3, 4]:
		nj: int = int(input("Quel est le nombre de joueur ? 2, 3 ou 4 ?"))
		if not (type(nj) is int):
			print("Veuillez renseigner votre réponse avec un chiffre et non des lettres.") 
		elif nj not in [2, 3, 4]:
			print("Le nombre de joueur indiqué n'est pas compris entre 2 et 4.")
	return nj


def init_joueurs(nb_joueur):
	joueurs = []
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
	return joueurs


def init_jetons(nb_joueur):
	rouge, vert, bleu, noir, blanc, jaune = PileJeton("Rouge", nb_joueur), PileJeton("Vert", nb_joueur), PileJeton(
		"Bleu", nb_joueur), PileJeton("Noir", nb_joueur), PileJeton("Blanc", nb_joueur), PileJeton("Jaune", nb_joueur),
	return {
		"rouge": rouge,
		"vert": vert,
		"bleu": bleu,
		"noir": noir,
		"blanc": blanc,
		"jaune": jaune,
	}


def afficher_jeu(partie):
	"""
	Affiche les nobles, les cartes et les jetons disponibles disponibles
	:param partie: Partie en cours
	"""
	print("Nobles disponibles :")
	for i, n in enumerate(partie.nobles_visibles):
		print(f"Noble {i + 1} --> {n}")

	print("------------------------------------------------")

	print("Cartes niveau 1 disponibles :")
	for i, n in enumerate(partie.pioches[0].cartes_visibles):
		print(f"Carte 1.{i + 1} --> {n}")

	print("------------------------------------------------")
	
	print("Cartes niveau 2 disponibles :")
	for i, n in enumerate(partie.pioches[1].cartes_visibles):
		print(f"Carte 2.{i + 1} --> {n}")

	print("------------------------------------------------")

		print("Cartes niveau 3 disponibles :")
	for i, n in enumerate(partie.pioches[2].cartes_visibles):
		print(f"Carte 3.{i + 1} --> {n}")

	print("------------------------------------------------")

	print("Jetons disponibles :")
	for cle, valeur in partie.jetons.items():
		print(f"Il y a {valeur.nb_jetons} jetons {cle}")

	print("------------------------------------------------")

	return False


def pioche2jetons(partie, joueur, compteur=0, couleur=None):
	"""
	Pioche de 2 jetons de même couleurs
	:param couleur: Couleur des jetons à piocher
	:param partie:
	:param compteur: Permet de vérifier si l'action est fini
	:param joueur: Joueur qui pioche les jetons
	:return: True si action terminé, False si action non aboutie
	"""
	gamer = partie.joueurs[joueur]
	while compteur == 0:
		couleur: str = input(f"""Quel jeton voulez vous en double? (indiquez "annuler" pour annuler)
		Jeton disponibles:
		- rouge: {partie.jetons["rouge"].nb_jetons}
		- vert: {partie.jetons["vert"].nb_jetons}
		- bleu: {partie.jetons["bleu"].nb_jetons}
		- noir: {partie.jetons["noir"].nb_jetons}
		- blanc: {partie.jetons["blanc"].nb_jetons}""")

		if couleur == "annuler":
			print("Vous avez choisi d'annuler votre action")
			return False  # utilisé pour indiquer que l'action n'est pas validé et reproposer les acions possible
		elif couleur not in partie.jetons or couleur == "jaune":
			print("Votre saisie est incorrect !\nVeuillez indiquez l'une des couleurs suivantes:")
			continue
		elif partie.jetons[couleur].nb_jetons < 4:
			print("Cette action n'est pas possible si il y a moins de 4 jetons de cette couleur disponibles\n"
			      "Veuillez choisir une couleur disponible :")
			continue
		else:
			gamer.jetons[couleur] += 2
			partie.jetons[couleur].nb_jetons -= 2
			compteur += 1
	print(f"""Vous avez choisi 2 jetons {couleur}.
	Vous avez maintenant {gamer.jetons['rouge']} rouge(s),
	{gamer.jetons['vert']} vert(s),
	{gamer.jetons['bleu']} bleu(s),
	{gamer.jetons['noir']} noir(s),
	{gamer.jetons['blanc']} blanc(s)""")
	return True


def pioche3jetons(partie, joueur):
	"""
	Pioche de 3 jetons de couleurs différentes
	:param partie: La partie en cours
	:param joueur: Joueur qui pioche les jetons
	"""
	gamer = partie.joueurs[joueur]

	def piocherjeton(tour, interdit=None):
		"""
		Pioche d'un jeton
		:param interdit: Liste des couleurs déjà piochées
		:param tour: Indique quel jeton est pioché (première, deuxième ou troisième)
		:return: La couleur du jeton pioché
		"""
		if interdit is None:
			interdit = []
		while True:
			couleur: str = input(f"""Quel jeton voulez vous en {tour}? (indiquez "annuler" pour annuler)
			Jeton disponibles:
			- rouge: {partie.jetons["rouge"].nb_jetons}
			- vert: {partie.jetons["vert"].nb_jetons}
			- bleu: {partie.jetons["bleu"].nb_jetons}
			- noir: {partie.jetons["noir"].nb_jetons}
			- blanc: {partie.jetons["blanc"].nb_jetons}""")

			if couleur == "annuler":
				print("Vous avez choisi d'annuler votre action")
				return False  # utilisé pour indiquer que l'action n'est pas validé et reproposer les acions possible
			elif couleur not in partie.jetons or couleur == "jaune":
				print("Votre saisie est incorrect !\nVeuillez indiquez l'une des couleurs suivantes:")
				continue
			elif partie.jetons[couleur].nb_jetons == 0:
				print("Il n'y a plus de jeton de cette couleur disponible\nVeuillez choisir une couleur disponible :")
				continue
			elif couleur in interdit:
				print(
					f"Vous avez déjà piocher un jeton {couleur}, vous ne pouvez pas en piocher un deuxième identique !")
			else:
				gamer.jetons[couleur] += 1
				partie.jetons[couleur].nb_jetons -= 1
				return couleur

	couleur1 = piocherjeton("premier")
	if not couleur1:
		return False
	couleur2 = piocherjeton("second", [couleur1])
	if not couleur2:
		gamer.jetons[couleur1] -= 1
		partie.jetons[couleur1].nb_jetons += 1
		return False
	couleur3 = piocherjeton("troisième", [couleur1, couleur2])
	if not couleur3:
		gamer.jetons[couleur1] -= 1
		gamer.jetons[couleur2] -= 1
		partie.jetons[couleur1].nb_jetons += 1
		partie.jetons[couleur2].nb_jetons += 1
		return False

	print(f"Vous avez choisi un jeton {couleur1}, {couleur2} et {couleur3}."
	      f"Vous avez maintenant {gamer.jetons['rouge']} rouge(s), {gamer.jetons['vert']} vert(s), "
	      f"{gamer.jetons['bleu']} bleu(s), {gamer.jetons['noir']} noir(s) et {gamer.jetons['blanc']} blanc(s)")
	return True


def acheter_carte(partie, joueur, jetonsRecues=None):
	"""
	Le joueur choisi une carte et l'achète si il le peut
	:param jetonsRecues: Liste des jetons reçu en échange de jetons jaune
	:param partie: La partie en cours
	:param joueur: Joueur qui pioche les jetons
	:return: True si action terminé, False si action non aboutie
	"""
	gamer = partie.joueurs[joueur]
	pioche: int = int(input("De quel niveau est la carte que vous souhaitez ? (1, 2 ou 3?) (\"0\" pour annuler "
	                        "l'action)")) - 1
	if not (type(pioche) is int):
		print("Veuillez renseigner votre réponse avec un chiffre et non des lettres.") 
	elif pioche == 0:
		return False
	numero: int = int(input("Quel est le numéro de la carte que vous souhaitez? (1, 2, 3 ou 4?) (\"0\" pour "
	                        "annuler l'action)")) - 1
	if not (type(numero) is int):
		print("Veuillez renseigner votre réponse avec un chiffre et non des lettres.") 
	elif numero == 0:
		return False
	carteChoisie = partie.pioches[pioche].cartes_visibles[numero]

	if gamer.jetons["jaune"] > 0:
		jetonsRecues = utiliser_jaune(partie, joueur)

	if check_jetons(partie, joueur, carteChoisie):
		payer_carte(partie, joueur, carteChoisie)
		return gamer.achete_carte(partie, pioche, numero)  # utilisé pour dire que l'action est validé
	print("Vous n'avez pas les jetons nécéssaires pour cette carte.")
	if jetonsRecues:
		no_jaune(partie, joueur, jetonsRecues)
	return False  # utilisé pour indiquer que l'action n'est pas validé et reproposer les acions possible


def check_jetons(partie, joueur, carte):
	"""
	On check si le joueur a les jetons pour acheter la carte selectionné
	:param partie: La partie en cours
	:param joueur: Joueur qui pioche les jetons
	:param carte: Carte dont il faut vérifier si l'achat est possible
	:return: True si le joueur a assez de jeton, sinon False
	"""
	gamer = partie.joueurs[joueur]
	return (gamer.jetons["rouge"] + gamer.bonus["rouge"]) >= carte.rouge and \
	       (gamer.jetons["vert"] + gamer.bonus["vert"]) >= carte.vert and \
	       (gamer.jetons["bleu"] + gamer.bonus["bleu"]) >= carte.bleu and \
	       (gamer.jetons["noir"] + gamer.bonus["noir"]) >= carte.noir and \
	       (gamer.jetons["blanc"] + gamer.bonus["blanc"]) >= carte.blanc


def afficher_main(partie, joueur):
	"""
	Affiche la main du joueur:
	- Cartes achetés
	- Nombre de points gagnés
	"""
	partie.joueurs[joueur].voir_main()
	return False


def reserver_carte(partie, joueur, pioche=None, numero=None):
	gamer = partie.joueurs[joueur]
	if len(gamer.cartes_cache) == 3:
		print("Tu as déjà reservé 3 cartes, tu ne peux pas en reserver plus.")
		return False
	while pioche not in [-1, 0, 1, 2]:
		pioche: int = int(input("De quel niveau est la carte que vous souhaitez réserver ? (1, 2 ou 3?) (\"0\" pour "
		                        "annuler l'action)")) - 1
	if not (type(pioche) is int):
		print("Veuillez renseigner votre réponse avec un chiffre et non des lettres.") 
	elif pioche == -1:
		return False
	while numero not in [-1, 0, 1, 2, 3]:
		numero: int = int(input("Quel est le numéro de la carte que vous souhaitez réserver ? (1, 2, 3 ou 4?) (\"0\" "
		                        "pour annuler l'action)")) - 1
	if not (type(numero) is int):
		print("Veuillez renseigner votre réponse avec un chiffre et non des lettres.") 
	elif numero == -1:
		return False
	return gamer.reserve_carte(partie, pioche, numero)


def jouer_carte_reserve(partie, joueur, jetonsRecuesReserve=None):
	gamer = partie.joueurs[joueur]
	if not gamer.cartes_cache:
		print("Vous n'avez aucune carte en reserve.")
		return False
	print("Vous avez reservé les cartes suivantes :")
	for i, carte in enumerate(gamer.cartes_cache):
		print(f"carte {i+1} - {carte}")
	choix = 0
	while choix not in [*range(len(gamer.cartes_cache))]:
		choix = int(input("""Quel carte reservée voulez vous jouer? (Renseigner le numéro indiqué devant la carte que vous 
voulez jouer. \"0\" pour annuler l'action"""))
		if not (type(pioche) is int):
			print("Veuillez renseigner votre réponse avec un chiffre et non des lettres.") 

	if choix == 0:
		return False

	if gamer.jetons["jaune"] > 0:
		jetonsRecuesReserve = utiliser_jaune(partie, joueur)

	if check_jetons(partie, joueur, gamer.cartes_cache[choix - 1]):
		payer_carte(partie, joueur, gamer.cartes_cache[choix - 1])
		return gamer.utilise_carte(choix - 1)  # utilisé pour dire que l'action est validé
	print("Vous n'avez pas les jetons nécéssaires pour cette carte.")

	if jetonsRecuesReserve:
		no_jaune(partie, joueur, jetonsRecuesReserve)

	return False  # utilisé pour indiquer que l'action n'est pas validé et reproposer les acions possible


def payer_carte(partie, joueur, carte):
	gamer = partie.joueurs[joueur]
	gamer.jetons["rouge"] -= carte.rouge
	gamer.jetons["bleu"] -= carte.bleu
	gamer.jetons["vert"] -= carte.vert
	gamer.jetons["noir"] -= carte.noir
	gamer.jetons["blanc"] -= carte.blanc
	partie.jetons["rouge"].nb_jetons += carte.rouge
	partie.jetons["bleu"].nb_jetons += carte.bleu
	partie.jetons["vert"].nb_jetons += carte.vert
	partie.jetons["blanc"].nb_jetons += carte.blanc
	partie.jetons["noir"].nb_jetons += carte.noir


def utiliser_jaune(partie, joueur):
	gamer = partie.joueurs[joueur]
	jaune_utilise = 0
	couleurs_recues = []
	while gamer.jetons["jaune"] > 0:
		utiliseJaune = input("Vous possédez un ou plusieurs jeton jaune. voulez vous en utiliser un? (o/n)")
		if utiliseJaune not in ["o", "n"]:
			print("Votre saisie est incorrect.")
		elif utiliseJaune == "o":
			while True:
				couleurChoisi = input("Quelle est la couleur que vous voulez que votre jeton jaune représente ? \n"
				                      "rouge, vert, bleu, noir ou blanc ?")
				if couleurChoisi not in partie.jetons or couleurChoisi == "jaune":
					print("Votre saisie est incorrect !")
				else:
					print(f"Vous avez choisi la couleur {couleurChoisi}")
					gamer.jetons[couleurChoisi] += 1
					partie.jetons[couleurChoisi].nb_jetons -= 1
					couleurs_recues.extend([couleurChoisi])
					gamer.jetons["jaune"] -= 1
					partie.jetons["jaune"].nb_jetons += 1
					jaune_utilise += 1
					break
		else:
			break
	return couleurs_recues


def no_jaune(partie, joueur, jetons):
	gamer = partie.joueurs[joueur]
	for jeton in jetons:
		gamer.jetons[jeton] -= 1
		gamer.jetons["jaune"] += 1
		partie.jetons[jeton].nb_jetons += 1
		partie.jetons["jaune"].nb_jetons -= 1


# def init_nobles(nj):
# 	"""
# 	- Défini les cartes de nobles
# 	- Mélanges les nobles
# 	- Distribut les nobles en fonctions du nombre de joueurs
# 	:param nj: nombre de joueurs
# 	"""
