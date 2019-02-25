import requests
import os
from bs4 import BeautifulSoup
import bs4
headers = {'content-type': 'application/json',
           'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}


def getHTMLText(url):
	try:
		r=requests.get(url,headers=headers)
		r.raise_for_status()
		r.encoding=r.apparent_encoding
		return r.text
	except Exception as e:
		return ""
	
def fillUnivList(ulist,html):
	soup=BeautifulSoup(html,'html.parser')
	for tr in soup.find('tbody').children:		
		if isinstance(tr,bs4.element.Tag):
			tds=tr('td')
			ulist.append([tds[0].string,tds[1].string,tds[2].string,tds[3].string])
def printUnivList(ulist,num):#输出num 条信息
	tplt='{0:^10}\t{1:^10}\t{2:^10}\t{3:^10}'
	print(tplt.format('排名','学校','省市','总分',chr(12288)))#表头,chr 用中文空格解决对齐问题。
	for i in range(num):
		u=ulist[i]
		print(tplt.format(u[0],u[1],u[2],u[3],chr(12288)))
	

def main():
	uinfo=[]
	url='http://zuihaodaxue.cn/zuihaodaxuepaiming2018.html'
	html=getHTMLText(url)
	fillUnivList(uinfo,html)
	printUnivList(uinfo,20)

main()