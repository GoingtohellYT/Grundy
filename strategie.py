from math import ceil


def mex(l):
    """Calcule le minimum excludant (mex) d'une liste"""
    m = len(l)
    j = 0
    while j < len(l) and m == len(l):
        if j not in l:
            m = j
        j += 1
    return m


def sumNimXOR(nim1, nim2):
    """Calcule le XOR de deux valeurs Nim"""
    return nim1 ^ nim2


def valEnsemble(n):
    """Calcule la valeur Grundy d'un ensemble de taille n"""
    if n < 3:
        return 0
    valeurs = list()
    for i in range(1, n):
        if n - i > 0 and n - i != i:
            valeurs.append(valGrundy([n - i, i]))
    return mex(valeurs)


def valGrundy(l):
    """Calcule la valeur Grundy d'une position (liste d'ensembles)"""
    if len(l) == 0:
        return 0

        # Filtrer les ensembles de taille < 3 (non jouables)
    ensembles_jouables = [x for x in l if x >= 3]
    if len(ensembles_jouables) == 0:
        return 0

    res = valEnsemble(ensembles_jouables[0])
    for i in range(1, len(ensembles_jouables)):
        res = sumNimXOR(res, valEnsemble(ensembles_jouables[i]))
    return res


def strategie_gagnante(l):
    """
    Trouve une stratégie gagnante dans la position actuelle.
    Retourne (indice_ensemble, position_coupe) ou None si aucune stratégie trouvée.
    """
    # Créer une copie pour éviter de modifier l'original
    liste_travail = l.copy()

    for i in range(len(liste_travail)):
        # Vérifier que l'ensemble est assez grand pour être coupé
        if liste_travail[i] < 3:
            continue

        for j in range(1, ceil(liste_travail[i] / 2)):
            reste = liste_travail[i] - j

            # Vérifier que les deux parties sont différentes et non nulles
            if reste > 0 and reste != j:
                # Créer une nouvelle position après le coup
                nouvelle_position = liste_travail.copy()
                nouvelle_position[i] = j  # Première partie
                nouvelle_position.insert(i + 1, reste)  # Deuxième partie

                # Si cette position a une valeur Grundy de 0, c'est gagnant
                if valGrundy(nouvelle_position) == 0:
                    return i, j  # Retourner l'indice réel (base 0)

    # Aucune stratégie gagnante trouvée
    return None
