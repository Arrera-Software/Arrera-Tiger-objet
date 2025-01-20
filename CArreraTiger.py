from jsonWork import*
import urllib.request
from dectectionOS import*
import zipfile
import os


class CArreraTiger :
    def __init__(self,tigerFile:str):
        # Initialisation des attributs
        self.__url = ""
        # Initialisation de l'objet pour lire le depot
        self.__depotFile = jsonWork()
        # Chargement du fichier local
        self.__tigerFile = jsonWork()
        self.__tigerFile.loadFile(tigerFile)
        # Initialisation de l'objet pour la detection du systeme d'explotation
        self.__system = OS()

    def loadDepots(self,url:str):
        self.__url = url

    
