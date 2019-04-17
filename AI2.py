import random
from tkinter import *
from PIL import Image , ImageDraw
import numpy as np

#window with changing of image
class Show():
    def __init__(self):
        self.canvas = Canvas(root, width = 512, height = 512)
        self.img = PhotoImage(file="parent.png")
        self.imgArea = self.canvas.create_image(0, 0, anchor = NW, image = self.img)
        self.canvas.pack()

    def changeImg(self):
        self.img = PhotoImage(file="parent.png")
        self.canvas.itemconfig(self.imgArea, image = self.img)

#polygon class
class Polygon(object):
    def __init__(self, x11, x22, x33, x44, y11, y22, y33, y44, r, g, b, a):
        self.x1 = x11
        self.x2 = x22
        self.x3 = x33
        self.x4 = x44
        self.y1 = y11
        self.y2 = y22
        self.y3 = y33
        self.y4 = y44
        self.r = r
        self.g = g
        self.b = b
        self.a = a


#fitness function
def compare(img11, img22):
    a1 = np.array(img11)[:, :, :3].astype("int64")
    a2 = np.array(img22)[:, :, :3].astype("int64")
    b1 = a1 - a2
    b2 = b1 * b1
    fit = b2.sum()
    '''  
    fit = 0
    for i in range(1, 512):
        for j in range(1, 512):
            r, g, b = img11.getpixel((i, j))
            r1, g1, b1 = img22.getpixel((i, j))
            fit += (r - r1) * (r - r1) + (g - g1) * (g - g1) + (b - b1) * (b - b1)
    '''
    return fit


#mutations
def polygon_change(n, poly):

    if n == 1:
        return Polygon(poly.x1, poly.x2, poly.x3, poly.x4, poly.y1, poly.y2, poly.y3, poly.y4, random.randint(0, 255), poly.g, poly.b, poly.a)

    if n == 2:
        return Polygon(poly.x1, poly.x2, poly.x3, poly.x4, poly.y1, poly.y2, poly.y3, poly.y4, poly.r, random.randint(0, 255), poly.b, poly.a)

    if n == 3:
        return Polygon(poly.x1, poly.x2, poly.x3, poly.x4, poly.y1, poly.y2, poly.y3, poly.y4, poly.r, poly.g, random.randint(0, 255), poly.a)

    if n == 4:
        return Polygon(poly.x1, poly.x2, poly.x3, poly.x4, poly.y1, poly.y2, poly.y3, poly.y4, poly.r, poly.g, poly.b, random.randint(1, 99))

    if n == 5:
        return Polygon(random.randint(1, 512), poly.x2, poly.x3, poly.x4, poly.y1, poly.y2, poly.y3, poly.y4, poly.r, poly.g, poly.b, random.randint(1, 99))

    if n == 6:
        return Polygon(poly.x1, random.randint(1, 512), poly.x3, poly.x4, poly.y1, poly.y2, poly.y3, poly.y4, poly.r, poly.g, poly.b, random.randint(1, 99))

    if n == 7:
        return Polygon(poly.x1, poly.x2, random.randint(1, 512), poly.x4, poly.y1, poly.y2, poly.y3, poly.y4, poly.r, poly.g, poly.b, random.randint(1, 99))

    if n == 8:
        return Polygon(poly.x1, poly.x2, poly.x3, random.randint(1, 512), poly.y1, poly.y2, poly.y3, poly.y4, poly.r, poly.g, poly.b, random.randint(1, 99))

    if n == 9:
        return Polygon(poly.x1, poly.x2, poly.x3, poly.x4, random.randint(1, 512), poly.y2, poly.y3, poly.y4, poly.r, poly.g, poly.b, random.randint(1, 99))

    if n == 10:
        return Polygon(poly.x1, poly.x2, poly.x3, poly.x4, poly.y1, random.randint(1, 512), poly.y3, poly.y4, poly.r, poly.g, poly.b, random.randint(1, 99))

    if n == 11:
        return Polygon(poly.x1, poly.x2, poly.x3, poly.x4, poly.y1, poly.y2, random.randint(1, 512), poly.y4, poly.r, poly.g, poly.b, random.randint(1, 99))

    if n == 12:
        return Polygon(poly.x1, poly.x2, poly.x3, poly.x4, poly.y1, poly.y2, poly.y3, random.randint(1, 512), poly.r, poly.g, poly.b, random.randint(1, 99))


#creating random parent with 70 black random polygons
global polygons
polygons = [Polygon(10, 20, 10, 20, 10, 20, 10, 20, 255, 255, 255, 70) for x in range(70)]
img = Image.new('RGBA', (512, 512), (255, 255, 255))


for x in range(70):
    x1 = random.randint(1, 512)
    x2 = random.randint(1, 512)
    x3 = random.randint(1, 512)
    x4 = random.randint(1, 512)
    y1 = random.randint(1, 512)
    y2 = random.randint(1, 512)
    y3 = random.randint(1, 512)
    y4 = random.randint(1, 512)
    polygons[x] = Polygon(x1, x2, x3, x4, y1, y2, y3, y4, 0, 0, 0, 70)
    img2 = Image.new('RGBA', (512, 512))
    img_draw = ImageDraw.Draw(img2)
    img_draw.polygon([x1, y1, x2, y2, x3, y3, x4, y4], fill = (0, 0, 0, 70))
    img.paste(img2.convert('RGB'), (0, 0), img2)

img.save('parent.png')


p = Image.open("parent.png").convert("RGB")
#write here your 512х512 image name
a = Image.open("Lenna.png").convert("RGB")
fitness = compare(a, p)

mutations = 0
q = 0
#reqursive function of mutations and selections
e = 10000
#change e if you need better image, but it if you increase e -> program needs more time for computations
def getans():
    global polygons
    global q
    global fitness
    global mutations
    #crossover -> copy parent
    gen = polygons.copy()

    newimg = Image.new('RGBA', (512, 512), (255, 255, 255))

    #mutation
    m = random.randint(0, 69)
    gen[m] = polygon_change(random.randint(1, 12), gen[m])

    for w in range(0, 69):
        img22 = Image.new('RGBA', (512, 512))
        img_draw2 = ImageDraw.Draw(img22)
        img_draw2.polygon([gen[w].x1, gen[w].y1, gen[w].x2, gen[w].y2, gen[w].x3, gen[w].y3, gen[w].x4, gen[w].y4], fill=(gen[w].r, gen[w].g, gen[w].b, gen[w].a))
        newimg.paste(img22.convert('RGB'), (0, 0), img22)

    newimg.save('child.png')
    newfit = compare(a, newimg.convert("RGB"))

    #selection
    if newfit < fitness:
        fitness = newfit
        newimg.save('parent.png')
        polygons = gen.copy()
        mutations += 1
    q += 1
    #q -> number of mutations, fitness -> current fitness, mutations -> number of successful mutations
    print(q, " ", fitness, " ", mutations)
    app.changeImg()

    if q == e :
        return
    root.after(1, getans)


#window geometry
root = Tk()
#do not resize window while using application in mac os, because it can cause black window of app(tkinter app problem)
#for Windows it is Ok
root.geometry("1444x800")
app = Show()
root.after(1, getans)
root.mainloop()