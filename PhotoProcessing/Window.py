import tkinter
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import Image, ImageTk

from Effects.Grayscale import Grayscale
from Effects.Sepia import Sepia
from Effects.Negative import Negative
from Effects.Noise import Noise
from Effects.Blur import Blur
from Effects.Brightness import Brightness

class Window:
    def __init__(self):
        print("Create Window")
        self.imageWidth = 600
        self.imageHeight = 450
        self.root = Tk()
        self.root.title("Photo Processing")
        self.root.geometry("1200x900")
        self.openImageName = ""
        self.saveImageName = ""

        buttonFrame = Frame(self.root)
        canvasFrame = Frame(self.root)

        searchFileButton = self.CreateButton(buttonFrame, "Search File", self.OpenFile)
        grayscaleButton = self.CreateButton(buttonFrame, "Grayscale", self.Grayscale)
        sepiaButton = self.CreateButton(buttonFrame, "Sepia", self.Sepia)
        negativeButton = self.CreateButton(buttonFrame, "Negative", self.Negative)
        noiseButton = self.CreateButton(buttonFrame, "Noise", self.Noise)
        blurButton = self.CreateButton(buttonFrame, "Blur", self.Blur)
        brightnessButton = self.CreateButton(buttonFrame, "Brightness", self.Brightness)
        darkenButton = self.CreateButton(buttonFrame, "Darken", self.Darken)
        saveFileButton = self.CreateButton(buttonFrame, "Save File", self.SaveFile)
        
        searchFileButton.pack(side="left")
        grayscaleButton.pack(side="left")
        sepiaButton.pack(side="left")
        negativeButton.pack(side="left")
        noiseButton.pack(side="left")
        blurButton.pack(side="left")
        brightnessButton.pack(side="left")
        darkenButton.pack(side="left")
        saveFileButton.pack(side="left")

        self.defaultCanvas = tkinter.Canvas(canvasFrame, width=self.imageWidth, height=self.imageHeight, bg="lightblue")
        self.defaultCanvas.pack(side="left")

        self.processingCanvas = tkinter.Canvas(canvasFrame, width=self.imageWidth, height=self.imageHeight, bg="lightblue")
        self.processingCanvas.pack(side="right")

        buttonFrame.pack()
        canvasFrame.pack()
        self.root.mainloop()

    def CreateButton(self, frame, text, command):
        return Button(frame,
            text=text,
            background="#555",
            foreground="#ccc",
            font="16",
            command=command)

    def OpenFile(self):
        self.openImageName = askopenfilename()
        if (self.openImageName != ""):
            self.opennedImage = Image.open(self.openImageName)
            self.defaultImage = ImageTk.PhotoImage(self.opennedImage.resize((self.imageWidth, self.imageHeight), Image.LANCZOS))
            self.defaultCanvas.create_image(0, 0, image=self.defaultImage, anchor="nw")

    def SaveFile(self):
        if self.openImageName != "":
            fout = asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All files", "*.*")])
            if fout:
                self.opennedImage.save(fout)

    def SetProcessingImage(self, filename):
        self.processingImage = ImageTk.PhotoImage(Image.open(filename).resize((self.imageWidth, self.imageHeight), Image.LANCZOS))
        self.processingCanvas.create_image(0, 0, image=self.processingImage, anchor="nw")

    def ApplyEffect(self, effect, *args):
        if self.openImageName != "":
            effectInstance = effect(*args)
            self.SetProcessingImage(effectInstance.Execute(self.opennedImage))

    def Grayscale(self):
        self.ApplyEffect(Grayscale)

    def Sepia(self):
        self.ApplyEffect(Sepia)

    def Negative(self):
        self.ApplyEffect(Negative)

    def Noise(self):
        self.ApplyEffect(Noise)
    
    def Blur(self):
        self.ApplyEffect(Blur, 5)

    def Brightness(self):
        self.ApplyEffect(Brightness, 100)

    def Darken(self):
        self.ApplyEffect(Brightness, -100)
