import requests
import re
from bs4 import BeautifulSoup
from setuptools.package_index import HREF


headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}

url = "https://www.coupang.com/vp/products/1684892432?vendorItemId=70859009055&sourceType=HOME_PERSONALIZED_ADS&searchId=feed-1617003162233-personalized_ads&isAddedCart="

res = requests.get(url, headers=headers)
res.raise_for_status()
item = BeautifulSoup(res.text, "lxml")

name = item.find("h2", attrs={"class":"prod-buy-header__title"}).get_text() # 제품명

price = item.find("span", attrs={"class":"total-price"}).get_text().strip() # 가격

rate = item.find("span", attrs={"class":"rating-star-container"}) # 평점
if rate:
    rate = rate.span["style"][-6:-2]
else:
    rate = "없음"

rate_cnt = item.find("span", attrs={"class":"count"}) # 평점 수 
if rate_cnt:
    rate_cnt = rate_cnt.get_text()[0:3] # 예 : (26)
else:
   rate_cnt = "평점 수 없음"


Shipping = item.find("em", attrs={"class":"prod-txt-bold"}).get_text() # 배송 

Courier = item.find("div", attrs={"class":"prod-vendor-info"}).span.get_text().strip() # 백배사
#
Seller = item.find("a", attrs={"class":"prod-sale-vendor-name"}).get_text() # 판매자 
#
# Sales_status = item.find("span", attrs={"class":"prod-sale-vendor-name"}) # 판매상태**
#
# Manufacturer = item.find("span", attrs={"class":"prod-sale-vendor-name"}) # 제조사명**
#
Country = item.find("li", attrs={"class":"prod-attr-item"}).get_text()[-3:]  # 원산지

ing = item.find("img", attrs={"class":"prod-image__detail"})["src"] # 이미지**
#
code = item.find("ul", attrs={"class":"prod-description-attribute"}).get_text()[-23:].strip()  # 상품코드
#
Kategorie = item.find("ul", attrs={"id":"breadcrumb"}) # 카테고리
#
Detailed = item.find("table", attrs={"class":"prod-delivery-return-policy-table essential-info-table"}) # 상세정보
#

#print(name, price, rate, rate_cnt)
print(f"제품명 : {name}")
print(f"가격 : {price}")
print(f"평점 : {rate}점 ({rate_cnt}개)")
print(f"배송 : {Shipping}")
print(f"택배사 : {Courier}")
print(f"판매자 : {Seller}")

print(f"제조사명 : {price}")
print(f"원산지 : {Country}")
print(f"이미지 : {ing}")
print(f"상품코드 : {code}")
print(f"카테고리 : 불가능")
print(f"상세정보 : {Detailed}")
print("-"*100) # 줄긋기
    