from kivy.app import App
from kivy.uix.screenmanager import Screen
from PIL import Image

class PhotoEditorApp(App):
    pass

class Display(Screen):
    def load(self):
        self.ids.image.source = self.ids.image_load.text

    def sepia(self):
        image = Image.open(self.ids.image.source)
        pixels = image.load()
        for y in range(image.size[1]):
            for x in range(image.size[0]):
                red = pixels[x, y][0]
                blue = pixels[x, y][1]
                green = pixels[x, y][2]
                newR = int(red * .393 + green * 0.769 + blue * 0.189)
                newG = int(red * .349 + green * 0.686 + blue * 0.168)
                newB = int(red * .272 + green * 0.534 + blue * 0.131)
                pixels[x, y] = (newR, newG, newB)
        image.save("sepia.png")
        self.ids.image.source = "sepia.png"

    def inverted(self):
        image = Image.open(self.ids.image.source)
        pixels = image.load()
        for y in range(image.size[1]):
            for x in range(image.size[0]):
                red = 255 - pixels[x, y][0]
                green = 255 - pixels[x, y][1]
                blue = 255 - pixels[x, y][2]
                pixels[x, y] = (red, green, blue)
        image.save("inverted.png")
        self.ids.image.source = "inverted.png"

    def brighten_image(self):
        image = Image.open(self.ids.image.source)
        pixels = image.load()
        for y in range(image.size[1]):
            for x in range(image.size[0]):
                pixels[x, y] = (
                pixels[x, y][0] + 100, pixels[x, y][1] + 100, pixels[x, y][2] + 100)
        image.save("brighten.png")
        self.ids.image.source = "brighten.png"

    def red(self):
        image = Image.open(self.ids.image.source)
        pixels = image.load()
        for y in range(image.size[1]):
            for x in range(image.size[0]):
                red = 255
                green = pixels[x, y][1]
                blue = pixels[x, y][2]
                pixels[x, y] = (red, green, blue)
        image.save("red.png")
        self.ids.image.source = "red.png"

    def vertical_lines(self):
        image = Image.open(self.ids.image.source)
        pixels = image.load()
        for y in range(image.size[1]):
            for x in range(image.size[0]):
                if x % 30 < 10:
                    pixels[x, y] = (200, 100, 200)
        image.save("vertical_lines.png")
        self.ids.image.source = "vertical_lines.png"

#self.ids.image.source = self.display_images()



PhotoEditorApp().run()