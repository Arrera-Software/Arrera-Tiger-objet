from CArreraTiger import*

objTiger = CArreraTiger("https://raw.githubusercontent.com/Arrera-Software/Software-debot/main/arrerasoft.json")
print(objTiger.listSoft())
objTiger.install("copilote","copilote.zip","soft")