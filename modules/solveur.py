###############################################################################
#                    Projet Fin Semestre 2 : Slitherlink                      #
#                            Mai 2021 - Juin 2021                             #
#                                                                             #
#                    Valentin Bernier - Jean-Pascal Trinh                     #
###############################################################################


import modules.fonction_acces as acces
import modules.victoire as vict
import modules.affichage as affi


def solveur(etat, taille_plateau, indices, marges, couleur, graphique,
            temps_actuel, debut_partie, coups):
    """
    Lance la fonction récursive de résolution de la grille à partir de
    différents points de départ

    :param etat: Dictionnaire représentant l'état de la partie
    :param taille_plateau: Couple contenant le nombre de cases de la grille
    :param indices: Liste des indices de la grille
    :param marges: Couple contenant les tailles des marges en haut et à gauche
        de la grille
    :param couleur: Couleur des traits à tracer
    :param graphique: Booléen indiquant si le solveur doit être graphique
    :param temps_actuel: Heure actuelle
    :param debut_partie: Heure de début de la partie
    :param coups: Nombre de coups effectués
    :return: True si une solution est trouvée, False sinon
    """
    # Pour chaque ligne de la grille
    for i in range(0, taille_plateau[0]):
        # S'il y a un 3 dans la ligne
        if 3 in indices[i]:
            # On lance le solveur sur un sommet du 3
            return recursive((i, indices[i].index(3)), etat, taille_plateau,
                             indices, marges, (i, indices[i].index(3)),
                             couleur, graphique, temps_actuel, debut_partie,
                             coups)
    # Si aucun 3, pour chaque ligne :
    for i in range(0, taille_plateau[0]):
        # S'il y a un 2
        if 2 in indices[i]:
            # On lance le solveur sur un sommet du 2
            if recursive((i, indices[i].index(2)), etat, taille_plateau,
                         indices, marges, (i, indices[i].index(2)), couleur,
                         graphique, temps_actuel, debut_partie, coups):
                return True
            # Si pas de solution, on essaye avec le sommet opposé du 2
            return recursive((i + 1, indices[i].index(2) + 1), etat,
                             taille_plateau, indices, marges,
                             (i + 1, indices[i].index(2) + 1), couleur,
                             graphique, temps_actuel, debut_partie, coups)
    # Si aucun 3 et aucun 2, pour chaque ligne :
    for i in range(0, taille_plateau[0]):
        # S'il y a un 1
        if 1 in indices[i]:
            # On lance le solveur sur un sommet du 1
            if recursive((i, indices[i].index(1)), etat, taille_plateau,
                         indices, marges, (i, indices[i].index(1)), couleur,
                         graphique, temps_actuel, debut_partie, coups):
                return True
            # Si pas de solution, on essaye avec le sommet opposé du 1
            return recursive((i + 1, indices[i].index(1) + 1), etat,
                             taille_plateau, indices, marges,
                             (i + 1, indices[i].index(1) + 1),
                             couleur, graphique, temps_actuel,
                             debut_partie, coups)
    # S'il n'y a ni 3, ni 2, ni 1... la grille est nulle
    print("Ta grille est vraiment nulle !")
    return False


def verification_case(coord, taille_plateau, indices, etat, egalite):
    """
    Vérifie si l'indice de la case de coordonnée "coord" est satisfait
     - Case en dehors de la grille : True
     - Pas d'indice : True
     - Statut Case positif : True
     - Statut Case nul : True si egalite vaut True
     - Statut Case négatf : False

    :param coord: Couple de coordonnées de la case à vérifier
    :param taille_plateau: Couple contenant le nombre de cases de la grille
    :param indices: Liste des indices de la grille
    :param etat: Dictionnaire représentant l'état de la partie
    :param egalite: Booléen indiquant si on accepte que statut case soit nul
    :return: Booléen

    >>> verification_case((-1, -1),(1, 1), [[0]], {}, False)
    True

    >>> verification_case((0, 0),(1, 1), [[None]], {((0, 0), (0, 1)): 1},\
        False)
    True

    >>> verification_case((0, 0),(1, 1), [[0]], {((0, 0), (0, 1)): 1}, False)
    False

    >>> verification_case((0, 0),(1, 1), [[1]], {((0, 0), (0, 1)): 1}, False)
    False

    >>> verification_case((0, 0),(1, 1), [[1]], {((0, 0), (0, 1)): 1}, True)
    True

    >>> verification_case((0, 0),(1, 1), [[3]], {((0, 0), (0, 1)): 1}, True)
    True
    """
    # Si les coordonnées sont en dehors de la grille, aucun problème d'indice
    if coord[0] >= taille_plateau[0] or coord[0] < 0 or\
            coord[1] >= taille_plateau[1] or coord[1] < 0:
        return True

    # Sinon, on regarde le statut de la case
    statut_case_coord = acces.statut_case(indices, etat, coord, taille_plateau)
    # S'il n'y a pas d'indice ou que l'indice est possible à satisfaire avec
    # au moins un trait, c'est bon
    if statut_case_coord is None or statut_case_coord > 0:
        return True
    # Si l'indice est satisfait et que egalite vaut True, c'est bon
    if egalite and statut_case_coord == 0:
        return True

    # Sinon on renvoie False
    return False


def verif_cases_adjacentes(segment, taille_plateau, indices, etat,
                           egalite=False):
    """
    Vérifie si les indices des deux cases adjacentes à un segement sont
    satisfaits

    :param segment: Couple de coordonnées de points
    :param taille_plateau: Couple contenant le nombre de cases de la grille
    :param indices: Liste des indices de la grille
    :param etat: Dictionnaire représentant l'état de la partie
    :param egalite: Booléen indiquant si on accepte que statut case soit nul
    :return: True si les indices sont satisfaits, False sinon

    >>> verif_cases_adjacentes(((0, 1), (1, 1)), [1, 2], [[1, None]],\
                               {((0, 1), (1, 1)): 1}, egalite=True)
    True
    >>> verif_cases_adjacentes(((1, 0), (1, 1)), [2, 1], [[0], [3]],\
                               {((1, 0), (1, 1)): 1})
    False
    """
    # Segment horizontal
    if (segment[0][0] == segment[1][0]
            # Case du bas
            and verification_case(segment[0], taille_plateau, indices, etat,
                                  egalite)
            # Case du haut
            and verification_case((segment[0][0] - 1, segment[0][1]),
                                  taille_plateau, indices, etat, egalite)):
        return True

    # Segment vertical
    elif (segment[0][1] == segment[1][1]
            # Case de droite
            and verification_case(segment[0], taille_plateau, indices, etat,
                                  egalite)
            # Case de gauche
            and verification_case((segment[0][0], segment[0][1] - 1),
                                  taille_plateau, indices, etat, egalite)):
        return True

    return False


def recursive(sommet, etat, taille_plateau, indices, marges, depart, couleur,
              graphique, temps_actuel, debut_partie, coups):
    """
    Fonction récursive qui cherche une solution à la grille

    :param sommet: Sommet vérifié
    :param etat: Dictionnaire représentant l'état de la partie
    :param taille_plateau: Couple contenant le nombre de cases de la grille
    :param indices: Liste des indices de la grille
    :param marges: Couple contenant les tailles des marges en haut et à gauche
        de la grille
    :param depart: Sommet de départ
    :param couleur: Couleur des traits à tracer
    :param graphique: Booléen indiquant si le solveur doit être graphique
    :param temps_actuel: Heure actuelle
    :param debut_partie: Heure de début de la partie
    :param coups: Nombre de coups effectués
    :return: True si une solution est trouvée, False sinon
    """
    lst_segments_traces = acces.segment_traces(etat, sommet, taille_plateau)
    # Si deux segments sont tracés autour du sommet alors on a formé une boucle
    if len(lst_segments_traces) == 2:
        # Donc si les indices sont satisfait, une solution est trouvée
        if vict.indices_satisfaits(indices, etat, taille_plateau):
            return True
        return False
    # Si plus de deux traits sont tracés, alors il y a un embranchement, ça ne
    # peut donc pas être la solution
    elif len(lst_segments_traces) > 2:
        return False

    else:
        # Pour chaque segment vierge autour du sommet
        for segment in acces.segment_vierges(etat, sommet, taille_plateau):

            # Si les indices des cases autour du segments permettent de tracer
            # un trait, on le trace
            if verif_cases_adjacentes(segment, taille_plateau, indices, etat):
                acces.tracer_segment(etat, segment, couleur)

                lst_segments_interdits = []
                if sommet != depart:
                    mauvais_indice = False

                    # Pour chaque segment vierges autour de sommet restants
                    for segment_restant in\
                            acces.segment_vierges(etat, sommet,
                                                  taille_plateau):
                        # On interdit le segment
                        lst_segments_interdits.append(segment_restant)
                        acces.interdire_segment(etat, segment_restant, couleur)

                        # Si un indice de case n'est plus possible à satisfaire
                        if not verif_cases_adjacentes(segment_restant,
                                                      taille_plateau, indices,
                                                      etat, egalite=True):
                            # On efface le trait et les croix tracés
                            acces.effacer_segment(etat, segment)
                            for segment_restant2 in lst_segments_interdits:
                                acces.effacer_segment(etat, segment_restant2)

                            # On passe au segment suivant de la première
                            # boucle for
                            mauvais_indice = True
                            break
                    if mauvais_indice:
                        continue

                # Si on a lancé le solveur graphique, on réalise un affichage
                if graphique:
                    affi.affichage(taille_plateau, indices, etat, marges,
                                   vict.indices_satisfaits(indices, etat,
                                                           taille_plateau),
                                   vict.boucle_ferme(etat, taille_plateau),
                                   int(temps_actuel - debut_partie[0]),
                                   couleur, coups, False, False)

                # On relance la fonction récursive sur l'autre point du
                # segment que l'on vient de tracer
                if segment[0] == sommet:
                    # Si la récursive renvoie True, une solution est trouvée
                    if recursive(segment[1], etat, taille_plateau, indices,
                                 marges, depart, couleur, graphique,
                                 temps_actuel, debut_partie, coups):
                        return True
                    # Sinon, ce n'est pas la bonne solution donc on efface le
                    # trait et les croix tracés dans cette execution de la
                    # récursive
                    else:
                        acces.effacer_segment(etat, segment)
                        for segment_interdit in lst_segments_interdits:
                            acces.effacer_segment(etat, segment_interdit)

                elif segment[1] == sommet:
                    if recursive(segment[0], etat, taille_plateau, indices,
                                 marges, depart, couleur, graphique,
                                 temps_actuel, debut_partie, coups):
                        return True
                    else:
                        acces.effacer_segment(etat, segment)
                        for segment_interdit in lst_segments_interdits:
                            acces.effacer_segment(etat, segment_interdit)

        return False


if __name__ == "__main__":
    import doctest
    doctest.testmod()
