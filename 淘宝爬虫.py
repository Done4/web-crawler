import requests
import re
#爬了Nike的两页数据
headers = {'content-type': 'application/json',
           'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}
def getHTMLText(url):
	try:
		r=requests.get(url,headers=headers)
		r.raise_for_status()
		r.encoding=r.apparent_encoding
		return r.text
	except Exception as e:
		print('shibai')
		return ""

def parsePage(ilt,html):
	try:
		plt=re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
		tlt=re.findall(r'\"raw_title\"\:\".*?\"',html)
		for i in range(len(plt)):
			try:
				
				price=eval(plt[i].split(':')[1])#获取有用的信息段
				title=eval(tlt[i].split(':')[1])
				
				ilt.append([price,title])
			except:
				print("不知")
		# for p in plt:
		# 	# print(p[14:-1])
		# 	ilt.append(p[14:-1])
		# for t in tlt:
		# 	ilt.append(t[13:-1])
		# 	# print(t[13:-1])
	except:
		print("error")
def printGoodsList(ilt):
	tplt='{0:^4}\t{1:^8}\t{2:^16}'
	print(tplt.format("序号","价格","商品名称"))
	count=0
	for g in ilt:
		count=count+1
		print(tplt.format(count,g[0],g[1]))

def main():
	goods='nike'
	depth=2
	st=0
	start_url='https://s.taobao.com/search?initiative_id=staobaoz_20180807&q='+goods
	iofoList=[]
	for i in range(depth):
		try:
			st=st+3
			#url=start_url+'&s='+str(44*i)
			url=start_url+'&bcoffset='+str(st)+'&ntoffset='+str(st)+'&p4ppushleft=1%2C48&s='+str(44*i)
			html=getHTMLText(url)
			parsePage(iofoList,html)
		except Exception as e:
			continue
	printGoodsList(iofoList)

main()	