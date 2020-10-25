"""
Created by Pınar Barlas; first uploaded to Github October 2020.

PURPOSE/FUNCTION: 
Goes through a directory to generate a list (.txt file) with every file in the (sub)directories.
See the attached ReadMe for more information.

TO USE:
1. Update directoryPath variable at the top to your directory containing the files to be processed.
2. Update fileTypes list to reflect the file extensions to be processed.
3. Update savePath variable at the top to your directory where the resulting text file should be saved.
4. Update saveName to the desired file name for the resulting text file (without extension).

FYI:
* The listed items have the subdirectory at the beginning of the line (if not in parent directory),
and the list is alphabetized - this allows for visual grouping of items. i.e. Files under the same
folder appear together, like "Archived\\some_file".
"""

import os

# the files to be counted/listed are in folder:
directoryPath = 'C:\\my\\folder'
# the files to be counted/listed have the extension(s):
fileTypes = ['.mkv', '.avi', '.mp4']

# the resulting txt file will be saved in folder:
savePath = 'C:\\my\\folder'
# the resulting txt file will be titled:
saveName = 'The name of the text file'

# initializing empty lists
fileNames = []
fullFilePaths = []

def get_filepaths(directory, filetype):
	"""
		Acquired from Kyriakos Kyriakou with thanks!
	This function will generate the file names in a directory
	tree by walking the tree either top-down or bottom-up. For each
	directory in the tree rooted at directory top (including top itself),
	it yields a 3-tuple (dirpath, dirnames, filenames).
	"""
	filePathslist = []
	for root, directories, files in os.walk(directory):
		for filename in files:
			# Join the two strings in order to form the full filepath.
			filepath = os.path.join(root, filename)
			# include only the .jpg file extensions except their hidden/shadow files
			if filepath.endswith(filetype) and not filename.startswith('.'):
				filePathslist.append(filepath)  # Add it to the list.
	return filePathslist  # Self-explanatory.

for type in fileTypes: fullFilePaths.extend(get_filepaths(directoryPath, type))

# Iterate this filepaths list
for file in fullFilePaths:
	file = file.replace(directoryPath+'\\', '')
	for type in fileTypes:
		file = file.replace(type, '')
	fileNames.append(file)

fileNames.sort()

print("List of files:")
for line in fileNames: print(line)

print("--------------------------")
print("Saving to file...")

saveFilePath = os.path.join(savePath, saveName)
with open(saveFilePath+'.txt', 'w') as txtFile:
	for item in fileNames:
		txtFile.write('%s\n' % item)
txtFile.close()

print("File saved!")
print("--------------------------")
print("Nr of files found:")
print(len(fileNames))