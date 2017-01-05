# -*- coding: utf-8 -*-
"""
  Author:  Sparrow
  Purpose: downloading one entire blog from Tumblr once.
  Created: 2017-1.1
"""

import re
import urllib.request
import threading
import TumblrPostDownload
import TumblrVideo
import Tumblrimage
import time
import traceback
import PersonalThemeSearch
import ArchiveSearch


def getHtml(url):
    try:
        page = urllib.request.urlopen(url)
        html = page.read().decode('utf-8')
        return html
    except:
        # traceback.print_exc()
        print('The URL you requested could not be found')
        return 'Html'

def reCodeURL(url):
    reg = '(.*?/post/.*?)/.*'
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
    reg = r'<a href="(.*?)" title=".*?" class="meta-item post-date">'
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

def FindPage(Homeurl):
    html = getHtml(Homeurl)
    PageList = {1:Homeurl}
    reg = r'<a href=".*?" class="next" data-current-page=".*?" data-total-pages="(.*?)">'
    total_pagere = re.compile(reg)
    total_page = re.findall(total_pagere,html)

    if total_page:
        PageNum = int(total_page[0])
        print('There is %s pages.' % PageNum)
        for i in range(2,PageNum+1):
            PageList[i] = Homeurl + 'page/%s' % i
            # print(i,PageList[i])
            i += 1
        print(PageList)
        return PageList
    else:
        print('There is only one page.')
        return PageList

def FindAllthePostUrl(url):
    PageList = FindPage(url)

    if PageList:
        Pagenum = len(PageList)
        PostUrlLists = {}
        for page in range(1,Pagenum+1):
            Posturl = FindCurrentPagePostUrl(PageList[page])
            if Posturl:
                PostUrlLists[page] = Posturl
                print(page, PostUrlLists[page], sep=' ')
            else:
                print("There is no post in page %s!" % page)

        print(PostUrlLists,'mark')
        return PostUrlLists

    else:
        print('There is no page!')
        return False

class ThreadTask(threading.Thread):

    def __init__(self, PostUrlList):
        super(ThreadTask, self).__init__()
        self.postUrllist = PostUrlList

    def run(self):
        for posturl in self.postUrllist:
            try:
                print(posturl)
                TumblrPostDownload.PostDownload(posturl)
            except:
                print('Something wrong in post %s' % posturl)


def DownloadAllthepsot(url):
    Task = []
    DefaultStyle = PersonalThemeSearch.BlogStyleDetection(url)
    # DefaultStyle = True

    if DefaultStyle:
        PostUrlLists = FindAllthePostUrl(url)
    else:
        PostUrlLists = ArchiveSearch.findalltheposturl(url)

    if PostUrlLists:
        PageNum = len(PostUrlLists)
        print(PageNum)
        for pageNum in range(1,PageNum+1):
            task = ThreadTask(PostUrlLists[pageNum])
            Task.append(task)
            print('-'*16,'\nThis is thread %s\n' % pageNum,'-'*16)

        for task in Task:
            task.setDaemon(True)
            task.start()
            print(time.ctime(),'thread %s start' % task)
        for task in Task:
            task.join()
        while 1:
            for task in Task:
                if task.is_alive():
                    continue
                else:
                    Task.remove(task)
                    print(time.ctime(),'thread %s is finished' % task)
            if len(Task) == 0:
                break


if __name__ == '__main__':
    select = 'N'
    reg = r'(http|https)://.*?'
    while not(select == 'Y'):
        URL = input('Input url: ')
        if re.match(reg,URL):
            try:
                start = time.time()
                # FindAllthePostUrl(URL)
                DownloadAllthepsot(URL)
                end = time.time()
                print(start,end,'=> Cost %ss' % (end-start))
            except:
                traceback.print_exc()
        else:
            print('Input wrong format.')
        select = input("Do you want to Quit? [Y/N]")


