from turtle import *

td = Turtle()  # tortue pour dessiner le décor (arrière-plan)
td.speed(0)  # on met la tortue en vitesse maximale durant la période de dev -> possibilité de la ralentir ensuite pour admirer la création du décor
td.screen.getcanvas().master.resizable(False, False)

from formes_basiques import *

# ---------- Pour cheminée ---------- #
def flamme(x, y, tortue=td, taille=1):
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


def foyer(x, y, tortue=td):
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
    rectangle(x, y, 15, 5, (0, 0, 0))
    rectangle(x + 5, y + 5, 5, 150, (120, 120, 120))
    rectangle(x, y + 5 + 150, 15, 5, (0, 0, 0))


def brique(x, y, portion):
    """
    portion est compris entre 0 et 1
    """
    rectangle(x, y, 22 * portion, 11, (200, 200, 200))


def chaussette(x, y, c, tortue=td):
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
def noeud(x, y, c, tortue=td):
    triangle_equi(x, y, 12, "droite", c)
    tortue.left(90)

    rectangle(x + 10, y - 8, 4, 4, c)

    triangle_equi(x + 24, y, 12, "gauche", c)


def cadeau(x, y, c1, c2, long, larg, tortue=td):
    # On trace la base du cadeau
    rectangle(x, y, long, larg, c1)
    rectangle(x - 2, y + larg, long + 4, 5, c1)

    # On fait la ficelle d'emballage
    rectangle(((x + long) / 2) - 3, y, 6, larg + 5, c2)

    # On fait le noeud
    noeud(x + (long / 2) - 12, y + larg + 11, c2)
    tortue.left(90)


# ---------- Pour le sapin -------- #
def dessineBouleDeNoel(x, y, c, t=td):
    dessineCercle(x, y, t, c)
    
    # Dessiner la suspension 
    t.up()
    t.goto(x, y + 15)  # Départ de la ligne au sommet de la boule
    t.down()
    t.color("black")
    t.goto(x, y + 30)  # Longueur de la ligne
    
   
# Couleurs des boules
couleurs_boules = ["#F40584", "#83F52C", "#2DDFF3", "#FFFF00"]

# Dessin des boules de Noël
def boules():
    x_position = -75
    for c in couleurs_boules:
        dessineBouleDeNoel(x_position, 0, td, c)
        x_position += 50  # Espacement horizontal entre les boules


def dessineSapin(taille,x,y,t=td):
    t.begin_fill()
    dessineCarre(taille,x,y,"#5b3c11",t) #couleur en hexadécimal trouvé à partir d'internet
    t.end_fill()
    t.begin_fill()
    dessineTriangle(taille*2,x+taille/2,y+taille,"#095228",t)
    t.end_fill()
    t.begin_fill()
    dessineTriangle(taille*1.5,x+taille/4,y+taille*1.8,"#095228",t)
    t.end_fill()
    t.begin_fill()
    dessineTriangle(taille,x+taille*1/80,y+taille*2.5,"#095228",t)
    t.end_fill()


def dessineEtoile(x, y, taille, t=td):
    t.up()
    t.goto(x, y)  
    t.down()

    t.color("#C5A643")  
    t.begin_fill()  # Commencer à colorier l'étoile

    for i in range(5):
        t.forward(taille) 
        t.right(144)
    t.end_fill()  # Finir de colorier l'étoile


# Fonction sapinNoel (sapin+étoile)
def sapinNoel(taille, x, y, t=td):
    dessineSapin(taille, x, y, t)
    dessineEtoile(x-taille*3/4, y + taille *3.5, taille / 2)


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

def decor():
    parquet()
    tapis()
    table()
    sapinNoel(50, -75, 50)
    for i in range(1):
        cadeau(-150, 60, "red", "yellow", 30, 25)
    # boules sapin
    # fauteuil
    cheminee(0, 50)


