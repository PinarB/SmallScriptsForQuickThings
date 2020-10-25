"""
Created by Pınar Barlas; first uploaded to Github October 2020.

PURPOSE/FUNCTION: 
Goes through all .srt files in a directory, makes sure they are all encoded
as utf8 (saving a copy encoded with utf8 if not). Created to deal with wrongly-encoded Turkish
subtitles, which usually have the encoding cp1254.
See the attached ReadMe for more information.

TO USE:
1. Update directoryPath variable at the top to your directory containing the files to be fixed.

FYI:
* Checked with Windows only.
* Made to work with Turkish subtitles only; with one specific (wrong) encoding.
* Has an option (commented out) to replace the original file instead of saving a copy; take care
when replacing.
* Currently allows other file types to be processed; this doesn't seem necessary so in the future
the code might be simplified by hard-coding the .srt file extension instead of reading from a list.
"""

import os

directoryPath = 'C:\\my\\folder'

fileTypes = ['.srt']

# init variables, lists
fullFilePaths = []
n=0
filesOK=0

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
			# include only the specific file types, except their hidden/shadow files
			if filepath.endswith(filetype) and not filename.startswith('.'):
				filePathslist.append(filepath)  # Add it to the list.
	return filePathslist


def replaceChars(folderAsListOfPaths):
    """
    Tries to open .srt file with the encoding type that messes up Turkish characters. If the lines
    can be read properly in this mode (indicating the file has the wrong encoding), then the file is 
    saved with the correct encoding (utf8). If the lines cannot be read, there is a UnicodeDecodeError,
    indicating that the file was already encoded correctly - so no further actions are taken.
    A copy of the file is saved with a suffix; a commented line allows the code to replace the original
    file instead of creating a copy.
    """

    file = open(folderAsListOfPaths[n], "r", encoding='cp1254')

    cleanedName = folderAsListOfPaths[n].replace(directoryPath, '')
    cleanedName = cleanedName.replace('\\', '')

    try:
        lines = file.readlines() # fails HERE if original encoding was already utf8

        newFileContent = ''
        for line in lines: newFileContent += line
        file.close()

        # nameOfNewFile = folderAsListOfPaths[n]   # REPLACES same file
        nameOfNewFile = folderAsListOfPaths[n].replace('.srt', '_FIXED.srt') # saves a copy with suffix

        newFile = open(nameOfNewFile, 'w', encoding='utf8')
        newFile.write(newFileContent)
        newFile.close()
        print("File fixed: "+cleanedName)
        
    except UnicodeDecodeError:
        print("File seems OK: "+cleanedName)
        global filesOK
        filesOK+=1

for type in fileTypes: fullFilePaths.extend(get_filepaths(directoryPath, type))
# fills the fullFilePaths list with the files 
# seems unnecessary if dealing only with .srt files... may be updated to simplify this

print('Finished with files:')

for file in fullFilePaths:	# for every file in this folder
    replaceChars(fullFilePaths)	# replace the characters
    n+=1	# move onto the next file

print("========================")
print("Done!"+"\n"+str(n)+" files processed."+"\n"+str(filesOK)+" didn't need changing.")