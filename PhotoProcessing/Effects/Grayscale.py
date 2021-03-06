from threading import Thread
from Effects.Effect import Effect
from PIL import ImageDraw

class Grayscale(Effect):

    def Iteration(self):
        for i in range(self.width):
            for j in range(self.height):
                a = self.pix[i, j][0]
                b = self.pix[i, j][1]
                c = self.pix[i, j][2]
                S = (a + b + c) // 3
                self.draw.point((i, j), (S, S, S))