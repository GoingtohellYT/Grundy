from turtle import *
from decor import td

colormode(255)


def setup_perso(x, y, tortue, c, fill=True):
    tortue.up()
    tortue.goto(x, y)
    tortue.down()
    if fill:
        tortue.fillcolor(c)
        tortue.begin_fill()


def rectangle(x, y, longueur, largeur, c, tortue=td):
    setup_perso(x, y, tortue, c)
    for i in range(2):
        tortue.forward(longueur)
        tortue.left(90)
        tortue.forward(largeur)
        tortue.left(90)
    tortue.end_fill()


def dessinePolygone(nombreCotes, longueurCotes, x, y, couleur, t=td):
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

# Fonction pour dessiner un carré
def dessineCarre(cote, x, y, couleur, t=td):
    dessinePolygone(4, cote, x, y, couleur, t)

# Fonction pour dessiner un triangle
def dessineTriangle(cote, x, y, couleur, t=td):
    dessinePolygone(3, cote, x, y, couleur, t)


def triangle_equi(x, y, longueur, direction, c, tortue=td):
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
    t.up()
    t.goto(x, y - 15)  # Ajustement pour centrer le cercle sur (x, y)
    t.down()
    t.color(c)
    t.begin_fill()
    t.circle(15)
    t.end_fill()