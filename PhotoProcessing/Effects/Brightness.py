from Effects.Effect import Effect

class Brightness(Effect):
    def __init__(self, factor):
        self.factor = factor

    def Iteration(self):
        for i in range(self.width):
            for j in range(self.height):
                r, g, b = self.pix[i, j]
                r = max(0, min(255, r + self.factor))
                g = max(0, min(255, g + self.factor))
                b = max(0, min(255, b + self.factor))
                self.pix[i, j] = (r, g, b)



