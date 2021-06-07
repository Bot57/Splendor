from actions import *



initialisation()
bot = Joueur("Bot")
pioche3jetons(bot)
pioche3jetons(bot)
pioche3jetons(bot)
choisir_carte(bot)
afficher_main(bot)
print(input("ok?"))

joueurs = ["joueur_1", "joueur_2", "joueur_3", "joueur_4"]


def lancement_partie():
	initialisation()
	for i in range(nb_joueur):
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
		pass



