import os
from config import *
import shutil

# os.rename(rawFilePath + '/exampletext.txt', pdfFilesPath + '/exampletext.txt')

a = rawFilePath + '/error handling - Jupyter Notebook (1).pdf'
shutil.move(a, pdfFilesPath)