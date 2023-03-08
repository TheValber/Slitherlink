###############################################################################
#                    Projet Fin Semestre 2 : Slitherlink                      #
#                            Mai 2021 - Juin 2021                             #
#                                                                             #
#                    Valentin Bernier - Jean-Pascal Trinh                     #
###############################################################################


import math
import modules.fltk as fltk


def ordonner_segment(segment):
    """
    Cette fonction ordonne les sommets d'un segment de façon croissante.
    :param segment: tuple, couples de deux sommets
    :return: tuple, segment ordonné de façon croissante

    >>> ordonner_segment(((2, 2), (1, 2))) # Non ordonné
    ((1, 2), (2, 2))

    >>> ordonner_segment(((0, 0), (0, 1))) # Ordonnée
    ((0, 0), (0, 1))
    """
    # Si le premier point est plus grand que le second, on les inverse
    if segment[0] > segment[1]:
        return (segment[1], segment[0])
    # Si les points sont égaux, ce n'est pas un segment
    elif segment[0] == segment[1]:
        print("Ceci n'est pas un segment. C'est un point.")
    # Sinon on garde le segment dans le même ordre
    return segment


def clic_dans_rectangle(evenement, ax, ay, bx, by):
    """
    Cette fonction renvoie True si un clic de la souris est détecté dans le
    rectangle de diagonale ab. Renvoie False sinon.

    :param evenement:
    :param ax: int, coordonnée en x du coin supérieur gauche du rectangle
    :param ay: int, coordonnée en y du coin supérieur gauche du rectangle
    :param bx: int, coordonnée en x du coin inférieur droit du rectangle
    :param by: int, coordonnée en y du coin inférieur droit du rectangle
    :return: bool
    """
    # Si les coordonnées du clic sont comprises entre les coordonnées données
    if ax <= fltk.abscisse(evenement) <= bx and \
            ay <= fltk.ordonnee(evenement) <= by:
        return True
    return False


def detection_clic_segment(x, y, marges):
    """
    Cette fonction détecte si le clic de la souris de coordonées x et y a été
    fait sur un segment (y compris ceux hors de la grille) et si c'est le cas,
    renvoie le segment.

    :param x: int, coordonée en x de la souris
    :param y: int, coordonée en y de la souris
    :param marges: tuple, couple désignant la marge en x et en y
    :return: tuple, couple représentant un segment

    >>> detection_clic_segment(450, 290, (440, 290)) # Dans la grille
    ((0, 0), (0, 1))

    >>> detection_clic_segment(310, 180, (440, 290)) # Hors de la grille
    ((-2, -2), (-1, -2))
    """
    # On calcule les coordonnées du clic dans le repère de la grille
    dx = (x - marges[0]) / 64
    dy = (y - marges[1]) / 64
    # Si la valeur est proche d'un entier alors le clic est proche d'un segment
    # Segment vertical
    if abs(dx - round(dx)) < 0.15:
        # On renvoie le segment correspondant
        return ((math.floor(dy), round(dx)), (math.floor(dy) + 1, round(dx)))
    # Segment horizontal
    elif abs(dy - round(dy)) < 0.15:
        return ((round(dy), math.floor(dx)), (round(dy), math.floor(dx) + 1))


def segment_dans_grille(segment, taille_plateau):
    """
    Cette fonction détecte si le segment est dans la grille. Si c'est le cas,
    renvoie True sinon False.

    :param segment: tuple; couple représentant un segment
    :param taille_plateau: tuple
    :return: bool

    >>> segment_dans_grille(((-1, -1), (-2, -1)) , (5, 5))
    False

    >>> segment_dans_grille(((0, 0), (0, 1)) , (5, 5))
    True
    """
    if segment is None:
        return False
    # On vérifie que les deux coordonnées des deux points du segment sont dans
    # la grille
    for i in range(2):
        for j in range(2):
            if segment[i][j] < 0 or segment[i][j] > taille_plateau[j]:
                return False
    return True


def chargement_grille(fichier):
    """
    Cette fonction charge le fichier dont le nom est donné en paramètre sous
    la forme d'une liste de liste représentant la grille.

    :param fichier: str, nom du fichier
    :return: list, représente la grille vide, None si erreur dans la grille
    """
    grille = []
    longeur_ligne = None
    # On ouvre le fichier en mode lecture
    with open(f"grille/{fichier}.txt", "r") as f:
        # Pour chaque ligne
        for ligne in f:
            # On enlève les caractères en bout de chaine et on la transforme
            # en liste
            lst_ligne = list(ligne.strip())
            # Pour chaque caractère de la liste
            for i, e in enumerate(lst_ligne):
                # Si l'élèment est _ la case est vide, on le remplace par None
                if e == "_":
                    lst_ligne[i] = None
                # Si c'est un chiffre, on le convertit dans le type int
                elif e == "0" or e == "1" or e == "2" or e == "3":
                    lst_ligne[i] = int(lst_ligne[i])
                # Sinon, un caractère non autorisé est présent, on renvoie None
                else:
                    print("Erreur dans la grille : Caractère interdit")
                    return None
            # On ajoute la ligne convertie dans la liste de la grille
            grille.append(lst_ligne)
            # Si la ligne n'est pas de la même taille que la précédente,
            # il y a une erreur, on renvoie None
            if longeur_ligne is not None and len(lst_ligne) != longeur_ligne:
                print("Erreur dans la grille : Lignes de longeurs différentes")
                return None
            longeur_ligne = len(lst_ligne)
    return grille


if __name__ == "__main__":
    import doctest
    doctest.testmod()
