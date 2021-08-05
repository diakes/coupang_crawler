"""
	쿠팡 상품 상세정보 관련 파일

	쿠팡 products_id,items_id, vendor_id 총 3개로 1건 조회후
    관련 내용을 result_es 리스트 안에 넣어 almost_done.py(master 파일로) 이동
    
    making_es(products_id,items_id,vendor_id) 
    return 값 result_es;
    result_es [0] -> 필수 고시 정보 제목 ex) 제품명, 생산자 및 소재지 등
    result_es [1] -> 필수 고시 정보 content ex) "칠성사이다" ,"중국" 등 내용
    result_es [2] -> 제품의 상세 정보 
    result_es [3] -> 배송비 정책
    
    making_kategorie(products_id,vendor_id) -> 쿠팡 카테고리 수집
    return  c[5:-1]
    checking_sex(category) -> 성별 정보 카테고리 값을 보고 판별
    return sextp

    making_maker_nm(es) -> 제조자/생산자 찾음

    making_origin_nm(es) -> 제조국/원산지 찾음

	2021-06-14 kdi : 개발

"""
import requests
import re
from bs4 import BeautifulSoup
import json
from setuptools.package_index import HREF
from selenium import webdriver
from openpyxl import load_workbook # 파일 불러오기
from openpyxl import Workbook


def making_es(products_id,items_id,vendor_id) : 
    url1 = f"https://www.coupang.com/vp/products/{products_id}/items/{items_id}/vendoritems/{vendor_id}"
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
    #print(url1)

    res = requests.get(url1, headers=headers)
    res.raise_for_status()
    subdict = json.loads(res.text)
    # with open("ex_book.lxml", "w", encoding="utf8") as f:
    #     f.write(res.text)
    #배송
    
    delivery_fee = str(subdict['returnPolicyVo']['vendorItemDeliveryNotice']['deliveryCharge']).split('<br/>')[0]
    #print("배송기간 : " + str(subdict['returnPolicyVo']['vendorItemDeliveryNotice']['shippingPeriod']))
    if delivery_fee == "무료배송" :
        delivery_fee = 0
    else :
        delivery_fee = delivery_fee.split("원")[0]
        delivery_fee = delivery_fee.replace(",","")
    
    #essentials(필수 표기 정보)
    #title
    es = list()
    for b in subdict ['essentials']:
        es.append(b['title'])

    #content
    es_con = list()
    for b in subdict ['essentials']:
        es_con.append(b['description'])
    #print(es)

    #details
    #es_detail = making_detials(subdict)
    es_detail = list()
    set_div=""
    saving_div = ""
    a = "<div class=\"detail-item\">"
    if len(subdict['details']) == 1 :
        if subdict['details'][0]['vendorItemContentDescriptions'][0]['detailType'] == 'IMAGE':
            set_div1 ="                        "+"<div class="+"\""+f"{subdict['details'][0]['cssClass']}"+"\""+">"+"\n"+"                                "
            for some in subdict['details'][0]['vendorItemContentDescriptions'] :
                set_div2 ="<div class="+"\""+f"{some['cssClass']}"+"\""+">"+"\n"+"                                            "
                img = "<img src="+"\""+f"{some['content']}"+"\""
                onerror= " onerror="+"\""+"this.src='//t1a.coupangcdn.com/thumbnails/remote/622x622/image/coupang/common/no_img_1000_1000.png'" +"\" "
                width = "width="+"\"100%\"" +" alt="+"\"\""+">"+"\n"+"                                "+"</div>"+"\n"+"                        "+"</div>" +"\n"
                set_div = set_div1+ set_div2 + img + onerror + width
                #print(a)
            # print(saving_div)
        else :
            set_div1 ="                        "+"<div class="+"\""+f"{subdict['details'][0]['cssClass']}"+"\""+">"+"\n"+"                                "
            for some in subdict['details'][0]['vendorItemContentDescriptions'] :
                set_div2 ="<div class="+"\""+f"{some['cssClass']}"+"\""+">"+"\n"+"                                            "
                content = f"{some['content']}"+"\n"+"                                "+"</div>"+"\n"+"                        "+"</div>" + "\n"
                set_div = set_div1+ set_div2 + content

        saving_div += set_div 
        a = a + "\n" + saving_div +"                " +"\n"+"                "+"</div>"
    else :
        for c in subdict ['details']:
            if c['vendorItemContentDescriptions'][0]['detailType'] == 'IMAGE':
                set_div1 ="                        "+"<div class="+"\""+f"{c['cssClass']}"+"\""+">"+"\n"+"                                "
                set_div2 ="<div class="+"\""+f"{c['vendorItemContentDescriptions'][0]['cssClass']}"+"\""+">"+"\n"+"                                            "
                img = "<img src="+"\""+f"{c['vendorItemContentDescriptions'][0]['content']}"+"\""
                onerror= " onerror="+"\""+"this.src='//t1a.coupangcdn.com/thumbnails/remote/622x622/image/coupang/common/no_img_1000_1000.png'" +"\" "
                width = "width="+"\"100%\"" +" alt="+"\"\""+">"+"\n"+"                                "+"</div>"+"\n"+"                        "+"</div>" +"\n"
                set_div = set_div1+ set_div2 + img + onerror + width
            else :
                set_div1 ="                        "+"<div class="+"\""+f"{c['cssClass']}"+"\""+">"+"\n"+"                                "
                set_div2 ="<div class="+"\""+f"{c['vendorItemContentDescriptions'][0]['cssClass']}"+"\""+">"+"\n"+"                                            "
                content = f"{c['vendorItemContentDescriptions'][0]['content']}"+"\n"+"                                "+"</div>"+"\n"+"                        "+"</div>" + "\n"
                set_div = set_div1+ set_div2 + content

            saving_div += set_div 
            #print(a)
        # print(saving_div)
        a = a + "\n" + saving_div +"                "+"                "+"</div>"
    #print(a)
    es_detail.append(a)
    #print(es_con)
    result_es = [es,es_con,es_detail,delivery_fee]
    return result_es


#쿠팡 카테고리 수집
def making_kategorie(products_id,vendor_id) :    
    url2 = f"https://www.coupang.com/vp/products/{products_id}/breadcrumb-gnbmenu?&invalidProduct=false&invalidUnknownProduct=false&vendorItemId={vendor_id}&_=1621305025902"
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
    res = requests.get(url2, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    Kategorie= soup.find_all("a", attrs={"class":"breadcrumb-link"})# 카테고리
    i=0
    for Kat in Kategorie:
        Kategorie[i] = Kat.get_text().strip()
        i+=1
    c=""
    for k in Kategorie:
        c=c+k+">"
    return c[5:-1]

#성별 판별 
def checking_sex(category) :
    sex_tp = '해당없음'
    if re.search(r'여성.+?',category, re.S) :
        sex_tp = '여'
    elif re.search(r'여아.+?',category, re.S) :
        sex_tp = '여'
    elif re.search(r'남성.+?',category, re.S) :
        sex_tp = '남'
    elif re.search(r'남아.+?',category, re.S) :
        sex_tp = '남'
    else :
        sex_tp = '해당없음'

    return sex_tp

#제조사/생산자 판별

def making_maker_nm(es) :
    maker_nm = ""
    for i in es[0]:
        #정규식으로 이름 케이스 들이 다양함
        if re.search(r'제조자.+?',i,re.S) :
            maker_nm = es[1][es[0].index(i)]
        elif re.search(r'생산자.+?',i,re.S):
            maker_nm = es[1][es[0].index(i)]
        elif re.search(r'제조업소.+?',i,re.S):
            maker_nm = es[1][es[0].index(i)]
        elif re.search(r'화장품제조업자 및.+?',i,re.S):
            maker_nm = es[1][es[0].index(i)]
    return maker_nm

#제조국/원산지 판별

def making_origin_nm(es) : 
    origin_nm = ""
    #print(es[0])
    for i in es[0]:
        if re.search(r'제조국',i,re.S) :
            origin_nm = es[1][es[0].index(i)]
        elif re.search(r'원산.+?',i,re.S):
            origin_nm = es[1][es[0].index(i)]
    
    #print("원산지 : " + origin_nm)
    if re.search(r'국.+?',origin_nm,re.S) :
        origin_nm = '국산'
    elif re.search(r'대한.+?',origin_nm,re.S) :
        origin_nm = '국산'
    elif re.search(r'한.+?',origin_nm,re.S) :
        origin_nm = '국산'
    else :
        origin_nm = '기타'


    return origin_nm
