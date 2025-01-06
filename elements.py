from turtle import *
from formes_basiques import *


# ---------- Pour les séparateurs ---------- #

def sucre_dorge(x, y, tortue):
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
        rectangle(x, y+(i*10), 12, 5, "red")

    tortue.left(45)
    rectangle(x-1, y+46, 12, 5, "red")
    tortue.left(45)
    rectangle(x-8, y+51, 12, 5, "red")
    tortue.left(45)
    rectangle(x-13, y+50, 15, 5, "red")
    tortue.left(20)
    rectangle(x - 20, y + 40, 15, 5, "red")
    tortue.right(145)  # On remet la tortue vers la droite


# Liste de couleurs pour la guirlande
couleurs_guirlandes = ["#F40584", "#83F52C", "#2DDFF3", "#FFFF00", "#B026FF"]


# Fonction pour dessiner une guirlande verticale
def dessineGuirlande(x, y, t, n, couleurs):
    for i in range(n):
        # Placer la tortue à la position (x, y - (i * 40)) pour chaque boule
        t.up()
        t.goto(x, y - (i * 40))
        t.down()
        
        # Choisir la couleur de la boule (alterner)
        t.color(couleurs[i % len(couleurs)])
        
        # Dessiner une petite boule (cercle)
        t.begin_fill()
        t.circle(10)  # Rayon de 10
        t.end_fill()
    
    # Dessiner le fil vertical
    t.up()
    t.goto(x, y + 10)  # Aller juste au-dessus de la première boule
    t.setheading(270)  # Orienter la tortue vers le bas (270 degrés)
    t.down()
    t.forward(n * 40)  # Dessiner le fil vertical en fonction du nombre de boules


# --------- Pour les objets --------- #
def pain_depices(x, y, mult, tortue=t):
    # On fait le contour
    setup_perso(x, y, tortue, (184, 135, 85))

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
    setup_perso(x-(35*mult), y+(45*mult), tortue, "blue")
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
    setup_perso(x-(17*mult), y-(30*mult), tortue, "white")
    tortue.circle(5*mult)
    tortue.end_fill()
    setup_perso(x-(17*mult), y-(50*mult), tortue, "red")
    tortue.circle(5*mult)
    tortue.end_fill()
    setup_perso(x-(17*mult), y-(70*mult), tortue, "green")
    tortue.circle(5*mult)
    tortue.end_fill()

    tortue.right(80)  # On remet la tortue vers la droite


def tasse():# Dessiner le corps de la tasse (un carré) 
    t.penup()
    t.goto(-50, -50)  # Positionner la tortue au coin inférieur gauche
    t.pendown()
    t.begin_fill()  
    dessineCarre(100, -50, -50, "red",t)  
    t.end_fill() 
    
    # Dessiner l'anse 
    # 1er demi-cercle, collé au côté gauche du carré
    t.penup()
    t.goto(-150, -50)  # Positionner la tortue sur le côté gauche du carré 
    t.pendown()
    t.setheading(0)  
    t.begin_fill()  
    t.fillcolor("red")  
    t.circle(30, -180)  # Dessiner un demi-cercle tourné vers la droite (effet miroir)
    t.end_fill()  
    
    # 2ème demi-cercle (plus petit), tourné vers la droite, collé au côté gauche du carré
    t.penup()
    t.goto(-150, -50)  # Positionner la tortue au même endroit
    t.pendown()
    t.setheading(0)  
    t.begin_fill()  
    t.fillcolor("white")  # Remplir avec la couleur blanche
    t.circle(20, -180)  
    t.end_fill()
    
    # Terminer le dessin
    t.penup()

