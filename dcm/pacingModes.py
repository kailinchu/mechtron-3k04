from tkinter import *
from PIL import ImageTk, Image
import modeSelection
import Patient as P

background = 'white'
class PacingMode:
    def __init__(self, window):
        self.window = window
        self.window.geometry('500x500')
        self.window.iconbitmap("images\logo.ico")
        self.patient = P.Patient()

    def initFrame(self):
        self.frame = Frame(self.window, bg = background, width = self.width, height = self.height)
        self.frame.place(anchor="c", relx=0.5, rely=0.5)
        self.frame.grid_propagate(False)
        
    def goBack(self, radioBtn): 
            self.frame.destroy()
            getattr(modeSelection.ModeSelect(self.window), radioBtn).select()

    def addTitleAndInstructions(self, mode):
        # title and instructions
        self.titleLabel = Label(self.frame, text = mode, font = ("Arial", 25), bg = background, padx = 10)
        self.instructionLabel = Label(self.frame, text = "Please enter the values for the following parameters", bg = background, padx = 10)
        self.instructionLabel2 = Label(self.frame, text  = "These values will be checked to ensure that they are valid entries", bg = background, padx = 10)

        self.titleLabel.grid(row = 1, column = 1, columnspan = 2)
        self.instructionLabel.grid(row = 2, column = 1, columnspan = 2)
        self.instructionLabel2.grid(row = 3, column = 1, columnspan = 2)

    def addLrl(self, r):
        self.lrlLabel = Label(self.frame, text = "Lower Rate Limit:", bg = background, padx = 10)
        self.lrlEntry = Entry(self.frame, bg = background)
        self.lrlLabel.grid(row = r, column = 1, sticky = W)
        self.lrlEntry.grid(row = r, column = 2, sticky = W)
        self.lrlEntry.insert(0,self.patient.lrl)

    def addUrl(self, r):
        self.urlLabel = Label(self.frame, text = "Upper Rate Limit:", bg = background, padx = 10)
        self.urlEntry = Entry(self.frame, bg = background)
        self.urlLabel.grid(row = r, column = 1, sticky = W)
        self.urlEntry.grid(row = r, column = 2, sticky = W)
        self.urlEntry.insert(0,self.patient.url)

    def addApw(self, r):
        self.apwLabel = Label(self.frame, text = "Atrial Pulse Width:", bg = background, padx = 10)
        self.apwEntry = Entry(self.frame, bg = background)
        self.apwLabel.grid(row = r, column = 1, sticky = W)
        self.apwEntry.grid(row = r, column = 2, sticky = W)
        self.apwEntry.insert(0,self.patient.apw)

    def addAamp(self, r):
        self.aampLabel = Label(self.frame, text = "Atrial Amplitude:", bg = background, padx = 10)
        self.aampEntry = Entry(self.frame, bg = background)
        self.aampLabel.grid(row = r, column = 1, sticky = W)
        self.aampEntry.grid(row = r, column = 2, sticky = W)
        self.aampEntry.insert(0,self.patient.aamp)

    def addBackAndConfirm(self, r, cmdBack, cmdConfirm):
        # add blank row before back and confirm buttons
        self.frame.grid_rowconfigure(r, minsize = 20)

        self.back = Button(self.frame, text = "Back", width=12, command = cmdBack)
        self.back.grid(row = r+1, column = 1, sticky=S)
        self.confirm = Button(self.frame, text = "Confirm changes", width=12, command = cmdConfirm)
        self.confirm.grid(row = r+1, column = 2, sticky = SW)

    def addVpw(self, r):
        self.vpwLabel = Label(self.frame, text = "Ventrical Pulse Width:", bg = background, padx = 10)
        self.vpwEntry = Entry(self.frame, bg = background)
        self.vpwLabel.grid(row = r, column = 1, sticky = W)
        self.vpwEntry.grid(row = r, column = 2, sticky = W)
        self.vpwEntry.insert(0,self.patient.vpw)

    def addVamp(self, r):
        self.vampLabel = Label(self.frame, text = "Ventrical Amplitude:", bg = background, padx = 10)
        self.vampEntry = Entry(self.frame, bg=background)
        self.vampLabel.grid(row = r, column = 1, sticky = W)
        self.vampEntry.grid(row = r, column = 2, sticky = W)
        self.vampEntry.insert(0,self.patient.vamp)

    def addAsens(self, r):
        self.asensLabel = Label(self.frame, text = "Atrial Sensitivity:", bg = background, padx = 10)
        self.asensEntry = Entry(self.frame, bg=background)
        self.asensLabel.grid(row = r, column = 1, sticky = W)
        self.asensEntry.grid(row = r, column = 2, sticky = W)
        self.asensEntry.insert(0,self.patient.asens)

    def addArp(self, r):
        self.arpLabel = Label(self.frame, text = "ARP:", bg = background, padx = 10)
        self.arpEntry = Entry(self.frame, bg=background)
        self.arpLabel.grid(row = r, column = 1, sticky = W)
        self.arpEntry.grid(row = r, column = 2, sticky = W)
        self.arpEntry.insert(0,self.patient.arp)

    def addPvarp(self, r):
        self.pvarpLabel = Label(self.frame, text = "PVARP:", bg = background, padx = 10)
        self.pvarpEntry = Entry(self.frame, bg=background)
        self.pvarpLabel.grid(row = r, column = 1, sticky = W)
        self.pvarpEntry.grid(row = r, column = 2, sticky = W)
        self.pvarpEntry.insert(0,self.patient.pvarp)

    def addHystBool(self, r):
        self.hystBool = Checkbutton(self.frame,text = "Hysteresis",command=self.updateFields, bg=background,padx=10)
        self.hystBool.grid(row=r,column=1,sticky=W)
        if(self.patient.hrl==0):
            self.hystBool.deselect()
        else:
            self.hystBool.select()

    def addHyst(self, r):
        boolState="normal"
        if(self.patient.hrl==0):
            boolState="disabled"
    
        self.hystLabel = Label(self.frame, text = "Hysteresis:", bg = background, padx = 10)
        self.hystEntry = Entry(self.frame, bg=background, state=boolState)
        self.hystLabel.grid(row = r, column = 1, sticky = W)
        self.hystEntry.grid(row = r, column = 2, sticky = W)
        self.hystEntry.insert(0,self.patient.hrl)

    def addRs(self, r):
        self.rsLabel = Label(self.frame, text = "Rate Smoothing:", bg = background, padx = 10)
        self.rsEntry = Entry(self.frame, bg=background)
        self.rsLabel.grid(row = r, column = 1, sticky = W)
        self.rsEntry.grid(row = r, column = 2, sticky = W)
        self.rsEntry.insert(0,self.patient.rs)
    
    def addVsens(self, r):
        self.vsensLabel = Label(self.frame, text = "Ventricular Sensitivity:", bg = background, padx  = 10)
        self.vsensEntry = Entry(self.frame, bg=background)
        self.vsensLabel.grid(row = r, column = 1, sticky = W)
        self.vsensEntry.grid(row = r, column = 2, sticky = W)
        self.vsensEntry.insert(0,self.patient.vsens)

    def updateFields(self):
        print("triggered")

        if(self.hyst==True):
            self.hyst=False
            self.hystEntry.config(state= "disabled")
        else:
            self.hyst=True
            self.hystEntry.config(state= "normal")

class AOO(PacingMode): 
    def __init__(self, window, patient):
        super().__init__(window)
        self.width = 450
        self.height = 350
        self.window.title("Pacemaker | AOO Pacing Mode")
        self.patient=patient
        
        #Methods
        def aooConfirm(): 
            pass
        
        def goBack(): 
            self.goBack("aooRadio")
        
        #AOO Frame
        self.initFrame()
        
        #Elements on the page
        self.addTitleAndInstructions("AOO")
        self.addLrl(4)
        self.addUrl(5)
        self.addApw(6)
        self.addAamp(7)
        self.addBackAndConfirm(8, goBack, aooConfirm)

class VOO(PacingMode): 
    def __init__(self, window, patient):
        super().__init__(window)
        self.width = 450
        self.height = 350
        self.window.title("Pacemaker | VOO Pacing Mode")
        self.patient=patient
        
        #Methods
        def vooConfirm(): 
            pass
        
        def goBack(): 
            self.goBack("vooRadio")
        
        #VOO Frame
        self.initFrame()
        
        #Elements on the page
        self.addTitleAndInstructions("VOO")
        self.addLrl(4)
        self.addUrl(5)
        self.addVpw(6)
        self.addVamp(7)
        self.addBackAndConfirm(8, goBack, vooConfirm)

class AAI(PacingMode): 
    def __init__(self, window, patient):
        super().__init__(window)
        self.width = 450
        self.height = 450
        self.window.title("Pacemaker | AAI Pacing Mode")
        self.patient=patient

        #set these to patient specific parameters
        self.hyst=False
        
        #Methods 
        def aaiConfirm(): 
            pass
        
        def goBack(): 
            self.goBack("aaiRadio")

        #AAI Frame
        self.initFrame()
        
        #Creating all the elements for the AAI Page
        self.addTitleAndInstructions("AAI")
        self.addLrl(4)
        self.addUrl(5)
        self.addApw(6)
        self.addAamp(7)
        self.addAsens(8)
        self.addArp(9)
        self.addPvarp(10)
        self.addHystBool(11)
        self.addHyst(12)
        self.addRs(13)
        self.addBackAndConfirm(14, goBack, aaiConfirm)
    
class VVI(PacingMode): 
    def __init__(self, window, patient):
        super().__init__(window)
        self.width = 450
        self.height = 450
        self.window.title("Pacemaker | VVI Pacing Mode")
        self.patient=patient

        #set these to patient specific parameters
        self.hyst=False
        
        def vviConfirm(): 
            pass
        
        def goBack(): 
            self.goBack("vviRadio")
        
        #VVI Frame
        self.initFrame()
        
        #Creating the elements for the VVI Frame
        self.addTitleAndInstructions("VVI")
        self.addLrl(4)
        self.addUrl(5)
        self.addVpw(6)
        self.addVamp(7)
        self.addVsens(8)
        self.addHystBool(9)
        self.addHyst(10)
        self.addRs(11)
        self.addBackAndConfirm(12, goBack, vviConfirm)
                
    
def launchAOO(window, patient): 
    AOO(window, patient)
    
def launchVOO(window, patient): 
    VOO(window, patient)

def launchAAI(window, patient): 
    AAI(window, patient)

def launchVVI(window, patient): 
    VVI(window, patient)
'''
def backToSelect(window):
    modeSelection.ModeSelect(window)
'''    
    