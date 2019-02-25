import requests
from bs4 import BeautifulSoup
import re
from multiprocessing import Pool
import os, time, random
proxies = {
  "http": "http://10.10.1.10:3128",
  "https": "http://10.10.1.10:1080",
}
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64)\
                AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.3964.2 Safari/537.36"}
headers = [{'content-type': 'application/json',
           'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'},
           {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.3964.2 Safari/537.36"},
                {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'}]

def getHTMLText(url):
	try:
		r=requests.get(url,headers=headers[random.randint(0,len(headers)-1)])
		r.raise_for_status()
		r.encoding=r.apparent_encoding
		return r.text
	except:
		print('失败')
		return ''

def getallurl(list,html):
	imgpath=re.findall(r'wx\d{1}\.sinaimg\.cn[\/\%0-9a-zA-Z]*\.jpg',html)
	dit={}
	for i in range(len(imgpath)):
		im=imgpath[0].split('%2Fmw690%2F')
		path='https://'+im[0]+'/mw690/'+im[1]
		print(path)
		dit[im[1]]=path
		list.append(path)
	with open('D://pics//hh.txt','a',encoding='utf-8') as f:
		f.write(str(dit)+'\n')

def downloadpic(url,root='D://pics//'):
	#root='D://pics//'
	path=root+url.split('/')[-1].split('"')[0]
	try:
		if not os.path.exists(root):#没有文件则创建
			os.mkdir(root)
		if not os.path.exists(path):#没有这个图片就爬
			r=requests.get(url,headers=headers[random.randint(0,len(headers)-1)])
			with open(path,'wb') as f:
				f.write(r.content)#读取图片s
				f.close()
				print('文件保存成功')
				time.sleep(random.random() * 3)
		else:
			print('文件已存在')
	except:
		print('爬取失败',path)

# https://wx1.sinaimg.cn/mw690/8e6b4a8egy1fsc8avcor8j22ds1sge81.jpg
# https://wx4.sinaimg.cn/mw690/8e6b4a8egy1fsc8azbhiej22ds1sge81.jpg
# https://wx4.sinaimg.cn/mw690/8e6b4a8ely1ftoq9prv2fj22c02c0x6p.jpg
# https://wx3.sinaimg.cn/mw690/8e6b4a8ely1fs3oom0y2sj22ds1sgx6r.jpg
# clear_picSrc=%2F%2Fwx3.sinaimg.cn%2Fmw690%2F8e6b4a8ely1fs3oom0y2sj22ds1sgx6r.jpg

def main():
	with open('D://pics//view-source_https___www.weibo.com_u_2389396110_refer_flag=1005055013_.html','r',encoding='utf-8') as f:
		html=f.read()
	fylist=[]
	getallurl(fylist,html)
	for l in fylist:
		print(l)
		# downloadpic(l)
	downloadpic('https://wx3.sinaimg.cn/mw690/8e6b4a8ely1fs3oom0y2sj22ds1sgx6r.jpg')

def test(t):
	imgpath=re.findall(r'wx\d{1}\.sinaimg\.cn[\/\%0-9a-zA-Z]*\.jpg',t)
	im=imgpath[0].split('%2Fmw690%2F')
	print('https://'+im[0]+'/mw690/'+im[1])

def thdown(urls,root='D://pics//'):
	pool = Pool()
	for url in urls:
		pool.apply_async(downloadpic,(url,root))
	pool.close()
	pool.join()

# 'http://python123.io/ws/demo.html'
# tttt='https://weibo.com/p/1005052389396110'
# r=requests.get('tttt',headers=headers)
# r.encoding='utf-8'
# demo=r.text
# soup=BeautifulSoup(demo,'html.parser')
# import re
# # for link in soup.find_all('img'):
# # 	print(link.get('src'))
# print(soup.find_all(re.compile('img')))
# test('wx4.sinaimg.cn%2Fmw690%2F8e6b4a8egy1fsc8azbhiej22ds1sge81.jpg')


