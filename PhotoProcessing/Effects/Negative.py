from Effects.Effect import Effect
from PIL import ImageDraw

class Negative(Effect):

    def Iteration(self):
        for i in range(self.width):
            for j in range(self.height):
                a = self.pix[i, j][0]
                b = self.pix[i, j][1]
                c = self.pix[i, j][2]
                self.draw.point((i, j), (255 - a, 255 - b, 255 - c))


