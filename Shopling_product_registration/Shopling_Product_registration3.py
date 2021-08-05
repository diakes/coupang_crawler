"""

쿠팡 웹 크롤러 GUI 부분

프로그램 구조 
        Shopling_proudct_registration3.py(최상단)
                        |
                        ▼
                almost_done.py        
                        |
                        ▼
making_goodAttri.py,making_essential.py,making_option.py,requesting_xml.py
로 구성됨 

디버깅을 위해서는 관련 패키지 설치 필요

pip install selenium
pip install requests
pip install Beautifulsoup4
pip install chromedriver_autoinstaller
pip install lxml
pip install openpyxl
로 설치 

2021.06.17 개발 kdi

tkinter을 이용한 gui 개발 

"""

# -*- coding: utf-8 -*-
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from requests.models import HTTPError
from selenium import webdriver
from tkinter import *
import requests
import re
import os,glob
from Selenium_Function.open import *
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
import subprocess
import shutil
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from tkinter import filedialog
from itertools import count
import almost_done as ad
import urllib.request as req

root = Tk()
root.title("Shopling_Version 1.0.0")
root.geometry("996x915+915+0")
root.iconbitmap(r"shopling.ico")#아이콘
root.configure(background="#F0F0F0")#배경색
menu = Menu(root)#메뉴


#브라운저 열기#
Open_browser=open_Shopping()


#함수
#쇼핑몰 링크
tta = True

Kin_URL="" #Kin_URL을 이용해서 사용 하기 
# 그리고 한글은 utf-8 인코딩 필요함
#global save_link
url_list = list()
saving_click_list = list()


# 쇼핑몰 선택 관련 함수
def Shopping_ling():
    global tta
    global tta_op
    global photo2
    global Shopping_mall_name
    global driver
    global Kin_URL
    Shopping_mall_name="쿠팡"
    # Search_combobox.set("쿠팡")
    #쿠팡 만 해당
    if tta == True :
        photo2 = PhotoImage(file="img2/"+img_file[0])
        url = "https://www.coupang.com/"
        if tta_op==False:
            driver=Open_browser.retrieval()
            tta_op=True
        driver.get(url)
        tta=False
    #다른 쇼핑몰
    else:
        driver.close()
        tta_op=False
        photo2 = PhotoImage(file="img/"+img_file[0])
        tta=True
    Shopping_photo1.config(image=photo2)
    Kin_URL=driver.current_url
    URL(Kin_URL)
    return driver

# 선택된 것을 더블클릭 할시 이벤트 해당 url 페이지로 이동
def aa(self): 
    selected = main_list_pricey_list.focus()
    values =main_list_pricey_list.item(selected, 'values')
    driver.get(values[5]) # 해당url로 이동 

# 상품 수집리스트를 정렬 하기 위한 것 
# ▲ 오름차순 정렬 ▼ 내림차순 정렬 
# 이름 순으로 정렬
def treeview_sort_column_name(tv, col, reverse):
    l = [(tv.set(k, col), k) for k in tv.get_children('')]
    l.sort(reverse=reverse)
    
    if reverse == True :
        main_list_pricey_list.heading("Name",text="상품명▲",anchor=CENTER, command = getting_order_name)
    else :
        main_list_pricey_list.heading("Name",text="상품명▼",anchor=CENTER, command = getting_order_name)
    # rearrange items in sorted positions
    for index, (val, k) in enumerate(l):
        tv.move(k, '', index)

#가격 순으로 리스트 정렬
def treeview_sort_column_price(tv, col, reverse):
    l = [(int(tv.set(k, col)), k) for k in tv.get_children('')]
    l.sort(reverse=reverse)
    if reverse == True :
        main_list_pricey_list.heading("price",text="가격▲",anchor=CENTER, command = getting_order_price)
    else :
        main_list_pricey_list.heading("price",text="가격▼",anchor=CENTER, command = getting_order_price)
    # rearrange items in sorted positions
    for index, (val, k) in enumerate(l):
        tv.move(k, '', index)

#별점 순으로 리스트 정렬
def treeview_sort_column_star(tv, col, reverse):
    l = [(float(tv.set(k, col)), k) for k in tv.get_children('')]
    l.sort(reverse=reverse)
    if reverse == True :
        main_list_pricey_list.heading("rate",text="별점▲",anchor=CENTER, command = getting_order_star)
    else :
        main_list_pricey_list.heading("rate",text="별점▼",anchor=CENTER, command = getting_order_star)
    # rearrange items in sorted positions
    for index, (val, k) in enumerate(l):
        tv.move(k, '', index)

#리뷰수 순으로 리스트 정렬
def treeview_sort_column_review(tv, col, reverse):
    l = [(int(tv.set(k, col)), k) for k in tv.get_children('')]
    l.sort(reverse=reverse)

    if reverse == True :
        main_list_pricey_list.heading("rate_cnt",text="리뷰수▲",anchor=CENTER, command = getting_order_review)
    else :
        main_list_pricey_list.heading("rate_cnt",text="리뷰수▼",anchor=CENTER, command = getting_order_review)

    # rearrange items in sorted positions
    for index, (val, k) in enumerate(l):
        tv.move(k, '', index)

#등록여부 순으로 리스트 정렬
def treeview_sort_column_enrolling(tv, col, reverse):
    l = [(tv.set(k, col), k) for k in tv.get_children('')]
    #print(l)
    #l.sort(reverse=reverse)
    if reverse == True :
        for j in range(0,len(l)):
            for i,(val,k) in enumerate(l):
                if val == "실패" :
                    l[i],l[j] = l[j],l[i]
    
    for index, (val, k) in enumerate(l):
        tv.move(k, '', index)

# 처음 눌렀을 떄 오름 차순으로 구현하기 위해서 사용
enroll_order = False
name_order = False
price_order = False
star_order = False
review_order = False

# 번호 순으로 정렬 오름차순만 구현
def getting_order_count():
    child = main_list_pricey_list.get_children('')
    l = [(main_list_pricey_list.item(k,'text'), k) for k in child]
    l.sort(reverse=False)

    for index, (val, k) in enumerate(l):
        main_list_pricey_list.move(k, '', index)

# 등록 여부로 정렬
def getting_order_enroll():
    global enroll_order
    #True(내림차순) 일때는 false (오름차순)으로 처리함
    if enroll_order == True :
        enroll_order = False
    # 반대로 처리됨
    else :
        enroll_order = True
    treeview_sort_column_enrolling(main_list_pricey_list,0,enroll_order)

# 이름 순으로 정렬
def getting_order_name():
    global name_order
    if name_order == True :
        name_order = False
    else :
        name_order = True
    treeview_sort_column_name(main_list_pricey_list,1,name_order)

# 가격 순으로 정렬
def getting_order_price():
    global price_order
    if price_order == True :
        price_order = False
    else:
        price_order = True
    treeview_sort_column_price(main_list_pricey_list,2,price_order)

# 별점 순으로 정렬
def getting_order_star():
    global star_order
    if star_order == True :
        star_order = False
    else:
        star_order = True
    treeview_sort_column_star(main_list_pricey_list,3,star_order)

# 리뷰수 순으로 정렬
def getting_order_review():
    global review_order
    if review_order == True :
        review_order = False
    else:
        review_order = True
    treeview_sort_column_review(main_list_pricey_list,4,review_order)


# URL 관련 함수
# url_list에 저장
def saving_url(url) :
    url_list.append(url)

#url_list 안에 삭제
def deleting_url(url) :
    url_list.remove(url)

# url_list 한번에 얻기 위한 것 
def geting_url_list():
    x=main_list_pricey_list.get_children()
    for child in x :
        values =main_list_pricey_list.item(child, 'values')
        saving_url(values[5])

    return url_list  

#전체 페이지 수집 함수
# 상품 검색시 나오는 페이지 수집 함수 
# 간단하게 이름, 가격, 평점, 리뷰수, URL 등을 수집함
def Enrollment(b):
    if b == "현재 페이지" :
        global count
        try :
            Kin_URL=driver.current_url
            URL(Kin_URL)
            prev_height = driver.execute_script("return document.body.scrollHeight")
        # 반복 수행
            while True:
            # 현재 문서 높이를 가져와서 저장
                curr_height = driver.execute_script("return document.body.scrollHeight")
                if curr_height == prev_height:
                    break
                    
                prev_height = curr_height
            soup = BeautifulSoup(driver.page_source, "lxml")
        
        except NameError: 
            try :
                headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
                res = req.Request(main_condition_key_box_Label.get(),headers=headers)
                result = req.urlopen(res)
            
            except HTTPError as e :
                err =  e.read()
                code = e.getcode()
                print(code)
            finally :
                soup = BeautifulSoup(result.read(), "lxml")
                result.close()
    else :
        Kin_URL=driver.current_url
        URL(Kin_URL)
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
        for i in range(0,int(b)):
            try : 
                url = "&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=1=4&backgroundColor=".format(i)
                url =Kin_URL+url
                res = requests.get(url, headers=headers)
                res.raise_for_status()
                soup = BeautifulSoup(res.text, "lxml")

            except HTTPError as e :
                msgbox.showerror('오류','현재 페이지에서는 정보를 수집할 수 없습니다.\n다른 페이지를 입력해주세요.')

    items = soup.find_all("li", attrs={"class":re.compile("^search-product")})
    if len(items) == 0 :
        msgbox.showerror('오류','현재 페이지에서는 정보를 수집할 수 없습니다.\n다른 페이지를 입력해주세요.')

    for idx, item in enumerate(items):
    
        name = item.find("div", attrs={"class":"name"}).get_text() # 제품명
        
        enrolling = "대기" # 등록 여부
        #default "대기"
        
        price = item.find("strong", attrs={"class":"price-value"}).get_text() # 가격

        price_int = int(price.replace(',','')) #정렬을 위한 가격의 정수형 변환 

        rate = item.find("em", attrs={"class":"rating"}) # 평점
        if rate:
            rate = rate.get_text()
        else:
            rate= 0 # 0일 떄는 "별점 없음"과 같음
        
        rate = float(rate) # 정렬을 위해 평점도 실수형 변환

        rate_cnt = item.find("span", attrs={"class":"rating-total-count"}) # 평점 수 
        
        if rate_cnt:
            rate_cnt = rate_cnt.get_text() # 예 : (26)
            rate_cnt = rate_cnt[1:-1]
        else:
            rate_cnt=0
        
        rate_cnt = int(rate_cnt)

        #URL 
        link = item.find("a", attrs={"class":"search-product-link"})["href"]
        link ="https://www.coupang.com" +link

        
        # count가 text로 가장 앞에 존재 그 뒤로 등록여부, 이름, 가격, 평점, 리뷰수, URL 순으로 리스트에 출력됨
        main_list_pricey_list .insert(parent='',index='end',text=count,values=(enrolling,name,price_int,rate,rate_cnt,link)) # main_list_pricey_list 에 넣어준다.

        count+=1
        progress = (idx + 1) / len(items) * 100 #percent 계산식
        main_progress_Var.set(progress)
        main_progress_box.update()

# 저장 경로 (폴더)
def URL(URL):
     main_condition_key_box_Label.delete(0, END) # 다 비어 주고
     main_condition_key_box_Label.insert(0, URL) # 이 URL값을 넣어준다.

#페이지 번호 관리 함수
def Refresh():
    box1=main_list_topl_Combobox.get()
    Enrollment(box1) # 여러 페이지면 범위를 지정해 주어서 해준다.

#리스트 전체 삭제
def main_list_all_del(event):
    global count
    x=main_list_pricey_list.get_children()
    if x != '' :
        for child in x :
            values =main_list_pricey_list.item(child, 'values')
            if len(url_list) != 0 :
                deleting_url(values[5])
            main_list_pricey_list.delete(child)
            
    count = 1
    # for record in x:
    #     main_list_pricey_list.delete(record)

#리스트 원하는 것만 삭제
def main_list_top_del(event):
    x=main_list_pricey_list.selection()
    for record in x:
        values =main_list_pricey_list.item(record, 'values')
        if len(url_list) != 0 :
                deleting_url(values[5])
        main_list_pricey_list.delete(record)

def main_list_top(event):
    main_list_topl_Combobox.pack(side="right", padx=5)

#api 체크 하기 위한 함수
def checking_api(event) : 
    #인증 실패 할시 다시 입력 하게 처리함
    if ad.responing_id(main_save_information_box1_entry.get(),main_save_information_box2_entry.get(),main_save_information_box3_entry.get()) == "인증 실패" : 
        msgbox.showinfo('오류','샵플링 등록 정보가 잘못 되었습니다. 다시 입력 해 주세요.')
    #성공시 입력 란을 막아버림
    else :
        btn_retrieval['state'] = DISABLED
        main_save_information_box1_entry['state'] = DISABLED
        main_save_information_box2_entry['state'] = DISABLED
        main_save_information_box3_entry['state'] = DISABLED
        msgbox.showinfo('알림','샵플링 등록 정보 확인 완료')

# 샵플링 선택 전송 버튼을 누를떄 발생하는 이벤트 
def click_shopling_save(event):
    #마진율 체크 
    if main_condition_price_box1_entry.get() == "":
        msgbox.showerror('오류','마진율 값을 입력 해 주세요.')
    elif int(main_condition_price_box1_entry.get()) < 20:
       msgbox.showerror('오류','마진율은 20%보다 낮을 수 없습니다. 다시 입력 해 주세요.')
    
    #마진율 정상적으로 입력 시 
    else:
        if btn_retrieval['state'] == DISABLED :
            url_list2 = list()
            magin_rate = main_condition_price_box1_entry.get() # 마진율 적용
            ad.getting_margin_rate(int(magin_rate))
            x=main_list_pricey_list.selection()
            if len(x) == 0 :
                msgbox.showerror('오류','등록할 값을 한 개 이상 선택해주세요.')
            elif len(x) >= 1 :
                for record in x:
                    values =main_list_pricey_list.item(record, 'values')
                    url_list2.append(values[5])
                result = msgbox.askquestion("선택" ,f"총{len(x)}개 선택 되었습니다.\n[마진율 {main_condition_price_box1_entry.get()}%]입니다.\n선택된 상품만 샵플링에 등록(수정) 진행하시겠습니까?")
            if result == "yes" :
                for idx,url in enumerate(url_list2) :
                    making_result = ad.making_things(url,main_save_information_box1_entry.get(),main_save_information_box2_entry.get(),main_save_information_box3_entry.get())
                    changing_things(making_result)
                    progress = (idx + 1) / len(url_list2) * 100 #percent 계산식
                    main_progress_Var.set(progress)
                    main_progress_box.update()

        else :
            msgbox.showinfo('오류','올바른 인증키 입력후 인증키 검사 버튼을 눌려주세요.')

# 안내를 클릭 할시 나타나는 안내문 
def things_information():
    msgbox.showinfo("알림" , "1.선택 상품을 더블클릭하면 해당 상품 URL로 이동합니다.\n2.표 제목 컬럼을 클릭하시면 정렬이 수행됩니다.\n3.여러 상품을 선택 하실려면 ctrl키를 눌려준 상태에서 상품을 선택해주세요\n")

# 샵플링 전체 전송 버튼 누를 때 발생하는 이벤트
def click_shopling_save_all(event):
    #마진율 체크 
    if main_condition_price_box1_entry.get() == "":
        msgbox.showerror('오류','마진율 값을 입력 해 주세요.')
    elif int(main_condition_price_box1_entry.get()) < 20:
       msgbox.showerror('오류','마진율은 20%보다 낮을 수 없습니다. 다시 입력 해 주세요.')
    else:
        # 인증 정보가 로그인이 완료 될때 실행 되도록 함
        if btn_retrieval['state'] == DISABLED :
            result = msgbox.askquestion("선택" , f"[마진율 {main_condition_price_box1_entry.get()}%]입니다.\n전체 상품을 샵플링에 등록(수정) 진행하시겠습니까?")
            if result == "yes" :
                magin_rate = main_condition_price_box1_entry.get() # 마진율 적용
                ad.getting_margin_rate(int(magin_rate))
                url_list1 = geting_url_list()
                if len(url_list1) == 0 :
                    msgbox.showerror('오류','물품 수집을 수행해주세요.')
                for idx,url in enumerate(url_list1) :
                    # 샵플링 등록 및 그 결과를 리턴 받음 
                    making_result = ad.making_things(url,main_save_information_box1_entry.get(),main_save_information_box2_entry.get(),main_save_information_box3_entry.get())
                    changing_things(making_result)
                    progress = (idx + 1) / len(url_list1) * 100 #percent 계산식
                    main_progress_Var.set(progress)
                    main_progress_box.update()
        #인증키 검사가 완료 X
        else :
            msgbox.showinfo('오류','올바른 인증키 입력후 인증키 검사 버튼을 눌려주세요.')

# 리스트 변화를 위한 함수 
def changing_things(making_result) :
    working_url = making_result[1]
    msg = making_result[0]
    x=main_list_pricey_list.get_children()
    for child in x :
        values =main_list_pricey_list.item(child, 'values')
        if values[5] == working_url :
            find_one = child
            text_thing = main_list_pricey_list.item(child,'text')
            break
    name = values[1]
    price = values[2]
    rate = values[3]
    rate_cnt = values[4]
    if msg[0] == "등록정상" or msg[0] == "수정정상" :
        enrolling = "성공"
        main_list_pricey_list.tag_configure("tag2", foreground="blue")
        main_list_pricey_list.item(find_one,text = text_thing ,values=(enrolling,name,price,rate,rate_cnt,working_url),tags="tag2")
    else :
        enrolling = "실패"
        main_list_pricey_list.tag_configure("tag3", foreground="red")
        main_list_pricey_list.item(find_one,text = text_thing ,values=(enrolling,name,price,rate,rate_cnt,working_url),tags="tag3")
    
    #root update 없이는 변화 반영 안됨 
    root.update()

# main 즉 gui 시작 부분  
if __name__ == '__main__':
    #변수
    count=1

    #배경색
    bg='#F0F0F0'

    Bg_top=bg

    bg_left_box=bg
    bg_left_top=bg
    bg_left_bottom=bg

    bg_right_box=bg
    bg_right_mid1=bg
    bg_right_mid2=bg
    bg_right_mid3=bg
    bg_right_bottom=bg
    #
    tta=True
    tta_op=False
    Shopping_mall_name="쇼핑몰 선택"

    #메뉴 파일
    menu_file = Menu(menu, tearoff=0)
    menu_file.add_command(label="불러오기",state="disable")# 비활성화
    menu_file.add_command(label="저장",state="disable")# 비활성화
    menu_file.add_separator()
    menu_file.add_command(label="사용 종료",command=root.quit)
    menu.add_cascade(label="파일", menu=menu_file)

    # 메뉴 내비게이션바 편집
    menu.add_cascade(label="편집")

    menu_lang = Menu(menu, tearoff=0)
    menu_lang.add_command(label="한국어")
    menu_lang.add_command(label="일본어")
    menu.add_cascade(label="언어", menu=menu_lang)

    #메뉴 내비게이션바 옵션
    menu.add_cascade(label="옵션")

    #메뉴 내비게이션바 도움말
    helpmenu =Menu(menu, tearoff=0)
    helpmenu.add_command(label="이 프로그램은 FHD 환경에 최적화 되어 있습니다." )
    helpmenu.add_command(label="안내" ,command= things_information)
    menu.add_cascade(label="도움말",menu=helpmenu)

    #메뉴 내비게이션바 쇼핑몰 링크 
    top_ling=Frame(root,bg=Bg_top)
    top_ling.pack(fill="x")

    #쇼핑몰 이미지
    img='img'
    img_file=os.listdir(img)# 쇼핑몰 박스 내용

    Shopping_photo=[]

    for pt in range(9):
        Shopping_photo.append(PhotoImage(file="img/"+img_file[pt]))
    #photo_btnt.append(Button(top_ling, image=Shopping_photo[pt],command=quit).pack(side="left",padx=15))

    #쿠팡
    Shopping_photo1=Button(top_ling, image=Shopping_photo[0],command= Shopping_ling)    
    Shopping_photo1.pack(side="left",padx=10, pady=10)

    #옥션
    Shopping_photo2=Button(top_ling, image=Shopping_photo[1])    
    Shopping_photo2.pack(side="left",padx=10, pady=10)

    #gmarket
    Shopping_photo3=Button(top_ling, image=Shopping_photo[2])    
    Shopping_photo3.pack(side="left",padx=10, pady=10)


    Shopping_photo4=Button(top_ling, image=Shopping_photo[3])    
    Shopping_photo4.pack(side="left",padx=10, pady=10)

    Shopping_photo5=Button(top_ling, image=Shopping_photo[4])    
    Shopping_photo5.pack(side="left",padx=10, pady=10)

    Shopping_photo6=Button(top_ling, image=Shopping_photo[5])    
    Shopping_photo6.pack(side="left",padx=10, pady=10)

    Shopping_photo7=Button(top_ling, image=Shopping_photo[6])    
    Shopping_photo7.pack(side="left",padx=10, pady=10)

    Shopping_photo8=Button(top_ling, image=Shopping_photo[7])    
    Shopping_photo8.pack(side="left",padx=10, pady=10)

    Shopping_photo9=Button(top_ling, image=Shopping_photo[8])    
    Shopping_photo9.pack(side="left",padx=10, pady=10)

    #쿠팡 이외의 사이트는 GUI상에서만 존재 구현 되지 않음

    #api 정보 체크
    main_save_information = LabelFrame(root, bg = Bg_top, text = '샵플링 인증 정보 입력')
    main_save_information.pack(fill="x",padx=15, pady=5)

    # 샵플링 로그인 id
    main_save_information_txt1_Label = Label(main_save_information, text="샵플링 로그인 id :",bg=bg_left_top)
    main_save_information_txt1_Label.pack( padx=5, pady=5,side="left")
    main_save_information_box1_entry = Entry(main_save_information,  width=25)
    main_save_information_box1_entry.pack(fill = "x" ,side="left")

    # company id
    main_save_information_txt2_Label = Label(main_save_information, text="company id :",bg=bg_left_top) 
    main_save_information_txt2_Label.pack( padx=5, pady=5,side="left")
    main_save_information_box2_entry = Entry(main_save_information,  width=25)
    main_save_information_box2_entry.pack(fill = "x" ,side="left")
        
    # api_key
    main_save_information_txt3_Label = Label(main_save_information, text="api_auth_key :",bg=bg_left_top) 
    main_save_information_txt3_Label.pack( padx=5, pady=5,side="left")
    main_save_information_box3_entry = Entry(main_save_information,  width=25)
    main_save_information_box3_entry.pack(fill = "x" ,side="left")

    btn_retrieval = Button(main_save_information, padx=3, pady=3, width=10, text="인증키 검사",bg="#5E5E5E",fg="white") #검색 버튼
    btn_retrieval.pack(side="right")
    btn_retrieval.bind('<Button-1>',checking_api)

   #main_label
    main_Label = LabelFrame(root,bg=bg_right_box)
    main_Label.pack(fill="both",side="right", padx=5, pady=5 , expand=True)

    #상세조건 레이블
    main_condition_Label= LabelFrame(main_Label, text="상세조건",bg=bg_left_top) 
    main_condition_Label.pack(padx=5, pady=5,fill="x" )

    #URL Label 사용함
    main_condition_key_URL_Label =Label(main_condition_Label, text="U  R  L :",bg=bg_left_top)
    main_condition_key_URL_Label.pack( padx=5, pady=5,side="left",fill="x")

    #URL 검색박스
    main_condition_key_box_Label = Entry(main_condition_Label,  width=150)
    main_condition_key_box_Label.pack(padx=5,pady=5,side="left")
    main_condition_key_box_Label.insert(0, Kin_URL)

    #키워드 박스2
    main_condition_key2_Label = LabelFrame(main_condition_Label,bg=bg_left_top)
    main_condition_key2_Label.pack(fill="both",side="left")

    #상품 리스트 레이블
    main_list_Label=LabelFrame(main_Label,bg=bg_left_bottom)
    main_list_Label.pack(padx=5,fill="x")

    #상품 리스트 상단
    main_list_top_Label=LabelFrame(main_list_Label,bg=bg_left_bottom)
    main_list_top_Label.pack(padx=5,fill="both")

    #리스트 상품 삭제
    #리스트 항목 전체 삭제
    main_list_all_del_buttonl=Button(main_list_top_Label, text="리스트 항목 전체 삭제", padx=10, pady=5,bg="red",fg="white")
    main_list_all_del_buttonl.pack(side="right",padx=15, pady=10)
    main_list_all_del_buttonl.bind("<Button-1>",main_list_all_del)

    #리스트 항목 선택 삭제
    main_list_selection_del_buttonl=Button(main_list_top_Label, text="리스트 항목 선택 삭제", padx=10, pady=5,bg="red",fg="white")
    main_list_selection_del_buttonl.pack(side="right",padx=15, pady=10)
    main_list_selection_del_buttonl.bind("<Button-1>",main_list_top_del)

    #리스트 상품 수집
    main_list_top_registration_buttonl=Button(main_list_top_Label, text="수집", padx=15, pady=5,bg="#1A699A",fg="white",command= Refresh)
    main_list_top_registration_buttonl.pack(side="right",padx=15, pady=10 )


    #페이지
    main_list_top_values= ["1","2","3","4","5","6","7","8","9"] # 페이지 내용
    main_list_topl_Combobox = ttk.Combobox(main_list_top_Label,  width=10, values=main_list_top_values)
    main_list_topl_Combobox.set("현재 페이지")
    main_list_topl_Combobox.pack(side="right", padx=5)
    main_list_topl_Combobox.bind("<<ComboboxSelected>>",main_list_top)

    #상품 리스트
    main_list_top_labe1_inform_Label = LabelFrame(main_list_Label)
    main_list_top_labe1_inform_Label.pack(fill="both",padx=5 )

     #상품 레이블
    main_list_pricey_Label =LabelFrame(main_list_Label,bg=bg_left_bottom)
    main_list_pricey_Label.pack(fill="both",padx=5 )

    #리스트 스크롤 바

    #x축
    main_list_pricey_scrollbar1= Scrollbar(main_list_pricey_Label, orient=HORIZONTAL)
    main_list_pricey_scrollbar1.pack(side="bottom", fill="x")
    #y축
    main_list_pricey_scrollbar= Scrollbar(main_list_pricey_Label)
    main_list_pricey_scrollbar.pack(side="right", fill="y")

    #리스트
    main_list_pricey_list =ttk.Treeview(main_list_pricey_Label,selectmode="extended", height=19, xscrollcommand=main_list_pricey_scrollbar1.set,
    yscrollcommand=main_list_pricey_scrollbar.set)
    
    #리스트 스타일 처리
    style =ttk.Style()
    #Pick a theme
    style.theme_use("default")
    #Configure our treeview colors
    style.configure("Treeview",
            background="#ffffff",
            foreground="black",
            rowheigt=25,
            fieldbackground="#ffffff"
            )
    style.map('Treeview', 
        background=[('selected', '#64A4FA')])

    #리스트 열 설정
    main_list_pricey_list['columns'] = ("enrolling","Name","price","rate","rate_cnt","url")

    #리스트 열 서식
    main_list_pricey_list.column("#0",width=15,minwidth=50)#타이틀,크기,최소사이즈
    main_list_pricey_list.column("enrolling",width=15)
    main_list_pricey_list.column("Name",width=200,anchor=W,minwidth=50)#이름,정렬
    main_list_pricey_list.column("price",width=15)
    main_list_pricey_list.column("rate",width=15)
    main_list_pricey_list.column("rate_cnt",width=15)
    main_list_pricey_list.column("url",width=200,anchor=W,minwidth=50)#이름,정렬

    #리스트 제목
    main_list_pricey_list.heading("#0",text="번호", command = getting_order_count)
    main_list_pricey_list.heading("enrolling",text="등록여부", command = getting_order_enroll)
    main_list_pricey_list.heading("Name",text="상품명",anchor=CENTER, command = getting_order_name)
    main_list_pricey_list.heading("price",text="가격", command = getting_order_price)
    main_list_pricey_list.heading("rate",text="별점", command = getting_order_star)
    main_list_pricey_list.heading("rate_cnt",text="리뷰수",command = getting_order_review)
    main_list_pricey_list.heading("url",text="URL",anchor=CENTER)

    #테그

    main_list_pricey_list.bind("<Double-1>",aa)
    
    #리스트 스크롤바 연결
    main_list_pricey_list.pack( fill="both")
    main_list_pricey_scrollbar1.config(command=main_list_pricey_list.xview)
    main_list_pricey_scrollbar.config(command=main_list_pricey_list.yview)

    #샵플링 등록 관련 내용
    main_save_Labeld = LabelFrame(main_Label,bg=bg_right_bottom)
    main_save_Labeld.pack(fill="both",side="top", padx=5, pady=5 )

    #샵플링 전체 상품 등록
    main_save_Labeld_saveBtn1 = Button(main_save_Labeld, padx=10, pady=5,bg="#1A699A",fg="white",text="샵플링 전체 등록")
    main_save_Labeld_saveBtn1.pack(fill="both",side="right",padx=10, pady=10)
    main_save_Labeld_saveBtn1.bind('<Button-1>',click_shopling_save_all)

    #샵플링 선택 상품 등록
    main_save_Labeld_saveBtn2 = Button(main_save_Labeld, padx=10, pady=5,bg="#8DB783",fg="white",text="샵플링 선택 등록")
    main_save_Labeld_saveBtn2.pack(fill="both",side="right", pady=10)
    main_save_Labeld_saveBtn2.bind('<Button-1>',click_shopling_save)
    
    
    #마진율 레이블
    main_condition_price_txet2_Label= Label( main_save_Labeld, text="%",bg=bg_left_top)
    main_condition_price_txet2_Label.pack( padx=8, pady=5,side="right")
    main_condition_price_box1_entry = Entry(main_save_Labeld,  width=15)
    main_condition_price_box1_entry.pack(side="right",padx=5)
    main_condition_price_txet1_Label = Label(main_save_Labeld, text="마진율 :",bg=bg_left_top, fg = 'red')
    main_condition_price_txet1_Label.pack( padx=5, pady=5,side="right")

    #진행 상황
    main_progress_Label = LabelFrame(main_Label, text="진행 상황",bg=bg_right_mid3)
    main_progress_Label.pack(fill="both",side="top", padx=5, pady=5 )
    main_progress_Var = DoubleVar()
    main_progress_box= ttk.Progressbar(main_progress_Label, maximum=100, variable=main_progress_Var)
    main_progress_box.pack(fill="x", padx=5, pady=5)

    #root 관련 내용
    root.config(menu=menu)
    root.resizable(True,True)
    root.mainloop()