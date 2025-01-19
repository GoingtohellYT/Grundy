from turtle import *
from decor import td

colormode(255)


def setup_perso(x, y, tortue, c, fill=True):
    """
    Procédure qui permet de préparer la tortue pour un dessin

    Pré-conditions :
        - x et y sont des entiers
        - tortue est une instance de Turtle()
        - c est une couleur (en (r,b,b) ou en chaîne de caractères)
        - fill est un booléen
    Post-conditions :
        la tortue est à l'emplacement voulu, avec la couleur de remplissage voulue
    """
    tortue.up()
    tortue.goto(x, y)
    tortue.down()
    if fill:
        tortue.fillcolor(c)
        tortue.begin_fill()


def rectangle(x, y, longueur, largeur, c, tortue=td):
    """
    Procédure qui trace un rectangle

    Pré-conditions :
        - x, y, longueur, largeur sont des entiers
        - c est une couleur (en (r,b,b) ou en chaîne de caractères)
        - tortue est une instance de Turtle()
    Post-conditions :
        Un rectangle de taille longueur, largeur est dessiné en (x, y)
    """
    setup_perso(x, y, tortue, c)
    for i in range(2):
        tortue.forward(longueur)
        tortue.left(90)
        tortue.forward(largeur)
        tortue.left(90)
    tortue.end_fill()


def dessinePolygone(nombreCotes, longueurCotes, x, y, couleur, t=td):
    """
    Procédure qui trace un polygone régulier

    Pré-conditions :
        - x, y, nombreCotes sont des entiers
        - longueurCotes est un nombre
        - couleur est une couleur (en (r,b,b) ou en chaîne de caractères)
        - t est une instance de Turtle()
    Post-conditions :
        Un polygone de côté longueurCotes, de nombreCotes côtés est dessiné en (x, y)
    """
    t.up()
    t.goto(x, y)
    t.down()
    t.fillcolor(couleur)
    angle = 360 / nombreCotes
    k = 0
    while k < nombreCotes:
        t.left(angle)
        t.forward(longueurCotes)
        k = k + 1


# Fonction pour dessiner un triangle
def dessineTriangle(cote, x, y, couleur, t=td):
    """
    Procédure qui trace un triangle équilatéral

    Pré-conditions :
        - x, y, nombreCotes sont des entiers
        - cote est un nombre
        - couleur est une couleur (en (r,b,b) ou en chaîne de caractères)
        - t est une instance de Turtle()
    Post-conditions :
        Un triangle équilatéral de côté cote est dessiné en (x, y)
    """
    dessinePolygone(3, cote, x, y, couleur, t)


def triangle_equi(x, y, longueur, direction, c, tortue=td):
    """
    Procédure qui trace un triangle équilatéral orienté vers la gauche ou la droite

    Pré-conditions :
        - x, y, nombreCotes sont des entiers
        - longueur est un nombre
        - direction vait "droite" ou "gauche"
        - c est une couleur (en (r,b,b) ou en chaîne de caractères)
        - tortue est une instance de Turtle()
    Post-conditions :
        Un triangle équilatéral de côté longueur, orienté vers la droite ou la gauche est dessiné en (x, y)
    """
    setup_perso(x, y, tortue, c)
    tortue.right(90)
    if direction == "droite":
        for i in range(3):
            tortue.forward(longueur)
            tortue.left(120)
        tortue.end_fill()
    else:
        for i in range(3):
            tortue.forward(longueur)
            tortue.right(120)
        tortue.end_fill()


# Fonction pour dessiner un cercle 
def dessineCercle(x, y, c, t=td):
    """
    Procédure qui trace un cercle rempli

    Pré-conditions :
        - x, y, nombreCotes sont des entiers
        - c est une couleur (en (r,g,b) ou en chaîne de caractères)
        - t est une instance de Turtle()
    Post-conditions :
        Un cercle de rayon 15, de couleur c, est dessiné en (x, y)
    """
    t.up()
    t.goto(x, y - 15)  # Ajustement pour centrer le cercle sur (x, y)
    t.down()
    t.color(c)
    t.begin_fill()
    t.circle(15)
    t.end_fill()
