from Effects.Effect import Effect
import random

class Noise(Effect):
    def __init__(self):
        self.factor = 10

    def Iteration(self):
        for i in range(self.width):
            for j in range(self.height):
                rand = random.randint(-self.factor, self.factor)
                r, g, b = self.pix[i, j]
                r = max(0, min(255, r + rand))
                g = max(0, min(255, g + rand))
                b = max(0, min(255, b + rand))
                self.draw.point((i, j), (r, g, b))


