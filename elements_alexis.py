from turtle import *

setup(1500, 900)
colormode(255)
t = Turtle()
t.speed(0)

# On rend la taille de la fenêtre non modifiable
t.screen.getcanvas().master.resizable(False, False)


def setup(x, y, tortue, c):
    tortue.up()
    tortue.goto(x, y)
    tortue.down()
    tortue.fillcolor(c)
    tortue.begin_fill()


def rectangle(x, y, longueur, largeur, c, tortue=t):
    setup(x, y, tortue, c)
    for i in range(2):
        tortue.forward(longueur)
        tortue.left(90)
        tortue.forward(largeur)
        tortue.left(90)
    tortue.end_fill()


def triangle_equi(x, y, longueur, direction, c, tortue=t):
    setup(x, y, tortue, c)
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


# ---------- Pour cheminée ---------- #
def flamme(x, y, tortue=t, taille=1):
    setup(x, y, tortue, (247, 107, 21))
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
    tortue.hideturtle()


def foyer(x, y, tortue=t):
    setup(x, y, tortue, (255, 0, 0))
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
    rectangle(x, y, 15, 5, (0, 0, 0))
    rectangle(x + 5, y + 5, 5, 150, (120, 120, 120))
    rectangle(x, y + 5 + 150, 15, 5, (0, 0, 0))


def brique(x, y, portion):
    """
    portion est compris entre 0 et 1
    """
    rectangle(x, y, 22 * portion, 11, (200, 200, 200))


def chaussette(x, y, c, tortue=t):
    # On fait la forme de la chaussette
    setup(x, y, tortue, c)
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
    setup(x - 3, y + 5, tortue, "white")
    tortue.circle(3)
    tortue.end_fill()

    # On fait la partie blanche en haut de la tortue
    rectangle(x + 17, y + 22, 8, 3, "white")

    # On remet la tortue dans sa position initiale pour faciliter la succession de plusieurs chaussettes
    tortue.up()
    tortue.goto(x, y)
    tortue.right(180)


def cheminee(x, y, tortue=t):
    """
    largeur totale : 300
    hauteur totale : 400
    """
    # On fait la délimitation murale de la cheminée
    rectangle(x, y, 10, 400, "white")
    rectangle(x + 290, y, 10, 400, "white")

    # On fait le mur de briques
    """
    entier = True
    for j in range(36):
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
    """

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
def noeud(x, y, c, tortue=t):
    triangle_equi(x, y, 12, "droite", c)
    tortue.left(90)

    rectangle(x + 10, y - 8, 4, 4, c)

    triangle_equi(x + 24, y, 12, "gauche", c)


def cadeau(x, y, c1, c2, long, larg):
    # On trace la base du cadeau
    rectangle(x, y, long, larg, c1)
    rectangle(x - 2, y + larg, long + 4, 5, c1)

    # On fait la ficelle d'emballage
    rectangle(((x + long) / 2) - 3, y, 6, larg + 5, c2)

    # On fait le noeud
    noeud(x + (long / 2) - 12, y + larg + 11, c2)


# ---------- Pour les ensembles ---------- #
def sucre_dorge(x, y, tortue=t):
    # On fait la forme de base
    setup(x, y, tortue, "white")
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
        rectangle(x, y+(i*10), 12, 5, "red")

    tortue.left(45)
    rectangle(x-1, y+46, 12, 5, "red")
    tortue.left(45)
    rectangle(x-8, y+51, 12, 5, "red")
    tortue.left(45)
    rectangle(x-13, y+50, 15, 5, "red")
    tortue.left(20)
    rectangle(x - 20, y + 40, 15, 5, "red")
    tortue.right(152)  # On remet la tortue vers la droite


def pain_depices(x, y, mult, tortue=t):
    # On fait le contour
    setup(x, y, tortue, (184, 135, 85))

    # tête
    tortue.left(20)
    tortue.circle(50*mult, 320)
    tortue.right(160)

    # côté gauche
    tortue.forward(55*mult)
    tortue.circle(20*mult, 180)
    tortue.forward(15*mult)
    tortue.circle(-20*mult, 100)
    tortue.forward(75*mult)
    tortue.circle(15*mult, 180)
    tortue.forward(50*mult)

    tortue.circle(-10*mult, 160)

    # côté droit
    tortue.forward(50*mult)
    tortue.circle(15*mult, 180)
    tortue.forward(75*mult)
    tortue.circle(-20*mult, 100)
    tortue.forward(15*mult)
    tortue.circle(20*mult, 180)
    tortue.forward(52*mult)

    tortue.end_fill()
    tortue.left(180)  # on remet la tortue vers la droite

    # On fait le visage
    setup(x-(35*mult), y+(45*mult), tortue, "blue")
    tortue.circle(5*mult)
    tortue.up()
    tortue.forward(35*mult)
    tortue.down()
    tortue.circle(5*mult)
    tortue.end_fill()
    tortue.color("white")
    tortue.pensize(5*mult)
    tortue.up()
    tortue.goto(x-(35*mult), y+(30*mult))
    tortue.down()
    tortue.right(80)
    tortue.circle(15*mult, 160)

    # On fait les boutons
    tortue.pensize(1)
    tortue.color("black")
    setup(x-(17*mult), y-(30*mult), tortue, "white")
    tortue.circle(5*mult)
    tortue.end_fill()
    setup(x-(17*mult), y-(50*mult), tortue, "red")
    tortue.circle(5*mult)
    tortue.end_fill()
    setup(x-(17*mult), y-(70*mult), tortue, "green")
    tortue.circle(5*mult)
    tortue.end_fill()

    tortue.right(80)  # On remet la tortue vers la droite


# ---------- Pour le sol ---------- #
def parquet():
    for i in range(0, 10, 2):
        rectangle(-750, -450+(i*50), 500, 50, (168, 116, 63))
        rectangle(-250, -450 + (i * 50), 500, 50, (168, 116, 63))
        rectangle(250, -450 + (i * 50), 500, 50, (168, 116, 63))

    for i in range(1, 11, 2):
        rectangle(-750, -450+(i*50), 250, 50, (168, 116, 63))
        rectangle(-500, -450 + (i * 50), 500, 50, (168, 116, 63))
        rectangle(0, -450 + (i * 50), 500, 50, (168, 116, 63))
        rectangle(500, -450 + (i * 50), 250, 50, (168, 116, 63))


def tapis():
    rectangle(-500, -350, 1000, 380, (162, 22, 30))
    rectangle(-490, -340, 980, 360, (142, 29, 45))


# ---------- Pour la table ---------- #
def table():
    rectangle(-750, -450, 1500, 80, (136, 51, 9))


# ---------- Couronne ---------- # 
def couronne(x, y, tortue=t):
    setup(x, y, tortue, "green")
    for i in range(12):
        tortue.circle(50, 60)
        tortue.right(30)
    tortue.end_fill()
    noeud(x+30)


couronne(0, 0)
done()
