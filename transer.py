from PIL import Image
import os

max_color = 253
pathto='static/pics/'


def save_transp(jpgfile='LO022EWIOK60_1_v2.jpg'):
    def is_white():
        if pixdata[x, y][0] > max_color and pixdata[x, y][1] > max_color and pixdata[x, y][2] > max_color:
            return True


    def is_trans():
        if pixdata[x, y][0] == 0 and pixdata[x, y][1] == 0 and pixdata[x, y][2] == 0 and pixdata[x, y][3] == 0:
            return True

    img = Image.open(jpgfile)
    pngfile='static/pics/'+jpgfile[:-3]+'png'
    if os.path.exists(pngfile):
        os.remove(pngfile)
    img = img.convert("RGBA")
    pixdata = img.load()

    # print(pixdata[100,0])
    for y in range(img.size[1]):
        for x in range(img.size[0]):
            # print (y,x, pixdata[x, y][0], pixdata[x, y][1], pixdata[x, y][2]   )
            if is_white():
                pixdata[x, y] = (0, 0, 0, 0)
    img.save(pngfile, "PNG")





