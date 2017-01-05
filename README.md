# Tumblr_Crawler
This is a multi-threade crawler for Tumblr. Able to download entire blog or any post that you like.

There are two crawler module for video and image. 
One is for video, another is for image including GIF.
The main file is Crawler.

#update2.0 for download any Post
This version of TumblrCrawler combine video and image including GIF in
the same file. What’s more, it can acknowledge whether the main content
is video or photo. Current version is only for download post page
directly. The whole blog searching function is undergoing. This
searching will be easy, ignoring the JS. My thoughts is using archive
page to get all the post pages, then get in every page to download.

#Update3.0
This version is final one which add crawler whole blog posts function,
which means this crawler can download all the file, including images
and video, of one blog once. This crawler uses threading.Thread Module.
Every 10 posts as a page in tumblr as a single thread one time,
Multi-thread accelerate whole procession. It needs no cookie can
crawler any account. Of course, the more post there are, the longer it
will take to crawler all.

#update4.0
Find out some blog install personal Theme, which means they use different stylesheet from the default one. So it leads to crawl from home page is unavailable, so I change to search the default page as Archive. All the Archive page is the same stylesheet. But every archive page has 50 post, which means one single thread has to process 50 post url download. Definitely, it slow downs the procession a lot. But it has to be. 

PersonalThemeSearch.py Module is for discriminating whether blog use default stylesheet or personal one.

ArchiveSearch.py is the Module for crawling all the post url in Archive page, every page has 50 posts url. Meanwhile, original way to crawl main page gets 10 posts every posts. 

This version only figure out that searching all the post in every kind of stylesheet blog. It need to be solved to design a more universal function to crawl personal template post’s content.

What’s more, this version fixes some exception in none post page and a little logical problem about input. There are some spacial cases of url format, like "https://.*?", "http://wanimal1983.org/" (WTF? Redirection? http://wanimal1983.tumblr.com)

#Envirment
Development under Python3.5 with some basic packages, such as requests. 

#Run
Run the TumblrCrawler.py directly.
The input could be the blog's url, such as "http://.*?.tumblr.com/"
Or any single post that you like.

Finally, Enjoy your Interested and Excited Dowload! :)
