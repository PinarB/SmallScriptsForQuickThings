"""
Created by Pınar Barlas; first uploaded to Github October 2020.

PURPOSE/FUNCTION: 
Goes through a directory to generate a list (.txt file) with every subfolder and the number of files each
subfolder contains. See the attached ReadMe for more information.

TO USE:
1. Update directoryPath variable at the top to your directory containing the folders to be processed.
2. Update unwantedFolders list to include the exact name of the folders to be ignored in the listing process.
3. Update savePath variable at the top to your directory where the resulting text file should be saved.
4. Update saveName to the desired file name for the resulting text file (without extension).

FYI:
* The items in the resulting file indicate the names of the subfolders, and in parantheses, the number of files
within that subfolder. There is no distinction regarding the file types or other details of the files; this 
may be added in the future. 
* Also, the code is not very "clean" and will probably be tidied up in the future with functions.
"""

import os

# the folders to be counted/listed are in parent folder:
directoryPath = 'C:\\my\\folder'
# folders that should be left out of the list:
unwantedFolders = []

# the resulting txt file will be saved in folder:
savePath = 'C:\\my\\folder'
# the resulting txt file will be titled:
saveName = 'The name of the text file'

# initializing empty lists
folderNames = []
folderNumberDict = {}

# listdir => returns list of files+folders in directory (a parent folder), randomly ordered,
# does NOT include "." or grandchild files, but DOES include first-level files
for item in os.listdir(directoryPath):
    # path.join => joins root and path "intelligently"
    pathToItem=os.path.join(directoryPath, item)
    # path.isdir => checks if path is an existing directory (i.e. folder, FALSE if pointing to  file)
    if os.path.isdir(pathToItem): # basically, if item is first-level folder
        if item not in unwantedFolders: # skip some folders
            folderNames.append(item) # add folder to final list
            nrOfFiles=len(os.listdir(pathToItem)) # count # of files inside folder
            # add to dict: key = folder name, value = nr of files
            folderNumberDict[item] = nrOfFiles

folderNames.sort()

namesAndNumbers = []
for folder in folderNames:
    nameWithNr = folder + " (" + str(folderNumberDict[folder]) + ")"
    namesAndNumbers.append(nameWithNr)

print("List of folders and their nr of files available:")
for name in namesAndNumbers: print(name)

print("--------------------------")
print("Saving to file...")

finalFilePath = os.path.join(savePath, saveName)
with open(finalFilePath+'.txt', 'w') as txtFile:
	for item in namesAndNumbers:
		txtFile.write('%s\n' % item)
txtFile.close()

print("File saved!")
print("--------------------------")
print("Nr of folders found:")
print(len(folderNames))