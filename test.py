#coding=utf-8
'''

<cite>百度 - yuedu.<b>baidu</b>.com 2014-10-14</cite>
\xe7\x99\xbe\xe5\xba\xa6 - yuedu.<b>baidu</b>.com&nbsp;2014-10-14
\x87\xba\xe5\x9b\xbd\xe7\x95\x99\xe5\xad\xa6\xe7\xbd\x91 - bbs.liuxue86.com
'''
import requests
import re 
url = "http://www.so.com/s?q=%E7%99%BE%E5%BA%A6&pn=4&j=0&ls=0&src=srp_paging&fr=360sou_newhome&psid=c5cddf32cfbd45611e01267b857b608f"
#url = "http://www.so.com/s?q=intitle%3Adiscuz&pn=7&j=0&ls=0&src=srp_paging&fr=360sou_newhome&psid=b4777daf55291fe35cc05545fffb88f6"
r = requests.get(url,timeout=8)
page = r.content
pattern = re.compile(r'<cite>(.*?)&nbsp;.*?</cite>')
pattern2 = re.compile(r'(.*?) - (.*?)')
res = pattern.findall(page)

urls = []
for x in res:
	x = x.replace('<b>','').replace('</b>','')
	if pattern2.match(x):
		x = x.split(' ')[2]
	if x.count('/'):
		x = x[0:x.index('/')]
	urls.append(x)

print urls