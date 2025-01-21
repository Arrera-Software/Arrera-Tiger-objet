from CArreraTiger import*

objTiger = CArreraTiger("tigerConf.json")

objTiger.loadDepots("https://arrera-software.fr/tigerFile.json")

print(objTiger.getSoftAvailable())