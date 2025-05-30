# Binôme : Héloïse Fouillout et Alexis Mengual
from turtle import *
from random import choice, randint

td = Turtle()  # tortue pour dessiner le décor (arrière-plan)
td.screen.getcanvas().master.resizable(False, False)  # on empêche le joueur de redimensionner la fenêtre
td.hideturtle()
td.screen.tracer(0)  # On affiche le décor instantanément

from formes_basiques import *


# ---------- Pour cheminée ---------- #
def flamme(x, y, tortue=td, taille=1):
    """
    Procédure qui dessine une flamme

    Pré-conditions :
        - x et y sont des entiers
        - tortue est une instance de Turtle()
        - taille est un nombre qui défini le facteur par lequel on multiplie la taille du dessin
    Post-condition :
        Une flamme est dessinée aux coordonnées (x, y)
    """
    setup_perso(x, y, tortue, (247, 107, 21))
    tortue.color((247, 107, 21))

    # On trace l'arc d cercle qui sert de base
    tortue.right(90)
    tortue.circle(50 * taille, 200)

    tortue.left(150)
    tortue.circle(-20 * taille, 150)

    tortue.right(20)
    tortue.circle(200 * taille, 15)

    tortue.left(150)
    tortue.circle(-100 * taille, 30)

    tortue.right(135)
    tortue.circle(13 * taille, -170)

    tortue.goto(x, y)
    tortue.end_fill()
    tortue.setheading(0)


def foyer(x, y, tortue=td):
    """
    Procédure qui dessine le foyer de la cheminée

    Pré-conditions :
        - x et y sont des entiers
        - tortue est une instance de Turtle()
    Post-condition :
         Le foyer est dessiné aux coordonnées (x, y)
    """
    setup_perso(x, y, tortue, (255, 0, 0))
    tortue.color((255, 0, 0))

    tortue.left(90)
    tortue.forward(40)
    tortue.circle(-48, 180)
    tortue.forward(40)

    tortue.left(90)
    tortue.forward(4.8)
    tortue.left(90)
    tortue.forward(40)
    tortue.circle(52.8, 180)
    tortue.forward(40)
    tortue.left(90)
    tortue.forward(4.8)

    tortue.end_fill()

    # On colorie l'intérieur
    tortue.fillcolor((178, 177, 85))
    tortue.begin_fill()
    tortue.forward(96)
    tortue.left(90)
    tortue.forward(40)
    tortue.circle(48, 180)
    tortue.forward(40)
    tortue.end_fill()
    # On se replace vers la droite
    tortue.left(90)


def pilier(x, y):
    """
    Procédure qui dessine un pilier de la cheminée

    Pré-conditions :
        - x et y sont des entiers
    Post-condition :
         Le pilier est dessiné aux coordonnées (x, y)
    """
    rectangle(x, y, 15, 5, (0, 0, 0))
    rectangle(x + 5, y + 5, 5, 150, (120, 120, 120))
    rectangle(x, y + 5 + 150, 15, 5, (0, 0, 0))


def brique(x, y, portion):
    """
    Procédure qui dessine une brique de mur de la cheminée

    Pré-conditions :
        - x et y sont des entiers
        - portion est un nombre compris entre 0 et 1
    Post-condition :
         La brique est dessinée aux coordonnées (x, y)
    """
    rectangle(x, y, 22 * portion, 11, (200, 200, 200))


def chaussette(x, y, c, tortue=td):
    """
    Procédure qui dessine une chaussette

    Pré-conditions :
        - x et y sont des entiers
        - c est la couleur de la chaussette
        - tortue est une instance de Turtle()
    Post-condition :
         La chaussette est dessinée aux coordonnées (x, y)
    """
    # On fait la forme de la chaussette
    setup_perso(x, y, tortue, c)
    tortue.forward(12)
    tortue.circle(5, 90)
    tortue.forward(15)
    tortue.left(90)
    tortue.forward(8)
    tortue.left(90)
    tortue.forward(10)
    tortue.circle(-5, 90)
    tortue.forward(7)
    tortue.end_fill()

    # On trace le bout blanc de la chaussette
    setup_perso(x - 3, y + 5, tortue, "white")
    tortue.circle(3)
    tortue.end_fill()

    # On fait la partie blanche en haut de la tortue
    rectangle(x + 17, y + 22, 8, 3, "white")

    # On remet la tortue dans sa position initiale pour faciliter la succession de plusieurs chaussettes
    tortue.up()
    tortue.goto(x, y)
    tortue.right(180)


def cheminee(x, y, tortue=td):
    """
    Procédure qui dessine la cheminée dans son ensemble

    Pré-conditions :
        - x et y sont des entiers
        - tortue est une instance de Turtle()
    Post-condition :
         La cheminée est dessinés aux coordonnées (x, y)
         (largeur totale : 300
          hauteur totale : 400)
    """
    # On fait la délimitation murale de la cheminée
    rectangle(x, y, 10, 400, (91, 60, 17))
    rectangle(x + 290, y, 10, 400, (91, 60, 17))

    # On fait le mur de briques
    entier = True
    for j in range(37):
        if entier:
            for i in range(12):
                brique(x + 10 + (22 * i), y + (11 * j), 1)
            brique(x + 274, y + (11 * j), 0.73)
            entier = False
        else:
            brique(x + 10, y + (11 * j), 0.73)
            for i in range(12):
                brique(x + 10 + (22 * 0.7) + (22 * i), y + (11 * j), 1)
            entier = True

    # On place les piliers dans la cheminée
    pilier(x + 69, y)
    pilier(x + 69 + 132, y)

    # On insère la poutre sur laquelle accrocher les chaussettes
    rectangle(x + 69, y + 161, 147, 10, "brown")

    # On masque les briques entre les piliers
    tortue.color((180, 65, 4))
    rectangle(x + 85, y + 1, 117, 160, (180, 65, 4))
    rectangle(x + 80, y + 6, 5, 148, (180, 65, 4))
    rectangle(x + 200, y + 6, 5, 148, (180, 65, 4))

    tortue.color("black")  # On remet la couleur de contour par défaut

    # On accroche les chaussettes
    couleurs = ["red", "green", "yellow"]
    for i in range(len(couleurs)):
        chaussette(x + 100 + (39 * i), y + 146, couleurs[i])

    # On place le foyer
    foyer(x + 94, y)

    # On place le feu dans la cheminée
    flamme(x + 115, y + 30, taille=0.5)


# ---------- Pour les cadeaux ---------- #
def noeud(x, y, c, tortue=td):
    """
    Procédure qui dessine un nœud

    Pré-conditions :
        - x et y sont des entiers
        - c est la couleur du nœud
        - tortue est une instance de Turtle()
    Post-condition :
         Le nœud est dessiné aux coordonnées (x, y)
    """
    triangle_equi(x, y, 12, "droite", c)
    tortue.left(90)

    rectangle(x + 10, y - 8, 4, 4, c)

    triangle_equi(x + 24, y, 12, "gauche", c)


def cadeau(x, y, c1, c2, long, larg, tortue=td, nd=True):
    """
    Procédure qui dessine un cadeau

    Pré-conditions :
        - x et y sont des entiers
        - c1 est la couleur du cadeau
        - c2 est la couleur du nœud
        - long est la longueur du cadeau
        - larg est la largeur du cadeau
        - tortue est une instance de Turtle()
        - nd est un booléen
    Post-condition :
         Le foyer est dessiné aux coordonnées (x, y)
    """
    # On trace la base du cadeau
    rectangle(x, y, long, larg, c1)
    rectangle(x - 2, y + larg, long + 4, 5, c1)

    # On fait la ficelle d'emballage
    rectangle(x + (long / 2) - 3, y, 6, larg + 5, c2)

    # On fait le nœud
    if nd:
        noeud(x + (long / 2) - 12, y + larg + 11, c2)
    tortue.setheading(0)


# ---------- Pour le sapin -------- #
def dessineBouleDeNoel(x, y, c, t=td):
    """
    Procédure qui dessine une boule de Noël

    Pré-conditions :
        - x et y sont des entiers
        - c est la couleur de la boule (chaine de caractères ou 3-uplets)
        - t est une instance de Turtle()
    Post-conditions :
        Une boule est affichée à l'écran
    """
    dessineCercle(x, y, c, t)

    # Dessiner la suspension 
    t.up()
    t.goto(x, y + 15)  # Départ de la ligne au sommet de la boule
    t.down()
    t.color("black")
    t.goto(x, y + 30)  # Longueur de la ligne


def dessineSapin(taille, x, y, t=td):
    """
    Procédure qui dessine le sapin de Noël

    Pré-conditions :
        - taille est un entier
        - x et y sont des entiers
        - t est une instance de Turtle()
    Post-conditions :
        Un sapin de taille "taille" est affiché aux coordonnées (x, y)
    """
    t.begin_fill()
    rectangle(x-taille, y, taille, taille, "#5b3c11")
    t.end_fill()
    t.begin_fill()
    dessineTriangle(taille * 2, x + taille / 2, y + taille, "#095228", t)
    t.end_fill()
    t.begin_fill()
    dessineTriangle(taille * 1.5, x + taille / 4, y + taille * 1.8, "#095228", t)
    t.end_fill()
    t.begin_fill()
    dessineTriangle(taille, x + taille * 1 / 80, y + taille * 2.5, "#095228", t)
    t.end_fill()


def dessineEtoile(x, y, taille, t=td):
    """
    Procédure qui dessine une étoile

    Pré-conditions :
        - x et y sont des entiers
        - taille est un entier
        - t est une instance de Turtle()
    Post-conditions :
        Une étoile de taille "taille" est affichée à l'écran aux coordonnées (x, y)
    """
    t.up()
    t.goto(x, y)
    t.down()

    t.color("#C5A643")
    t.begin_fill()  # Commencer à colorier l'étoile

    for i in range(5):
        t.forward(taille)
        t.right(144)
    t.end_fill()  # Finir de colorier l'étoile
    t.color("black")


# Fonction sapinNoel (sapin+étoile)
def sapinNoel(taille, x, y, t=td):
    """
    Procédure qui dessine le sapin et l'étoile

    Pré-conditions :
        - x et y sont des entiers
        - taille est un entier
        - t est une instance de Turtle()
    Post-conditions :
        Le sapin et l'étoile sont dessinés
    """
    dessineSapin(taille, x, y, t)
    dessineEtoile(x - taille * 3 / 4, y + taille * 3.5, taille / 2)

    # Paramètres des boules
    couleurs_boules = ["#F40584", "#83F52C", "#2DDFF3", "#FFFF00"]
    pos_boules = [(x, y+taille*1.5), (x-taille/2, y+taille*2.6), (x-taille/1.2, y+taille*1.8)]
    
    # On place les boules aléatoirement sur le sapin
    for i in range(randint(3, 3)):
        coordonnees = choice(pos_boules)
        dessineBouleDeNoel(coordonnees[0], coordonnees[1], choice(couleurs_boules))
        pos_boules.remove(coordonnees)  # Pour ne pas dessiner deux boules au même endroit


# ---------- Pour le sol ---------- #
def parquet():
    """
    Procédure qui dessine le parquet

    Post-condition :
         Le parquet est dessiné sur la fenêtre de jeu
    """
    for i in range(0, 10, 2):
        rectangle(-750, -450 + (i * 50), 500, 50, (168, 116, 63))
        rectangle(-250, -450 + (i * 50), 500, 50, (168, 116, 63))
        rectangle(250, -450 + (i * 50), 500, 50, (168, 116, 63))

    for i in range(1, 11, 2):
        rectangle(-750, -450 + (i * 50), 250, 50, (168, 116, 63))
        rectangle(-500, -450 + (i * 50), 500, 50, (168, 116, 63))
        rectangle(0, -450 + (i * 50), 500, 50, (168, 116, 63))
        rectangle(500, -450 + (i * 50), 250, 50, (168, 116, 63))


def tapis():
    """
    Procédure qui dessine le tapis

    Post-condition :
         Le tapis est dessiné sur la fenêtre de jeu
    """
    rectangle(-500, -350, 1000, 380, (162, 22, 30))
    rectangle(-490, -340, 980, 360, (142, 29, 45))


# ---------- Pour la table ---------- #
def table():
    """
    Procédure qui dessine la table

    Post-condition :
         La table est dessinée sur la fenêtre de jeu
    """
    rectangle(-750, -450, 1500, 80, (136, 51, 9))


couleurs_cadeaux = [("red", "yellow"), ("purple", "green"), ("blue", "orange")]


def pile_cadeaux(x, y, n, couleurs):
    """
    Procédure récursive qui crée une pile de cadeau

    Pré-conditions :
        - x, y et n sont des entiers
    Post-conditions :
        Une pile de base n cadeaux est dessinée en (x, y)
    """
    if n == 0:
        return
    elif n == 1:
        cadeau(x, y, "red", "yellow", 30, 25)
    else:
        for i in range(n):
            couleur = choice(couleurs)
            cadeau(x+i*40, y, couleur[0], couleur[1], 30, 25, nd=False)
        pile_cadeaux(x+20, y+30, n-1, couleurs)


def decor():
    """
    Procédure qui dessine tout le décor

    Post-condition :
         Le décor est dessiné sur la fenêtre de jeu
    """
    parquet()
    tapis()
    table()
    sapinNoel(100, 25, 50)
    sapinNoel(100,75,50)

    # On fait les cadeaux au pied du sapin
    for i in range(12):
        cadeau(-50 + i * 40, 50, "red", "yellow", 30, 25)

    pile_cadeaux(-650, 50, 7, couleurs_cadeaux)
    cheminee(200, 50)
