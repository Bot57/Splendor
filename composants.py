from lancement import n3_dispo, pioche_n3


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
			self.cartes.append(n3_dispo.pop(numero+1))
			n3_dispo.append(pioche_n3.pop())

	def reserve_carte(self):
		pass

