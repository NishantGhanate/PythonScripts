"""
@Author : Nishant Ghanate
@Created : 21-10-19
@Tested : Windows10 x64
"""

import os
import random

class DeleteFiles:

    def __init__(self):
        self.__files = list()

    def scan(self,path):
        # print("Recursive call {}".format(path))
        try :
            for p in os.scandir(path):
                isDirectory = os.path.isdir(p)
                if isDirectory:
                    # print('\nInside Dir = {}'.format(p.path))
                    files = os.listdir(p.path)
                    for f in files:
                        l = os.path.join(p.path,f)
                        isDirectory = os.path.isdir(l)
                        if isDirectory:
                            # print("\nNested Directory {} ".format(l))
                            self.scan(l)
                        else:
                            self.__files.append(l)
                            # print(l)   
                else:
                    # print(p.path)
                    self.__files.append(p.path)
            return self.__files
        except Exception as e:
            print('Access Denied on {}' .format(p.path))
            return self.__files

    def delete(self,files,extensions=None):
        filesRemoved = []
        try:
            for f in files:
                isFile = os.path.isfile(f)
                if isFile and extensions != None:
                    ext = f.split('.')
                    if ext[1] in extensions:
                        os.remove(f)
                        print('File removed = {} '.format(f))
                        filesRemoved.append(f)
                elif isFile and extensions == None:
                    os.remove(f)
                    print('File removed = {} '.format(f))
                    filesRemoved.append(f)
                else:
                    print("File not found {}".format(f))
                    filesRemoved.append(f)
            return filesRemoved         
        except FileNotFoundError as e:
            print("File not found {}".format(e))
            return filesRemoved


""" Add your file path with C:\\folders\\dolders\\ """
filePath = "D:\\VirusSignature"
fileExts = ['.asm' , '.byte']
fileCount = 2
deleteFiles = DeleteFiles()
files = deleteFiles.scan(filePath)
# print(files)

""" Option 1 . Delete all files from given path"""
# for f in files:
#     deleteFiles.delete(f)

""" Option 2 . Delete all files with given extensions """
# deleteFiles.delete(files,fileExts)

""" Option 3 . Delete all files with given extensions which has same file name"""
# Delete Random Files with same file name different extension
count = 0 
sameNames = []
extCount = len(fileExts)
lenFiles = len(files)


for _ in range(fileCount):
    lenFiles = len(files)
    print("New len =  {} ".format(lenFiles))
    n = random.randint(0,lenFiles-1)
    print('Random index = {}'.format(n) )
    f = files[n]

    ext = f.split('.')
    print('\n')
    for e in fileExts:
        newFile = ext[0] + e
        isFile  = os.path.isfile(newFile)
        if isFile:
            # print(newFile)
            # lenFiles = len(files)
            count += 1
            sameNames.append(newFile)
        else:
            count = 0
            sameNames = []
            break

    if count == extCount:
        print(sameNames)
        for s in sameNames:
            files.remove(s)
            # deleteFiles.delete(s)

        # print(files)
    

    


        




