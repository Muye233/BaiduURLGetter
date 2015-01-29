#coding=utf-8
f = open('data_for_dedetext.txt','r')
f2 = open('data_for_dedetitle.txt','r')
wf = open('new_dede.txt','a')
urls = "%s%s" % (f.read(),f2.read()) 
urls = set(urls.split('\n'))
for x in urls:
	wf.write("%s\n" % x)
wf.close()
f.close()
