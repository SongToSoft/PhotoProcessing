from Effects.Effect import Effect

class Sepia(Effect):
    def __init__(self):
        self.depth = 10

    def Processing(self):
        for i in range(self.width):
            for j in range(self.height):
                r, g, b = self.pix[i, j]
                s = (r + g + b) // 3
                r = max(0, min(255, s + self.depth * 2))
                g = max(0, min(255, s + self.depth))
                b = max(0, min(255, s))
                self.draw.point((i, j), (r, g, b))


