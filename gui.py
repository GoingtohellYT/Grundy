from turtle import *

# -------------- Création des tortues nécessaires à l'affichage du jeu -------------- #

setup(1500, 900)

to = Turtle()  # tortue pour dessiner le jeu (objets et séparateurs)
to.speed(0)  # on met la vitesse de la tortue à la vitesse maximale pour ne pas ralentir le jeu

td = Turtle()  # tortue pour dessiner le décor (arrière-plan)
td.speed(0)  # on met la tortue en vitesse maximale durant la période de dev -> possibilité de la ralentir ensuite pour admirer la création du décor

tx = Turtle()  # tortue pour afficher les actions de l'ordi


def dessineCroix(x, y, l, c, t):
    """
    Fonction qui dessine une croix dans le carré de côté l dont le point en bas à gauche a pour coordonnées (x,y)
    """
    t.up()
    t.goto(x, y)
    t.down()
    t.color(c)
    t.width(5)
    t.goto(x + l, y + l)
    t.up()
    t.goto(x + l, y)
    t.down()
    t.goto(x, y + l)
    t.width(1)


def dessineSeparateur(x, y, l, t, c="red"):
    """
    Fonction qui dessine un séparateur à l'écran

    Pré-conditions :
        x et y sont les coordonnées de départ
        l est la hauteur du séparateur
        t est l'instance() de Turtle à utiliser
        c est la couleur du séparateur
    Post-conditions :
        La valeur des paramètres est inchangée
    """
    t.up()
    t.goto(x, y)
    t.down()
    t.color(c)
    t.width(5)
    t.goto(x, y + l)
    t.width(1)


def dessineObjet(x, y, t, n, c="blue"):
    """
    Fonction qui dessine un objet à l'écran

    Pré-conditions :
        x et y sont les coordonnées de départ
        t est l'instance de Turtle() à utiliser
        n est le numéro de l'objet
        c est la couleur du séparateur
    Post-conditions :
        La valeur des paramètres est inchangée
    """
    t.up()
    t.goto(x, y)
    t.down()
    t.color(c)
    t.circle(20)
    t.write(str(n))


def representationJeu(jeu, tortue=to, x=-120, y=100):
    """
    Fonction qui représente l'état actuel du jeu

    Pré-conditions :
        jeu est la structure actuelle du jeu
        tortue est une instance de Turtle()
        x et y sont les coordonnées de départ
    Post-conditions :
        Le jeu est dessiné à l'écran
    """
    objets = [dessineObjet, dessineObjet]
    separateurs = [dessineSeparateur, dessineSeparateur]
    x_base = x
    for j in range(len(jeu)):  # Pour chaque type d'ensemble
        separateurs[j](x, y, 100, tortue)
        x += 25
        for e in jeu[j]:  # Pour chaque ensemble
            for i in range(e):
                objets[j](x, y, tortue, i + 1)
                if i == e - 1:  # Si c'est le dernier élément, on laisse moins d'espace pour ne pas avoir un trou avant le séparateur
                    x += 30
                else:
                    x += 50
            separateurs[j](x, y, 100, tortue)
            x += 25
        y -= 300  # on change la hauteur pour le type d'ensemble suivant
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
    tortue.write(text, font=("arial", 18, "bold"))


# on dessine le décor, ici 2 croix, l'une verte, l'autre jaune
dessineCroix(-100, -150, 100, "green", td)
dessineCroix(100, -150, 50, "yellow", td)
