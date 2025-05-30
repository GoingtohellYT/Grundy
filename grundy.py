# Binôme : Héloïse Fouillout et Alexis Mengual
# Jeu de Grundy

"""Le jeu consiste à séparer des ensembles d'objets. La position de départ consiste en un unique ensemble d'objets.
  Pour jouer, le seul coup possible consiste à séparer un ensemble d'objets en deux ensembles de tailles distinctes et
  non nulles. Les joueurs jouent à tour de rôle, jusqu'à ce que l'un d'entre eux ne puisse plus jouer."""

from random import randint  # pour que l'ordinateur puisse jouer aléatoirement
from time import sleep  # pour que l'ordinateur puisse réfléchir 1 seconde
from gui import representationJeu, reset, display_text  # pour l'interface graphique
from turtle import numinput, done  # pour demander les valeurs et garder la fenêtre ouverte en fin de partie
from strategie import strategie_gagnante, valGrundy  # pour déterminer le coup de l'ordi


def initJeu(n, nb_e):
    """
    Initialise le jeu en début de partie.

    Pré-conditions :
        n est le nombre maximal d'éléments à placer dans chaque ensemble
        nb_e est le nombre de types d'ensembles à créer
    Renvoie :
        le jeu sous la forme d'une liste de listes. Chaque sous liste représente un type d'ensemble
    """
    jeu = list()
    for i in range(nb_e):
        jeu.append([randint(5, n)])
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

# ------------ Joueur ----------#

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

    jeu[type_ens_joueur - 1].insert(ensemble_joueur, nb_elem_ensemble - coupe_joueur)  # On insère un ensemble avec les éléments suivants la coupe
    display_text(f"Vous avez joué dans le type d'ensemble n°{type_ens_joueur}, ensemble {ensemble_joueur}, position {coupe_joueur}", -610, -400, clear=True)

# ---------- Partie ordi ---------- #

# fait jouer l'ordi, et affiche où il a joué
# met à jour le jeu
def ordiJoue(jeu):
    """
    Fait jouer l'ordinateur

    Renvoie :
        Rien
    Pré-conditions :
        jeu est une liste de nombre entiers strictement positifs
    Post-conditions :
        jeu est modifié de façon à refléter l'action de l'ordi
    """

    # Combiner tous les ensembles pour calculer l'indice global
    tous_ensembles = jeu[0] + jeu[1]
    taille_type1 = len(jeu[0])
    indice_ensemble, position_coupe = strategie_gagnante(tous_ensembles)

    # Vérifier que l'indice est valide
    if indice_ensemble < 0 or indice_ensemble >= len(tous_ensembles):
        print(f"Erreur : Indice d'ensemble invalide : {indice_ensemble}")
        return False

    # Vérifier que l'ensemble est assez grand
    taille_ensemble = tous_ensembles[indice_ensemble]
    if taille_ensemble < 3:
        print(f"Erreur : Ensemble trop petit pour être coupé : {taille_ensemble}")
        return False

    # Vérifier que la position de coupe est valide
    if position_coupe <= 0 or position_coupe >= taille_ensemble:
        print(f"Erreur : Position de coupe invalide : {position_coupe}")
        return False

    reste = taille_ensemble - position_coupe
    if reste == position_coupe:
        print(f"Erreur : Les deux parties auraient la même taille : {position_coupe}")
        return False

    # Appliquer le coup
    if indice_ensemble < taille_type1:
        # Coup dans le type d'ensemble 1
        print(f"L'ordi a joué dans le type d'ensemble n°1, ensemble {indice_ensemble+1}, position {position_coupe}")
        display_text(f"L'ordi a joué dans le type d'ensemble n°1, ensemble {indice_ensemble+1}, position {position_coupe}", -610, -430)
        jeu[0][indice_ensemble] = reste
        jeu[0].insert(indice_ensemble, position_coupe)
    else:
        # Coup dans le type d'ensemble 2
        indice_local = indice_ensemble - taille_type1
        print(f"L'ordi a joué dans le type d'ensemble n°2, ensemble {indice_local+1}, position {position_coupe}")
        display_text(f"L'ordi a joué dans le type d'ensemble n°2, ensemble {indice_local+1}, position {position_coupe}", -610, -430)
        jeu[1][indice_local] = reste
        jeu[1].insert(indice_local, position_coupe)




# Fait jouer alternativement le joueur et l'ordi
# tant que la fin de jeu n'est pas atteinte
def partie(n, nb_type_ens=2):
    """
    Algorithme qui déroule une partie.

    Renvoie :
        Rien
    Pré-conditions :
        n est un entier qui correspond au nombre maximal d'éléments par ensemble en début de partie
    """
    jeu = initJeu(n, nb_type_ens)
    loser = None
    if valGrundy(jeu[0]+jeu[1]) == 0:
        order = [joueurJoue, ordiJoue]
        display_text("L'ordinateur vous laisse commencer", -610, -400)
    else:
        order = [ordiJoue, joueurJoue]
        display_text("L'ordinateur souhaite commencer", -610, -400)

    while loser is None:
        reset()
        representationJeu(jeu)
        order[0](jeu)
        if finDeJeu(jeu):
            reset()
            representationJeu(jeu)
            if str(order[1]) == "ordiJoue":
                loser = "Ordi"
            else:
                loser = "Joueur"
        else:
            reset()
            representationJeu(jeu)
            order[1](jeu)
            if finDeJeu(jeu):
                reset()
                representationJeu(jeu)
                if str(order[0]) == "ordiJoue":
                    loser = "Ordi"
                else:
                    loser = "Joueur"
    display_text(f"{loser} a perdu !", -610, -415, clear=True)
    done()


partie(8)  # Pour plus de 8 éléments, des objets/séparateurs risquent de sortie de la zone de jeu
