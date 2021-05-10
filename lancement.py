from random import shuffle
# from composants import Noble, Carte, Joueur


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


class Joueur:
	def __init__(self, name):
		self.name = name
		self.cartes = []
		self.cartes_cache = []
		self.points = 0
		self.jeton = {"rouge": 0, "vert": 0, "bleu": 0, "noir": 0, "blanc": 0, "jaune": 0}

	def voir_main(self):
		if self.cartes:
			for i in self.cartes:
				print(i)
		else:
			print(f"{self.name} n'a acheté aucune carte")

	def pioche3jetons(self):
		pass

	def pioche2jetons(self):
		pass

	def achete_carte(self, niveau, numero):
		if niveau == 3:
			self.cartes.append(n3_dispo.pop(numero-1))
			n3_dispo.append(pioche_n3.pop())

	def reserve_carte(self):
		pass


pile_nobles = []
pioche_n1 = []
pioche_n2 = []
pioche_n3 = []
n1_dispo = []
n2_dispo = []
n3_dispo = []


def init_nobles():
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
	               range(5)]


def init_pioches():
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
	global pioche_n3, n3_dispo
	pioche_n3 = [Carte(n3[i][0], n3[i][1], n3[i][2], n3[i][3], n3[i][4], n3[i][5], n3[i][6]) for i in
	             range(20)]

	for _ in range(4):
		n3_dispo.append(pioche_n3.pop())


def afficher_jeu():
	print("Nobles disponibles :")
	for i, n in enumerate(pile_nobles):
		print(f"Noble {i+1} --> {n}")

	print("------------------------------------------------")

	print("Cartes niveau 3 disponibles :")
	for i, n in enumerate(n3_dispo):
		print(f"Carte 3.{i+1} --> {n}")


init_nobles()
init_pioches()
bot = Joueur("Bot")
afficher_jeu()
bot.voir_main()
bot.achete_carte(3, 3)
bot.voir_main()
afficher_jeu()
