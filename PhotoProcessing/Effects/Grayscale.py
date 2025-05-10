from Effects.Effect import Effect

class Grayscale(Effect):

    def Iteration(self):
        for i in range(self.width):
            for j in range(self.height):
                r, g, b = self.pix[i, j]
                s = (r + g + b) // 3
                self.draw.point((i, j), (s, s, s))