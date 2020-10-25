"""
Created by Pınar Barlas; first uploaded to Github October 2020.

PURPOSE/FUNCTION: 
Checks whether it's daytime or nighttime based on current system time,
updates the registry to change Windows to dark/light mode to match. Meant to be run automatically 
via a batch file.
See the attached ReadMe for more information.

TO USE:
Nothing needs to be changed.

FYI:
* Works only on Windows.
* Current thresholds are 7am - 6pm, and hard-coded; future version may extract this variable for easier
updates and personalization. 
* Future version might also switch from 1s and 0s to True and False for functions/variables.
"""

import winreg as wr
import datetime as dt

# determine if it's daylight
def isItDaylight():
    """
    Determines whether it's currently day or night; returns 1 if it's day (i.e. there's light),
    returns 0 if it's night. Takes current hour from system's time, checks it against hard-coded 
    thresholds (currently 7 and 18). Does not consider minutes.
    """
    timeNowHour = dt.datetime.now().hour     # get time now
    # timeNowMinute = dt.datetime.now().minute # might be useful later!

    # check if between the two thresholds (7am, 6pm) or not
    if timeNowHour < 7 or timeNowHour >= 18: itsLightOut=0
    if 18 > timeNowHour >= 7: itsLightOut=1

    return itsLightOut


# LOOK AT AND EDIT KEY

keyVal = r'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Themes\\Personalize'  # key to edit
key = wr.OpenKey(wr.HKEY_CURRENT_USER, keyVal, 0, wr.KEY_ALL_ACCESS) # open the key, returns a PyHKEY object

# get value of AppsUseLightTheme (a key from the registry where its value => the current theme)
currentValue=wr.QueryValueEx(key, "AppsUseLightTheme") 
themeNow=currentValue[0] # if 0, theme is dark. if 1, theme is light.

changeMade=0
def editKey(newValue):
    """
    Sets value of AppsUseLightTheme key from the registry to a variable passed as argument.
    Indicates that a change has been made (updates changeMade variable to 1), prints informative
    message.
    """
    wr.SetValueEx(key, "AppsUseLightTheme", 0, wr.REG_DWORD, newValue)
    global changeMade
    changeMade=1
    print("Theme changed!")

def informativeMessages():
    """
    Prints a number of informative messages independent of actions taken at other parts of code.
    Messages indicate: 1) what time it is currently, 2) whether there is light outside, and
    3) what the current OS theme is.
    """
    # informative message: what is the time now?
    hourNow=dt.datetime.now().hour
    minuteNow=dt.datetime.now().minute
    print("Time now is: "+str("{:02d}".format(hourNow))+":"+str("{:02d}".format(minuteNow)))

    # informative message: is there daylight?
    if not isItDaylight(): justSayNo="NOT "
    elif isItDaylight(): justSayNo=""
    print("Right now it is "+justSayNo+"light outside.")

    # informative message: what is the theme now?
    if themeNow == 0: currentTheme="Dark" 
    elif themeNow == 1: currentTheme="Light"
    print("Currently, the theme is "+currentTheme+".")

def informativeMessage2():
    """
    Prints an informative message only if there was a change made to the theme, indicating what
    the new theme is. (Skips if there was no change made -- if changeMade == 0)
    """
    if changeMade:
        # update themeNow
        currentValue=wr.QueryValueEx(key, "AppsUseLightTheme") 
        themeNow=currentValue[0] # if 0, theme is dark. if 1, theme is light.
        # informative message: what is the theme now?
        if themeNow == 0: currentTheme="Dark" 
        elif themeNow == 1: currentTheme="Light"
        print("The theme is now "+currentTheme+".")
    elif not changeMade: pass

def editIfInconsistent():
    """
    Checks whether the theme matches the daylight status; if they match (e.g. Light theme while
    it's daylight outside) only prints a message indicating no changes are made. If there is a 
    mismatch, edits the key to update the theme. 
    """
    if isItDaylight():
        if themeNow: print("Theme is appropriate, no changes made.")
        elif not themeNow: editKey(1)
    elif not isItDaylight():
        if not themeNow: print("Theme is appropriate, no changes made.")
        elif themeNow: editKey(0)

try:
    informativeMessages()
    print("===================================")
    editIfInconsistent()
    informativeMessage2()
    print("===================================")
except:
    print("Error :(") # mainly for debugging purposes; hopefully you're not seeing this! 

wr.CloseKey(key) # Remember to close the key!