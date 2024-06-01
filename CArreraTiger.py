from jsonWork import*
import urllib.request
import zipfile
import os


class CArreraTiger :
    def __init__(self,url:str) :
        self.__json = jsonWork()
        self.__json.loadInternet(url)
    
    def downloadFile(self,soft:str,fileName,emplacemntSoft):
        link = self.__json.lectureJSON(soft)
        urllib.request.urlretrieve(link,fileName)  
        sortie = self.__unzip(fileName,emplacemntSoft)
        if sortie==False :
            return 2 
        else : 
            return 0

    def __unzip(self,zipFile, floder):
        if not os.path.exists(zipFile):
            return False
        if not os.path.exists(floder):
            os.makedirs(floder)
        with zipfile.ZipFile(zipFile, 'r') as zip_ref:
            zip_ref.extractall(floder)
            self.__delFile(zipFile)
            return True   
    
    def __delFile(self,file_path):
        try:
            os.remove(file_path)
            return True
        except FileNotFoundError:
            return False
        except PermissionError:
            return False
        except Exception as e:
            return False