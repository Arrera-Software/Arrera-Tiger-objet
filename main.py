from CArreraTiger import*
import tkinter.filedialog as fd

def main():
    objTiger = CArreraTiger("tigerConf.json")
    sortieFolder =  objTiger.loadEmplacementFile()

    if (objTiger.loadDepots("https://arrera-software.fr/tigerFile.json")==True):
        print("Depot chargé")
        print(objTiger.getSoftAvailable())
        if sortieFolder == False:
            if objTiger.setEmplacementArreraSoft(fd.askdirectory()) == True:
                print("Emplacement enregistré")
        else :
            print("Emplacement déjà enregistré")
        print(objTiger.getSoftInstall())
        print(objTiger.checkUpdate())
        sortie = input("1.Installer\n2.Uninstaller\n#")

        if sortie == "1":
            soft = input("Nom du logiciel à installer: ")
            if (soft != ""):
                print(objTiger.install(soft))
        else :
            if sortie == "2":
                soft = input("Nom du logiciel à désinstaller: ")
                if (soft != ""):
                    print(objTiger.uninstall(soft))


if __name__ == "__main__":
    main()