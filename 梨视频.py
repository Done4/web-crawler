import requests
import re
import random
from 爬图片 import thdown,downloadpic

headers = [{'content-type': 'application/json',
           'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'},
           {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.3964.2 Safari/537.36"},
                {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'}]

def getUrlList(url):
	try:
		r=requests.get(url,headers=headers[random.randint(0,len(headers)-1)])
		r.raise_for_status()
		r.encoding='UTF-8'
		return r.text
	except Exception as e:
		print('失败')
		return ""

def keji(id):
	thl=[]
	for ids in id:
		url='http://www.pearvideo.com/video_%s' % ids
		html=getUrlList(url)
		regex=re.compile(r'srcUrl=\"(.*)\"\,vdoUrl')
		li=regex.findall(html)
		thl.append(li[0])
	# for u in thl:#单线程97.9s
	# 	downloadpic(u)
	thdown(thl) #多进程49.8s

if __name__ == '__main__':
	#categoryId=8 科技区
	path='http://www.pearvideo.com/category_loading.jsp?reqType=5&categoryId=8&start=%s&mrd=0.0771187188634328&hotContIds=1406824,1406796,1401417' 
	for i in range(2):
		url=path % str(i*12)
		html=getUrlList(url)
		regex=re.compile(r'href=\"video_(\d+)\"')
		li=regex.findall(html)
		keji(li)

# print(regex.findall('l=\"\",srcUrl="http://video.pearvideo.com/mp4/third/20180720/cont-1393005-10898606-113644-hd.mp4",vdo'))


# print(regex.findall('<a href="video_1406796" class="vervideo-lilink actplay">'))
