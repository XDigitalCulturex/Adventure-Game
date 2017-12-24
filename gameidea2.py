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
        if "_currentVehicle" not in locals():
            self._currentVehicle =[var]
        if var in self._currentVehicle:
            
            self._currentVehicle.remove(var)
        else:
            self._currentVehicle = add2List(var,self_currentVehicle)
        
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
            doEvent(completeEvents[val])

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
        if os.path.exists("./saves") == False:
            os.mkdir("./saves")
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

##terrains = [["Tomb",2,["mummy","giant snake"],["Dungeon",2,["Troll"," "]],["Forest",1,["Elf","Dryad"],["Desert",1,["Bug Ranger", "WereCroc"]]

def generateSpot():
    '''
    Generate a location
    '''
    return location

class locale(object):
    def __init__(self,x,y,z,nEx=False,sEx=False, wEx=False,eEx=False,upEx=False,dEx=False):
        self.Xcoord = x
        self.Ycoord = y
        self.Zcoord = z
        self.southExit =sEx
        self.northExit = nEx
        self.westExit = wEx
        self.eastExit = eEx
        self.upExit = upEx
        self.downExit = dEx
        self.encounteredofType = 0
        self.tileTypes()

    def pickRules(self):
        self.encounteredofType +=1


    def tileTypes(self):
        self.Types = ["Desert Temple", "Dirty Town", "Castle", "Dungeon","Outdoors","Lava","Crystal","Underground"]
        self.themeID = range(len(self.Types))
        self.tileDict = {}
        self.tileLst = []
        x=0
        while x < len(self.Types):
            self.tileDict[x] = self.Types[x]
            self.tileLst.append({"ID":x,"Theme":self.Types[x]})
    
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

class locale(object):
    def __init__(self,x,y,z,nEx=False,sEx=False, wEx=False,eEx=False,upEx=False,dEx=False):
        self.Xcoord = x
        self.Ycoord = y
        self.Zcoord = z
        self.southExit =sEx
        self.northExit = nEx
        self.westExit = wEx
        self.eastExit = eEx
        self.upExit = upEx
        self.downExit = dEx
        self.encounteredofType = 0
        self.tileTypes()

    def pickRules(self):
        self.encounteredofType +=1


    def tileTypes(self):
        self.Types = ["Desert Temple", "Dirty Town", "Castle", "Dungeon","Outdoors","Lava","Crystal","Underground"]
        self.themeID = range(len(self.Types))
        self.tileDict = {}
        self.tileLst = []
        x=0
        while x < len(self.Types):
            self.tileDict[x] = self.Types[x]
            self.tileLst.append({"ID":x,"Theme":self.Types[x]})    

class guiFrame(Frame):
    '''To create a frame that will be added in to the root Tk object'''    
    def __init__(self, master, numBox=[], title = "Start", returnType = "string", cmbBox=[], bttnEntry={}, drpDown = {"Keys":[]}):
        Frame.__init__(self, master)
        self.grid_propagate(0)
        self.master = master
        self.cmd=""
        self.returnType = returnType
        self.dialog_frame = Frame(self).pack(side = TOP, padx=20, pady=15)
        self.master.attributes("-topmost", True)
        self.master.resizable(False, False)
        self.master.tk_setPalette(background = "#ececec")
        x = (self.master.winfo_screenwidth() - self.master.winfo_reqwidth())/2
        y = (self.master.winfo_screenheight() - self.master.winfo_reqheight())/3
        self.master.geometry("+{}+{}".format(x,y))
        self.master.protocol('WM_DELETE_WINDOW',lambda : self.cancelFr(self.cmd))
        self.master.bind('<Return>', lambda : self.cancelFr(self.cmd))
        self.master.bind('<Escape>', lambda : self.cancelFr(self.cmd))
        addMenuHelp(self,{"Help me": "http://google.com"})
        self.numBox = numBox

        if drpDown["Keys"] != []:
            self.doDrop(drpDown)
        
        self.entryDict = {}
        x=0
        for lbl in self.numBox:
            self.entryDict[lbl] = Label(self.dialog_frame, text = lbl)
            self.entryDict[lbl].pack(side=TOP)             
            self.entryDict[str(x)] = Entry(self.dialog_frame, width=45)          
            self.entryDict[str(x)].pack(side=TOP, expand=YES, pady=2, anchor=W)           
            x+=1
        self.cmbBox = cmbBox

        bottom_frame = Frame(self).pack(side = BOTTOM, padx = 15, pady  =5)
        for k,v in bttnEntry.iteritems():
            self.entryDict[k] = Button(self.dialog_frame,height = 3, text = k, default = 'active', command = lambda opt = [k,v]: self.runIt(opt)).pack(side = RIGHT,fill='x',pady=30,padx=5)
        done = Button(bottom_frame, text = "Done", default = 'active', command = self.doEntries).pack(side = TOP)
        self.TxT = ScrolledText(bottom_frame)
        self.TxT.pack(side = BOTTOM)
        
        self.master.mainloop()

    def doDrop(self, dic={}):
        self.drpDown = dic        
        self.drpDownKeys = self.drpDown["Keys"]
        self.DDval = StringVar()
        self.Drop = OptionMenu(self.dialog_frame, self.DDval, self.drpDownKeys)
        self.Drop.pack()

    def runIt(self, *args):
        '''
        executes function of funky and adds output to self.cmd
        '''
        globals()[args[0][1]](args[0][0])
        if self.cmd == "list":
            self.cmd.append(val)
        else:
            self.cmd = val

    def doEntries(self, *args):
        '''
        compile all the values from the entry boxes
        '''
        try:
            val = []
            for k in self.entryDict.keys():
                if k.isdigit() == True:
                    val.append(self.entryDict[k].get())
            if self.DDVal in locals():
                val.append(self.DDVal)
        except:
            print "failed"
                
charTemplates = {"Keys":["DoubleDrizzle"],"Values":{"DoubleDrizzle":{"picture":"","Keywords":["Human","Navigator"],"Ability":["Reduce Danger by 1",""]}}}

def buildCharacter(var):
    '''
    go through the status and needs for character creation
    '''
    var = guiFrame(root, [],var,drpDown=charTemplates).cmd
    tempWorld.players = int(guiFrame(root, ["How many characters do you have?"], "How many players do you have?").cmd[0])
    chars = {}
    x= 0
    print tempWorld.players
    while x < int(tempWorld.players):
        x+=1        
        chars["Pick Character " + str(x)] = "buildCharacter"
    tempWorld.characterList = guiFrame(root, [], "Pick Char", bttnEntry=chars).cmd
    print guiFrame(root,[], "Pick ability",bttnEntry={"Talents":["Sailing","Navigation"]})

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
    root = Tk()
    if os.path.exists("./saves/001.sve")==False:
    
        tempWorld = curWorld()
            
        tempWorld.players = gui(1, "How many players do you have?", "integer")
        saveFile("./saves/001",tempWorld)
    else:
        tempWorld = loadFile("./saves/001")
