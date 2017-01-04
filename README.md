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

#Envirment
Development under Python3.5 with some basic packages, such as requests. 

#Run
Run the TumblrCrawler.py directly.
The input could be the blog's url, such as "http://.*?.tumblr.com/"
Or any single post that you like.

Finally, Enjoy your Interested and Excited Dowload! :)
