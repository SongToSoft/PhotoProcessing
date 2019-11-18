import tkinter
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfile
from PIL import Image, ImageTk
from Effects.Grayscale import Grayscale
from Effects.Sepia import Sepia
from Effects.Negative import Negative
from Effects.Noise import Noise
from Effects.Brightness import Brightness

class Window:
    def __init__(self):
        print("Create Window")
        self.canvasWidth = 600
        self.canvasHeight = 450
        self.root = Tk()
        self.root.title("Photo Processing")
        self.root.geometry("1200x900")
        self.defaultImageName = ""

        #Create buttons
        buttonFrame = Frame(self.root)
        canvasFrame = Frame(self.root)

        searchFileButton = Button(buttonFrame,
                                  text="Search File",
                                  background="#555",
                                  foreground="#ccc",
                                  font="16",
                                  command=self.OpenFile)
        searchFileButton.pack(side="left")

        grayscaleButton = Button(buttonFrame,
                                 text="Grayscale",
                                 background="#555",
                                 foreground="#ccc",
                                 font="16",
                                 command=self.Grayscale)
        sepiaButton = Button(buttonFrame,
                                 text="Sepia",
                                 background="#555",
                                 foreground="#ccc",
                                 font="16",
                                 command=self.Sepia)

        negativeButton = Button(buttonFrame,
                                 text="Negative",
                                 background="#555",
                                 foreground="#ccc",
                                 font="16",
                                 command=self.Negative)
        noiseButton = Button(buttonFrame,
                                 text="Noise",
                                 background="#555",
                                 foreground="#ccc",
                                 font="16",
                                 command=self.Noise)

        brightnessButton = Button(buttonFrame,
                                 text="Brightness",
                                 background="#555",
                                 foreground="#ccc",
                                 font="16",
                                 command=self.Brightness)

        darkenButton = Button(buttonFrame,
                                 text="Darken",
                                 background="#555",
                                 foreground="#ccc",
                                 font="16",
                                 command=self.Darken)

        saveFileButton = Button(buttonFrame,
                                 text="Save File",
                                 background="#555",
                                 foreground="#ccc",
                                 font="16",
                                 command=self.SaveFile())

        grayscaleButton.pack(side="left")
        sepiaButton.pack(side="left")
        negativeButton.pack(side="left")
        noiseButton.pack(side="left")
        brightnessButton.pack(side="left")
        darkenButton.pack(side="left")
        saveFileButton.pack(side="left")

        # Create start image
        self.defaultCanvas = tkinter.Canvas(canvasFrame, width=self.canvasWidth, height=self.canvasHeight, bg="lightblue")
        self.defaultCanvas.pack(side="left")

        self.processingCanvas = tkinter.Canvas(canvasFrame, width=self.canvasWidth, height=self.canvasHeight, bg="lightblue")
        self.processingCanvas.pack(side="right")

        buttonFrame.pack()
        canvasFrame.pack()
        self.root.mainloop()

    def OpenFile(self):
        self.defaultImageName = askopenfilename()
        if (self.defaultImageName != ""):
            self.opennedImage = Image.open(self.defaultImageName)
            self.defaultImage = ImageTk.PhotoImage(self.opennedImage.resize((self.canvasWidth, self.canvasHeight), Image.ANTIALIAS))
            self.defaultCanvas.create_image(0, 0, image=self.defaultImage, anchor="nw")

    def SaveFile(self):
        if (self.defaultImageName != ""):
            fout = asksaveasfile(mode='w', defaultextension=".jpg")
            text2save = str(self.text.get(0.0, END))
            fout.write(text2save)
            fout.close()

    def SetProcessingImage(self, filename):
        self.processingImage = ImageTk.PhotoImage(Image.open(filename).resize((self.canvasWidth, self.canvasHeight), Image.ANTIALIAS))
        self.processingCanvas.create_image(0, 0, image=self.processingImage, anchor="nw")

    def Grayscale(self):
        if (self.defaultImageName != ""):
            grayscale = Grayscale()
            self.SetProcessingImage(grayscale.Execute(self.opennedImage))

    def Sepia(self):
        if (self.defaultImageName != ""):
            sepia = Sepia()
            self.SetProcessingImage(sepia.Execute(self.opennedImage))

    def Negative(self):
        if (self.defaultImageName != ""):
            negative = Negative()
            self.SetProcessingImage(negative.Execute(self.opennedImage))

    def Noise(self):
        if (self.defaultImageName != ""):
            noise = Noise()
            self.SetProcessingImage(noise.Execute(self.opennedImage))

    def Brightness(self):
        if (self.defaultImageName != ""):
            brightness = Brightness(100)
            self.SetProcessingImage(brightness.Execute(self.opennedImage))

    def Darken(self):
        if (self.defaultImageName != ""):
            brightness = Brightness(-100)
            self.SetProcessingImage(brightness.Execute(self.opennedImage))
