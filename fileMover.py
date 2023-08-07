from glob import glob
import os 
import sys
from config import *
import shutil

fileList = glob(rawFilePath+'/*')
print(fileList)

def fileProccessor(fileList, mode = 'all'):
    txtList = []
    pdfList = []
    if mode == 'all':
        for files in fileList:
            if files[-3:] == 'txt':
                txtList.append(files)
                shutil.move(files, txtFilesPath)
            elif files[-3:] == 'pdf':
                pdfList.append(files)
                shutil.move(files, pdfFilesPath)
    elif mode == 'txt':
        for files in fileList:
            if files[-3:] == 'txt':
                txtList.append(files)
                shutil.move(files, txtFilesPath)
    elif mode == 'pdf':
        for files in fileList:
            if files[-3:] == 'pdf':
                pdfList.append(files)
                shutil.move(files, pdfFilesPath)


fileProccessor(fileList, mode= 'pdf')