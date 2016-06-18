#!/usr/bin/env python3
import sys
import urllib
import os
from lxml import etree

def downloader:
# f=open('/home/ubuntu/workspace/pics/product/A/A/AA001EWIVK05_1_v2.jpg','w')
    flinks=open('pic-links.txt','r')
    for line in flinks:
        print(line)
        lamodaname='http://pn.lmcdn.ru'+line[:-1]
        localname='/home/ubuntu/workspace/pics/'+line[13:-1]
        fpic=open(localname,'w')
        fpic.write(urllib.urlopen(lamodaname).read())
        fpic.close()

def link_saver:
    tree = etree.parse('static/1405344794565foi.xml')
    nodes = tree.xpath('/yml_catalog/shop/offers/offer')
    i=0
    f=open('pic-links.txt','w')
    for node in nodes:
        pass
        for subnode in node:
            # if i>20:
            #     f.close()
            #     sys.exit()
            # i+=1
            if subnode.tag == 'picture':
                print(subnode.text)
                fullname=subnode.text[18:]
                f.write(fullname+"\n")


