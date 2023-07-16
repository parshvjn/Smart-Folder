import os
import sys

root = os.getcwd() #cwd = current working directory

#checking if the dir exists in the given path
if os.path.exists(root+'/txtFiles'):
    print('already exists')
else:
    print('no')
    # adding a dir
    os.mkdir(root+'/txtFiles')

for root, dirs, file in os.walk('/Users/parshv/files/googledrive/CodingForParshv/smartFolder'):
    print('root->', root)
    print("|")
    print('|-->', dirs)
    print(dirs, '|-->', file)

# tree = os.walk('/Users/parshv/files/googledrive/CodingForParshv/smartFolder')
# print(list(tree))

#removing a dir
# os.rmdir(root+'/txtFiles')
#FILE HANDLING WITH PYTHON
# files can be created or deleted very easily
#there are several modes for accessing a file
#first mode is 'r' --r means reading the text (read mode)
#for writing, we use 'w' mode
#'a' for appending text
#'x' is use for creating or writing a new file

#create a file
file = open('exampletext.txt', 'a')
# write something in a file
text = file.write('person')
print(text)
file.close()#removes from memory, so you need to close it. and sometimes not closing it can give error

file = open('exampletext.txt', 'r')
text = file.read()
print(text)
file.close()