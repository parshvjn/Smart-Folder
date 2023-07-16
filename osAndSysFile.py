import os
import sys
import glob

path = os.path.join('smartfolder', 'pdfFiles')
# print(path)

#sys.stdout is a built-in file object which is used as a standard output string in python
#with stdout we can display the output directly to the screen console
#sys.stdout doesn't switch to a new line, rather we need to provide the escape character \n 
# sys.stdout.write('hello parshv')
#sys.stdin used for standard input, (not like input()).
# h = sys.stdin.read()
# print(h)

d = glob.glob('*.txt') #accessing all files with the extension '.txt'
print(d)