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
			               range(20)]

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
			               range(20)]

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
			               range(20)]

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

	def voir_main(self):
		"""
		Affiche la main du joueur:
		- Cartes achetés
		- Nombre de points gagnés
		"""
		if self.cartes:
			print(f"{self.name} à les cartes suivantes : ")
			for i in self.cartes:
				print(i)
		else:
			print(f"{self.name} n'a acheté aucune carte")
		print(f"Il a {self.points} point(s).")

	def achete_carte(self, pioche, numero):
		"""
		Déplace une carte depuis le jeu à la main du joueur
		:param pioche: A quelle pioche (niveau 1, 2 ou 3) appartient la carte achetée
		:param numero: Quelle carte est acheté.
		"""
		print(f"{self.name} a acheté la carte suivante : "
		      f"{pioche.cartes_visibles[numero - 1]}")
		self.points += pioche.cartes_visibles[numero - 1].points
		self.cartes.append(pioche.cartes_visibles.pop(numero - 1))
		pioche.cartes_visibles.append(pioche.cartes.pop())

	def reserve_carte(self):
		"""
		Le joueur reserve une carte et pioche un jeton jaune
		"""
		pass
