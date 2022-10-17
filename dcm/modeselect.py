from tkinter import *

def openMode():
    mode = modeVar.get()
    chooseFrame.grid_remove()
    if mode == "AOO":
        aooFrame.grid()
    elif mode == "VOO":
        vooFrame.grid()
    elif mode == "AAI":
        aaiFrame.grid()
    elif mode == "VVI":
        vviFrame.grid()

def aooSubmit(): 
    pass

def vooSubmit(): 
    pass

def aaiSubmit(): 
    pass
def vviSubmit(): 
    pass

######
#Main#
######
root = Tk()

chooseFrame = Frame(root)
chooseLabel = Label(chooseFrame, text = "Please choose a pacing mode")
modeVar = StringVar()
modeVar.set("None")
aooRadio = Radiobutton(chooseFrame, text = "AOO", variable = modeVar, value = "AOO")
vooRadio = Radiobutton(chooseFrame, text = "VOO", variable = modeVar, value = "VOO")
aaiRadio = Radiobutton(chooseFrame, text = "AAI", variable = modeVar, value = "AAI")
vviRadio = Radiobutton(chooseFrame, text = "VVI", variable = modeVar, value = "VVI")
nextButton = Button(chooseFrame, text = "Next", command = openMode)

chooseFrame.grid(padx = 50, pady = 50)
chooseLabel.grid(row = 1, column = 1, columnspan = 8)
aooRadio.grid(row = 2, column = 1, sticky = W)
vooRadio.grid(row = 3, column = 1, sticky = W)
aaiRadio.grid(row = 4, column = 1, sticky = W)
vviRadio.grid(row = 5, column = 1, sticky = W)
nextButton.grid(row = 6, column = 2, sticky = W)


#####
#AOO#
#####
aooFrame = Frame(root)
aooLabel = Label(aooFrame, text = "AOO", font = ("Arial", 25))
instructionLabel = Label(aooFrame, text = "Please enter the values for the following parameters")
instructionLabel2 = Label(aooFrame, text  = "These values will be checked to ensure that they are valid entries")
lrlLabel = Label(aooFrame, text = "Lower Rate Limit:")
lrlVar = IntVar()
lrlEntry = Entry(aooFrame, textvariable = lrlVar)
urlLabel = Label(aooFrame, text = "Upper Rate Limit:")
urlVar = IntVar()
urlEntry = Entry(aooFrame, textvariable = urlVar)
apwLabel = Label(aooFrame, text = "Atrial Pulse Width:")
apwVar = DoubleVar()
apwEntry = Entry(aooFrame, textvariable = apwVar)
aampLabel = Label(aooFrame, text = "Atrial Amplitude:")
aampVar = DoubleVar()
aampEntry = Entry(aooFrame, textvariable = aampVar)
aoosubmitButton = Button(aooFrame, text = "Confirm changes", command = aooSubmit)

aooFrame.grid(padx = 50, pady = 50)
aooLabel.grid(row = 1, column = 1, columnspan = 2)
instructionLabel.grid(row = 2, column = 1, columnspan = 2)
instructionLabel2.grid(row = 3, column = 1, columnspan = 2)
lrlLabel.grid(row = 4, column = 1, sticky = W)
lrlEntry.grid(row = 4, column = 2, sticky = W)
urlLabel.grid(row = 5, column = 1, sticky = W)
urlEntry.grid(row = 5, column = 2, sticky = W)
apwLabel.grid(row = 6, column = 1, sticky = W)
apwEntry.grid(row = 6, column = 2, sticky = W)
aampLabel.grid(row = 7, column = 1, sticky = W)
aampEntry.grid(row = 7, column = 2, sticky = W)
aoosubmitButton.grid(row = 8, column = 3, sticky = E)
aooFrame.grid_remove()


#####
#VOO#
#####
vooFrame = Frame(root)
vooLabel = Label(vooFrame, text = "VOO", font = ("Arial", 25))
instructionLabel = Label(vooFrame, text = "Please enter the values for the following parameters")
instructionLabel2 = Label(vooFrame, text  = "These values will be checked to ensure that they are valid entries")
lrlLabel = Label(aooFrame, text = "Lower Rate Limit:")
lrlVar = IntVar()
lrlEntry = Entry(vooFrame, textvariable = lrlVar)
urlLabel = Label(vooFrame, text = "Upper Rate Limit:")
urlVar = IntVar()
urlEntry = Entry(vooFrame, textvariable = urlVar)
vpwLabel = Label(vooFrame, text = "Ventrical Pulse Width:")
vpwVar = DoubleVar()
vpwEntry = Entry(vooFrame, textvariable = vpwVar)
vampLabel = Label(vooFrame, text = "Ventrical Amplitude:")
vampVar = DoubleVar()
vampEntry = Entry(vooFrame, textvariable = vampVar)

vooFrame.grid(padx = 50, pady = 50)
vooLabel.grid(row = 1, column = 1, columnspan = 2)
instructionLabel.grid(row = 2, column = 1, columnspan = 2)
instructionLabel2.grid(row = 3, column = 1, columnspan = 2)
lrlLabel.grid(row = 4, column = 1, sticky = W)
lrlEntry.grid(row = 4, column = 2, sticky = W)
urlLabel.grid(row = 5, column = 1, sticky = W)
urlEntry.grid(row = 5, column = 2, sticky = W)
vpwLabel.grid(row = 6, column = 1, sticky = W)
vpwEntry.grid(row = 6, column = 2, sticky = W)
vampLabel.grid(row = 7, column = 1, sticky = W)
vampEntry.grid(row = 7, column = 2, sticky = W)
vooFrame.grid_remove()

#####
#AAI#
#####
aaiFrame = Frame(root)
aaiLabel = Label(aaiFrame, text = "AAI", font = ("Arial", 25))
instructionLabel = Label(aaiFrame, text = "Please enter the values for the following parameters")
instructionLabel2 = Label(aaiFrame, text  = "These values will be checked to ensure that they are valid entries")
lrlLabel = Label(aaiFrame, text = "Lower Rate Limit:")
lrlVar = IntVar()
lrlEntry = Entry(aaiFrame, textvariable = lrlVar)
urlLabel = Label(aaiFrame, text = "Upper Rate Limit:")
urlVar = IntVar()
urlEntry = Entry(aaiFrame, textvariable = urlVar)
apwLabel = Label(aaiFrame, text = "Atrial Pulse Width:")
apwVar = DoubleVar()
apwEntry = Entry(aaiFrame, textvariable = apwVar)
aampLabel = Label(aaiFrame, text = "Atrial Amplitude:")
aampVar = DoubleVar()
aampEntry = Entry(aaiFrame, textvariable = aampVar)
asensLabel = Label(aaiFrame, text = "Atrial Sensitivity:")
asensVar = DoubleVar()
asensEntry = Entry(aaiFrame, textvariable = asensVar)
arpLabel = Label(aaiFrame, text = "ARP:")
arpVar = IntVar()
arpEntry = Entry(aaiFrame, textvariable = arpVar)
pvarpLabel = Label(aaiFrame, text = "PVARP:")
pvarpVar = IntVar()
pvarpEntry = Entry(aaiFrame, textvariable = pvarpVar)
hystLabel = Label(aaiFrame, text = "Hysteresis:")
hystVar = DoubleVar()
hystEntry = Entry(aaiFrame, textvariable = hystVar)
rsLabel = Label(aaiFrame, text = "Rate Smoothing:")
rsVar = DoubleVar()
rsEntry = Entry(aaiFrame, textvariable = rsVar)



aaiFrame.grid(padx = 50, pady = 50)
aaiLabel.grid(row = 1, column = 1)
instructionLabel.grid(row = 2, column = 1, columnspan = 2)
instructionLabel2.grid(row = 3, column = 1, columnspan = 2)
lrlLabel.grid(row = 4, column = 1, sticky = W)
lrlEntry.grid(row = 4, column = 2, sticky = W)
urlLabel.grid(row = 5, column = 1, sticky = W)
urlEntry.grid(row = 5, column = 2, sticky = W)
apwLabel.grid(row = 6, column = 1, sticky = W)
apwEntry.grid(row = 6, column = 2, sticky = W)
aampLabel.grid(row = 7, column = 1, sticky = W)
aampEntry.grid(row = 7, column = 2, sticky = W)
asensLabel.grid(row = 8, column = 1, sticky = W)
asensEntry.grid(row = 8, column = 2, sticky = W)
arpLabel.grid(row = 9, column = 1, sticky = W)
arpEntry.grid(row = 9, column = 2, sticky = W)
pvarpLabel.grid(row = 10, column = 1, sticky = W)
pvarpEntry.grid(row = 10, column = 2, sticky = W)
hystLabel.grid(row = 11, column = 1, sticky = W)
hystEntry.grid(row = 11, column = 2, sticky = W)
rsLabel.grid(row = 12, column = 1, sticky = W)
rsEntry.grid(row = 12, column = 2, sticky = W)
aaiFrame.grid_remove()

#####
#VVI#
#####
vviFrame = Frame(root)
vviLabel = Label(vviFrame, text = "VVI", font = ("Arial", 25))
instructionLabel = Label(vviFrame, text = "Please enter the values for the following parameters")
instructionLabel2 = Label(vviFrame, text  = "These values will be checked to ensure that they are valid entries")
lrlLabel = Label(vviFrame, text = "Lower Rate Limit:")
lrlVar = IntVar()
lrlEntry = Entry(vviFrame, textvariable = lrlVar)
urlLabel = Label(vviFrame, text = "Upper Rate Limit:")
urlVar = IntVar()
urlEntry = Entry(vviFrame, textvariable = urlVar)
vpwLabel = Label(vviFrame, text = "Ventricular Pulse Width:")
vpwVar = DoubleVar()
vpwEntry = Entry(vviFrame, textvariable = apwVar)
vampLabel = Label(vviFrame, text = "Ventricular Amplitude:")
vampVar = DoubleVar()
vampEntry = Entry(vviFrame, textvariable = aampVar)
vsensLabel = Label(vviFrame, text = "Ventricular Sensitivity:")
vsensVar = DoubleVar()
vsensEntry = Entry(vviFrame, textvariable = asensVar)
hystLabel = Label(vviFrame, text = "Hysteresis:")
hystVar = DoubleVar()
hystEntry = Entry(vviFrame, textvariable = hystVar)
rsLabel = Label(vviFrame, text = "Rate Smoothing:") 
rsVar = DoubleVar()
rsEntry = Entry(vviFrame, textvariable = rsVar)


vviFrame.grid(padx = 50, pady = 50)
vviLabel.grid(row = 1, column= 1)
instructionLabel.grid(row = 2, column = 1, columnspan = 2)
instructionLabel2.grid(row = 3, column = 1, columnspan = 2)
lrlLabel.grid(row = 4, column = 1, sticky = W)
lrlEntry.grid(row = 4, column = 2, sticky = W)
urlLabel.grid(row = 5, column = 1, sticky = W)
urlEntry.grid(row = 5, column = 2, sticky = W)
vpwLabel.grid(row = 6, column = 1, sticky = W)
vpwEntry.grid(row = 6, column = 2, sticky = W)
vampLabel.grid(row = 7, column = 1, sticky = W)
vampEntry.grid(row = 7, column = 2, sticky = W)
vsensLabel.grid(row = 8, column = 1, sticky = W)
vsensEntry.grid(row = 8, column = 2, sticky = W)
hystLabel.grid(row = 9, column = 1, sticky = W)
hystEntry.grid(row = 9, column = 2, sticky = W)
rsLabel.grid(row = 10, column = 1, sticky = W)
rsEntry.grid(row = 10, column = 2, sticky = W)
vviFrame.grid_remove()






