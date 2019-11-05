from Effects.Effect import Effect
from PIL import Image, ImageDraw

class Grayscale(Effect):
    def Execute(self, opennedImage):
        #image = Image.open(fileName)  # Открываем изображение.
        draw = ImageDraw.Draw(opennedImage)  # Создаем инструмент для рисования.
        width = opennedImage.size[0]  # Определяем ширину.
        height = opennedImage.size[1]  # Определяем высоту.
        pix = opennedImage.load()  # Выгружаем значения пикселей.
        for i in range(width):
            for j in range(height):
                a = pix[i, j][0]
                b = pix[i, j][1]
                c = pix[i, j][2]
                S = (a + b + c) // 3
                draw.point((i, j), (S, S, S))
        opennedImage.save("result.jpg", "JPEG")
        del draw
        print("Grayscale")
        return "result.jpg"


