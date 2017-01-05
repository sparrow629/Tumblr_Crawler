# -*- coding: utf-8 -*-
"""
  Author:  Sparrow
  Purpose: downloading one entire blog from Tumblr once.
  Created: 2017-1.1
"""

import re
import urllib.request
import time

def getHtml(url):
    try:
        page = urllib.request.urlopen(url)
        html = page.read().decode('utf-8')
        return html
    except:
        # traceback.print_exc()
        print('The URL you requested could not be found')
        return 'Html'

def ArchivePostfix(url):
    URL = url + 'archive'
    return URL

def findNextpage(ArchiveURL, url, PageList, PageNum):
    html = getHtml(url)
    reg = r'<a id="next_page_link" href="/archive(\?before_time=.*?)"'
    regc = re.compile(reg)
    nextpage = re.findall(regc, html)

    if nextpage:
        nextpageUrl = ArchiveURL + nextpage[0]
        PageNum += 1
        PageList[PageNum] = nextpageUrl
        print('Page %s' % PageNum,nextpageUrl)
        findNextpage(ArchiveURL, nextpageUrl, PageList, PageNum)

def findAllPage(url):
    archiveURL = ArchivePostfix(url)
    PageList = {1:archiveURL}
    PageNum = 1
    findNextpage(archiveURL, archiveURL, PageList, PageNum)
    print(len(PageList),PageList)
    return PageList

def reCodeURL(url):
    reg = '(.*?/post/.*)/.*'
    urlre = re.compile(reg)
    try:
        newnurl = re.findall(urlre, url)[0]
        print(url,'=>',newnurl)
        return newnurl
    except:
        print(url,'=>')
        return url

def FindCurrentPagePostUrl(url):
    html = getHtml(url)
    reg = r'<a target="_blank" class="hover" title="" href="(.*?)"'
    PostUrlre = re.compile(reg)
    PostUrlString = re.findall(PostUrlre, html)

    if PostUrlString:
        PostUrl = []
        for url in PostUrlString:
            Url = reCodeURL(url)
            PostUrl.append(Url)
        # print(PostUrl)
        return PostUrl
    else:
        return False

def findalltheposturl(url):
    PageList = findAllPage(url)

    if PageList:
        Pagenum = len(PageList)
        PostUrlLists = {}
        for page in range(1,Pagenum+1):
            Posturl = FindCurrentPagePostUrl(PageList[page])
            if Posturl:
                PostUrlLists[page] = Posturl
                print(page,PostUrlLists[page],sep=' ')
            else:
                print("There is no post in page %s!" % page)

        print(PostUrlLists,'mark')
        return PostUrlLists

    else:
        print('There is no page!')
        return False

if __name__ == '__main__':
    select = 'N'
    while not(select == 'Y'):
        URL = input('Input url: ')

        start = time.time()
        findalltheposturl(URL)
        # reCodeURL(URL)
        end = time.time()
        print(start, end, '=> Cost %ss' % (end - start))

        select = input("Do you want to Quit? [Y/N]")