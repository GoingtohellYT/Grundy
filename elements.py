from formes_basiques import *
from gui import to


# ---------- Pour les séparateurs ---------- #
def sucre_dorge(x, y, tortue):
    """
    Procédure qui dessine un sucre d'orge en (x, y)

    Pré-conditions :
        - x est un entier
        - y est un entier
        - tortue est une instance de Turtle()
    Post-conditions :
        Un sucre d'orge est dessiné à l'écran aux coordonnées (x, y)
    """
    # On fait la forme de base
    setup_perso(x, y, tortue, "white")
    tortue.right(90)
    tortue.circle(6, 180)
    tortue.forward(40)
    tortue.circle(24, 180)
    tortue.circle(8, 180)
    tortue.circle(-10, 180)
    tortue.forward(40)
    tortue.end_fill()

    # On ajoute les bandes rouges
    tortue.left(90)
    for i in range(5):
        rectangle(x, y + (i * 10), 12, 5, "red", tortue)

    tortue.left(45)
    rectangle(x - 1, y + 46, 12, 5, "red", tortue)
    tortue.left(45)
    rectangle(x - 8, y + 51, 12, 5, "red", tortue)
    tortue.left(45)
    rectangle(x - 13, y + 50, 15, 5, "red", tortue)
    tortue.left(20)
    rectangle(x - 20, y + 40, 15, 5, "red", tortue)
    # tortue.right(155)  # On remet la tortue vers la droite
    # tortue.up()


# Fonction pour dessiner une guirlande verticale
def dessineGuirlande(x, y, t, n=3):
    """
    Procédure qui dessine une guirlande en (x, y)

    Pré-conditions :
        - x est un entier
        - y est un entier
        - n est un entier
        - t est une instance de Turtle()
    Post-conditions :
        Une guirlande est dessiné à l'écran aux coordonnées (x, y)
    """
    # Liste de couleurs pour la guirlande
    couleurs = ["#F40584", "#83F52C", "#2DDFF3", "#FFFF00", "#B026FF"]

    for i in range(n):
        # Placer la tortue à la position (x, y - (i * 40)) pour chaque boule
        t.up()
        t.goto(x, y + (i * 40))
        t.down()

        # Choisir la couleur de la boule (alterner)
        t.fillcolor(couleurs[i % len(couleurs)])

        # Dessiner une petite boule (cercle)
        t.begin_fill()
        t.circle(10)  # Rayon de 10
        t.end_fill()

    # Dessiner le fil vertical
    t.up()
    t.goto(x, y - 10)  # Aller juste au-dessus de la première boule
    t.setheading(90)  # Orienter la tortue vers le bas (270 degrés)
    t.down()
    t.forward(n * 40)  # Dessiner le fil vertical en fonction du nombre de boules
    t.setheading(0)


# --------- Pour les objets --------- #
def pain_depices(x, y, tortue, nb, mult=0.3):
    """
    Procédure qui dessine un pain d'épice aux coordonnées (x, y)

    Pré-conditions :
        - x est un entier
        - y est un entier
        - tortue est une instance de Turtle()
        - nb est un entier
        - mult est un nombre qui défini par combien on multiplie la taille du dessin
    Post-condition :
        Un d'épice de la taille voulue est dessiné en (x, y)
    """
    # On fait le contour
    setup_perso(x, y, tortue, (184, 135, 85))

    # tête
    tortue.left(20)
    tortue.circle(50 * mult, 320)
    tortue.right(160)

    # côté gauche
    tortue.forward(55 * mult)
    tortue.circle(20 * mult, 180)
    tortue.forward(15 * mult)
    tortue.circle(-20 * mult, 100)
    tortue.forward(75 * mult)
    tortue.circle(15 * mult, 180)
    tortue.forward(50 * mult)

    tortue.circle(-10 * mult, 160)

    # côté droit
    tortue.forward(50 * mult)
    tortue.circle(15 * mult, 180)
    tortue.forward(75 * mult)
    tortue.circle(-20 * mult, 100)
    tortue.forward(15 * mult)
    tortue.circle(20 * mult, 180)
    tortue.forward(52 * mult)

    tortue.end_fill()
    tortue.left(180)  # on remet la tortue vers la droite

    # On fait le visage
    setup_perso(x - (35 * mult), y + (45 * mult), tortue, "blue")
    tortue.circle(5 * mult)
    tortue.up()
    tortue.forward(35 * mult)
    tortue.down()
    tortue.circle(5 * mult)
    tortue.end_fill()
    tortue.color("white")
    tortue.pensize(5 * mult)
    tortue.up()
    tortue.goto(x - (35 * mult), y + (30 * mult))
    tortue.down()
    tortue.right(80)
    tortue.circle(15 * mult, 160)

    # On fait les boutons
    tortue.pensize(1)
    tortue.color("black")
    setup_perso(x - (17 * mult), y - (30 * mult), tortue, "white")
    tortue.circle(5 * mult)
    tortue.end_fill()
    setup_perso(x - (17 * mult), y - (50 * mult), tortue, "red")
    tortue.circle(5 * mult)
    tortue.end_fill()
    setup_perso(x - (17 * mult), y - (70 * mult), tortue, "green")
    tortue.circle(5 * mult)
    tortue.end_fill()

    tortue.right(80)  # On remet la tortue vers la droite
    setup_perso(x, y - (100 * mult), tortue, "black", False)
    tortue.write(str(nb))


def flocon(t, mult=0.15):
    """
    Procédure qui dessine un flocon en (x, y)

    Pré-conditions :
        - t est une instance de Turtle()
    Post-conditions :
        Un flocon est dessiné à l'écran aux coordonnées (x, y)
    """
    to.getscreen().tracer(0)  # On affiche le flocon instantanément pour ne pas ralentir trop le jeu
    for i in range(3):
        for i in range(3):
            t.forward(30 * mult)
            t.backward(30 * mult)
            t.right(45)
        t.left(90)
        t.backward(30 * mult)
        t.left(45)
    t.right(90)
    t.forward(90 * mult)
    to.getscreen().tracer(1)  # On remet la vitesse de dessin par défaut


def tasse(x, y, t, nb):  # Dessiner le corps de la tasse (un carré)
    """
    Procédure qui dessine une tasse en (x, y)

    Pré-conditions :
        - x est un entier
        - y est un entier
        - nb est un entier
        - t est une instance de Turtle()
    Post-conditions :
        Une tasse est dessinée à l'écran aux coordonnées (x, y)
    """
    t.penup()
    t.goto(x, y)  # Positionner la tortue au coin inférieur gauche
    t.pendown()
    t.begin_fill()
    rectangle(x, y, 50, 50, "red", t)
    t.end_fill()

    # Dessiner l'anse 
    # 1er demi-cercle, collé au côté gauche du carré
    t.goto(x, y)
    t.setheading(0)
    t.begin_fill()
    t.fillcolor("red")
    t.circle(15, -180)  # Dessiner un demi-cercle tourné vers la droite (effet miroir)
    t.end_fill()

    # 2ème demi-cercle (plus petit), tourné vers la droite, collé au côté gauche du carré
    t.goto(x, y)
    t.setheading(0)
    t.begin_fill()
    t.fillcolor((142, 29, 45))  # Remplir avec la couleur du tapis
    t.circle(8, -180)
    t.end_fill()

    # ajout du flocon de neige
    t.penup()
    t.goto(x + 15, y + 33)  # Positionner la tortue au centre de la tasse
    t.begin_fill()
    t.color("white")
    t.pendown()
    for i in range(8):
        flocon(t)
        t.left(45)
    t.end_fill()
    t.color("black")

    t.up()
    t.forward(-20)
    t.write(str(nb))

    # Terminer le dessin
    t.penup()
