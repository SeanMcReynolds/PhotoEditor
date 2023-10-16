from kivy.app import App
from kivy.uix.screenmanager import Screen
from PIL import Image

class PhotoEditorApp(App):
    pass

class Display(Screen):
    def display_images(self):
        return images[index]
    def advance(self):
        global index
        if self.ids.image_load.text == "lake.jpg":
            return index
        elif self.ids.image_load.text == "vancouver.jpg":
            index = 1
        elif self.ids.image_load.text == "cat.jpg":
            index = 2
        else:
            pass

    lake = Image.open("lake.jpg")
    vancouver = Image.open("vancouver.jpg")
    cat = Image.open("cat.jpg")

    def sepia(self, image):
        if self.ids.image_load.text == "lake.jpg":
            image = self.lake
        elif self.ids.image_load.text == "vancouver.jpg":
            image = self.vancouver
        elif self.ids.image_load.text == "cat.jpg":
            image = self.cat
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

# self.ids.image.source = self.display_images()

images = ["lake.jpg","vancouver.jpg","cat.jpg"]
index = 0

PhotoEditorApp().run()