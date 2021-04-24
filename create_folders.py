# -*- coding: utf-8 -*-

import os
from os.path import dirname, abspath, join
import errno


file = "primero.txt"

def createFolder(foldername):
    import os
    try:
        os.makedirs(foldername)
        print("folder ",foldername," created succesfully")

    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
        print("folder ",foldername," not created ERROR")
        pass
    pass

def createFile(filename,folderpath):
    """
    with open(os.path.join(folderpath, filename), 'wb') as temp_file:
        temp_file.write(filename)
    """
    outFileName=os.path.join(folderpath, filename)
    outFile=open(outFileName, "w")
    outFile.write("")
    outFile.close()
    pass


def readfileandgetarray(filename):
    f = open(filename, "r")
    filecontent = f.read()
    f.close()
    return filecontent.splitlines()

folders = readfileandgetarray(file)


base=os.path.basename(file)
masterfolder = os.path.splitext(base)[0]

for folder_to_create in folders:
    folder_to_create = folder_to_create.encode('iso-8859-1').decode('utf8')#.encode('utf8')
    #folder_to_create = str(folder_to_create, 'utf-8')
    #folder_to_create = folder_to_create.encode().decode('unicode_escape')
    subfolder = os.path.join(masterfolder,folder_to_create)
    createFolder(subfolder)
    
    filename = folder_to_create + '.md'
    createFile(filename,subfolder)
    pass

