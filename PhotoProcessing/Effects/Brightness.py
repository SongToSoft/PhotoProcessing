from concurrent.futures import thread
from threading import Thread

from Effects.Effect import Effect

class Brightness(Effect):
    def __init__(self, factor):
        self.factor = factor

    def Iteration(self):
        for i in range(self.width):
            for j in range(self.height):
                a = self.pix[i, j][0] + self.factor
                b = self.pix[i, j][1] + self.factor
                c = self.pix[i, j][2] + self.factor
                if (a < 0):
                    a = 0
                if (b < 0):
                    b = 0
                if (c < 0):
                    c = 0
                if (a > 255):
                    a = 255
                if (b > 255):
                    b = 255
                if (c > 255):
                    c = 255
                self.draw.point((i, j), (a, b, c))



