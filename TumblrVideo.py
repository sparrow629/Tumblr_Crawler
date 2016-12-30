#coding:utf-8
import multiprocessing
import re
import urllib.request
import time
import os

def getHtml(url):
	page = urllib.request.urlopen(url)
	html = page.read().decode('utf-8')
	return html

def getPostname(posturl):
	reg = r'http://.*?\/post\/(.*)'
	postname = re.compile(reg)
	postnamelist = re.findall(postname, posturl)
	print(postnamelist)
	if postnamelist:
		return postnamelist[0]
	else:
		postnamelist = ['page1']
		return postnamelist[0]

def getMP4(url):
    html = getHtml(url)
    reg = r'<iframe src=\'(https\://www\.tumblr\.com/video/.*?)\''
    videopagere = re.compile(reg)
    videopageurl = re.findall(videopagere, html)[0]
    print(videopageurl)

    videohtml = getHtml(videopageurl)
    reg_url = r'<source src="(https://www.tumblr.com/video_file/t:.*?)" type="video/mp4">'
    videore = re.compile(reg_url)
    videourl = re.findall(videore, videohtml)[0]
    print(videourl)

    path = 'TumblrMP4download/'
    if not os.path.exists(path):
        os.makedirs(path)

    if videourl:
        Postname = getPostname(url)
        if len(Postname) > 12:
            Name = Postname[:12]
        else:
            Name = Postname

        target = path + '%s.mp4' % Name

        print("Downloading %s " % target)
        urllib.request.urlretrieve(videourl, target)

    else:
        print('There is no Video!')


if __name__ == '__main__':
    select = 'Y'
    while (select == 'Y'):
        URL = input('Input url: ')
        getMP4(URL)
        select = input("Do you want to Continue? [Y/N]")
