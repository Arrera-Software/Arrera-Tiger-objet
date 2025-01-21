from jsonWork import*
import urllib.request
from dectectionOS import*
import zipfile
import os


class CArreraTiger :
    def __init__(self,tigerFile:str):
        # Initialisation des attributs
        self.__url = ""
        self.__emplacementSoft = ""
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

    def loadEmplacementFile(self):
        folder = self.__tigerFile.lectureJSON("folder")
        if folder == "error":
            return False
        else :
            self.__emplacementSoft = folder
            return True

    def setEmplacementArreraSoft(self,emplacementSoft : str):
        if emplacementSoft == "":
            return False
        else :
            self.__emplacementSoft = emplacementSoft
            self.__tigerFile.EcritureJSON("folder",emplacementSoft)
            return True

    def getEmplacementSaved(self):
        if not self.__emplacementSoft :
            return False
        else :
            return True

    def checkUpdate(self):
        listeSoft = []
        listeSoft = self.__tigerFile.dictJson().keys()

    def update(self,soft : str):
        pass

    def install(self,soft : str):
        pass

    def getSoftAvailable(self):
        listeSoft = []
        dictAllSoft = self.__tigerFile.dictJson()
        listeAllSoft = list(dictAllSoft.keys())

        windowsOS = self.__system.osWindows()
        linuxOs = self.__system.osLinux()
        for i in range(0,len(listeAllSoft)):
            if (windowsOS == True and linuxOs == False
                    and dictAllSoft[listeAllSoft[i]]["namezipwin"]!=""
                    and dictAllSoft[listeAllSoft[i]]["linkWin"]!=""
                    and dictAllSoft[listeAllSoft[i]]["namefolderWin"]!=""):
                listeSoft.append(listeAllSoft[i])
            else :
                if (windowsOS == False and linuxOs == True
                        and dictAllSoft[listeAllSoft[i]]["nameziplinux"]!=""
                        and dictAllSoft[listeAllSoft[i]]["linkLinux"]!=""
                        and dictAllSoft[listeAllSoft[i]]["namefolderLinux"]!=""):
                    listeSoft.append(listeAllSoft[i])

        if (len(listeSoft) == 0):
            return "error"
        else :
            return listeSoft



    def getSoftInstall(self):
        pass

    def uninstall(self,soft : str):
        pass