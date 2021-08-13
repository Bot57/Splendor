from random import shuffle

"""
Définitions des classes nécéssaires :
- Cartes de jeux
- Nobles
- Piles de jetons de chaque couleur
- Joueur
"""


class Carte:
	def __init__(self, bonus, points, rouge=0, vert=0, bleu=0, noir=0, blanc=0, ):
		self.points = points
		self.bonus = bonus
		self.rouge = rouge
		self.vert = vert
		self.bleu = bleu
		self.noir = noir
		self.blanc = blanc

	def __repr__(self):
		rou = f" {self.rouge} rouges" if self.rouge != 0 else ""
		ver = f" {self.vert} verts" if self.vert != 0 else ""
		ble = f" {self.bleu} bleus" if self.bleu != 0 else ""
		noi = f" {self.noir} noirs" if self.noir != 0 else ""
		bla = f" {self.blanc} blancs" if self.blanc != 0 else ""

		return f"Point: {self.points} | Bonus: {self.bonus} | Coût:" + rou + ver + ble + noi + bla + "."


class Pioche:
	def __init__(self, niveau):
		self.niveau = niveau
		if self.niveau == 1:
			n1 = [("rouge", 0, 0, 1, 1, 1, 1),
			      ("rouge", 0, 0, 1, 2, 0, 0),
			      ("rouge", 0, 1, 0, 0, 3, 1),
			      ("rouge", 0, 2, 0, 0, 0, 2),
			      ("rouge", 0, 0, 0, 0, 0, 3),
			      ("rouge", 0, 0, 1, 0, 2, 2),
			      ("rouge", 0, 0, 1, 1, 1, 2),
			      ("rouge", 1, 0, 0, 0, 0, 4),
			      ("vert", 0, 2, 0, 1, 2, 0),
			      ("vert", 0, 1, 0, 1, 1, 1),
			      ("vert", 0, 1, 0, 1, 2, 1),
			      ("vert", 0, 0, 0, 1, 0, 2),
			      ("vert", 0, 3, 0, 0, 0, 0),
			      ("vert", 0, 2, 0, 2, 0, 0),
			      ("vert", 0, 0, 1, 3, 0, 1),
			      ("vert", 1, 0, 0, 0, 4, 0),
			      ("bleu", 0, 0, 0, 0, 2, 1),
			      ("bleu", 0, 2, 2, 0, 0, 1),
			      ("bleu", 0, 1, 1, 0, 1, 1),
			      ("bleu", 0, 2, 1, 0, 1, 1),
			      ("bleu", 0, 0, 0, 0, 3, 0),
			      ("bleu", 0, 0, 2, 0, 2, 0),
			      ("bleu", 0, 1, 3, 1, 0, 1),
			      ("bleu", 1, 4, 0, 0, 0, 0),
			      ("noir", 0, 3, 1, 0, 1, 0),
			      ("noir", 0, 1, 0, 2, 0, 2),
			      ("noir", 0, 1, 1, 1, 0, 1),
			      ("noir", 0, 1, 1, 2, 0, 1),
			      ("noir", 0, 0, 3, 0, 0, 0),
			      ("noir", 0, 0, 2, 0, 0, 2),
			      ("noir", 0, 1, 2, 0, 0, 0),
			      ("noir", 1, 0, 0, 4, 0, 0),
			      ("blanc", 0, 1, 1, 1, 1, 0),
			      ("blanc", 0, 0, 0, 2, 2, 0),
			      ("blanc", 0, 0, 0, 1, 1, 3),
			      ("blanc", 0, 0, 2, 2, 1, 0),
			      ("blanc", 0, 2, 0, 0, 1, 0),
			      ("blanc", 0, 0, 0, 3, 0, 0),
			      ("blanc", 0, 1, 2, 1, 1, 0),
			      ("blanc", 1, 0, 4, 0, 0, 0)]
			shuffle(n1)
			self.cartes = [Carte(n1[i][0], n1[i][1], n1[i][2], n1[i][3], n1[i][4], n1[i][5], n1[i][6]) for i in
			               range(39)]

		if self.niveau == 2:
			n2 = [("rouge", 1, 2, 0, 0, 3, 2),
			      ("rouge", 1, 2, 0, 3, 3, 0),
			      ("rouge", 2, 0, 0, 0, 5, 3),
			      ("rouge", 2, 0, 0, 0, 5, 0),
			      ("rouge", 2, 0, 2, 4, 0, 1),
			      ("rouge", 3, 6, 0, 0, 0, 0),
			      ("vert", 1, 3, 2, 0, 0, 3),
			      ("vert", 1, 0, 0, 3, 2, 2),
			      ("vert", 2, 0, 5, 0, 0, 0),
			      ("vert", 2, 0, 3, 5, 0, 0),
			      ("vert", 2, 0, 0, 2, 1, 4),
			      ("vert", 3, 0, 6, 0, 0, 0),
			      ("bleu", 1, 3, 2, 2, 0, 0),
			      ("bleu", 1, 0, 3, 2, 3, 0),
			      ("bleu", 2, 0, 0, 5, 0, 0),
			      ("bleu", 2, 0, 0, 3, 0, 5),
			      ("bleu", 2, 1, 0, 0, 4, 2),
			      ("bleu", 3, 0, 0, 6, 0, 0),
			      ("noir", 1, 0, 2, 2, 0, 3),
			      ("noir", 1, 0, 3, 0, 2, 3),
			      ("noir", 2, 0, 0, 0, 0, 5),
			      ("noir", 2, 2, 4, 1, 0, 0),
			      ("noir", 2, 3, 5, 0, 0, 0),
			      ("noir", 3, 0, 0, 0, 6, 0),
			      ("blanc", 1, 2, 3, 0, 2, 0),
			      ("blanc", 1, 2, 0, 3, 0, 2),
			      ("blanc", 2, 4, 1, 0, 2, 0),
			      ("blanc", 2, 5, 0, 0, 0, 0),
			      ("blanc", 2, 5, 0, 0, 3, 0),
			      ("blanc", 3, 0, 0, 0, 0, 6)]
			shuffle(n2)
			self.cartes = [Carte(n2[i][0], n2[i][1], n2[i][2], n2[i][3], n2[i][4], n2[i][5], n2[i][6]) for i in
			               range(29)]

		if self.niveau == 3:
			n3 = [("rouge", 3, 0, 3, 5, 3, 3),
			      ("rouge", 4, 0, 7, 0, 0, 0),
			      ("rouge", 4, 3, 6, 3, 0, 0),
			      ("rouge", 5, 3, 7, 0, 0, 0),
			      ("vert", 3, 3, 0, 3, 3, 5),
			      ("vert", 4, 0, 0, 7, 0, 0),
			      ("vert", 4, 0, 3, 6, 0, 3),
			      ("vert", 5, 0, 3, 7, 0, 0),
			      ("bleu", 3, 3, 3, 0, 5, 3),
			      ("bleu", 4, 0, 0, 3, 3, 6),
			      ("bleu", 4, 0, 0, 0, 0, 7),
			      ("bleu", 5, 0, 0, 3, 0, 7),
			      ("noir", 3, 3, 5, 3, 0, 3),
			      ("noir", 4, 7, 0, 0, 0, 0),
			      ("noir", 4, 6, 3, 0, 3, 0),
			      ("noir", 5, 7, 0, 0, 3, 0),
			      ("blanc", 3, 5, 3, 3, 3, 0),
			      ("blanc", 4, 0, 0, 0, 7, 0),
			      ("blanc", 4, 3, 0, 0, 6, 3),
			      ("blanc", 5, 0, 0, 0, 7, 3)]
			shuffle(n3)
			self.cartes = [Carte(n3[i][0], n3[i][1], n3[i][2], n3[i][3], n3[i][4], n3[i][5], n3[i][6]) for i in
			               range(19)]

		self.cartes_visibles = []
		for _ in range(4):
			self.cartes_visibles.append(self.cartes.pop())


class Noble:
	def __init__(self, points, rouge=0, vert=0, bleu=0, noir=0, blanc=0):
		self.points = points
		self.rouge = rouge
		self.vert = vert
		self.bleu = bleu
		self.noir = noir
		self.blanc = blanc

	def __repr__(self):
		rou = f" {self.rouge} rouges" if self.rouge != 0 else ""
		ver = f" {self.vert} verts" if self.vert != 0 else ""
		ble = f" {self.bleu} bleus" if self.bleu != 0 else ""
		noi = f" {self.noir} noirs" if self.noir != 0 else ""
		bla = f" {self.blanc} blancs" if self.blanc != 0 else ""

		return f"Point: {self.points} | Coût:" + rou + ver + ble + noi + bla + "."


class Nobles:
	def __init__(self, nj):
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
		self.nobles_dispo = []
		for i in range(nj + 1):
			self.nobles_dispo.append(
				Noble(nobles[i][0], nobles[i][1], nobles[i][2], nobles[i][3], nobles[i][4], nobles[i][5]))


class PileJeton:
	def __init__(self, couleur, nb_joueur):
		self.couleur = couleur
		if self.couleur == "Jaune" or nb_joueur == 3:
			self.nb_jetons = 5
		elif nb_joueur == 2:
			self.nb_jetons = 4
		elif nb_joueur == 4:
			self.nb_jetons = 7


class Joueur:
	def __init__(self, name):
		self.name = name
		self.cartes = []
		self.cartes_cache = []
		self.points = 0
		self.jetons = {"rouge": 0, "vert": 0, "bleu": 0, "noir": 0, "blanc": 0, "jaune": 0}
		self.bonus = {"rouge": 0, "vert": 0, "bleu": 0, "noir": 0, "blanc": 0}
		self.nobles = []

	def __repr__(self):
		return self.name

	def voir_main(self):
		"""
		Affiche la main du joueur:
		- Cartes achetées
		- Cartes reservées
		- Nombre de points gagnés
		"""
		print("------------------------------------------------")
		if self.cartes:
			print(f"{self.name} à les cartes suivantes : ")
			for i in self.cartes:
				print(i)
		else:
			print(f"{self.name} n'a acheté aucune carte")
		if self.cartes_cache:
			print(f"{self.name} reserve les cartes suivantes : ")
			for i in self.cartes_cache:
				print(i)
		else:
			print(f"{self.name} n'a réservé aucune carte")
		print(f"""{self.name} a:
- {self.jetons['rouge']} jetons rouge
- {self.jetons['vert']} jetons vert
- {self.jetons['bleu']} jetons bleu
- {self.jetons['noir']} jetons noir
- {self.jetons['blanc']} jetons blanc
- {self.jetons['jaune']} jetons jaune""")
		print(f"Il a {self.points} point(s).")
		print("------------------------------------------------")

	def achete_carte(self, partie, pioche, numero):
		"""
		Déplace une carte depuis le jeu à la main du joueur
		:param partie: La partie en cours
		:param pioche: A quelle pioche (niveau 1, 2 ou 3) appartient la carte achetée
		:param numero: Quelle carte est achetée.
		"""
		carte = partie.pioches[pioche].cartes_visibles[numero]
		print(f"{self.name} a acheté la carte suivante : "
		      f"{carte}")
		self.points += carte.points
		self.bonus[carte.bonus] += 1
		self.cartes.append(partie.pioches[pioche].cartes_visibles.pop(numero))
		partie.pioches[pioche].cartes_visibles.append(partie.pioches[pioche].cartes.pop())
		return True

	def reserve_carte(self, partie, pioche, numero):
		"""
		Le joueur reserve une carte et pioche un jeton jaune
		:param partie: La partie en cours
		:param pioche: A quelle pioche (niveau 1, 2 ou 3) appartient la carte reservée
		:param numero: Quelle carte est reservée.
		"""
		carte = partie.pioches[pioche].cartes_visibles[numero]
		print(f"{self.name} a reservé la carte suivante : "
		      f"{carte}")
		self.cartes_cache.append(partie.pioches[pioche].cartes_visibles.pop(numero))
		partie.pioches[pioche].cartes_visibles.append(partie.pioches[pioche].cartes.pop())
		if partie.jetons["jaune"].nb_jetons > 0:
			self.jetons["jaune"] += 1
			partie.jetons["jaune"].nb_jetons -= 1
		return True

	def utilise_carte(self, choix):
		carte = self.cartes_cache[choix]
		print(f"{self.name} a utilisé la carte suivante : "
		      f"{carte}")
		self.points += carte.points
		self.bonus[carte.bonus] += 1
		self.cartes.append(self.cartes_cache.pop(choix))
		return True

	def gagne_noble(self, partie, noble):
		self.nobles.append(partie.nobles_visibles.pop(noble))
		self.points += noble.points


class Partie:
	def __init__(self, nj):
		self.joueurs = []
		self.pioches = [Pioche(1), Pioche(2), Pioche(3)]
		nobles = Nobles(nj)
		self.nobles_visibles = nobles.nobles_dispo
		self.jetons = {}
