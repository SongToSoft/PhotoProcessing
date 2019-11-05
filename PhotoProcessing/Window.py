import tkinter
from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
from Effects.Grayscale import Grayscale


class Window:
    def __init__(self):
        print("Create Window")
        self.canvasWidth = 600
        self.canvasHeight = 450
        self.root = Tk()
        self.root.title("Photo Processing")
        self.root.geometry("1200x900")
        self.defaultImageName = ""

        buttonFrame = Frame(self.root)
        canvasFrame = Frame(self.root)

        # Create button Search
        searchFileButton = Button(buttonFrame,
                                  text="Search File",  # текст кнопки
                                  background="#555",  # фоновый цвет кнопки
                                  foreground="#ccc",  # цвет текста
                                  #padx="20",  # отступ от границ до содержимого по горизонтали
                                  #pady="8",  # отступ от границ до содержимого по вертикали
                                  font="16",  # высота шрифта
                                  command=self.OpenFile) # метод вызываемый при нажатии на кнопку
        #buttonSearchFile.place(x=10, y=10)
        searchFileButton.pack(side="left")

        # Create grayscale button
        grayscaleButton = Button(buttonFrame,
                                 text="Grayscale",  # текст кнопки
                                 background="#555",  # фоновый цвет кнопки
                                 foreground="#ccc",  # цвет текста
                                 #padx="20",  # отступ от границ до содержимого по горизонтали
                                 #pady="8",  # отступ от границ до содержимого по вертикали
                                 font="16",  # высота шрифта
                                 command=self.Grayscale) # метод вызываемый при нажатии на кнопку
        grayscaleButton.pack(side="left")

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

    def SetProcessingImage(self, filename):
        self.processingImage = ImageTk.PhotoImage(Image.open(filename).resize((self.canvasWidth, self.canvasHeight), Image.ANTIALIAS))
        self.processingCanvas.create_image(0, 0, image=self.processingImage, anchor="nw")

    def Grayscale(self):
        if (self.defaultImageName != ""):
            grayscale = Grayscale()
            grayscale.Execute(self.opennedImage)
            self.SetProcessingImage(grayscale.Execute(self.opennedImage))
            print("Main Grayscale")