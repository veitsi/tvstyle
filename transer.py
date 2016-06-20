from PIL import Image
import os
from urllib.request import urlopen

max_color = 253


def save_transp(jpgfile, pngfile):
    jpgfile='http://pn.lmcdn.ru/product/'+jpgfile[0]+'/'+jpgfile[1]+"/"+jpgfile
    print('is there? '+jpgfile)
    def is_white():
        if pixdata[x, y][0] > max_color and pixdata[x, y][1] > max_color and pixdata[x, y][2] > max_color:
            return True

    def is_trans():
        if pixdata[x, y][0] == 0 and pixdata[x, y][1] == 0 and pixdata[x, y][2] == 0 and pixdata[x, y][3] == 0:
            return True

    tmp=open('tmp.jpg','wb')
    tmp.write(urlopen(jpgfile).read())
    tmp.close()
    img = Image.open('tmp.jpg')
    img = img.convert("RGBA")
    pixdata = img.load()

    # print(pixdata[100,0])
    for y in range(img.size[1]):
        for x in range(img.size[0]):
            # print (y,x, pixdata[x, y][0], pixdata[x, y][1], pixdata[x, y][2]   )
            if is_white():
                pixdata[x, y] = (0, 0, 0, 0)
    img.save(pngfile, "PNG")
