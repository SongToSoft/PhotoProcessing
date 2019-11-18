from Effects.Effect import Effect
from PIL import ImageDraw
import random

class Noise(Effect):
    def __init__(self):
        self.factor = 10

    def Iteration(self):
        for i in range(self.width):
            for j in range(self.height):
                rand = random.randint(-self.factor, self.factor)
                a = self.pix[i, j][0] + rand
                b = self.pix[i, j][1] + rand
                c = self.pix[i, j][2] + rand
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


