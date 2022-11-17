import tkinter
from tkinter import *
from tkinter.scrolledtext import ScrolledText
image = 1

def convertToKilometers():
    try:
        numMiles = float(userEntry.get())
        numKilometers = 1.6 * numMiles
        numMiles = "{:.2f}".format(numMiles)
        msg = str(userEntry.get()) + " Miles is ~" + str(numKilometers) + " Kilometers"
        outputLabel.configure(text=msg)
        status.configure(text="ok")
    except ValueError:
        incorrect = str("Input a valid number")
        outputLabel.configure(text=incorrect)
    else:
        pass
    
def convertToMiles():
    try:
        numKilometers = float(userEntry.get())
        numMiles = numKilometers / 1.6
        numKilometers = "{:.2f}".format(numMiles)
        msg = str(userEntry.get()) + " Kilometers is ~" + str(numMiles) + " Miles"
        outputLabel.configure(text=msg)
        status.configure(text="ok")
    except ValueError:
        incorrect = str("Input a valid number")
        outputLabel.configure(text=incorrect)
    else:
        pass
def convertToPounds():
    try:
        numKG = float(userEntry.get())
        numPounds = numKG * 2.2
        numPounds = "{:.2f}".format(numPounds)
        msg = str(userEntry.get()) + "KG is ~" + str(numPounds) + " Pounds"
        outputLabel.configure(text=msg)
        status.configure(text="ok")
    except ValueError:
        incorrect = str("Input a valid number")
        outputLabel.configure(text=incorrect)
    else:
        pass
def convertToKilograms():
    try:
        numPounds = float(userEntry.get())
        numKG = numPounds / 2.2
        numKG = "{:.2f}".format(numKG)
        msg = str(userEntry.get()) + " Pounds is ~" + str(numKG) + " KG"
        outputLabel.configure(text=msg)
        status.configure(text="ok")
    except ValueError:
        incorrect = str("Input a valid number")
        outputLabel.configure(text=incorrect)
    else:
        pass

  

def changePic():
    global image
    if image % 2 == 0:
        photoLabel.configure(image=photo1)
        photoLabel.image = photo1
    else:
        photoLabel.configure(image=photo2)
     
    image = image + 1
    
def quitWindow():
    root.destroy()
    sys.exit(0)

def metric():
    met = Toplevel()
    met.title("Metric")
    met.geometry("500x800")
    metricHead = tkinter.Label(met, text="Metric", fg= "black", font=("Arial", 20))
    metricHead.grid(row=0, sticky=NW, padx=100)
    metricBody = Label(met, width=40, wraplength=275, text="this is the system of measurement that uses grams, litres and meters as its form of measurement. The metric system of measurement is used all around the world with an exception of a few countries such as America.", anchor ='w')
    metricBody.grid(row=1, column=0,sticky=N)
    metric = PhotoImage(file='metric.png')
    metricimage = Label(met, image=metric)
    metricimage.grid(row=2, column=1)
    
    
    met.mainloop()

    
root = tkinter.Tk()

root.title("Converter")

root.geometry("500x600")
sb = Scrollbar(root)  


title = tkinter.Label(root, text="Converter", font=('Helvetica', 14))
title.grid(row=0, column=0, columnspan=2)

ConverterLabel = tkinter.Label(root, text="Please enter value to be converted:", font=('Helvetica', 11))
root.grid_rowconfigure(1, minsize=50)
ConverterLabel.grid(row=1)



userEntry = Entry(root, bd=2)
userEntry.grid(row=1, column=1)




convertButton1 = tkinter.Button(text="Kilometers --> miles", command=convertToMiles)
convertButton1.grid(row=2, column=0)
    
    
convertButton2 = tkinter.Button(text="Miles --> Kilometers", command=convertToKilometers)
convertButton2.grid(row=2, column=1)
    
    
convertButton3 = tkinter.Button(text="Pounds --> KG", command=convertToKilograms)
convertButton3.grid(row=3, column=0)
    
    
convertButton4 = tkinter.Button(text="KG --> Pounds", command=convertToPounds)
convertButton4.grid(row=3, column=1)

    
outputLabel = tkinter.Label(root, text="Select conversion button above", font=('Arial', 14))
outputLabel.grid(row=4, column=0, columnspan=2)
root.grid_rowconfigure(3, minsize=50)


photo1 = PhotoImage(file="milesandkilo.png")

photo2 = PhotoImage(file="pounds.png")

photoLabel = Label(root, image=photo1)
photoLabel.grid(row=5, column=0, columnspan=2)

pressbutton = Button(root, text='Press to change image', bg='black', fg='white', command=changePic) 
pressbutton.grid(row=6, column=0, columnspan=2)

metricButton = Button(root, text= "Metric Info", command = metric).grid(row=7,column=0, columnspan = 2)

status = Label(root, text="Waiting for user input.", bd=5, relief=SUNKEN, anchor=W)
status.grid(row=9, column=0, sticky=N, columnspan=2, pady=4)
root.grid_rowconfigure(6, minsize=50)

Button(root, text='Quit', command=quitWindow).grid(row=10, column=0, rowspan=2, columnspan=2, sticky=N, pady=4)









root.mainloop()
