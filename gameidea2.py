import pickle
import tkFileDialog, tkMessageBox
import sys
from Tkinter import *
import ScrolledText
import os
import time

class curWorld(object):
    def __init__(self, curTime = 0):
        '''
        creates basic attributes for all of the possible needed save states
        '''
        self.currentAdventurers = []
        self.currentQuests = []
        self.currentLocation = {}
        self.currentKeywords=[]
        self.curTime = curTime

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
        self._characterList = var

    @property
    def caravanVehicle(self):
        '''
        What type of vehicle does the character have
        '''
        return self._caravanVehicle

    @caravanVehicle.setter
    def CaravanVehicle(self,var):
        self._caravanVehicle = var

    @property
    def caravanLocations(self):
        '''
        What locations are available wherever the caravan goes
        '''
        return self._caravanLocations

    @caravanLocations.setter
    def caravanLocations(self,var):
        if self._caravanLocations not in locals():
            self._caravanLocations = [var]
        else:
            self._caravanLocations.append(var)

    @property
    def caravanResources(self):
        '''
        What resources are available wherever the caravan goes
        '''
        return self._caravanResources

    @caravanResources.setter
    def caravanResources(self,var):
        if self._caravanResources not in locals():
            self._caravanResources = [var]
        else:
            self._caravanResources.append(var)

    @property
    def caravanGear(self):
        '''
        What geaer are available wherever the caravan goes
        '''
        return self._caravanGear

    @caravanGear.setter
    def caravanGear(self,var):
        if self._caravanGear not in locals():
            self._caravanGear = [var]
        else:
            self._caravanGear.append(var)               

    @property
    def players(self):
        '''
        The number of players to keep track of
        '''
        return self._players

    @players.setter
    def players(self,var):
        self._players = var
    
    @property
    def currentKeywords(self):
        '''
        All the keywords currently in the party
        '''
        return self._currentKeywords
    @currentKeywords.setter
    def currentKeywords(self,var):
        self._currentKeywords = var
        
    @property
    def gridMap(self):
        '''
        Track all the locations available on the map
        '''
    @gridMap.setter
    def Add2gridMap(self,var):
        temp = generateSpot()

def settlementQuery(settlementNam):
    '''
    settlementNam Show attributes of the settlement
    '''
    pass

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
            doEvent(val)

def advanceTimeline(advance = 1):
    '''
    Add a bit of time to the current timeline
    '''
    tempWorld.setcurTime += advance

def loadFile(save="./001"):
    '''
    Load previously saved data
    '''
    try:
        with open(''.join([save,".sve"]),'rb') as log:
            pickle.load(log)
        return saves
    except pickle.UnpicklingError:
        print "File can't be loaded"
        return None

def saveFile(save="", data=[]):
    '''
    Save current data
    '''
    try:
        with open(''.join([save,".sve"]),'rb') as log:
            pickle.dump(data, log)
        return True
    except pickle.PicklingError:
        print "Object can't be saved"
        return False

terrainSchema = {"Name": "", "Danger":0, "Basic Encounters":[],}

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

    tempWorld = curWorld()
        
    tempWorld.players = gui(1, "How many players do you have?", "integer")
