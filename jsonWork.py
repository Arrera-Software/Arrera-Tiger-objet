import json
import requests

class jsonWork : 
    def __init__(self):
        self.fichier = str 
        self.contenuJson = str
    
    def __reloadFile(self):
        self.__readFile.close()
        self.__readFile = open(self.fichier, 'r', encoding='utf-8')
        self.__readFile.seek(0)  # Rembobiner le fichier au début
        self.contenuJson = json.load(self.__readFile)
        
    def loadFile(self, fichier: str):
        self.fichier = fichier
        self.__readFile =  open(fichier, 'r', encoding='utf-8') 
        
        self.contenuJson = json.load(self.__readFile)
        
    def __openWrite(self):
        self.__writeFile = open(self.fichier,"w")
        
    def lectureJSON(self,flag): # Permet de lire la valeur du flag defini a l'appel de la fonction
        dict = self.contenuJson[flag]
        return str(dict)
    
    def lectureJSONMultiFlag(self,flag1,flag2):
        dict = self.contenuJson[flag1][flag2]
        return str(dict)
    
    def lectureJSONList(self,flag):
        liste = self.contenuJson[flag]
        return list(liste)
    
    def lectureJSONDict(self,flag):
        dictionnaire = self.contenuJson[flag]
        return dict(dictionnaire)
     
    def EcritureJSON(self,flag,valeur):#Permet d'ecrire une nouvelle valeur a flag definie
        self.__openWrite()
        self.contenuJson[flag] = valeur
        json.dump(self.contenuJson,self.__writeFile,indent=2)
        self.__writeFile.close()
        self.__reloadFile()
        
    def EcritureJSONList(self, flag, valeur):
        self.__openWrite()
        if flag in self.contenuJson and isinstance(self.contenuJson[flag], list):
            # Ajoutez la nouvelle valeur à la liste
            self.contenuJson[flag].append(valeur)
            # Écrivez le fichier JSON mis à jour
            json.dump(self.contenuJson, self.__writeFile, indent=2)
        self.__writeFile.close()
        self.__reloadFile()
        
                
    
    def EcritureJSONDictionnaire(self, flag, cle, valeur):
        self.__openWrite()
        if flag in self.contenuJson and isinstance(self.contenuJson[flag], dict):
            self.contenuJson[flag][cle] = valeur  # Met à jour le dictionnaire
            json.dump(self.contenuJson, self.__writeFile, indent=2)
        self.__writeFile.close()
        self.__reloadFile()
    
    def supprJSONDict(self, flag, cle):
        self.__openWrite()
        if flag in self.contenuJson and isinstance(self.contenuJson[flag], dict):
            if cle in self.contenuJson[flag]:
                del self.contenuJson[flag][cle]  # Supprime la clé spécifiée du dictionnaire
                json.dump(self.contenuJson,self.__writeFile, indent=2)
        self.__writeFile.close()
        self.__reloadFile()
                    
    
    def suppressionJson(self, flag:str):
        self.__openWrite()
        if flag in self.contenuJson:
            self.contenuJson[flag]="" # Supprime le champ spécifié
            json.dump(self.contenuJson, self.__writeFile, indent=2)
        self.__writeFile.close()
        self.__reloadFile()
    
    def suppressionJsonList(self, flag, valeur):
        self.__openWrite()
        if flag in self.contenuJson and isinstance(self.contenuJson[flag], list):
            liste = self.contenuJson[flag]
            if valeur in liste:
                liste.remove(valeur)  # Supprime la valeur spécifiée de la liste
                json.dump(self.contenuJson, self.__writeFile, indent=2)
        self.__writeFile.close()
        self.__reloadFile()

    def dictJson(self):
        return self.contenuJson
       
    def compteurFlagJSON(self):
        return len(self.contenuJson)
    
    def supprDictReorg(self,flag):  
        self.__openWrite()
        del self.contenuJson[flag]
        newDict = {}
        newKey = 0
        for cle in sorted(self.contenuJson.keys(), key=lambda x: int(x)):
            newDict[str(newKey)] = self.contenuJson[cle]
            newKey += 1
        json.dump(newDict,self.__writeFile,indent=2)
        self.__writeFile.close()
        self.__reloadFile()