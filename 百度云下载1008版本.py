# -*- coding:utf-8 -*-
import urllib2
import urllib
import json
import time
from selenium import webdriver
import sys
import time

reload(sys)
sys.setdefaultencoding('utf-8')
bigStr = ""
driver = webdriver.PhantomJS(executable_path='D:\Program Files\JohnnyIDE\Python27\phantomjs.exe')
def findShare(bdUserId):
	shareUserId = []
	html_content = urllib2.urlopen('http://yun.baidu.com/pcloud/friend/getfollowlist?limit=24&start=0&query_uk='+bdUserId).read()
	d2 = json.loads(html_content)
	total_count = d2['total_count']
	#print total_count
	if total_count>24:
		print str((total_count+23)/24)+"页用户开始"
		for t in range(((total_count+23)/24)):
			html_content2 = urllib2.urlopen('http://yun.baidu.com/pcloud/friend/getfollowlist?limit=24&start='+str(t*24)+'&query_uk='+bdUserId).read()
			time.sleep(2)#休息两秒
			d3 = json.loads(html_content)
			for i in range(len(d3['follow_list'])-1):
				shareUserId.append(d3['follow_list'][i]['follow_uk'])
			#print t*24
	else:
		for i in range(len(d2['follow_list'])-1):
			#print d2['follow_list'][i]['follow_uk']
			shareUserId.append(d2['follow_list'][i]['follow_uk'])
	return shareUserId

	# html_content = urllib2.urlopen('http://yun.baidu.com/share/home?uk=2440913687&view=share#category/type=0').read()
	# print html_content
def isElementExist(element):
	flag=True
	try:
		driver.find_element_by_xpath(element)
		return flag
	except:
		flag=False
		return flag

def testmoni(bdUserId):
	global bigStr
	driver.get("http://yun.baidu.com/share/home?uk="+str(bdUserId)+"&view=share#category/type=0")
	time.sleep(2)
	#print driver.title
	#print bdUserId
	isGood = isElementExist('//p[@class="no-result-title"]')
	isGood2 = isElementExist('//dl[@id="infiniteListView"]/dd[last()]')
	isGood3 = isElementExist('//div[@id="_disk_id_1"]')
	print str(bdUserId)+"   "+str(isGood)+"   "+str(isGood2)+"   "+str(isGood3)
	# if not isGood2:
	# 	print "****************此处被限制了***********************"
	#element = driver.find_element_by_xpath('//html')
	#print element.text
	if not isGood and isGood2:
		totalNum = driver.find_element_by_xpath('//dl[@id="infiniteListView"]/dd[last()]').get_attribute("_position")
		for num in range(0,int(totalNum)):
			#driver.find_element_by_xpath('//input[@name="wd"]').send_keys("Nirvana")
			fileLink = driver.find_element_by_xpath('//dl[@id="infiniteListView"]/dd[@_position="'+str(num)+'"]').get_attribute("_link")
			print fileLink
			#print driver.find_element_by_xpath('//dl[@id="infiniteListView"]/dd[@_position="1"]/div[1]/span/a[last()]').get_attribute("title")
			#print driver.current_url
			fileName = driver.find_element_by_xpath('//dl[@id="infiniteListView"]/dd[@_position="'+str(num)+'"]').text
			print fileName
			#bigStr = str(fileName)+str(fileLink)+str(bigStr)
			bigStr += str(fileName)+" "+str(fileLink)+" \n"
		return bigStr



def runBdProcess(myUserId):
	global bigStr
	timeNow = time.strftime("%Y-%m-%d%H%M%S", time.localtime())
	shareUserIds = findShare(myUserId)
	print "开始爬百度云  "+myUserId+"   的所有关注的分享用户数"+str(len(shareUserIds)+1)
	for i in range(len(shareUserIds)):
		print "-------------------------"+str(shareUserIds[i])+"-------------------------------------------"
		driver = webdriver.PhantomJS(executable_path='D:\Program Files\JohnnyIDE\Python27\phantomjs.exe')
		testmoni(shareUserIds[i])
		#time.sleep(10)
		if i % 5==0:
			#print "整除"
			driver.quit()
		print "========================="+str(shareUserIds[i])+"==========================================="
	print "oooooooooooooooooooooo结束ooooooooooooooooooooooooooo"
	print bigStr
	f1 = open('C:\\Users\\Administrator\\Desktop\\baiduyun'+str(myUserId)+'d'+str(timeNow)+'.txt','w')
	f1.write(bigStr)
	f1.close

runBdProcess('3359263108')