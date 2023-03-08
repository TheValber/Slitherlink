###############################################################################
#                    Projet Fin Semestre 2 : Slitherlink                      #
#                            Mai 2021 - Juin 2021                             #
#                                                                             #
#                    Valentin Bernier - Jean-Pascal Trinh                     #
###############################################################################


import modules.fltk as fltk
import modules.fonction_acces as acces


def affichage(taille_plateau, indices, etat, marges, condition_indices,
              condition_boucle, temps, couleur, coups, solveur_possible,
              partie_gagnee):
    """
    Gère l'affichage de l'écran de jeu

    :param taille_plateau: Nombre de cases du plateau
    :param indices: Liste des indices de la grille
    :param etat: Etat des segments
    :param marges: Marges autour de la grille de jeu
    :param condition_indices: Booléen indiquant si les indices sont satisfaits
    :param condition_boucle: Booléen indiquant si les segments forment une
        unique boucle fermée
    :param temps: Temps écoulé depuis le début de la partie
    :param couleur: Couleur des traits à tracer
    :param coups: Nombre de coups effectués
    :param solveur_possible: Booléen indiquant s'il est possible de lancer le
        solveur
    :param partie_gagnee: Booléen indiquant si la partie est gagnée
    """
    fltk.efface_tout()
    affiche_coin(taille_plateau, marges)
    affiche_chiffre(taille_plateau, indices, etat, marges)
    affiche_segment(etat, marges)
    affiche_interface(condition_indices, condition_boucle, temps, couleur,
                      coups, solveur_possible)
    if partie_gagnee:
        fltk.texte(600, marges[1] / 2, "Victoire", ancrage="center",
                   taille="100", couleur="blue")
    fltk.mise_a_jour()


def affiche_coin(taille_plateau, marges):
    """
    Affiche des point sur chaque coin de case de la grille

    :param taille_plateau: Nombre de case de la grille
    :param marges: Taille des marges en haut et à gauche de la grille
    """
    # Pour chaque colonne (+1)
    for i in range(taille_plateau[1] + 1):
        # Pour chaque ligne (+1)
        for j in range(taille_plateau[0] + 1):
            # On trace un cercle
            fltk.cercle(marges[0] + i * 64, marges[1] + j * 64, 2,
                        remplissage="black")


def affiche_chiffre(taille_plateau, indices, etat, marges):
    """
    Affiche les indices de a grille, leur couleur dépend de si ils sont
    satisfaits ou pas

    :param taille_plateau:  Nombre de case de la grille
    :param indices: Liste des indiace de la grille
    :param etat: Dictionnaire représentant l'état des segments
    :param marges: Taille des marges en haut et à gauche de la grille
    """
    # Pour chaque case de la grille
    for i in range(taille_plateau[1]):
        for j in range(taille_plateau[0]):
            # Y'a-t-il un indice et si oui, est-il satisfait
            case = acces.statut_case(indices, etat, (j, i), taille_plateau)
            if case is not None:
                # Indice satisfait
                if case == 0:
                    couleur_chiffre = "blue"
                # Indice impossible à satisfaire
                elif case < 0:
                    couleur_chiffre = "red"
                # Indice possible à satisfaire
                else:
                    couleur_chiffre = "black"
                # Affichage du chiffre dans la couleur correspondante
                fltk.texte(marges[0] + 32 + i * 64, marges[1] + 32 + j * 64,
                           indices[j][i], ancrage="center",
                           couleur=couleur_chiffre)


def affiche_segment_unique(marges, segments, couleur):
    """
    Affiche le segment donné en paramètre de la couleur donnée en paramètre

    :param marges: Taille des marges en haut et à gauche de la grille
    :param segments: Couple de deux coordonnées (x, y) représentant le
        segment à afficher
    :param couleur: Couleur du segment
    """
    fltk.ligne(marges[0] + segments[0][1] * 64,
               marges[1] + segments[0][0] * 64,
               marges[0] + segments[1][1] * 64,
               marges[1] + segments[1][0] * 64,
               epaisseur=2, couleur=couleur)


def affiche_croix_unique(milieu_x, milieu_y, couleur):
    """
    Affiche la croix dont le milieu est donné en paramètre de la couleur
    donnée en paramètre

    :param milieu_x: Coordonnée en x du milieur de la croix
    :param milieu_y: Coordonnée en y du milieur de la croix
    :param couleur: Couleur de la croix
    :return:
    """
    fltk.ligne(milieu_x - 5, milieu_y - 5, milieu_x + 5, milieu_y + 5,
               epaisseur=2, couleur=couleur)
    fltk.ligne(milieu_x + 5, milieu_y - 5, milieu_x - 5, milieu_y + 5,
               epaisseur=2, couleur=couleur)


def affiche_segment(etat, marges):
    """
    Affiche les segments et les croix en fonction de l'état du jeu

    :param etat: Dictionnaire représentant l'état des segments
    :param marges: Taille des marges en haut et à gauche de la grille
    """
    # Pour chaque segment
    for segments in etat:
        # Si c'est un trait, affiche le trait dans la couleur correspondante
        if etat[segments] == 1:
            affiche_segment_unique(marges, segments, "blue")
        elif etat[segments] == 2:
            affiche_segment_unique(marges, segments, "green")
        elif etat[segments] == 3:
            affiche_segment_unique(marges, segments, "purple")
        # Si c'est une croix
        else:
            # Calcul des coordonnées du milieu du segment où se trouve la croix
            milieu_x = (marges[0] + segments[0][1] * 64 +
                        marges[0] + segments[1][1] * 64) // 2
            milieu_y = (marges[1] + segments[0][0] * 64 +
                        marges[1] + segments[1][0] * 64) // 2
            # Affiche la croix dans la couleur correspondante
            if etat[segments] == -1:
                affiche_croix_unique(milieu_x, milieu_y, "red")
            elif etat[segments] == -2:
                affiche_croix_unique(milieu_x, milieu_y, "orange")
            elif etat[segments] == -3:
                affiche_croix_unique(milieu_x, milieu_y, "#FACADE")


def affiche_interface(condition_indices, condition_boucle, temps, couleur,
                      coups, solveur_possible):
    """
    Affiche les éléments de l'interface à droite de l'écran

    :param condition_indices: Booléen indiquant si les indices sont satisfaits
    :param condition_boucle: Booléen indiquant si les segments forment une
        unique boucle fermée
    :param temps: Temps écoulé depuis le début de la partie
    :param couleur: Couleur de traits selectionnée
    :param coups: Nombre de coups effectués
    :param solveur_possible: Booléen indiquant s'il est possible de lancer le
        solveur
    """
    fltk.ligne(1200, 0, 1200, 900)

    # Bouton Menu
    fltk.rectangle(1405, 850, 1590, 890)
    fltk.texte(1497, 870, "Menu", ancrage="center", taille=22)

    # Bouton Recommencer
    fltk.rectangle(1210, 850, 1395, 890)
    fltk.texte(1302, 870, "Recommencer", ancrage="center", taille=18)

    if solveur_possible:
        # Solveur graphique
        fltk.rectangle(1405, 800, 1590, 840)
        fltk.texte(1497, 820, "Solveur Graphique", ancrage="center", taille=16)

        # Solveur classique
        fltk.rectangle(1210, 800, 1395, 840)
        fltk.texte(1302, 820, "Solveur Classique", ancrage="center", taille=16)

    # Annuler
    fltk.rectangle(1210, 750, 1590, 790)
    fltk.texte(1400, 770, "Annuler", ancrage="center", taille=24)

    # Conditions de victoire
    if condition_indices:
        fltk.texte(1400, 30, "Indices Satisfaits", ancrage="center",
                   taille=24, couleur="blue")
    else:
        fltk.texte(1400, 30, "Indices Satisfaits", ancrage="center",
                   taille=24, couleur="red")
    if condition_boucle:
        fltk.texte(1400, 80, "Boucle Fermée", ancrage="center",
                   taille=24, couleur="blue")
    else:
        fltk.texte(1400, 80, "Boucle Fermée", ancrage="center",
                   taille=24, couleur="red")

    # Nombre de coups
    fltk.texte(1302, 200, "Coups :", ancrage="center", taille=24)
    fltk.texte(1497, 200, coups, ancrage="center", taille=24)

    # Temps
    fltk.texte(1302, 250, "Temps :", ancrage="center", taille=24)
    fltk.texte(1497, 250, "{:0>2d}:{:0>2d}".format(temps // 60, temps % 60),
               ancrage="center", taille=24)

    # Couleurs
    couleurs = ["blue", "green", "purple"]
    fltk.cercle(1505, 400, 20, couleur=couleurs[couleur[0] - 1],
                remplissage=couleurs[couleur[0] - 1])
    for i in range(3):
        fltk.cercle(1230, 400 + 100 * i, 20, couleur=couleurs[i],
                    remplissage=couleurs[i])
        fltk.rectangle(1260, 380 + 100 * i, 1400, 420 + 100 * i)
        fltk.texte(1330, 400 + 100 * i, "Selectionner", ancrage="center",
                   taille=18)
        if i != 0:
            fltk.rectangle(1410, 380 + 100 * i, 1500, 420 + 100 * i)
            fltk.rectangle(1510, 380 + 100 * i, 1590, 420 + 100 * i)
            fltk.texte(1455, 400 + 100 * i, "Effacer", ancrage="center",
                       taille=18)
            fltk.texte(1550, 400 + 100 * i, "Valider", ancrage="center",
                       taille=18)


def affichage_menu():
    """
    Affiche les éléments du menu principal
    """
    fltk.efface_tout()

    # Titre
    fltk.texte(800, 200, "Slitherlink", ancrage="center", taille=100)

    # Bouton Quitter
    fltk.rectangle(500, 770, 1100, 850, epaisseur=3)
    fltk.texte(800, 810, "Quitter", ancrage="center", taille=50)

    # Boutons de choix de grille
    tailles = ["5x5", "6x6", "7x7", "10x10"]
    for i in range(4):
        fltk.texte(400, 350 + 100 * i, tailles[i], ancrage="center", taille=30)
        n = 5
        # Pour les grilles 10x10, il n'y a que 3 grilles donc 3 boutons
        if i == 3:
            n = 3
        for j in range(n):
            fltk.rectangle(580 + 100 * j, 330 + 100 * i, 620 + 100 * j,
                           370 + 100 * i, epaisseur=2)
            fltk.texte(600 + 100 * j, 350 + 100 * i, str(j + 1),
                       ancrage="center")
