from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")

browser = webdriver.Chrome(options=options)
browser.maximize_window()

# 페이지 이동
url = "https://www.coupang.com/vp/products/315056439?itemId=1001136291&vendorItemId=72519414151&q=%ED%8C%A8%EB%94%A9&itemsCount=36&searchId=049347aedc9044ce9aa8599377293697&rank=1&isAddedCart="
browser.get(url)

import time
interval = 2 # 2초에 한번씩 스크롤 내림

# 현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script("return document.body.scrollHeight")

# 반복 수행
while True:
    # 스크롤을 가장 아래로 내림
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    # 페이지 로딩 대기
    time.sleep(interval)

    # 현재 문서 높이를 가져와서 저장
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height:
        break

    prev_height = curr_height

print("스크롤 완료")

import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(browser.page_source, "lxml")
print(soup)
name = soup.find("h2", attrs={"class":"prod-buy-header__title"}).get_text() # 제품명
print(f"제품명 : {name}")

price = soup.find("span", attrs={"class":"total-price"}).get_text().strip() # 가격
print(f"가격 : {price}")

rate = soup.find("span", attrs={"class":"rating-star-container"}) # 평점
if rate:#평점
    rate = rate.span["style"][-6:-2]
else:
    rate = "없음"
    
rate_cnt = soup.find("span", attrs={"class":"count"}) # 평점 수 
if rate_cnt:
    rate_cnt = rate_cnt.get_text()[0:3] # 예 : (26)
else:
   rate_cnt = "평점 수 없음"
print(f"평점 : {rate}점 ({rate_cnt}개)")

ing = soup.find("img", attrs={"class":"prod-image__detail"})["src"] # 대표이미지
print(f"이미지 : {ing}")

Kategorie= soup.find_all("a", attrs={"class":"breadcrumb-link"})# 카테고리
i=0
for Kat in Kategorie:
    Kategorie[i] = Kat.get_text().strip()
    i+=1
print(f"카테고리: {Kategorie}")

Detailed = soup.find("table", attrs={"class":"prod-delivery-return-policy-table essential-info-table"}) # 상세정보
#print(f"상세정보 : {Detailed}")

code = soup.find("meta", attrs={"property":"og:url"})["content"].strip()# 상품코드
code2=code.replace("https://www.coupang.com/vp/products/", "").strip()
print(f"상품코드 : {code2}")

Seller = soup.find("a", attrs={"class":"prod-brand-name"}).get_text()# 판매자명**
print(f"판매자 : {Seller}")

Shipping = soup.find("div", attrs={"class":"prod-shipping-fee-message"}).get_text().strip()# 배송 
print(f"배송 : {Shipping}")

