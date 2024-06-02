from CArreraTiger import*

objTiger = CArreraTiger("https://raw.githubusercontent.com/Arrera-Software/Software-debot/main/arrerasoft.json")
print(objTiger.listSoft())
objTiger.downloadFile("copilote","copilote.zip","soft")