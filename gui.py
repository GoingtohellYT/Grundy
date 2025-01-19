from decor import *

# -------------- Création des tortues nécessaires à l'affichage du jeu -------------- #

setup(1500, 900)

decor()

to = Turtle()  # tortue pour dessiner le jeu (objets et séparateurs)
to.speed(0)  # on met la vitesse de la tortue à la vitesse maximale pour ne pas ralentir le jeu
td.getscreen().tracer(1)  # On désactive l'affichage instantané

tx = Turtle()  # tortue pour afficher les actions de l'ordi
tx.speed(0)
tx.hideturtle()

from elements import *


# ---------- Fonctions de représentation du jeu ---------- #
def representationJeu(jeu, tortue=to, x=-450, y=-60):
    """
    Fonction qui représente l'état actuel du jeu

    Pré-conditions :
        jeu est la structure actuelle du jeu
        tortue est une instance de Turtle()
        x et y sont les coordonnées de départ
    Post-conditions :
        Le jeu est dessiné à l'écran
    """
    objets = [pain_depices, tasse]
    separateurs = [sucre_dorge, dessineGuirlande]
    x_base = x
    for j in range(len(jeu)):  # Pour chaque type d'ensemble
        separateurs[j](x, y, tortue)
        tortue.setheading(0)
        x += 50
        for e in jeu[j]:  # Pour chaque ensemble
            for i in range(e):
                objets[j](x, y + 50, tortue, i + 1)
                tortue.setheading(0)
                if i == e - 1:  # Si c'est le dernier élément, on laisse moins d'espace pour ne pas avoir un trou avant le séparateur
                    x += 80
                else:
                    x += 70
            separateurs[j](x, y, tortue)
            tortue.setheading(0)
            x += 50
        y -= 200  # on change la hauteur pour le type d'ensemble suivant
        x = x_base


def reset(tortue=to):
    """
    Fonction qui efface tout ce qui a été déssiné par la tortue passée en paramètre

    Pré-conditions :
        tortue est une instance de Turtle()
    """
    tortue.clear()


def display_text(text, x, y, tortue=tx, clear=False):
    """
    Fonction qui permet d'écrire un texte à l'écran

    Pré-conditions :
        - text est du type str
        - x et y sont des entiers et définissent les coordonnées du texte
        - tortue est une instance de Turtle()
        - clear vaut True si ce qui a été déssiné par la tortue doit être effacé, False sinon
    Post-conditions :
        Le texte spécifié en paramètre est écrit à l'écran en police Arial, en taille 18, et en gras
    """
    if clear:
        reset(tortue)
    tortue.up()
    tortue.goto(x, y)
    tortue.width(7)
    tortue.down()
    tortue.write(text, font=("arial", 14, "bold"))
