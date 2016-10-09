import  re  
import  urllib  
import  urllib2  
import  sys  
      
class dict :  
    def __init__(self):  
        reload(sys)  
        sys.setdefaultencoding('utf8')    
    def serach(self):  
        waitWord = raw_input(unicode('请输入英文单词','utf-8').encode('gbk')+"\n")  
        waitWord = urllib.quote(waitWord)  
  
        baiduUrl = "http://dict.youdao.com/search?q="+waitWord+"&keyfrom=dict.index"  
        userAgent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:32.0) Gecko/20100101 Firefox/32.0'  
        headers = {'User-Agent':userAgent}  
        req = urllib2.Request(baiduUrl,headers = headers)  
        Res = urllib2.urlopen(req)  
        ResultPage = Res.read().decode("utf-8")  
  
        show = re.findall(r'<div class="trans-container">.*<div id="webTrans" class="trans-wrapper trans-tab">',ResultPage,re.S)  
        try:  
            s = show[0].decode("utf-8")  
            pos = re.findall(r'<li>.*<\/li>',s,re.S)  
            arr = pos[0].split('\n')  
            if len(arr)>0:  
                for x in arr:  
                    print re.sub('<[^>]+>','',x).strip()  
        except :  
            print unicode('没有查到','utf-8')  
  
  
if __name__ == '__main__':  
    mydict  = dict()  
    mydict.serach()  