from abc import ABC, abstractmethod

from PIL import ImageDraw


class Effect(ABC):

    def Execute(self, processingImage):
        self.processingImage = processingImage
        self.draw = ImageDraw.Draw(processingImage)
        self.width = processingImage.size[0]
        self.height = processingImage.size[1]
        self.pix = processingImage.load()
        self.Processing()
        processingImage.save("result.png", "PNG")
        del self.draw
        return "result.png"

    @abstractmethod
    def Processing(self):
        pass