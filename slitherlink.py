###############################################################################
#                    Projet Fin Semestre 2 : Slitherlink                      #
#                            Mai 2021 - Juin 2021                             #
#                                                                             #
#                    Valentin Bernier - Jean-Pascal Trinh                     #
###############################################################################


import modules.fltk as fltk
import modules.affichage as affi
import modules.victoire as vict
import modules.utilitaire as util
import modules.fonction_acces as acces
import modules.solveur as solv
import time


def detection_evenement(type_evenement, evenement, marges, etat,
                        taille_plateau, couleur, debut_partie, historique,
                        coups, temps_actuel, solveur_possible, indices):
    """
    Gére les événements détectés par fltk

    :param type_evenement: Type de l'évennement fltk
    :param evenement: Evenement fltk
    :param marges: Marges autour de la grille de jeu
    :param etat: Etat des segments
    :param taille_plateau: Nombre de cases du plateau
    :param couleur: Couleur des traits à tracer
    :param debut_partie: Heure de début de la partie
    :param historique: Historique des derniers coups effectués
    :param coups: Nombre de coups effectués
    :param temps_actuel: Heure actuelle
    :param solveur_possible: Booléen indiquant s'il est possible de lancer le
        solveur
    :param indices: Liste des indices de la grille
    :return: Couple de booléens, le premier indique si le jeu doit etre fermé,
        le second indique si il y a un retour au menu principal
    """
    if type_evenement == "Quitte":
        return False, False

    elif type_evenement == "ClicGauche":
        return evenement_clic_gauche(evenement, etat, couleur, debut_partie,
                                     coups, historique, temps_actuel,
                                     solveur_possible, marges, taille_plateau,
                                     indices)

    elif type_evenement == "ClicDroit":
        evenement_clic_droit(evenement, marges, taille_plateau, etat, couleur,
                             coups)

    return True, True


def evenement_clic_gauche(evenement, etat, couleur, debut_partie, coups,
                          historique, temps_actuel, solveur_possible, marges,
                          taille_plateau, indices):
    """
    Si l'évenement fltk est un clic gauche, réalise une certaine action en
    fonction de l'emplacement du clic

    :param evenement: Evenement fltk
    :param etat: Etat des segments
    :param couleur: Couleur des traits à tracer
    :param debut_partie: Heure de début de la partie
    :param coups: Nombre de coups effectués
    :param historique: Historique des derniers coups effectués
    :param temps_actuel: Heure actuelle
    :param solveur_possible: Booléen indiquant s'il est possible de lancer le
        solveur
    :param marges: Marges autour de la grille de jeu
    :param taille_plateau: Nombre de cases du plateau
    :param indices: Liste des indices de la grille
    :return: Couple de booléens, le premier indique si le jeu doit etre fermé,
        le second indique si il y a un retour au menu principal
    """
    # Clic dans l'interface à droite de l'écran
    if util.clic_dans_rectangle(evenement, 1200, 0, 1600, 900):
        return detection_clic_interface(evenement, etat, couleur,
                                        debut_partie, coups, historique,
                                        temps_actuel, solveur_possible,
                                        taille_plateau, indices, marges)
    # Sinon on regarde si le clic est sur un segment
    else:
        segment_clic = util.detection_clic_segment(
            fltk.abscisse(evenement), fltk.ordonnee(evenement), marges)

        # Si le segment est dans la grille
        if util.segment_dans_grille(segment_clic, taille_plateau):

            # Si le segment est tracé
            if acces.est_trace(etat, segment_clic):
                # On sauvegarde la couleur du trait pour retracer le même si
                # le joueur annule
                couleur_segment = etat[util.ordonner_segment(segment_clic)]
                # On efface le segment
                acces.effacer_segment(etat, segment_clic)
                # On ajoute cette action à l'historique des coups du joueur
                historique.append([util.ordonner_segment(segment_clic),
                                   "effacer", couleur_segment])

            # Si le segment est vierge
            elif acces.est_vierge(etat, segment_clic):
                # On trace le segment
                acces.tracer_segment(etat, segment_clic, couleur)
                # On ajoute cette action à l'historique des coups du joueur
                historique.append([util.ordonner_segment(segment_clic),
                                   "tracer"])
            coups[0] += 1
            # On ajoute 1 coup au nombre total de coups du joueur
    return True, True


def evenement_clic_droit(evenement, marges, taille_plateau, etat, couleur,
                         coups):
    """
    Si l'évenement fltk est un clic droit, réalise une certaine action en
    fonction de l'emplacement du clic

    :param evenement: Evenement fltk
    :param marges: Marges autour de la grille de jeu
    :param taille_plateau: Nombre de cases du plateau
    :param etat: Etat des segments
    :param couleur: Couleur des traits à tracer
    :param coups: Nombre de coups effectués
    """
    # La fonction fonctionne de la même façon que evenement_clic_gauche()
    segment_clic = util.detection_clic_segment(
        fltk.abscisse(evenement), fltk.ordonnee(evenement), marges)
    if util.segment_dans_grille(segment_clic, taille_plateau):
        if acces.est_interdit(etat, segment_clic):
            couleur_segment = etat[util.ordonner_segment(segment_clic)]
            acces.effacer_segment(etat, segment_clic)
            historique.append([util.ordonner_segment(segment_clic),
                               "effacer", couleur_segment])
        elif acces.est_vierge(etat, segment_clic):
            acces.interdire_segment(etat, segment_clic, couleur)
            historique.append([util.ordonner_segment(segment_clic),
                               "interdire"])
        coups[0] += 1


def detection_clic_interface(evenement, etat, couleur, debut_partie, coups,
                             historique, temps_actuel, solveur_possible,
                             taille_plateau, indices, marges):
    """
    Réalise une certaine action en fonction de l'emplacement du clic dans
    l'interface à droite de l'écran

    :param evenement: Evenement fltk
    :param etat: Etat des segments
    :param couleur: Couleur des traits à tracer
    :param debut_partie: Heure de début de la partie
    :param coups: Nombre de coups effectués
    :param historique: Historique des derniers coups effectués
    :param temps_actuel: Heure actuelle
    :param solveur_possible: Booléen indiquant s'il est possible de lancer le
        solveur
    :param taille_plateau: Nombre de cases du plateau
    :param indices: Liste des indices de la grille
    :param marges: Marges autour de la grille de jeu
    :return: Couple de booléens, le premier indique si le jeu doit etre fermé,
        le second indique si il y a un retour au menu principal
    """
    # Bouton Menu
    if util.clic_dans_rectangle(evenement, 1405, 850, 1590, 890):
        return True, False

    # Bouton Recommencer
    elif util.clic_dans_rectangle(evenement, 1210, 850, 1395, 890):
        etat.clear()
        debut_partie[0] = time.time()
        coups[0] = 0
        historique.clear()

    # Bouton Annuler
    elif util.clic_dans_rectangle(evenement, 1210, 750, 1590, 790):
        acces.annuler(etat, historique)
        coups[0] += 1

    # Boutons de changment de couleurs
    clic_couleur(evenement, etat, couleur)

    # Boutons de solveur
    if solveur_possible:
        clic_solveur(evenement, etat, taille_plateau, indices, marges, couleur,
                     temps_actuel, debut_partie, coups)

    return True, True


def clic_couleur(evenement, etat, couleur):
    """
    Gère les couleur de tracé :
     - Selection de la couleur
     - Effacer tous les traits de la couleur
     - Remplacer tous les traits de la couleur dans la couleur par défaut

    :param evenement: Evenement fltk
    :param etat: Dictionnaire représentant l'état des segments de la grille
    :param couleur: Couleur selectionnée
    """
    # Pour les 3 couleurs :
    for i in range(3):
        # Selectionne la couleur
        if util.clic_dans_rectangle(evenement, 1260, 380 + 100 * i, 1400,
                                    420 + 100 * i):
            couleur[0] = i + 1
        if i != 0:
            # Efface tous les traits de la couleur
            if util.clic_dans_rectangle(evenement, 1410, 380 + 100 * i, 1500,
                                        420 + 100 * i):
                acces.efface_couleur(etat, i + 1)
            # Remplace tous les traits de la couleur dans la couleur par défaut
            if util.clic_dans_rectangle(evenement, 1510, 380 + 100 * i, 1590,
                                        420 + 100 * i):
                acces.remplace_couleur(etat, i + 1)


def clic_solveur(evenement, etat, taille_plateau, indices, marges, couleur,
                 temps_actuel, debut_partie, coups):
    """
    Détecte les clics sur les boutons de lancement du solveur

    :param evenement: Evenement fltk
    :param etat: Etat des segments
    :param taille_plateau: Nombre de cases du plateau
    :param indices: Liste des indices de la grille
    :param marges: Marges autour de la grille de jeu
    :param couleur: Couleur des traits à tracer
    :param temps_actuel: Heure actuelle
    :param debut_partie: Heure de début de la partie
    :param coups: Nombre de coups effectués
    """
    # Solveur Classique
    if util.clic_dans_rectangle(evenement, 1210, 800, 1395, 840):
        debut = time.time()
        solv.solveur(etat, taille_plateau, indices, marges, couleur, False,
                     temps_actuel, debut_partie, coups)
        fin = time.time()
        print("Temps de résolution :", fin - debut)

    # Solveur Graphique
    elif util.clic_dans_rectangle(evenement, 1405, 800, 1590, 840):
        debut = time.time()
        solv.solveur(etat, taille_plateau, indices, marges, couleur, True,
                     temps_actuel, debut_partie, coups)
        fin = time.time()
        print("Temps de résolution graphique :", fin - debut)


def detection_clic_menu(evenement):
    """
    Détecte les clics sur les boutons du menu principal

    :param evenement: Evenement fltk
    :return: False si on clic sur le bouton quitter,
        ou le str correspondant à la grille que l'on souhaite charger,
        sinon None
    """
    if util.clic_dans_rectangle(evenement, 500, 770, 1100, 850):
        return False

    tailles = ["5x5", "6x6", "7x7", "10x10"]
    # Pour chauque ligne de boutons
    for i in range(4):
        n = 5
        if i == 3:
            n = 3
        # Pour chaque colonne de boutons
        for j in range(n):
            if util.clic_dans_rectangle(evenement, 580 + 100 * j,
                                        330 + 100 * i, 620 + 100 * j,
                                        370 + 100 * i):
                return tailles[i] + "-" + str(j + 1)
    return None


def menu():
    """
    Gère le menu principal

    :return: Couple de booléens qui indique si le jeu doit etre fermé et si
        une partie doit démarrer puis la liste des indices de la grille
        selectionnée
    """
    while True:
        # Affiche le menu
        affi.affichage_menu()

        # Détecte les événements fltk
        evenement = fltk.attend_ev()
        type_evenement = fltk.type_ev(evenement)

        if type_evenement == "Quitte":
            return False, False, [[]]
        elif type_evenement == "ClicGauche":
            grille = detection_clic_menu(evenement)

            # Si une grille a été chargée
            if grille is not None:
                # S'il y a une erreur dans la grille on ne lance pas de partie
                if not grille:
                    return False, False, [[]]
                # Sinon on renvoie la grille et on lance la partie
                return True, True, util.chargement_grille(grille)


if __name__ == "__main__":
    fltk.cree_fenetre(1600, 900)

    jeu = True
    while jeu:
        # Démarrage du menu principal
        jeu, partie, indices = menu()

        # Quitte le jeu si erreur dans la grille
        if indices is None:
            jeu, partie, indices = False, False, [[]]

        # Initialisation d'une partie
        taille_plateau = (len(indices), len(indices[0]))
        marges = (600 - taille_plateau[1] * 32, 450 - taille_plateau[0] * 32)
        etat = {}
        couleur = [1]
        historique = []
        coups = [0]
        debut_partie = [time.time()]
        temps_actuel = time.time()
        solveur_possible = False
        partie_gagnee = False

        while partie:

            # Détecte si le solveur peut être lancé
            if taille_plateau[0] != 10:
                if solveur_possible and len(etat) != 0:
                    solveur_possible = False
                elif not solveur_possible and len(etat) == 0:
                    solveur_possible = True

            # Affiche les éléments du jeu
            affi.affichage(taille_plateau, indices, etat, marges,
                           vict.indices_satisfaits(indices, etat,
                                                   taille_plateau),
                           vict.boucle_ferme(etat, taille_plateau),
                           int(temps_actuel - debut_partie[0]), couleur, coups,
                           solveur_possible, partie_gagnee)

            # Détecte les événements fltk
            evenement = fltk.donne_ev()
            type_evenement = fltk.type_ev(evenement)

            # Réalise des actions en fonction de l'évenement fltk
            jeu, partie = detection_evenement(type_evenement, evenement,
                                              marges, etat, taille_plateau,
                                              couleur, debut_partie,
                                              historique, coups, temps_actuel,
                                              solveur_possible, indices)

            # Détecte si la partie est gagnée
            if vict.victoire(indices, etat, taille_plateau):
                partie_gagnee = True
            else:
                temps_actuel = time.time()
                partie_gagnee = False
