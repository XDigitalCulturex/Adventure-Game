import pickle
import tkFileDialog, tkMessageBox
import sys
from Tkinter import *
import ScrolledText
import os
import time
import random

def add2List(var, orgAttr):
    '''
    check if the variable is a list to append to current list
    or if its a value to add alone
    '''
    
    if type(var) == type(list):
        for val in var:
            orgAttr.append(val)
    else:
        orgAttr.append(var)
    return orgAttr
    

class curWorld(object):
    def __init__(self, curTime = 0, curQuest = ["Find a place to rest safely"], curCaravan = ["Wagon"], curVehicle=["Wagon"]):
        '''
        creates basic attributes for all of the possible needed save states
        '''
        self.currentAdventurers = []
        self.currentQuests = curQuest
        self.currentLocation = {}
        self.currentKeywords=[]
        self.curTime = curTime
        self.caravanLocations = curCaravan
        self.caravanVehicle = curVehicle

    @property
    def curTime(self):
        '''
        A list of the characters in the party
        '''
        return self._curTime

    @curTime.setter
    def curTime(self, var):
        self._curTime = var

    @property
    def characterList(self):
        '''
        A list of the characters in the party
        '''
        return self._characterList

    @characterList.setter
    def characterList(self, var):
        if self._characterList not in locals():
            self._characterList = add2List(var, self._characterList)
        else:
            self._characterList( var, [])
        
            
    @property
    def caravanVehicle(self):
        '''
        What type of vehicle does the character have
        '''
        return self._caravanVehicle

    @caravanVehicle.setter
    def caravanVehicle(self,var):
        if var in self._currentKeywords:
            
            self._currentKeywords.remove(var)
        else:
            self._currentKeywords = add2List(var,self_currentKeywords)
        
    @property
    def gridMap(self):
        '''
        Track all the locations available on the map
        '''
        return self._gridMap
        
    @gridMap.setter
    def gridMap(self,var,direction):
        temp = generateSpot()
        self._gridMap["{}{}{}".format(self.curSpotX, ",", self.curSpotY)] = temp
        
    @property
    def timelineEvents(self):
        '''
        dictionary of timeline where the keys are the time
        and values are ids of events.
        '''
        return self._timelineEvents
    @timelineEvents.setter
    def timelineEvents(self, var, timefrmNow=1):
        if not self._timelineEvents :
            self._timelineEvents = {}
        self._timelineEvents[timefrmNow].append(var)
        
def settlementQuery(settlementNam):
    '''
    settlementNam Show attributes of the settlement
    '''
    return tempWorld.Settlements[settlementNam]
    
events = [[1,"Acid rain", "Outdoor", "Acid rain falls from the heavens and you must seek shelter.","Check Acrobatics or Survival "]]

eventsTemplate=["ID","Name","Traits","Description","Mechanisms"]

completeEvents={}

def add2timeline(var, x):
    '''
    add an event to the future timeline
    '''
    tempWorld.timeLine[tempWorld.curTime + x].append(var)
    
def checkTimeline():
    '''
    see if anything needs to happen based on current time
    '''
    if tempWorld.timeLine[curTime] != []:
        for val in tempWorld.timeLine[curTime]:
            doEvent(completeEvents[val)

def advanceTimeline(advance = 1):
    '''
    Add a bit of time to the current timeline
    '''
    tempWorld.curTime += advance

def loadFile(save="./001"):
    '''
    Load previously saved data
    '''
    try:
        with open(''.join([save,".sve"]),'rb') as log:
            saves = pickle.load(log)
        return saves
    except pickle.UnpicklingError:
        print "File can't be loaded"
        return False

def saveFile(save="", data=[]):
    '''
    Save current data
    '''
    try:
        with open(''.join([save,".sve"]),'wb') as log:
            pickle.dump(data, log)
        return True
    except pickle.PicklingError:
        print "Object can't be saved"
        return False

##a = curWorld()
##saveFile(r"H:/test",a)
##a = loadFile(r"H:/test")

terrainSchema = {"Name": " ", "Danger":0, "Basic Encounters":[],}

terrains = [["Tomb",2,["mummy","giant snake"],["Dungeon",2,["Troll"," "]],["Forest",1,["Elf","Dryad"],["Desert",1,["Bug Ranger", "WereCroc"]]

def generateSpot():
    '''
    Generate a location
    '''
    return location
    
creatureSchema = {"creature":"", "stories":[{"":""},{"":""}],
                  "clues":[{"Debris": []}],
                  "hit locations":[],
                  "size":"",
                  "picture_id":"", "keywords":[], "resources":[]
  }

def addMenuHelp(guiObj, entries):
    '''
    This function adds a menu to a gui object
    Inputs:
    guiObj - the Tk() object that is going to have a menu added to it
    entries - a python dictionary with keys as labels and values as links
    '''

    '''
    Setting default colors for use with adding objects in Tk()
    '''
    sunkenColor = '#%02x%02x%02x' % (24,50,100)
    raisedColor = '#%02x%02x%02x' % (24,142,186)
    hoverColor = '#%02x%02x%02x' % (0,100,150)
    masterBackground = '#%02x%02x%02x' % (70,70,70)
    frameBackground = '#%02x%02x%02x' % (0,0,0)
    entryBackground = '#%02x%02x%02x' % (40,40,40)    
    buttBackground = '#%02x%02x%02x' % (24,142,186)

    '''
    The code for adding the menu to the gui object
    '''
    menuBar = Menu(guiObj.master)
    helpMenu = Menu(menuBar)
    for k,v in entries.iteritems():
        helpMenu.add_command(label=k,command=lambda k=k: os.startfile(entries[k]))
    menuBar.add_cascade(label='Help',menu=helpMenu)
    guiObj.master.config(menu=menuBar)
    helpMenu.config(background=masterBackground,fg='white')

class gui(object):
    """Graphical User Interface template"""
###### tool needs a number of text boxes and a title to execute
    def __init__(self, numBox=1, title = "Start", Browse = False):
            """
            initfname - path to initial library (integer value opens file dialog on startup)
            defaultReverse - coverage to initially highlight in coverages list
            reverseElevated - feature tables of elevated priority
            title - title of GUI
            """
            self.master = Tk() #start Tkinter
            self.numBox = numBox
            self.Browse = False
            self.configureGui(title) #build user interface elements
            
            self.master.mainloop()


    def configureGui(self, title):
        """build the GUI.  Use pack methods.  Frames in lower portion is built in individual
        confiture routines."""

        self.master.title(title)
        self.master.iconname(title)
        self.master.protocol('WM_DELETE_WINDOW', self.master.destroy)
        self.cFrame = Frame(self.master)
        self.cFrame.pack(side=TOP, fill=X)
        Label(self.cFrame, text=title).pack(side=TOP, anchor=W)
        self.varDict = {}
        x=0
        while x < self.numBox:
            self.varDict[str(x)] = Entry(self.cFrame, width=45)
##            self.varDict[k].bind('<Button-3>', self.rClicker)           
            self.varDict[str(x)].pack(side=TOP, expand=YES, pady=2, anchor=W)
            x+=1
##        if self.chB == True:            
##            self.chton = Checkbutton(self.master, text = self.chBtxt, variable=self.var, command = self.chkClk)
##            self.chton.pack(side = TOP, fill=X)
##            self.chBx = self.var.get()

        if self.Browse >= True:            
            Button(self.cFrame, text="Browse for save file", width=13,command=self.browseButton).pack(side=RIGHT)     
        self.closeButton = Button(self.master, text="Close", command=self.cancel_command)
        self.closeButton.pack(side=RIGHT)

        self.submitButton = Button(self.master, text="Submit", command=self.subFunk)
        self.submitButton.pack(side=RIGHT)

    def subFunk(self):
        self.cmd = self.varDict["0"].get()

    def cancel_command(self, event = None):
        self.master.quit()
        self.master.destroy()
        
    def browseButton(self, event=None):

        inPath=tkFileDialog.askfileopen(title="Browse to a save.", mustexist=True)
        print inPath
        if inPath:
            self.varDict["0"].delete(0, END)
            self.varDict["0"].insert(0, inPath)

if __name__ == "__main__":
    if os.path.exists("/saves/001.sve")==False:
    
        tempWorld = curWo
            
        temp tempWorld.players = gui(1, "How many players do you have?", "integer")
        saveFile("/saves/001",tempWorld)
    else:
        tempWorld = loadFile("/saves/001")