from PIL import ImageFilter

from Effects.Effect import Effect

class Blur(Effect):
    def __init__(self, gaussBlurRadius):
        self.gaussBlurRadius = gaussBlurRadius

    def Processing(self):
        blurredImage = self.processingImage.filter(ImageFilter.GaussianBlur(radius=self.gaussBlurRadius))
        self.processingImage.paste(blurredImage)