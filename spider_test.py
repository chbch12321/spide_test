"""
import requests   ##功能：爬取特定url所用时间
import time

def getHTML(url):
  try :
    r=requests.get(url,timeout=30)
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    return r.text
  except:
    return "error"

if __name__=="__main__":
  start=time.perf_counter()
  url="http://www.nbu.edu.cn/"
  for i in range(30):
    time1=time.perf_counter()
    getHTML(url)
    print("第{}次爬取网站用时：{:.2f}s".format(i+1, time.perf_counter()-time1))
  end=time.perf_counter()-start
  print("爬取网站总体用时：{:.2f}s".format(end))
  print("爬取网站平均用时：{:.2f}s".format(end/30))
  """
'''
import requests    #爬取图片并保存
import os
url="https://img10.360buyimg.com/n1/jfs/t3847/338/2200026645/140646/c239125d/58537d88Nc15f021d.jpg"
root="D://PICTURE//"
path=root+url.split('/')[-1]

try :
  if not os.path.exists(root):
    os.mkdir(root)
  if not os.path.exists(path):
    r=requests.get(url)
    with open (path,"wb") as f:
      f.write(r.content)
      f.close()
      print("文件以保存")
  else:
    print("文件已存在")
except:
  print("爬取失败")
'''
'''
import requests   #查询IP地址
url="http://m.ip138.com/ip.asp?ip="
r=requests.get(url+"122.227.213.154")
print(r.status_code)
print(r.text[-300:])
'''
'''   
import bs4                      #爬取中国大学排名并打印
import requests
from bs4 import BeautifulSoup
def getHTML(url):
  try:
    r=requests.get(url,timeout=30)
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    return r.text
  except :
    return" "

def fillGroup(group,html):
  soup=BeautifulSoup(html,"html.parser")
  for tr in soup.find('tbody').children:
    if isinstance(tr,bs4.element.Tag):
      tds=tr.find_all('td')
      group.append([tds[0].string,tds[1].string,tds[2].string,tds[3].string])
    

def printGroup(group,num):
  print("{0:^15}\t{1:{4}^15}\t{2:^15}\t{3:^15}".format("排名","学校","省份","总分",chr(12288)))
  for i in range(num):
    print("{0:^15}\t{1:{4}^15}\t{2:^15}\t{3:^15}".format(group[i][0],group[i][1],group[i][2],group[i][3],chr(12288)))

def main():
  url="http://www.zuihaodaxue.cn/zuihaodaxuepaiming2018.html"
  html=getHTML(url)
  group_univs=[]
  fillGroup(group_univs,html)
  printGroup(group_univs,30)

main() 
'''
