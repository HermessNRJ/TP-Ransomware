# -*- coding: utf-8 -*-

from path import Path

#Scan des fichiers présent dans les répertoires et renvoie une liste de tous les fichiers présents dans le dossier et sous dossier courant
def scanner():
    #initialise la liste
    files = []

    #parcours les fichiers
    for f in Path('.').walkfiles():
        files.append(f)

    return files