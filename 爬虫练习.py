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

#爬取整个微博主页照片的函数 :)

def whole(id,index,restpath='&page_type=03&page='):
	url='https://m.weibo.cn/api/container/getIndex?containerid=230413%s_-_WEIBO_SECOND_PROFILE_WEIBO' % (id)
	html=getUrlList(url+restpath+str(index))

	regex=re.compile(r'\"url\"\:\"(.{70})')
	img=regex.findall(html)[::2]
	
	regex1=re.compile(r'\\')
	realimg=[]
	for p in img:
		im=regex1.split(p)
		if len(im)>4:
			realimg.append(im[0]+im[1]+im[2]+im[3]+im[4])
			#downloadpic(im[0]+im[1]+im[2]+im[3]+im[4],'D://pics//'+id+'//')
	thdown(realimg,'D://pics//'+id+'//')
#3251967895
if __name__ == '__main__':
	try:
		for i in range(6):
			whole(id='1280761142',index=i)
		print('OK')
	except:
		print('error')



# s='4j30jg0jgglx","url":"https:\/\/wx3.sinaimg.cn\/orj360\/0065X9Cxly1fu1yv1ugj4j30jg0jgglx.jpg",'
# h='jgglx","url":"https:\/\/wx3.sinaimg.cn\/orj360\/0065X9Cxly1fu1yv1ugj4j30jg0jgglx.jpg","size":"orj360","g'
# regex=re.compile(r'\"url\"\:\"(.{70})') #暂时万能图片正则	
# img=regex.findall(h)
# print(img)

# hh="https:\/\/wx3.sinaimg.cn\/orj360\/0065X9Cxly1fu1z2efuzyj30jg0jg76d.jpg"
# print(len(hh))





# s='https:\/\/wx1.sinaimg.cn\/large\/0065X9Cxly1fu0t8q3dh2j30jg0jgjtc.jpg'
# regex=re.compile(r'\\')
# im=regex.split(s)
# if len(im)>4:
# 	print(im[0]+im[1]+im[2]+im[3]+im[4])