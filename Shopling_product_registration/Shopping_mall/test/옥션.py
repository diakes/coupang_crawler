import tkinter.ttk as ttk
from tkinter import *
from tkinter import filedialog
import requests
import re
import os
import csv
from bs4 import BeautifulSoup
class aat:
    def retrieval(self):
        e="사이다"
        url ="https://www.coupang.com/np/search?component=&q="+e+"&channel=user"
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"}
        
        res = requests.get(url, headers=headers)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "lxml")
        items = soup.find_all("li", attrs={"class":re.compile("^search-product")})
        
        for idx, item in enumerate(items):
            name = item.find("div", attrs={"class":"name"}).get_text() # 제품명
            price = item.find("strong", attrs={"class":"price-value"}).get_text() # 가격
                 
            rate = item.find("em", attrs={"class":"rating"}) # 평점
            if rate:
                rate = rate.get_text()
            else:
                print("<평점 없는 상품 제외합니다>")
            
            rate_cnt = item.find("span", attrs={"class":"rating-total-count"}) # 평점수 
            if rate_cnt:
                rate_cnt = rate_cnt.get_text() # (수)
                rate_cnt = rate_cnt[1:-1]
            else:
                print("<평점 수 없는 상품 제외합니다>")
                
            link = item.find("a", attrs={"class":"search-product-link"})["href"]
            
            if float(rate) >= 0 and int(rate_cnt) >= 0:
                content="제품명:"+name+"\t가격:"+price+"\t평점:"+rate+"\t점("+rate_cnt+"개)\t"+" 바로가기:{}".format("https://www.coupang.com"+ link)
                print(content)
