import pickle
import tkFileDialog, tkMessageBox
import sys
from Tkinter import *
from ScrolledText import *
import os
import time
import random

def killIt(TkObj):
    ''' Ends a loop and destroys said object'''
    TkObj.quit()
    TkObj.destroy()

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
    menuBar = Menu(guiObj)
    helpMenu = Menu(menuBar)
    for k,v in entries.iteritems():
        helpMenu.add_command(label=k,command=lambda k=k: os.startfile(entries[k]))
    menuBar.add_cascade(label='Help',menu=helpMenu)
    guiObj.config(menu=menuBar)
    helpMenu.config(background=masterBackground,fg='white')    

def guiPreferences(TkWindow, title):
    '''Set up things in the Tk window with the custom formatting'''
    master = TkWindow

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
    Setting up size and short cut prefs
    '''
    TkWindow.grid_propagate(0)
    master.title(title)
    master.attributes("-topmost", True)
    master.resizable(False, False)
    master.tk_setPalette(background = "#ececec")
    x = (master.winfo_screenwidth() - master.winfo_reqwidth())/2
    y = (master.winfo_screenheight() - master.winfo_reqheight())/3
    master.geometry("+{}+{}".format(x,y))
    master.protocol('WM_DELETE_WINDOW',lambda : killIt(TkWindow))
##    master.bind('<Return>', lambda : pass)
    master.bind('<Escape>', lambda : TkWindow.quit)
    addMenuHelp(master,{"Help me": "http://google.com", "Change Number in Party":""})


charTemplates = {"keys": ["Blue Paladin","Gold Dwarf"],
                 "values":{"Blue Paladin":{"picture":"./GameIdea/Fantasy/20170812_143454.jpg","Keywords":["Human","Male"],"Ability":["Shield Block","Defend Others"]}}}

class partyScreen(Frame):
    '''The screen for all things setting up your party'''
    def __init__(self, master, title ="Create your party", partynum = 2, drpDown=charTemplates):
        Frame.__init__(self, master)
        guiPreferences(master, title)
        self.dialog_frame = Frame(self).pack(side = TOP, padx=20, pady=15)
        self.charN = Label(self.dialog_frame, text = "Character Name")
        self.charN.pack(side=TOP)             
        self.charEnt = Entry(self.dialog_frame, width=45)          
        self.charEnt.pack(side=TOP, expand=YES, pady=2, anchor=W)

        
        '''
        gui to pick party members
        '''
        self.doDrop(drpDown)


        bottom_frame = Frame(self).pack(side = BOTTOM, padx = 15, pady  =5)
##        for k,v in bttnEntry.iteritems():
##            self.entryDict[k] = Button(self.bottom_frame,height = 3, text = k, default = 'active', command = lambda opt = [k,v]: self.runIt(opt)).pack(side = RIGHT,fill='x',pady=30,padx=5)
        done = Button(bottom_frame, text = "Done", default = 'active', command = self.doEntries)
        done.pack(side = TOP)
        self.TxT = ScrolledText(bottom_frame)

        self.TxT.pack(side = BOTTOM)
        self.TxT.insert(END,'\n')
        self.picFrame = PhotoImage(file= charTemplates["values"]["Blue Paladin"]["picture"])
        self.TxT.image_create(END, image=self.picFrame)                
        
        
        self.master.mainloop()

    def doDrop(self, dic={}):
        self.drpDown = dic        
        self.drpDownKeys = self.drpDown["keys"]
        self.DDval = StringVar()
        self.Drop = OptionMenu(self.dialog_frame, self.DDval, tuple(self.drpDownKeys))
        self.Drop.pack()
        
    def doEntries(self):
        self.returns = {}
        self.returns["Name"] = self.charEnt.get()
        self.returns["Character"] = self.DDval.get()

##def buildCharacter(var):
##    '''
##    go through the status and needs for character creation
##    '''
##    var = guiFrame(root, [],var,drpDown=charTemplates).cmd
##    tempWorld.players = int(guiFrame(root, ["How many characters do you have?"], "How many players do you have?").cmd[0])
##    chars = {}
##    x= 0
##    print tempWorld.players
##    while x < int(tempWorld.players):
##        x+=1        
##        chars["Pick Character " + str(x)] = "buildCharacter"
##    tempWorld.characterList = guiFrame(root, [], "Pick Char", bttnEntry=chars).cmd
##    print guiFrame(root,[], "Pick ability",bttnEntry={"Talents":["Sailing","Navigation"]})



if __name__ == "__main__":
    root = Tk()
    tempWorld = 2
    partyScreen(root)
