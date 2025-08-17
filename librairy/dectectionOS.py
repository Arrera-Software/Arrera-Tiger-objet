import platform

class OS :
    def __init__(self) :
        self.__os = platform.system()
        
    def osWindows(self):
        return self.__os == "Windows"
    
    def osLinux(self):
        return self.__os == "Linux"

    def osMac(self):
        return self.__os == "Darwin"