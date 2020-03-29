import os , sys , platform 

class PortScanner:

    def __init__(self):
        self.__sn = []
        if sys.platform == 'win32':
            self.__findCommand =  'netstat -ano | findstr :'
            self.__showActiveCommand = 'netstat -aon'
        elif sys.platform == 'linux' or sys.platform == 'linux2' :
            self.scanCommand =  ''
            self.showActiveCommand = ''

    def find(self,i):
            command =  self.__findCommand + str(i)
            temp = os.popen(command).read()
            print(temp)

    def showActive(self):
        temp = os.popen(self.__showActiveCommand).read()
        print(temp)
        
    def close(self,i):
        command =  self.__findCommand + str(i)
        temp = os.popen(command).read()
        if temp:
            pid = temp.split()[-1]
            print('Process id = {} '.format(pid))
            if sys.platform == 'win32':
                self.__taskKill = 'taskkill /PID '+ str(pid) +' /F'
                os.popen(self.__taskKill).read()


if __name__ == "__main__":
    portScanner = PortScanner()
    # portScanner.showActive()
    # portScanner.find(8080)
    # portScanner.close(135)
   