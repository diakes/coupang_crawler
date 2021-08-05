from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
import subprocess
import shutil
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import re
from bs4 import BeautifulSoup


# 사이트를 여는 부분 
class open_Shopping:
    def retrieval(self):
        
        try:
            shutil.rmtree(r"c:\chrometemp")  #쿠키 / 캐쉬파일 삭제
        except FileNotFoundError:
            pass
        
        try :
            #64 bit
            subprocess.Popen(r'C:\Program Files\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\chrometemp"') # 디버거 크롬 구동
        except FileNotFoundError :
            #32 bit 
            subprocess.Popen(r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\chrometemp"')
        # Google driver 처리
        
        option = Options()
        option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        option.add_argument("disable-gpu")
        
        chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
        global driver
        try:
            driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe',options=option)
        except:
            chromedriver_autoinstaller.install(True)#맞는 버전 선택
            driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)
        driver.implicitly_wait(10)
        driver.set_window_size(940,1050)
        driver.set_window_position(-10,0)
        
        return driver
        
        
if __name__=="__main__" :
    print("모듈실행")
    open_p=open_Shopping()
    open_p.retrieval()
    url = "https://www.coupang.com/"
    driver.get(url)
    elem = WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.XPATH, "//*[@id='searchOptionForm']/div[1]")))
    print("성공")
    prev_height = driver.execute_script("return document.body.scrollHeight")
    
    # 반복 수행
    while True:
        # 현재 문서 높이를 가져와서 저장
        curr_height = driver.execute_script("return document.body.scrollHeight")
        if curr_height == prev_height:
            break
            
        prev_height = curr_height
        
    print("스크롤 완료")
    soup = BeautifulSoup(driver.page_source, "lxml")
    
    items = soup.find_all("li", attrs={"class":re.compile("^search-product")})
    #print(items[0].find("div", attrs={"class":"name"}).get_text())
    for item in items:
    
        # 광고 제품은 제외
        ad_badge = item.find("span", attrs={"class":"ad-badge-text"})
        if ad_badge:
            print("광고 상품 제외합니다")
            continue
            
        name = item.find("div", attrs={"class":"name"}).get_text() # 제품명
        
        
        price = item.find("strong", attrs={"class":"price-value"}).get_text() # 가격
        
        # 리뷰 100개 이상, 평점 4.5 이상 되는 것만 조회
        rate = item.find("em", attrs={"class":"rating"}) # 평점
        if rate:
            rate = rate.get_text()
        else:
            print("평점 없는 상품 제외합니다")
            continue
            
        rate_cnt = item.find("span", attrs={"class":"rating-total-count"}) # 평점 수 
        if rate_cnt:
            rate_cnt = rate_cnt.get_text() # 예 : (26)
            rate_cnt = rate_cnt[1:-1]
            #print("리뷰 수", rate_cnt)
        else:
            print("평점 수 없는 상품 제외합니다")
            continue
            
        print(name, price, rate, rate_cnt)
else:
    print("외부 호출2")
    
    
    


        