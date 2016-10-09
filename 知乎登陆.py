# -*- coding:utf-8 -*-
import urllib2
import urllib
import cookielib
posturl = 'https://www.zhihu.com/login/phone_num'
headers={
		    'User-Agent':
		    'Mozilla/5.0 (Windows NT 10.0; WOW64)'
			'AppleWebKit/537.36 (KHTML, like Gecko)'
			'Chrome/50.0.2661.102 Safari/537.36',
    'Referer':'https://www.zhihu.com/'
}
value = {
    'password':'*****************',
    'remember_me':True,
    'phone_num':'*******************',
    '_xsrf':'**********************'
}
data=urllib.urlencode(value)
#初始化一个CookieJar来处理Cookie
cookieJar=cookielib.CookieJar()
cookie_support = urllib2.HTTPCookieProcessor(cookieJar)
#实例化一个全局opener
opener=urllib2.build_opener(cookie_support)
request = urllib2.Request(posturl, data, headers)
result=opener.open(request)
print result.read()