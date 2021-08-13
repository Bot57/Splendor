def check_noble(partie, joueur):
	gamer = partie.joueurs[joueur]
	for noble in partie.nobles_visibles:
		if gamer.bonus["rouge"] >= noble.rouge and \
				gamer.bonus["vert"] >= noble.vert and \
				gamer.bonus["bleu"] >= noble.bleu and \
				gamer.bonus["noir"] >= noble.noir and \
				gamer.bonus["blanc"] >= noble.blanc:
			gamer.gagne_noble(partie, noble)


def check_point(partie, joueur):
	gamer = partie.joueurs[joueur]
	if gamer.points >= 15:
		print('/!\\------------------------------------------/!\\')
		print(f"{gamer.name} a obtenu {gamer.points} points ! Il a gagné la partie !")
		print("/!\\------------------------------------------/!\\")
		return True
	return False


def check_nb_jetons(partie, joueur):
	gamer = partie.joueurs[joueur]
	while sum(gamer.jetons.values()) > 10:
		print("Vous avez trop de jetons en main.")
		couleur = input("Quel jeton voulez-vous reposer ?"
		                "rouge, bleu, vert, blanc, noir")
		gamer.jetons[couleur] -= 1
		partie.jetons[couleur].nb_jetons += 1
		print(f"Vous avez reposé un jeton {couleur}")
