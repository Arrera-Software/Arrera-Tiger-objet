from jsonWorkOnline import*
from travailJSON import*
import urllib.request
from dectectionOS import*
import zipfile
import os
from pathlib import Path


class CArreraTiger :
    def __init__(self,tigerFile:str):
        # Initialisation des attributs
        self.__url = ""
        self.__emplacementSoft = ""
        # Initialisation de l'objet pour lire le depot
        self.__depotFile = jsonWorkOnline()
        # Chargement du fichier local
        self.__tigerFile = jsonWork(tigerFile)
        # Initialisation de l'objet pour la detection du systeme d'explotation
        self.__system = OS()

    def loadDepots(self,url:str):
        if url == "":
            return False
        else :
            self.__url = url
            self.__depotFile.loadInternet(url)
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
            print(emplacementSoft)
            self.__tigerFile.EcritureJSON("folder",self.__emplacementSoft)
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
        dictAllSoft = self.__depotFile.dictJson()
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
        if (self.__emplacementSoft == ""):
            return "error"
        else :
            softAvailable = self.getSoftAvailable()
            dictSoft = self.__depotFile.dictJson()
            windowsOS = self.__system.osWindows()
            linuxOs = self.__system.osLinux()
            listOut = []
            try:
                # Convertir le chemin en objet Path
                chemin_path = Path(self.__emplacementSoft).resolve()  # resolve() normalise le chemin
                # Vérifier si le chemin existe
                if not chemin_path.exists():
                    return "le chemin {self.__emplacementSoft} n'existe pas"
                # Lister uniquement les dossiers
                dossiers = [str(d) for d in chemin_path.iterdir() if d.is_dir()]
                for i in range(0,len(dossiers)):
                    dossiers[i] = (dossiers[i].replace
                                   (self.__emplacementSoft,"").replace
                                   ("/","").replace
                                   ("\\",""))
                for i in range(0,len(softAvailable)):
                    if (windowsOS == True) and (dictSoft[softAvailable[i]]["namefolderWin"] in dossiers):
                        listOut.append(softAvailable[i])
                    else :
                        if (linuxOs == True) and (dictSoft[softAvailable[i]]["namefolderLinux"] in dossiers):
                            listOut.append(softAvailable[i])

                if (len(listOut) == 0):
                    return "Accun logiciel installé"
                else :
                    return listOut

            except PermissionError:
                return "Erreur de permission pour accéder"
            except Exception as e:
                return "Une erreur s'est produite"


    def uninstall(self,soft : str):
        pass