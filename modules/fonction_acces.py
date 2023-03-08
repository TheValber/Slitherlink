###############################################################################
#                    Projet Fin Semestre 2 : Slitherlink                      #
#                            Mai 2021 - Juin 2021                             #
#                                                                             #
#                    Valentin Bernier - Jean-Pascal Trinh                     #
###############################################################################


import modules.utilitaire as util


def est_trace(etat, segment):
    """
    Vérifie si le segment donné en paramètre est tracé
     ==> Valeur dans etat >= 1

    :param etat: Dictionnaire représentant l'état des segments
    :param segment: Couple des coordonnées du segment à vérifier
    :return: True si le segment est tracé, False sinon

    >>> est_trace({((0, 0), (0, 1)): 1}, ((0, 0), (0, 1)))
    True

    >>> est_trace({((0, 0), (0, 1)): -2}, ((0, 0), (0, 1)))
    False

    >>> est_trace({}, ((0, 0), (0, 1)))
    False

    >>> est_trace({((0, 0), (0, 1)): 3}, ((0, 1), (0, 0)))
    True
    """
    if util.ordonner_segment(segment) in etat:
        return etat[util.ordonner_segment(segment)] >= 1
    return False


def est_interdit(etat, segment):
    """
    Vérifie si le segment donné en paramètre est interdit
     ==> Valeur dans etat <= 1

    :param etat: Dictionnaire représentant l'état des segments
    :param segment: Couple des coordonnées du segment à vérifier
    :return: True si le segment est interdit, False sinon

    >>> est_interdit({((0, 0), (0, 1)): -1}, ((0, 0), (0, 1)))
    True

    >>> est_interdit({((0, 0), (0, 1)): 2}, ((0, 0), (0, 1)))
    False

    >>> est_interdit({}, ((0, 0), (0, 1)))
    False

    >>> est_interdit({((0, 0), (0, 1)): -3}, ((0, 1), (0, 0)))
    True
    """
    if util.ordonner_segment(segment) in etat:
        return etat[util.ordonner_segment(segment)] <= -1
    return False


def est_vierge(etat, segment):
    """
    Vérifie si le segment donné en paramètre est vierge
     ==> Non présent dans etat

    :param etat: Dictionnaire représentant l'état des segments
    :param segment: Couple des coordonnées du segment à vérifier
    :return: True si le segment est vierge, False sinon

    >>> est_vierge({}, ((0, 0), (0, 1)))
    True

    >>> est_vierge({((0, 0), (0, 1)): 1}, ((0, 0), (0, 1)))
    False

    >>> est_vierge({((0, 0), (0, 1)): -2}, ((0, 0), (0, 1)))
    False

    >>> est_vierge({((0, 0), (0, 1)): 3}, ((0, 1), (0, 0)))
    False
    """
    return util.ordonner_segment(segment) not in etat


def tracer_segment(etat, segment, couleur):
    """
    Trace le segment donné en paramètre
     ==> etat[segment] = couleur

    :param etat: Dictionnaire représentant l'état des segments
    :param segment: Couple des coordonnées du segment à tracer
    :param couleur: Couleur du segment à tracer

    >>> etat = {}
    >>> tracer_segment(etat, ((0, 0), (0, 1)), [1])
    >>> etat
    {((0, 0), (0, 1)): 1}

    >>> etat = {}
    >>> tracer_segment(etat, ((0, 1), (0, 0)), [2])
    >>> etat
    {((0, 0), (0, 1)): 2}
    """
    etat[util.ordonner_segment(segment)] = couleur[0]


def interdire_segment(etat, segment, couleur):
    """
    Interdit le segment donné en paramètre
     ==> etat[segment] = - couleur

    :param etat: Dictionnaire représentant l'état des segments
    :param segment: Couple des coordonnées du segment à interdire
    :param couleur: Couleur du segment à interdire

    >>> etat = {}
    >>> interdire_segment(etat, ((0, 0), (0, 1)), [1])
    >>> etat
    {((0, 0), (0, 1)): -1}

    >>> etat = {}
    >>> interdire_segment(etat, ((0, 1), (0, 0)), [2])
    >>> etat
    {((0, 0), (0, 1)): -2}
    """
    etat[util.ordonner_segment(segment)] = -couleur[0]


def effacer_segment(etat, segment):
    """
    Efface le segment donné en paramètre
     ==> Enleve le segment de etat

    :param etat: Dictionnaire représentant l'état des segments
    :param segment: Couple des coordonnées du segment à effacer
    :param couleur: Couleur du segment à effacer

    >>> etat = {((0, 0), (0, 1)): -1}
    >>> effacer_segment(etat, ((0, 0), (0, 1)))
    >>> etat
    {}

    >>> etat = {((0, 0), (0, 1)): -2}
    >>> effacer_segment(etat, ((0, 1), (0, 0)))
    >>> etat
    {}
    """
    etat.pop(util.ordonner_segment(segment))


###############################################################################


def sommets_adjacents(sommet, taille_plateau):
    """
    Renvoie tous les sommets adjacents au sommet donné en paramètre
     ==> Au dessus, en dessous, à gauche et à droite
     Ne renvoie pas de sommet en dehors de la grille

    :param sommet: Couple (x, y) des coordonnée du sommet ciblé
    :param taille_plateau: Couple (x, y) de la taille du plateau
    :return: Liste des sommets adjacents (couples de cooronnées)

    >>> sommets_adjacents((1, 1), (3, 3))
    [(0, 1), (2, 1), (1, 0), (1, 2)]

    >>> sommets_adjacents((3, 3), (3, 3))
    [(2, 3), (3, 2)]

    >>> sommets_adjacents((-2, -2), (3, 3))
    []
    """
    lst_sommets = []
    # Pour chaque direction
    for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        # Coordonnées du sommet dans cette direction
        sommet2 = (sommet[0] + i, sommet[1] + j)
        # Si le sommet est dans la grille, on le garde
        if sommet2[0] >= 0 and sommet2[0] <= taille_plateau[0] and \
                sommet2[1] >= 0 and sommet2[1] <= taille_plateau[1]:
            lst_sommets.append(sommet2)
    # On renvoie les sommets qu'on a gardé
    return lst_sommets


def segments_adjacents(etat, sommet, taille_plateau, fonc_verif):
    """
    Renvoie la liste des segments adjacents à un sommet qui vérifie la
    fonction donnée en paramètre

    :param etat: Dictionnaire représentant l'état des segments
    :param sommet: Couple (x, y) des coordonnée du sommet ciblé
    :param taille_plateau: Couple (x, y) de la taille du plateau
    :param fonc_verif: Fonction de vérification revoyant un booléen
    :return: Liste des segments adjacents vérifiant la fonction

    >>> segments_adjacents({}, (1, 1), (3, 3), est_vierge)
    [((0, 1), (1, 1)), ((1, 1), (2, 1)), ((1, 0), (1, 1)), ((1, 1), (1, 2))]

    >>> segments_adjacents({((0, 0), (1, 0)): 1, ((0, 0), (0, 1)): -1},\
                           (0, 0), (3, 3), est_trace)
    [((0, 0), (1, 0))]

    >>> segments_adjacents({((0, 0), (1, 0)): 1, ((0, 0), (0, 1)): -1},\
                           (2, 2), (3, 3), est_interdit)
    []
    """
    lst_segments = []
    # Pour chaque sommet adjacent à un sommet donné
    for sommet2 in sommets_adjacents(sommet, taille_plateau):
        # On forme un segment avec le sommet donné et le sommet adjacent
        segment = util.ordonner_segment((sommet, sommet2))
        # Si le segment respecte la condition on le garde
        if fonc_verif(etat, segment):
            lst_segments.append(segment)
    # On renvoie tous les segments adjacents qui respectent la condition
    return lst_segments


def segment_traces(etat, sommet, taille_plateau):
    """
    Renvoie la liste des segments tracés adjacents à un sommet

    :param etat: Dictionnaire représentant l'état des segments
    :param sommet: Couple (x, y) des coordonnée du sommet ciblé
    :param taille_plateau: Couple (x, y) de la taille du plateau
    :return: Liste des segments tracés adjacents

    >>> segment_traces({}, (0, 0), (3, 3))
    []

    >>> segment_traces({((0, 0), (1, 0)): 1, ((0, 0), (0, 1)): -1},\
                       (0, 0), (3, 3))
    [((0, 0), (1, 0))]
    """
    return segments_adjacents(etat, sommet, taille_plateau, est_trace)


def segment_interdits(etat, sommet, taille_plateau):
    """
    Renvoie la liste des segments interdits adjacents à un sommet

    :param etat: Dictionnaire représentant l'état des segments
    :param sommet: Couple (x, y) des coordonnée du sommet ciblé
    :param taille_plateau: Couple (x, y) de la taille du plateau
    :return: Liste des segments interdits adjacents

    >>> segment_interdits({}, (0, 0), (3, 3))
    []

    >>> segment_interdits({((0, 0), (1, 0)): 1, ((0, 0), (0, 1)): -1},\
                       (0, 0), (3, 3))
    [((0, 0), (0, 1))]
    """
    return segments_adjacents(etat, sommet, taille_plateau, est_interdit)


def segment_vierges(etat, sommet, taille_plateau):
    """
    Renvoie la liste des segments vierges adjacents à un sommet

    :param etat: Dictionnaire représentant l'état des segments
    :param sommet: Couple (x, y) des coordonnée du sommet ciblé
    :param taille_plateau: Couple (x, y) de la taille du plateau
    :return: Liste des segments vierges adjacents

    >>> segment_vierges({}, (0, 0), (3, 3))
    [((0, 0), (1, 0)), ((0, 0), (0, 1))]

    >>> segment_vierges({((0, 0), (1, 0)): 1, ((0, 0), (0, 1)): -1},\
                       (0, 0), (3, 3))
    []
    """
    return segments_adjacents(etat, sommet, taille_plateau, est_vierge)


###############################################################################


def statut_case(indices, etat, case, taille_plateau):
    """
    Retourne le statut de la case
     - 0 si l'indice est satisfait
     - Nombre positif s’il est encore possible de satisfaire l’indice en
        traçant des segments autour de la case
     – Nombre négatif s’il n’est plus possible de satisfaire l’indice parce que
        trop de segments sont déjà tracés ou interdits autour de la case.

    :param indices: Liste des indices des cases de la grille
    :param etat: Dictionnaire représentant l'état des segments
    :param case: Couple (x, y) des coordonnée de la case ciblé
    :param taille_plateau: Couple (x, y) de la taille du plateau
    :return: Nombre entier indiquant le statut de la case ou None si la case
        n'a pas d'indice

    >>> statut_case([[None]], {}, (0, 0), (1, 1))


    >>> statut_case([[0]], {}, (0, 0), (1, 1))
    0

    >>> statut_case([[1]], {}, (0, 0), (1, 1))
    1

    >>> statut_case([[0]], {((0, 0), (0, 1)): 1}, (0, 0), (1, 1))
    -1
    """
    x, y = case
    indice = indices[x][y]
    # Si il n'y a pas d'indice ou que la case est en dehors de la grille
    if indice is None or x < 0 or y < 0\
            or x >= taille_plateau[0] or y >= taille_plateau[1]:
        return None
    else:
        traces, interdits = 0, 0
        # Pour chaque segment autour de la case, on compte ceux qui sont
        # tracés et ceux qui sont interdits
        for segment in [((x, y), (x+1, y)), ((x+1, y), (x+1, y+1)),
                        ((x, y+1), (x+1, y+1)), ((x, y), (x, y+1))]:
            if est_trace(etat, segment):
                traces += 1
            elif est_interdit(etat, segment):
                interdits += 1

        # Calcul du nombre de traits que l'on peut encore tracer et interdire
        traces_manquants = indice - traces
        interdits_manquants = 4 - indice - interdits

        # Si on a tracé trop de trait : return - nombre de traits en trop
        # Si on a tracé le bon nombre de trait : return 0
        # Si on a tracé pas assez de trait et pas trop de croix : return nombre
        #     de traits à tracer
        if traces_manquants <= 0 or interdits_manquants >= 0:
            return traces_manquants
        # Sinon : return - nombre de croix en trop
        else:
            return interdits_manquants


###############################################################################


def remplace_couleur(etat, couleur):
    """
    Remplace tous les trait et croix de la couleur choisie dans la couleur par
    défaut

    :param etat: Dictionnaire représentant l'état des segments
    :param couleur: Couleur choisie

    >>> etat = {((0, 0), (0, 1)): 2, ((0, 0), (1, 0)): -2}
    >>> remplace_couleur(etat, 2)
    >>> etat
    {((0, 0), (0, 1)): 1, ((0, 0), (1, 0)): -1}

    >>> etat = {((0, 0), (0, 1)): 2, ((0, 0), (1, 0)): -1}
    >>> remplace_couleur(etat, 3)
    >>> etat
    {((0, 0), (0, 1)): 2, ((0, 0), (1, 0)): -1}
    """
    for cle in etat:
        if etat[cle] == couleur:
            etat[cle] = 1
        elif etat[cle] == -couleur:
            etat[cle] = -1


def efface_couleur(etat, couleur):
    """
    Efface tous les trait et croix de la couleur choisie

    :param etat: Dictionnaire représentant l'état des segments
    :param couleur: Couleur choisie

    >>> etat = {((0, 0), (0, 1)): 2, ((0, 0), (1, 0)): -2}
    >>> efface_couleur(etat, 2)
    >>> etat
    {}

    >>> etat = {((0, 0), (0, 1)): 2, ((0, 0), (1, 0)): -1}
    >>> efface_couleur(etat, 3)
    >>> etat
    {((0, 0), (0, 1)): 2, ((0, 0), (1, 0)): -1}
    """
    lst_cle = []
    # Pour chaque clé de etat
    for cle in etat:
        # Si sa valeur correspond à la couleur donnée en paramètre
        if etat[cle] == couleur or etat[cle] == -couleur:
            # On conserve la clé dans une liste
            lst_cle.append(cle)
    # On efface de etat chaque clé de la liste
    for cle in lst_cle:
        effacer_segment(etat, cle)


###############################################################################


def annuler(etat, historique):
    """
    Annule le dernier coup effectué

    :param etat: Dictionnaire représentant l'état des segments
    :param historique: Historique des derniers coups effectués

    >>> etat = {((0, 0), (0, 1)): 2}
    >>> historique = [[((0, 0), (0, 1)), "effacer", 1], [((0, 0), (0, 1)),\
        "tracer"]]
    >>> annuler(etat, historique)
    >>> etat
    {}
    >>> historique
    [[((0, 0), (0, 1)), 'effacer', 1]]
    >>> annuler(etat, historique)
    >>> etat
    {((0, 0), (0, 1)): 1}
    >>> historique
    []
    """
    # Si pas d'actions effectuées, on ne fait rien
    if historique == []:
        return
    # Si la dernière action est tracer ou interdire alors on efface le segment
    elif historique[-1][1] == "tracer" or historique[-1][1] == "interdire":
        effacer_segment(etat, historique[-1][0])
    # Si la dernière action est effacer, on trace ou interdit le segment dans
    # sa couleur d'origine
    elif historique[-1][1] == "effacer":
        if historique[-1][2] <= 0:
            interdire_segment(etat, historique[-1][0], [-historique[-1][2]])
        else:
            tracer_segment(etat, historique[-1][0], [historique[-1][2]])
    # On supprime la denière action de l'historique
    historique.pop()


if __name__ == "__main__":
    import doctest
    doctest.testmod()
