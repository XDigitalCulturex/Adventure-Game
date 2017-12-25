import pickle
import tkFileDialog, tkMessageBox
import sys
from Tkinter import *
from ScrolledText import *
import os
import time
import random
from PIL import Image, ImageTk  


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
                 "values":{"Blue Paladin":{"picture":"./Gameidea/Fantasy/20170812_143454.jpg","Keywords":["Human","Male"],"Ability":["Shield Block","Defend Others"]}}}

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
        self.charLabel=dict()
        self.charTemplates = drpDown
        
        '''
        gui to pick party members
        '''
        self.doDrop(drpDown)


        self.bottom_frame = Frame(self).pack(side = BOTTOM, padx = 15, pady  =5)
##        for k,v in bttnEntry.iteritems():
##            self.entryDict[k] = Button(self.bottom_frame,height = 3, text = k, default = 'active', command = lambda opt = [k,v]: self.runIt(opt)).pack(side = RIGHT,fill='x',pady=30,padx=5)
        self.done = Button(self.bottom_frame, text = "Select Character", default = 'active', command = self.doEntries)
        self.done.pack(side = TOP)
        self.TxT = ScrolledText(self.bottom_frame)

        self.TxT.pack(side = BOTTOM)
        self.TxT.insert(END,'\n')

        self.charPic = ImageTk.PhotoImage(Image.open(charTemplates["values"]["Blue Paladin"]["picture"]).resize((250,200), Image.ANTIALIAS).rotate(-90))
        self.charLabel[0] = Label(self.bottom_frame, height = 250, width = 200, image=self.charPic)
        self.charLabel[0].pack(side=TOP, padx=5, pady=5)              
        
        
        self.master.mainloop()

    def doDrop(self, dic={}):
        self.drpDown = dic        
        self.drpDownKeys = self.drpDown["keys"]
        self.DDval = StringVar()
        self.Drop = OptionMenu(self.dialog_frame, self.DDval, *tuple(self.drpDownKeys), command= self.addTxt)
    
        self.Drop.pack()

    def addTxt(self, var):
        self.TxT.insert(END,'\n')
        self.TxT.insert(END, "Keywords: " + ', '.join(self.charTemplates["values"][var]["Keywords"]) + "\n")
        self.TxT.insert(END, "Ability: " + ', '.join(self.charTemplates["values"][var]["Ability"]) + "\n")        
        
    def doEntries(self):
        self.returns = {}
        self.returns["title"] = self.master.title()
        self.returns["name"] = self.charEnt.get()
        self.returns["character"] = self.DDval.get()
        self.returns["keywords"] = self.charTemplates["values"][self.returns["Character"]]["Keywords"]
        self.returns["ability"] = self.charTemplates["values"][self.returns["Character"]]["Ability"]
        self.master.quit()
        removeWindows(self.master)
        self.pack_forget()
        self.destroy()
        return self.returns

def removeWindows(vals):
    for x in vals.winfo_children():
        for y in x.winfo_children():
            y.destroy()
        x.destroy()                                                     

def buildCharacter(tempWorld):
    '''
    go through the status and needs for character creation
    '''
    returns=[]
    x=0
    while x < tempWorld:
        x+=1        
        returns.append(partyScreen(root, "Select Character " + str(x)).returns)
    print returns    
 
##    tempWorld.characterList = guiFrame(root, [], "Pick Char", bttnEntry=chars).cmd
##    print guiFrame(root,[], "Pick ability",bttnEntry={"Talents":["Sailing","Navigation"]})
    return returns



if __name__ == "__main__":
    root = Tk()
    guiPreferences(root,"Main Window")
    tempWorld = 2
    buildCharacter(tempWorld)

    guiPreferences(root,"Main Window")    
    root.mainloop()
