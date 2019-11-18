from abc import ABC, abstractmethod

from PIL import ImageDraw


class Effect(ABC):

    def Execute(self, opennedImage):
        self.draw = ImageDraw.Draw(opennedImage)
        self.width = opennedImage.size[0]
        self.height = opennedImage.size[1]
        self.pix = opennedImage.load()
        self.Iteration()
        opennedImage.save("result.jpg", "JPEG")
        del self.draw
        return "result.jpg"

    @abstractmethod
    def Iteration(self):
        pass