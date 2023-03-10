# Slitherlink [EN]

University project

May 2021 - June 2021

Slitherlink is a puzzle game programmed in Python in which the player, on a grid, must draw lines between points
to form a single loop respecting indices (from 0 to 3) which indicate how many lines surround
a box.

(The in-game menus are in French)

## Specific Features

- Graphical interface with mouse interactions
- Naive automatic solver

---

## How to launch the game?

Run the slitherlink.py file

## How to play ?

### Main Menu

When you launch the game, you arrive on the main menu which offers you several options on which you can click with the mouse:
- A Quit button that will close the game
- Buttons with numbers from 1 to 5 that correspond to the 18 playable grids of different sizes

### Gate

In the left part of the interface is the grid that you will have to solve. To do this, you can use the left click to draw or erase a line and the right click to put or erase a cross to indicate that you are sure that there is no line at this location.

### Interface

#### Satisfied Indices / Closed Loop:

At the top of the interface are two victory conditions that must be met to win. These can change color depending on the state of the grid: Blue if a condition is met, Red if it is not.

#### Moves / Time:

Below, we can find a section in which we can see the number of moves the player has made and the time elapsed since the start of the game.

#### Line Colors:

Towards the middle of the interface, we can find several buttons associated with a color allowing the player to make guesses.
- The Select button is used to select a color
- The Erase button is used to erase all strokes of the selected color
- The Validate button is used to replace the selected color with Blue.
The selected color is displayed at the top right of the color selection area.

#### Cancel :

The undo button is used to undo the player's last move.

#### Classic/Graphical Solver:

The Classic Solver allows you to directly display the solution of the grid. The Graphical Solver allows the same thing as the classic solver but allows you to follow the steps of solving the grid.

#### Restart :

This button allows you to restart a game. Thus the grid becomes empty, the number of moves and the elapsed time are reset.

#### Menu:

This button allows you to return to the menu.

### Console

When the solver (graphical or not) finds a solution, a console message appears. It indicates the time, in seconds, for the solver to solve the grid.

---

---

# Slitherlink [FR]

Projet Universitaire

Mai 2021 - Juin 2021

Le Slitherlink est un jeu de r??flexion programm?? en Python dans lequel le joueur, sur une grille, doit tracer des lignes entre des points
pour former une boucle unique en respectant des indices (de 0 ?? 3) qui indiquent combien de lignes entourent
une case.

(Les menus en jeu sont en Fran??ais)

## Fonctionnalit??s sp??cifiques

- Interface graphique avec des int??ractions ?? la souris
- Solveur automatique naif

---

## Comment lancer le jeu ?

Lancer le fichier slitherlink.py

## Comment jouer ?

### Menu Principal

Au lancement du jeu, vous arrivez sur le menu principal qui vous propose plusieurs options sur lesquelles vous pouvez cliquer avec la souris :
- Un bouton Quitter qui fermera le jeu
- Des boutons avec des chiffres de 1 ?? 5 qui correspondent aux 18 grilles de tailles diff??rentes jouables

### Grille

Dans la partie de gauche de l???interface se trouve la grille que vous allez devoir r??soudre. Pour se faire, vous pouvez utiliser le clic gauche pour tracer ou effacer un trait et le clic droit pour mettre ou effacer une croix afin d???indiquer que vous ??tes s??r qu???il n???y a pas de trait ?? cet endroit.

### Interface

#### Indices Satisfaits / Boucle Ferm??e :

En haut de l???interface se trouve deux conditions de victoire qui doivent ??tre remplies pour gagner. Celles-ci peuvent changer de couleur en fonction de l?????tat de la grille : Bleu si une condition est satisfaite, Rouge si elle ne l???est pas.

#### Coups / Temps :

En dessous, on peut trouver une section dans laquelle on peut voir le nombre de coups que le joueur a effectu?? et le temps ??coul?? depuis le d??but de la partie.

#### Couleurs du Trait :

Vers le milieu de l???interface, on peut trouver plusieurs boutons associ?? ?? une couleur permettant au joueur de faire des suppositions. En effet :
- Le bouton S??lectionner sert ?? s??lectionner une couleur
- Le bouton Effacer sert ?? effacer tous les traits de la couleur s??lectionn??e
- Le bouton Valider sert ?? remplacer la couleur s??lectionn??e par du Bleu.
La couleur s??lectionn??e est affich??e en haut ?? droite de la zone de s??lection de couleur.

#### Annuler :

Le bouton annuler sert ?? annuler le dernier coup du joueur.

#### Solveur Classique/Graphique :

Le Solveur Classique permet d???afficher directement la solution de la grille. Le Solveur Graphique permet la m??me chose que le solveur classique mais permet de suivre les ??tapes de r??solution de la grille.

#### Recommencer :

Ce bouton permet de recommencer une partie. Ainsi la grille devient vide, le nombre de coups et le temps ??coul?? se r??initialisent.

#### Menu :

Ce bouton permet de revenir sur le menu.

### Console

Lorsque le solveur (graphique ou non) trouve une solution, un message en console appara??t. Il indique le temps, en secondes, de r??solution de la grille par le solveur.
