# -*- coding: utf-8 -*-
"""
  Author:  Sparrow
  Purpose: downloading one entire blog from Tumblr once.
  Created: 2017-1.1
"""
import re
import urllib.request
import Tumblrimage
import TumblrVideo
import traceback
from urllib.parse import quote


def getHtml(url):
    url = quote(url, safe='/:?=')
    try:
        page = urllib.request.urlopen(url)
        html = page.read().decode('utf-8')
        return html
    except:
        # traceback.print_exc()
        print('The URL you requested could not be found In Module PostDownload')
        return 'Html'

def vedio_image_judge(url):
    html = getHtml(url)
    reg = r'<meta property="og:type" content="tumblr-feed:(.*?)" />'
    typere = re.compile(reg)
    type =re.findall(typere, html)
    if type:
        print('This is %s' % type[0])
        return type[0]
    else:
        return False

def PostDownload(url):
    Type =vedio_image_judge(url)

    if Type == 'video':
        TumblrVideo.getMP4(url)
    elif Type == 'photoset' or 'photo':
        Tumblrimage.getImg(url)
    else:
        print('There is nothing!')

if __name__ == '__main__':
    select = 'N'
    while not(select == 'Y'):
        URL = input('Input url: ')
        # vedio_image_judge(URL)
        PostDownload(URL)
        select = input("Do you want to Quit? [Y/N]")