from jsonWorkOnline import*
from travailJSON import*
import urllib.request
from dectectionOS import*
import zipfile
import os
from pathlib import Path
import shutil


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
        if folder == "":
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
        pass

    def update(self,soft : str):
        pass

    def install(self, soft : str):
        softInstalled = self.getSoftInstall()
        softAvailable = self.getSoftAvailable()

        if (soft in softInstalled):
            return False
        else :
            if soft not in softAvailable :
                return False
            else:
                linuxOs = self.__system.osLinux()
                windowsOS = self.__system.osWindows()
                dictSofts = self.__depotFile.dictJson()
                dictSoft = dictSofts[soft]
                if (windowsOS == True):
                    link = dictSoft["linkWin"]
                    fileName = self.__emplacementSoft+"/"+dictSoft["namezipwin"]
                else :
                    if (linuxOs == True):
                        link = dictSoft["linkLinux"]
                        fileName = self.__emplacementSoft+dictSoft["nameziplinux"]
                    else :
                        return False

                if (link == ""):
                    return False
                else :
                    urllib.request.urlretrieve(link,fileName)
                    if not os.path.exists(fileName):
                        return False
                    if not os.path.exists(self.__emplacementSoft):
                        os.makedirs(self.__emplacementSoft)
                    with zipfile.ZipFile(fileName, 'r') as zip_ref:
                        zip_ref.extractall(self.__emplacementSoft)
                        zip_ref.close()
                        try:
                            self.getSoftInstall()
                            if (linuxOs == True): # Mise en place du raccourci sur linux
                                os.remove(fileName)
                                nameExe = dictSoft["nameexelinux"]
                                # Creation du fichier lauch.sh qui permet de lancer le logiciel
                                with open(f"{self.__emplacementSoft}/{dictSoft['namefolderLinux']}/lauch.sh", "w") as file:
                                    file.write("#!/bin/bash\n"
                                               "cd "+self.__emplacementSoft+"/"+dictSoft['namefolderLinux']+
                                               "\n./"+nameExe)
                                    file.close()
                                # Rendu du logiciel executable et du fichier lauch.sh
                                os.chmod(f"{self.__emplacementSoft}/{dictSoft['namefolderLinux']}/lauch.sh",0o777)
                                os.chmod(f"{self.__emplacementSoft}/{dictSoft['namefolderLinux']}/{nameExe}",0o777)
                                # Ecrire le fichier .desktop
                                contentDesk = ("[Desktop Entry]"+
                                               "\nVersion="+dictSoft["version"]+
                                               "\nType=Application"+
                                               "\nName="+self.formatNameApp(soft)+
                                               "\nExec="+self.__emplacementSoft+"/"+dictSoft['namefolderLinux']+"/lauch.sh"+
                                               "\nTerminal=false"+
                                               "\nStartupNotify=false")
                                # Ajouter l'icone si elle existe
                                if dictSoft["iconLinux"] != "":
                                    contentDesk += "\nIcon="+self.__emplacementSoft+"/"+dictSoft['namefolderLinux']+"/"+dictSoft["iconLinux"]
                                dir =  os.path.expanduser("~")+ "/.local/share/applications/"+soft+".desktop"
                                # Ecrire le fichier .desktop
                                with open(dir, "w") as file :
                                    file.write(contentDesk)
                                    file.close()

                            else :
                                if (windowsOS == True):
                                    # Importation de la librairy pour cree un raccourci
                                    import win32com.client
                                    # Suppression du fichier zip
                                    fileName = fileName.replace("/","\\")
                                    os.system(f'del /f /q "{fileName}"')
                                    # Creation de variable pour le raccourci
                                    emplacementExe = r""+self.__emplacementSoft+dictSoft["namefolderWin"]+"/"+dictSoft["nameexewin"]
                                    shorcutPath = r""+str(os.path.join(os.environ['APPDATA'], 'Microsoft', 'Windows', 'Start Menu'))+"\\"+soft+".lnk"
                                    workFolder = r""+self.__emplacementSoft+dictSoft["namefolderWin"]

                                    # Debut creation raccourci
                                    shell = win32com.client.Dispatch("WScript.Shell")
                                    shortcut = shell.CreateShortCut(shorcutPath)
                                    shortcut.TargetPath = emplacementExe
                                    shortcut.WorkingDirectory = workFolder
                                    shortcut.Description = self.formatNameApp(soft)
                                    # Mise en place de l'icon du raccourci si elle existe
                                    icon = dictSoft["iconWin"]
                                    if (icon != ""):
                                        iconLnk = workFolder+"/"+icon
                                        shortcut.IconLocation = iconLnk
                                    # Sauvegarde du raccourci
                                    shortcut.save()

                            return True
                        except FileNotFoundError:
                            return False
                        except PermissionError:
                            return False
                        except Exception as e:
                            return False

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
                    if linuxOs == True:
                        dossiers[i] = (dossiers[i].replace
                                       (self.__emplacementSoft,"").replace
                                       ("/","").replace
                                       ("\\",""))
                    else :
                        if windowsOS == True:
                            emplacementsoft = self.__emplacementSoft.replace("/","\\")
                            dossiers[i] = (dossiers[i].replace
                                           (emplacementsoft,"").replace
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
                    if ("arrera-interface" in listOut):
                        self.__tigerFile.EcritureJSON("arrera-interface","1")
                    else :
                        self.__tigerFile.EcritureJSON("arrera-interface","0")

                    if ("ryley" in listOut):
                        self.__tigerFile.EcritureJSON("ryley","1")
                    else :
                        self.__tigerFile.EcritureJSON("ryley","0")

                    if ("six" in listOut):
                        self.__tigerFile.EcritureJSON("six","1")
                    else :
                        self.__tigerFile.EcritureJSON("six","0")

                    if ("arrera-raccourci" in listOut):
                        self.__tigerFile.EcritureJSON("arrera-raccourci","1")
                    else :
                        self.__tigerFile.EcritureJSON("arrera-raccourci","0")

                    if ("arrera-postite" in listOut):
                        self.__tigerFile.EcritureJSON("arrera-postite","1")
                    else :
                        self.__tigerFile.EcritureJSON("arrera-postite","0")

                    if ("arrera-video-download" in listOut):
                        self.__tigerFile.EcritureJSON("arrera-video-download","1")
                    else :
                        self.__tigerFile.EcritureJSON("arrera-video-download","0")

                    if ("arrera-copilote" in listOut):
                        self.__tigerFile.EcritureJSON("arrera-copilote","1")
                    else :
                        self.__tigerFile.EcritureJSON("arrera-copilote","0")

                    return listOut

            except PermissionError:
                return "Erreur de permission pour accéder"
            except Exception as e:
                return "Une erreur s'est produite"

    def uninstall(self,soft : str):
        if (soft == ""):
            return False
        else :
            softInstalled = self.getSoftInstall()
            if (soft in softInstalled):
                dictSofts = self.__depotFile.dictJson()
                dictSoft = dictSofts[soft]
                if (self.__system.osLinux() == True):
                    folder = self.__emplacementSoft+"/"+dictSoft["namefolderLinux"]
                    if os.path.exists(folder):
                        shutil.rmtree(folder)
                else :
                    if (self.__system.osWindows() == True):
                        folder = self.__emplacementSoft+"/"+dictSofts[soft]["namefolderWin"]
                        if os.path.exists(folder):
                            shutil.rmtree(folder)
                self.getSoftInstall()
                return True
            else :
                return False


    def formatNameApp(self, nameApp:str):
        # Supprimer les tirets
        nameApp = nameApp.replace("-", " ")

        # Mettre la première lettre en majuscule
        nameApp = nameApp.capitalize()

        # Mettre la première lettre après chaque espace en majuscule
        nameApp = ' '.join(word.capitalize() for word in nameApp.split())

        return nameApp