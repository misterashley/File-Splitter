
#Windows folder name inside the quotes
bksource =r"C:\Users\mrashley\Documents\temp\Sage X3 - Use From Now On - Copy" #the r is for 'raw' allowing \ 
source = bksource.replace('\\','/')
if source[-1] != '/':
	source = source + '/'
#user configuration
##source = "c:/Users/mrashley/Downloads/Fire Safety Council/Split Web photos/Processed/"
##dest = "c:/Users/mrashley/Downloads/Fire Safety Council/Split Web photos/"
dest = source
project_name = "subfolder"
filesperfolder = 200  # how many files per folder. 200 default lower if wanted

move = False #True to move the file to destination folder
             #False will copy, leaving your originals intact.

#----------------------- no config below this -----------------

import os
import shutil

def copyFile(source, dest):
    shutil.copy(source, dest)

def moveFile(source, dest):
    shutil.move(source, dest)


filecount = 0  #don't edit
foldercount = 1 # don't edit
for filename in os.listdir(source):
    filecount = filecount + 1
    sourceFileName = (source+filename)
    destFileName = (dest+project_name + "_" + str(foldercount) + "/" + filename)
    folder_dest = (dest+project_name + "_" + str(foldercount) + "/")
    if os.path.isdir(folder_dest) == False:
        os.makedirs(folder_dest)
    if move: moveFile(sourceFileName, destFileName)
    else: copyFile(sourceFileName, destFileName)
    if filecount % filesperfolder == 0:
        foldercount = foldercount + 1
        
