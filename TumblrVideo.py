#coding:utf-8
import multiprocessing
import re
import urllib.request
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
    videopageurl = re.findall(videopagere, html)
    if videopageurl:
        print(videopageurl[0])

        videohtml = getHtml(videopageurl[0])
        reg_url = r'<source src="(https://www.tumblr.com/video_file/t:.*?)" type="video/mp4">'
        videore = re.compile(reg_url)
        videourl = re.findall(videore, videohtml)[0]
        print(videourl)

        Postname = getPostname(url)
        if len(Postname) > 12:
            Name = Postname[:12]
        else:
            Name = Postname
        path = 'TumblrMP4download/'
        if not os.path.exists(path):
            os.makedirs(path)
        target = path + '%s.mp4' % Name

        print("Downloading %s " % target)
        urllib.request.urlretrieve(videourl, target)
        return True

    else:
        print('There is no Video!')
        return False


if __name__ == '__main__':
    select = 'Y'
    while (select == 'Y'):
        URL = input('Input url: ')
        getMP4(URL)
        select = input("Do you want to Continue? [Y/N]")
