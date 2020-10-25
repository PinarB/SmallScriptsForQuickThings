# ReadMe for SmallScriptsForQuickThings

Written by **[Pınar Barlas](https://www.pinarbarlas.com/ "pinarbarlas.com")**, first uploaded to Github October 2020.

### Contents of this repository

In this repository, there are four Python scripts, independent of each other. In the following sections of this ReadMe, you can find the description and a sample use case of each script, followed by information on how to use the script and things to keep in mind.

---

## Script: generateListOf_Files.py

This script goes through a directory to generate a list of files in the directory (including subfolders). The script checks for specific file types, ignoring other files. Outputs a .txt file where each line corresponds to a file in the directory; any subfolders appear at the beginning of the line, which allows visual grouping since the list is alphabetized.

**My use case:** I use this script to list the files I have saved under a folder in my external hard disk. My version of the script looks for videos (ignoring subtitles). The videos in the archive subfolder appear together in the final list. By having this .txt file on my computer, I can avoid connecting the external disk to check whether a specific file is in there.

### How to use this script

1. Update directoryPath (string) to your directory containing the files to be processed.

2. Update fileTypes (list containing strings) to reflect the file extensions to be processed.

3. Update savePath (string) to your directory where the resulting text file should be saved.

4. Update saveName (string) to the desired file name for the resulting text file (without extension).

5. Run the script!

### Things to remember, Bugs, and Future Features

None found/none planned - [let me know](#contact-me) if you have an idea!

---

## Script: generateListOf_Folders.py

This script goes through a directory to generate a list of subfolders in the directory and the number of files each subfolder contains. The script can ignore certain folders if desired. Outputs a .txt file where each line corresponds to the name of a folder in the directory, followed by a number in parantheses which indicates the number of files within that folder.

**My use case:** I use this script to keep an inventory of the folders I have saved in a directory in my external hard disk. Each folder corresponds to a video project while the number of files within the folder indicates the number of "episodes" completed. By having this .txt file on my computer, I can avoid connecting the external disk to check how many episodes we have.

### How to use this script

1. Update unwantedFolders (list containing strings) to include the exact name of the folders to be ignored in the listing process.

2. Update fileTypes (list containing strings) to reflect the file extensions to be processed.

3. Update savePath (string) to your directory where the resulting text file should be saved.

4. Update saveName (string) to the desired file name for the resulting text file (without extension).

5. Run the script!

### Things to remember, Bugs, and Future Features

The number of files, indicated in parantheses, makes no distinction regarding the file types or other details; this may be added in the future.  Also, the code is not very "clean" or compact, I will probably tidy it up in the future with functions.

[Let me know](#contact-me) if you have an idea for a future feature or found a bug!

---

## Script: fixSubs_TR.py

This script goes through all .srt files in a directory, and makes sure they are all encoded
with *utf8* (saving an identical copy encoded with *utf8* if not). Created to deal with wrongly-encoded Turkish subtitles, which usually have the encoding *cp1254*.

**My use case:** I use this script to check and automatically fix the Turkish subtitles I have found. By using this script, I can make sure an entire folder of subtitles will function correctly, without having to check (and fix) each file individually. In my version, the script actually *replaces* the original file.

### How to use this script

1. Update directoryPath (string) to your directory containing the files to be fixed.

2. Run the script!

### Things to remember, Bugs, and Future Features

Created to deal with Turkish subtitles (wrongly-)encoded with a specific encoding. To use with other languages or encodings, determine the encoding that is causing the problem, replace *cp1254* in the script with that encoding, and check. I am **not** planning to expand this script to deal with other encodings/languages; I might however tidy up the code to hard-code the '.srt' selection as an earlier draft of the script dealt with multiple file types.

---

## Script: autoDarkmode.py

This script checks whether it's daytime or nighttime based on current system time, and changes the Windows theme (by editing the registry) to dark/light mode to match. Currently, the script changes modes at 7am and 6pm.

**My use case:** I have a batch file that runs this script twice a day at specific times and at user logon. This way, my system always uses dark mode after sundown, and always light mode during the day.

### How to use this script

Nothing needs to be changed in the script. However, to automate the script in the same manner as my setup as described above, create a .bat file consisting of the following, and run it at desired times via Task Scheduler:
`"C:\location\of\python.exe" "C:\location\of\autoDarkmode.py" pause 
timeout 10`
where the first line points to first the Python application, then to this script, and the second line ensures that the Command Line window stays open for 10 seconds after the script runs, giving the user enough time to see what has happened and read the informative messages.

### Things to remember, Bugs, and Future Features

This script presumably works only on Windows, and it edits the registry (so proceed with caution, especially if altering the code). Currently, the thresholds for changing modes are hard-coded; in the future, I may extract these as variables to make updates and personalization easier. I may also switch from 1/0 to True/False for functions & variables.

---

### Contact me

If you need to contact me for whatever reason, please do so through my website **[pinarbarlas.com](https://www.pinarbarlas.com/)**.

---