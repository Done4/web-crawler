import requests
import re
import random
from 爬图片 import downloadpic

# ...
# https://m.weibo.cn/5584777009/4270804164709750 单条动态
# https://m.weibo.cn/status/4270804164709750? 单条有用的url
# https://m.weibo.cn/p/2304135584777009_-_WEIBO_SECOND_PROFILE_WEIBO 个人主页
# https://m.weibo.cn/p/2304135584777009_-_WEIBO_SECOND_PROFILE_WEIBO&page_type=03&page=2 第二页
# ...
header = {'content-type': 'application/json',
           'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}
headers = [{'content-type': 'application/json',
           'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'},
           {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.3964.2 Safari/537.36"},
                {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'}]
def getUrlList(url):
	# try:
		r=requests.get(url,headers=headers[random.randint(0,len(headers)-1)])
		# r=requests.get(url,headers=headers)
		r.raise_for_status()
		r.encoding='UTF-8'
		return r.text
	# except Exception as e:
	# 	print('shibai')
	# 	return ""

if __name__ == '__main__':
	#url='https://m.weibo.cn/status/4270128512743810?'#模特url
	url='https://m.weibo.cn/status/4264637136718583?'#网红url
	ilt=[]
	html=getUrlList(url)
	regex=re.compile(r'\"url\"\:\s\"(.*)\"\,') #模特正则
	img=regex.findall(html)
	for m in img:
		downloadpic(m)
