# -*- coding: UTF-8 -*-
# 爬取贴吧图片,网址：http://tieba.baidu.com/p/2166231880

import urllib2
import urllib
import re
import os
import time
from lxml import etree


def fetch_pictures(url):
	timeNow = time.strftime("%Y-%m-%d%H%M%S", time.localtime())
	print str(timeNow)
	os.mkdir('pictures%s' %str(timeNow))
	myabspath = os.path.dirname(os.path.abspath('__file__'))+"\\pictures"+str(timeNow)
	print myabspath
	jishu = 0
	totalNum = getPages(url)
	for mypage in range(1,totalNum+1):
		print url.split("=")[0]+"="+url.split("=")[1]+"="+str(mypage)
		html_content = urllib2.urlopen(url.split("=")[0]+"="+url.split("=")[1]+"="+str(mypage)).read()
		page_source = etree.HTML(html_content.decode('utf-8'))
		titleInfo = page_source.xpath("//img[@class='BDE_Image']/@src")
		if not os.path.exists(myabspath+'\\pictures%s' %mypage):
			os.mkdir(myabspath+'\\pictures%s' %mypage)
		os.chdir(os.path.join(myabspath+"\\", 'pictures%s' %mypage))
		for i in range(len(titleInfo)):
			picture_name = str(i) + '.jpg'
			print titleInfo[i].encode('utf-8')
			urllib.urlretrieve(titleInfo[i], picture_name)
			jishu=jishu+1
	print "------------------------------"
	print "总共下载了%d页%d张图片" %(totalNum,jishu)
	        
		# r = re.compile('<img pic_type="0" class="BDE_Image" src="(.*?)"')
		# picture_url_list = r.findall(html_content.decode('utf-8'))


def getPages(url):
	html_content = urllib2.urlopen(url).read()
	page_source = etree.HTML(html_content.decode('utf-8'))
	titleInfo = page_source.xpath("//ul[@class='l_posts_num']/li/a/@href")
	pageNum = str(titleInfo[-1]).split("=")[-1]
	print "共有%s页" %pageNum
	print type(int(str(pageNum)))
	return int(str(pageNum))
	# #os.mkdir('pictures')
	# os.chdir(os.path.join(os.getcwd(), 'pictures'))
	# for i in range(len(picture_url_list)):
	# 	picture_name = str(i) + '.jpg'
	# 	try:
	# 		urllib.urlretrieve(picture_url_list[i], picture_name)
	# 		print("Success to download " + picture_url_list[i])
	# 	except:
	# 		print("Fail to download " + picture_url_list[i])


if __name__ == '__main__':
	#fetch_pictures("http://tieba.baidu.com/p/4768497141?see_lz=1&pn=1")
    fetch_pictures("http://tieba.baidu.com/p/4810590155?see_lz=&pn=1")