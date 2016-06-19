from urllib.request import urlopen


def img_exists(img='http://ya.ru/somewwwwwwwwwwww.jpg'):
    try:
        f = urlopen(img)
        return True
    except:
        return False

if __name__ == '__main__':
    print(img_exists('http://ya.ru'))
    print(img_exists('http://pn.lmcdn.ru/product/M/I/MI052EWISL34_1_v2.jpg'))
    print(img_exists())
