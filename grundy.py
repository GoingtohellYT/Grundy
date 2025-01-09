# Binôme : Héloïse Fouillout et Alexis Mengual
# Jeu de Grundy

"""Le jeu consiste à séparer des ensembles d'objets. La position de départ consiste en un unique ensemble d'objets.
  Pour jouer, le seul coup possible consiste à séparer un ensemble d'objets en deux ensembles de tailles distinctes et
  non nulles. Les joueurs jouent à tour de rôle, jusqu'à ce que l'un d'entre eux ne puisse plus jouer."""

from random import randint  # pour que l'ordinateur puisse jouer aléatoirement
from time import sleep  # pour que l'ordinateur puisse réfléchir 1 seconde
from gui import representationJeu, reset, display_text  # pour l'interface graphique
from turtle import numinput, done  # pour demander les valeurs et garder la fenêtre ouverte en fin de partie


def initJeu(n, nb_e):
    """
    Initialise le jeu en début de partie.

    Pré-conditions :
        n est le nombre d'éléments à placer dans chaque ensemble
        nb_e est le nombre de types d'ensembles à créer
    Renvoie :
        le jeu sous la forme d'une liste de listes. Chaque sous liste représente un type d'ensemble
    """
    jeu = list()
    for i in range(nb_e):
        jeu.append([n])
    return jeu


def finDeJeu(jeu):
    """
    Défini si on peut encore jouer, soit quand au moins 1 ensemble contient plus de 2 éléments
    
    Renvoie :
        - True si le jeu est fini
        - False si on peut toujours jouer
    Pré-conditions :
        jeu est une liste de listes d'entiers
    Post-conditions :
        jeu est inchangée après l'exécution de la fonction
    """
    i = 0
    fini = True  # On suppose le jeu terminé
    while fini and i < len(jeu):
        j = 0
        while fini and j < len(jeu[i]):
            if jeu[i][j] > 2:
                fini = False  # Si un ensemble contient plus de 2 éléments, on indique que le jeu n'est pas terminé
            j += 1
        i += 1
    return fini


def typeEnsembleJouable(type_ens):
    """
    Vérifie s'il est possible de jouer dans le type d'ensemble passé en paramètre

    Renvoie :
        True si on peut jouer dans ce type d'ensemble, False sinon
    Pré-conditions :
        type_ens est une liste qui correspond au type d'ensemble dont on souhaite vérifier si l'on peut jouer dedans.
    Post-conditions :
        type_ens est inchangé
    """
    jouable = False
    i = 0
    while not jouable and i < len(type_ens):
        if type_ens[i] > 2:
            jouable = True
        i += 1
    return jouable


def choixTypeEnsembleJoueur(jeu):
    """
    Permet au joueur de sélectionner le type d'ensemble dans lequel il souhaite jouer

    Renvoie :
        le type d'ensemble dans lequel le joueur souhaite jouer
    Pré-conditions :
        jeu est une liste de liste qui suit la structure de jeu générée par la fonction initJeu
    Post-conditions :
        jeu est inchangée
    """
    choix_joueur = int(numinput("Type d'ensemble", "Dans quel type d'ensemble souhaitez-vous jouer ?"))
    while not (0 < choix_joueur <= len(jeu) and typeEnsembleJouable(jeu[choix_joueur - 1])):
        choix_joueur = int(numinput("Type d'ensemble", "Dans quel type d'ensemble souhaitez-vous jouer ?"))
    return choix_joueur


# Fonction dédiée à lire l'ensemble dans lequel le joueur veut jouer
# Demande un n° d'ensemble tant que le joueur donne un n° qui n'est pas correct
# Renvoie le n° d'ensemble
def choixEnsembleJoueur(type_ens):
    """
    Détermine l'ensemble dans lequel le joueur souhaite jouer (les ensembles sont numérotés de 1 à len(type_ens))

    Renvoie :
        le numéro de l'ensemble dans lequel le joueur souhaite jouer
    Pré-conditions :
        type_ens est une liste de nombre entiers strictement positifs
    Post-conditions :
        type_ens reste inchangée suite à l'exécution.
        Le joueur ne peut jouer dans un ensemble qui contient moins de 3 éléments
    """
    choix_joueur = int(numinput("Ensemble", "Dans quel ensemble souhaitez-vous jouer ?"))
    while not (0 < choix_joueur <= len(type_ens) and type_ens[choix_joueur - 1] > 2):
        choix_joueur = int(numinput("Ensemble", "Dans quel ensemble souhaitez-vous jouer ?"))
    return choix_joueur


# Fonction dédiée à lire à quel endroit le joueur veut couper l'ensemble
# nbEltEnsemble est le nombre d'éléments de l'ensemble dans lequel on joue
# Demande un n° de coupe tant que le joueur donne un n° qui n'est pas correct
# Renvoie le n° de coupe
def choixCoupeJoueur(nbEltEnsemble):
    """
    Détermine à quel endroit le joueur souhaite couper l'ensemble

    Renvoie :
        le numéro de coupe
    Pré-conditions :
        nbEltEnsemble est un nombre entier qui correspond au nombre d'éléments de l'ensemble
    Post-conditions :
        nbEltEnsemble est inchangé après l'exécution
    """
    choix_joueur = int(numinput("Coupe", "A quel endroit souhaitez-vous couper ? "))
    while not (0 < choix_joueur < nbEltEnsemble and choix_joueur * 2 != nbEltEnsemble):
        choix_joueur = int(numinput("Coupe", "A quel endroit souhaitez-vous couper ? "))
    return choix_joueur


# fait jouer le joueur
# utilise choixEnsembleJoueur et choixCoupeJoueur
# met à jour le jeu
def joueurJoue(jeu):
    """
    Fait jouer le joueur

    Renvoie :
        Rien
    Pré-conditions :
        jeu est une liste de nombre entiers strictement positifs
    Post-conditions :
        jeu est modifié de façon à refléter l'action du joueur
    """
    type_ens_joueur = choixTypeEnsembleJoueur(jeu)
    ensemble_joueur = choixEnsembleJoueur(jeu[type_ens_joueur - 1])
    nb_elem_ensemble = jeu[type_ens_joueur - 1][ensemble_joueur - 1]

    coupe_joueur = choixCoupeJoueur(nb_elem_ensemble)
    jeu[type_ens_joueur - 1][ensemble_joueur - 1] = coupe_joueur  # On change la taille de l'ensemble coupé

    jeu[type_ens_joueur - 1].insert(ensemble_joueur,
                                    nb_elem_ensemble - coupe_joueur)  # On insère un ensemble avec les éléments suivants la coupe
    display_text(f"Vous avez joué dans le type d'ensemble n°{type_ens_joueur} et avez choisi de couper l'ensemble {ensemble_joueur} à l'endroit {coupe_joueur}", -610, -400, clear=True)



def choixTypeEnsembleOrdi(jeu):
    """
    Permet à l'ordi de sélectionner le type d'ensemble dans lequel il joue

    Renvoie :
        le type d'ensemble dans lequel l'ordi joue
    Pré-conditions :
        jeu est une liste de liste qui suit la structure de jeu générée par la fonction initJeu
    Post-conditions :
        jeu est inchangée
    """
    choix_ordi = randint(1, len(jeu))
    while not (typeEnsembleJouable(jeu[choix_ordi - 1])):
        choix_ordi = randint(1, len(jeu))
    return choix_ordi


# Fait choisir un ensemble aléatoirement à l'ordinateur
# renvoie le n° de l'ensemble
# tire un n° d'ensemble tant que l'ensemble choisi est trop petit pour être découpé
def choixEnsembleOrdi(type_ens):
    """
    Détermine l'ensemble dans lequel l'ordi joue (les ensembles sont numérotés de 1 à len(type_ens))

    Renvoie :
        le numéro de l'ensemble dans lequel l'ordi joue
    Pré-conditions :
        type_ens est une liste de nombre entiers strictement positifs
    Post-conditions :
        type_ens reste inchangée suite à l'exécution.
        L'ordi ne peut jouer dans un ensemble qui contient moins de 3 éléments
    """
    choix_ordi = randint(1, len(type_ens))
    while not (type_ens[choix_ordi - 1] > 2):
        choix_ordi = randint(1, len(type_ens))
    return choix_ordi


# Fait choisir une coupe aléatoirement à l'ordinateur
# nbEltEnsemble est le nombre d'éléments de l'ensemble dans lequel on joue
# renvoie la coupe
# tire une coupe tant qu'elle divise l'ensemble en deux parties égales
# (si le nombre d'objets est pair)
def choixCoupeOrdi(nbEltEnsemble):
    """
    Détermine à quel endroit l'ordi va couper l'ensemble

    Renvoie :
        le numéro de coupe
    Pré-conditions :
        nbEltEnsemble est un nombre entier qui correspond au nombre d'éléments de l'ensemble
    Post-conditions :
        nbEltEnsemble est inchangé après l'exécution
    """
    choix_ordi = randint(1, nbEltEnsemble - 1)
    while not (choix_ordi * 2 != nbEltEnsemble):
        choix_ordi = randint(1, nbEltEnsemble - 1)
    return choix_ordi


# fait jouer l'ordi, et affiche où il a joué
# utilise choixEnsembleJoueur et choixCoupeJoueur
# met à jour le jeu
def ordiJoue(jeu):
    """
    Fait jouer le joueur

    Renvoie :
        Rien
    Pré-conditions :
        jeu est une liste de nombre entiers strictement positifs
    Post-conditions :
        jeu est modifié de façon à refléter l'action de l'ordi
    """
    sleep(1)  # pause d'1s pour simuler la réflexion de l'ordi
    type_ens_ordi = choixTypeEnsembleOrdi(jeu)
    ensemble_ordi = choixEnsembleOrdi(jeu[type_ens_ordi - 1])
    nb_elem_ensemble = jeu[type_ens_ordi - 1][ensemble_ordi - 1]

    coupe_ordi = choixCoupeOrdi(nb_elem_ensemble)
    jeu[type_ens_ordi - 1][ensemble_ordi - 1] = coupe_ordi  # On change la taille de l'ensemble coupé

    jeu[type_ens_ordi - 1].insert(ensemble_ordi,
                                  nb_elem_ensemble - coupe_ordi)  # On insère un ensemble avec les éléments suivants la coupe
    display_text(f"L'ordi a joué dans le type d'ensemble n°{type_ens_ordi} et a choisi de couper l'ensemble {ensemble_ordi} à l'endroit {coupe_ordi}", -610, -430)


# Fait jouer alternativement le joueur et l'ordi
# tant que la fin de jeu n'est pas atteinte
def partie(n, nb_type_ens=2):
    """
    Algorithme qui déroule une partie.

    Renvoie :
        Rien
    Pré-conditions :
        n est un entier qui correspond au nombre maximal d'éléments en début de partie
    """
    jeu = initJeu(randint(3, n), nb_type_ens)
    loser = None

    while loser is None:
        reset()
        representationJeu(jeu)
        joueurJoue(jeu)
        if finDeJeu(jeu):
            reset()
            representationJeu(jeu)
            loser = "ordi"
        else:
            reset()
            representationJeu(jeu)
            ordiJoue(jeu)
            if finDeJeu(jeu):
                reset()
                representationJeu(jeu)
                loser = "joueur"
    display_text(f"{loser} a perdu !", -610, -415, clear=True)
    done()


partie(8)  # Pour plus de 8 éléments, des objets/séparateurs risquent de sortie de la zone de jeu
