from CArreraTiger import*
import tkinter.filedialog as fd

def main():
    objTiger = CArreraTiger("tigerConf.json")
    sortieFolder =  objTiger.loadEmplacementFile()

    if (objTiger.loadDepots("https://arrera-software.fr/depots.json")==True):
        print("Depot chargé")
        print(objTiger.getSoftAvailable())
        if sortieFolder == False:
            if objTiger.setEmplacementArreraSoft(fd.askdirectory()) == True:
                print("Emplacement enregistré")
        else :
            print("Emplacement déjà enregistré")
        print(objTiger.getSoftInstall())
        print(objTiger.checkUpdate())
        sortie = input("1.Installer\n2.Uninstaller\n3.Update\n#")

        match sortie:
            case "1":
                soft = input("Nom du logiciel à installer: ")
                if (soft != ""):
                    print(objTiger.install(soft))
            case "2":
                soft = input("Nom du logiciel à désinstaller: ")
                if (soft != ""):
                    print(objTiger.uninstall(soft))
            case "3":
                print("Soft a mettre a jour : ")
                print(objTiger.checkUpdate())
                soft = input ("Logiciel a mettre a jour : ")
                if (soft != ""):
                    print(objTiger.update(soft))

if __name__ == "__main__":
    main()