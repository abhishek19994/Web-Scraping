import requests
from bs4 import BeautifulSoup as bs
from string import ascii_lowercase
import numpy
URL = "https://pharmeasy.in/online-medicine-order/browse?alphabet={alphabet}&page={page}/"
# alphabets= # choosing wh
f1=open("file.csv",'w')
f1.close()
print("Enter pages for scraping(If None then all pages will be scraped) :")
pages=input()
flag=False
if pages :
    pages=int(pages)
else:
    flag=True
ans=0
for alphabet in (ascii_lowercase):
    page=1
    while flag or pages>0 :
        arr=[]
        p=URL.format(alphabet=alphabet,page=page)
        req = requests.get(p)
        print(p)
        soup = bs(req.text, 'html.parser')
        # print(soup)
        titles = soup.find_all('div',{'class':'_3_nhL'})
        for title in titles:
            furt=title.find_all('div',{'class':'U9o7k'})
            for fu in furt:
                arr.append([fu.text])
        ans+=len(arr)
        if len(arr)==0:
            break
        else:
            # arr=numpy.asarray(arr)
            # print(arr)
            f1=open("file.csv",'a')
            numpy.savetxt(f1,arr,fmt="%s")
            f1.close()
        page+=1
        if not flag:
            pages-=1
    if  not flag and pages==0:
        break

print("Total Items Scraped:",ans)