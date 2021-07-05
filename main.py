from actions import *



initialisation()
bot = Joueur("Bot")
bot.jetons["jaune"] += 1
pioche3jetons(bot)
pioche3jetons(bot)
# pioche3jetons(bot)
choisir_carte(bot)
afficher_main(bot)
print(input("ok?"))



def lancement_partie():
	initialisation()
	for joueur in joueurs:
        while choix >< True:
            choix = int(input(f"""{joueur.name} doit choisir une action parmi les suivantes :\n
            - (1) piocher 2 jetons
            - (2) piocher 3 jetons
            - (3) choisir une carte
            - (4) reserver une carte
            - (5) afficher sa main
            - (6) afficher le jeu"""))
            
            if choix == 1:
                choix = pioche2jetons(joueur)
            elif choix == 2:
                choix = pioche3jetons(joueur)
            elif choix == 3:
                choix = choisir_carte(joueur)
            elif choix == 4:
                choix = reserver_carte(joueur)
            elif choix == 5:
                choix = afficher_main(joueur)
            elif choix == 6:
                choix = afficher_jeu
            else:
                print(f"Le choix de {joueur.name} n'est pas valide.")


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



