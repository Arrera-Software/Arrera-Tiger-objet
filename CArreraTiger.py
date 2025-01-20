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
        if url == "":
            return False
        else :
            self.__url = url
            self.__tigerFile.loadInternet(url)
            return True

    def setEmplacementArreraSoft(self,emplacementSoft : str):
        pass

    def getEmplacementSaved(self):
        pass

    def checkUpdate(self):
        pass

    def update(self,soft : str):
        pass

    def install(self,soft : str):
        pass

    def getSoftAvailable(self):
        pass

    def getSoftInstall(self):
        pass

    def uninstall(self,soft : str):
        pass