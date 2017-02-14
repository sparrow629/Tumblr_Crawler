import re
import os
from PersonalThemeSearch import BlogStyleDetection
import Tumblrimage
from urllib.parse import quote
import urllib.request
import urllib
import traceback

def getHtml(url):
	url = quote(url, safe='/:?=')
	try:
		page = urllib.request.urlopen(url)
		html = page.read().decode('utf-8')
		return html
	except:
		# traceback.print_exc()
		print('The URL you requested could not be found in Module image')
		return 'Html'

def ImgDownloadException(url):
    html = getHtml(url)
    reg = '<img src="(.*.(jpg))"'
    imgre = re.compile(reg)
    imglist_none = re.findall(imgre, html)
    imglist = list(set(imglist_none))

    if imglist and not BlogStyleDetection(url):
        PrePostname = Tumblrimage.getPostname(url)
        txt = re.search('/', PrePostname)
        if txt:
            Postnames = PrePostname.split('/')
            Postname = Postnames[0]
        # print(PrePostname,Postnames)
        else:
            Postname = PrePostname
        print(len(imglist))
        print(imglist)
        i = 0
        path = 'Tumblrimgdownload/'
        if not os.path.exists(path):
            os.makedirs(path)
        for imgurls in imglist:
            Name = Postname + '_' + str(i)
            imgurl = imgurls[0]
            Postfix = imgurls[1]

            target = path + '%s.%s' % (Name, Postfix)
            i += 1

            loop(imgurl,target)
        return True

    else:
        print('There is no image!')
        return False

def loop(imgurl,target):
    try:
        print("Downloading %s " % target)
        urllib.request.urlretrieve(imgurl, target)
    except urllib.error.URLError as ex:         #处理超时、url不正确异常
        print("Connecting error:%s"% ex)
        # loop(imgurl, target)
        print('The image is lost.')

if __name__ == '__main__':

    select = 'Y'
    while (select == 'Y'):
        URL = input('Input url: ')
        ImgDownloadException(URL)
        select = input("Do you want to Continue? [Y/N]")