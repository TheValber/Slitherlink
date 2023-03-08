###############################################################################
#                    Projet Fin Semestre 2 : Slitherlink                      #
#                            Mai 2021 - Juin 2021                             #
#                                                                             #
#                    Valentin Bernier - Jean-Pascal Trinh                     #
###############################################################################


import modules.fonction_acces as acces


def indices_satisfaits(indices, etat, taille_plateau):
    """
    Cette fonction vérifie si tous les indices de la grille sont satisfaits.
    Si c'est le cas, retourne True sinon False.

    :param indices: list
    :param etat: dict
    :param taille_plateau: tuple
    :return: bool

    >>> indices_satisfaits([[0]], {}, (1, 1))
    True

    >>> indices_satisfaits([[1]], {}, (1, 1))
    False
    """
    # Pour chaque indice
    for i in range(taille_plateau[0]):
        for j in range(taille_plateau[1]):
            # Si le statut de la case n'est égal à 0, on renvoie False
            if acces.statut_case(indices, etat, (i, j), taille_plateau) != 0\
                and acces.statut_case(indices, etat, (i, j),
                                      taille_plateau) is not None:
                return False
    # Sinon, tous les indices sont satisfaits, on renvoie True
    return True


def longueur_boucle(etat, segment, taille_plateau):
    """
    Cette fonction retourne le nombre de segment que compose la boucle formée
    par le joueur.

    :param etat: dict
    :param segment: tuple
    :param taille_plateau: tuple
    :return: int, longueur de la boucle formée

    # Grille triviale
    >>> longueur_boucle({((0, 0), (0, 1)): 1, ((0, 1), (0, 2)): 1, ((0, 2),\
    (1, 2)): 1, ((1, 2), (2, 2)): 1, ((2, 1), (2, 2)): 1, ((2, 0), (2, 1)): 1,\
    ((1, 0), (2, 0)): 1, ((0, 0), (1, 0)): 1}, ((0, 0), (1, 0)), (2,2))
    8

     >>> longueur_boucle({((0, 0), (0, 1)): 1, ((0, 1), (0, 2)): 1},\
     ((0, 0), (1, 0)), (2, 2))
    """
    depart = segment[0]
    precedent, courant = segment
    nombre_segments = 1
    # Tant que la boucle n'est pas fermée
    while courant != depart:
        # On prend la liste des segments tracés autour du point courant
        segments = acces.segment_traces(etat, courant, taille_plateau)
        # Si la longueur n'est pas 2, il y a soit un embranchement, soit une
        # impasse. Cela ne peut pas être une boucle
        if len(segments) != 2:
            return None
        # Sinon, on continue d'avancer dans la boucle
        for i in range(2):
            if segments[i][0] == courant and segments[i][1] != precedent:
                precedent = courant
                courant = segments[i][1]
            elif segments[i][1] == courant and segments[i][0] != precedent:
                precedent = courant
                courant = segments[i][0]
        # On augmente de 1 le compteur de segments
        nombre_segments += 1
    return nombre_segments


def boucle_ferme(etat, taille_plateau):
    """
    Cette fonction vérifie si les traits tracés forment une boucle fermée.
    Si c'est le cas, retourne True sinon False.

    :param etat: dict
    :param taille_plateau: tuple
    :return: bool

    # Grille triviale
    >>> boucle_ferme({((1, 0), (1, 1)) : 1, ((0, 1), (1, 1)): 1,\
    ((1, 1), (2, 1)): 1, ((1, 1), (1, 2)): 1}, (2, 2))
    False

    # Grille triviale
    >>> boucle_ferme({((0, 0), (0, 1)): 1, ((0, 0), (1, 0)): 1,\
    ((1, 0), (2, 0)): 1, ((2, 0), (2, 1)): 1, ((1, 2), (2, 2)): 1,\
    ((2, 1), (2, 2)): 1, ((0, 2), (1, 2)): 1, ((0, 1), (0, 2)): 1}, (2, 2))
    True
    """
    nombre_trait = 0
    # Segment par défaut, pour éviter de créer une erreur si etat est vide
    segment = ((0, 0), (0, 1))
    # Pour chaque segment de etat
    for cle in etat:
        # Si la valeur est positive, alors c'est un trait, on le compte
        if etat[cle] >= 1:
            nombre_trait += 1
            segment = cle
    # On compare les deux valeurs obtenues pour savoir si la boucle est unique
    return nombre_trait == longueur_boucle(etat, segment, taille_plateau)


def victoire(indices, etat, taille_plateau):
    """
    Cette fonction vérifie si le joueur a formé une boucle fermée en respectant
    les indices de la grille.
    Si ces deux conditions sont respectées alors le joueur gagne et la fonction
    retourne True, sinon False.

    :param indices: list
    :param etat: dict
    :param taille_plateau: tuple
    :return: bool

    >>> victoire([[2, 2], [2, 2]], {((0, 1), (1, 1)): 1, ((1, 0), (1, 1)): 1,\
    ((1, 1), (2, 1)): 1, ((1, 1), (1, 2)): 1}, (2, 2))
    False

    >>> victoire([[2, 2], [2, 2]], {((0, 0), (0, 1)): 1}, (2, 2))
    False

    >>> victoire([[2, 2], [2, 2]], {((0, 0), (0, 1)): 1, ((0, 0), (1, 0)): 1,\
    ((1, 0), (2, 0)): 1, ((2, 1), (2, 2)): 1, ((1, 2), (2, 2)): 1,\
    ((2, 0), (2, 1)): 1, ((0, 2), (1, 2)): 1, ((0, 1), (0, 2)): 1}, (2, 2))
    True
    """
    return (indices_satisfaits(indices, etat, taille_plateau) and
            boucle_ferme(etat, taille_plateau))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
