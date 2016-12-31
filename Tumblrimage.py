#coding:utf-8
import multiprocessing
import re
import urllib.request
import os

def getHtml(url):
    try:
        page = urllib.request.urlopen(url)
        html = page.read().decode('utf-8')
        return html
    except:
        # traceback.print_exc()
        print('The URL you requested could not be found')
        return 'Html'

def getPostname(posturl):
	reg = r'http://.*?\/post\/(.*)'
	postname = re.compile(reg)
	postnamelist = re.findall(postname, posturl)
	# print(postnamelist)
	if postnamelist:
		return postnamelist[0]
	else:
		postnamelist = ['page1']
		return postnamelist[0]

def getImg(url):
	html = getHtml(url)

	reg = r'<meta property="og:image" content="(http://68.media.tumblr.com/.*?\.(jpg|gif|png))" />'
	imgre = re.compile(reg)
	imglist_none = re.findall(imgre, html)
	imglist = list(set(imglist_none))

	if imglist:
		PrePostname = getPostname(url)
		if len(PrePostname) > 12:
			Postname = PrePostname[:12]
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

			target = path + '%s.%s' % (Name,Postfix)
			i += 1
			print("Downloading %s " % target)
			try:
				urllib.request.urlretrieve(imgurl, target)
			except:
				print('The image is lost.')
		return True

	else:
		print('There is no image!')
		return False

if __name__ == '__main__':

	select = 'Y'
	while (select == 'Y'):
		URL = input('Input url: ')
		getImg(URL)
		select = input("Do you want to Continue? [Y/N]")