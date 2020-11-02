# TP-Ransomware

L’objectif de ce TP est de mettre en place les premières briques d’un ransomware affectant un système de
type Unix.
Ce TP est réalisé dans le cadre de l'enseignement **Sécurité Cloud** suivie à l'ESIEE.
Déveleppoment effectué par Elvin GUILLOTON et Rémi BOIDET

## Exigences

Voici les demandes spécifiques pour la réalisation de ce malware :
- Code développé en Python3
- Code commenté en français
- Doit être fonctionnel sur Kali
- Peut comporter des librairies externes mais ne doit pas en abuser (le spécifier dans un fichier
nommé requirements.txt)

## Les étapes

- [ ] Le code doit s’exécuter sans demander la moindre information à l’utilisateur
- [x] Le ransomware parcours la totalité du dossier /tmp de manière récursive pour trouver l’ensemble
des fichiers présents
- [] Pour chaque fichier, chiffrer celui-ci dans un nouveau fichier (nom_du_fichier.enc) avec un système
de chiffrement utilisant de l’AES 256
- [ ] La clé de chiffrement doit être obtenue depuis un site Internet puis supprimée de la mémoire.
    - [ ] Expliquer quel mécanisme (et son fonctionnement) de Python permet de sauter cette étape
- [ ] Le fichier en clair doit être supprimé de manière sécurisée
- [ ] Le ransomware doit disposer d’une fonction permettant de déchiffrer les fichiers

## Utilisation

```bash
pip3 install -r requirements.txt
python3 ransomware.py
```