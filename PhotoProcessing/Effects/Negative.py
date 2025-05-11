from Effects.Effect import Effect

class Negative(Effect):
    def Processing(self):
        for i in range(self.width):
            for j in range(self.height):
                r, g, b = self.pix[i, j]
                self.draw.point((i, j), (255 - r, 255 - g, 255 - b))
