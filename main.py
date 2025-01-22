from CArreraTiger import*
import tkinter.filedialog as fd

def main():
    objTiger = CArreraTiger("tigerConf.json")

    if (objTiger.loadDepots("https://arrera-software.fr/tigerFile.json")==True):
        print("Depot chargé")
        print(objTiger.getSoftAvailable())
        if objTiger.setEmplacementArreraSoft(fd.askdirectory()) == True:
            print("Emplacement enregistré")
            print(objTiger.getSoftInstall())


if __name__ == "__main__":
    main()