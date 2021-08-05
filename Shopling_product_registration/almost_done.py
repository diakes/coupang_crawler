"""
모든 작업을 수행 하기위한 python 파일

import making_option as mo
import making_goodsAttri as md
import making_essential as me
import requesting_xml as rx

이용해 모든 과정을 함수로 만들어 낸 후 처리 함 

2021.06.18 kdi 개발 

먼저 checking_api
물품 수집은 making_things에서 수집하고 rx로 보내 xml 파일 생성
만들어진 xml 파일 받아와서  sending_api

"""
from tkinter.constants import FALSE, NO
import requests
import re
from bs4 import BeautifulSoup
import json
from setuptools.package_index import HREF
from selenium import webdriver
from openpyxl import load_workbook # 파일 불러오기
from openpyxl import Workbook
import making_option as mo
import making_goodsAttri as md
import making_essential as me
import requesting_xml as rx
import time
import xml.etree.ElementTree as elemTree

# to connect id
def responing_id(shopling_id,company_id,api_auth_key):
    test_root = rx.get_root()
    root = rx.making_test_api(test_root,shopling_id,company_id,api_auth_key)
    text = rx.sending_test_api(root)
    print(text)
    return text

# cacluate margin
def getting_margin_rate(margin): # 마진율 계산 함수
    global margin_rate
    margin_rate = 0
    margin_rate = margin*0.01 + 1

# data를 보내줌 
# 등록 완료 및 수정된 여부를 체크 하기 위해 사용하는 함수
def sending_datas(datas) :

    root = elemTree.fromstring(datas)
    api = root.findall("apiProdMdyRst")
    goodrs = [x.find("goodsRst") for x in api]
    msg = [x.findtext("msg") for x in goodrs]
    
    return msg

#url 정보, 인증키를 받아서 상품 수집하고 api를 만들어 send 하는 함수(제일 중요한 함수)
# 각각의 상품 URL에 접속해 관련 상품을 수집함 
def making_things(url,shopling_id,company_id,api_auth_key) :
    root = rx.get_root()
    node_api = rx.making_node_api(root,shopling_id,company_id,api_auth_key)
    # 각각의 상품 파싱 시작
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
    res = requests.get(url, headers=headers)
    res.raise_for_status()

    item = re.search(r'exports.sdp = (.+?);',res.text, re.S)
    json_str = item.group(1)
    try :
        dict = json.loads(json_str)

        #제품 기본 정보
        #제품 명
        products_title = str(dict['title'])
        #products_id(제품 아이디)
        products_id = str(dict['productId'])
        #items_id(상품 그 자체의 아이디)
        items_id = str(dict['itemId'])
        #vendero_id(생산자 아이디)
        vendor_id = str(dict['vendorItemId'])


        #판매 가능여부
        if str(dict['soldOut']) == 'False' :
            Onsale = 'B'
        else :
            Onsale = 'C'
        
        ptn_goods_cd = "scoupang_"+f"{items_id}" # 샵플링 상품 코드

        # calcaluate cost
        try:
            orgin_price = dict['quantityBase'][0]['price']['originPrice'] #원가
            sale_price = dict['quantityBase'][0]['price']['salePrice']# 쿠팡 판매가 
        # 판매 금액이 없을 시는 판매 종료 된 상품
        # 예외 처리
        except TypeError :
            keys = [key for key in dict['options']['attributeVendorItemMap']]
            Onsale = 'E' 
            sale_price = dict['options']['attributeVendorItemMap'][keys[0]]['quantityBase'][0]['price']['salePrice']
            orgin_price = dict['options']['attributeVendorItemMap'][keys[0]]['quantityBase'][0]['price']['originPrice']
       
         #쿠팡 판매가가 없는 경우는 그대로 원가로 팜
        if sale_price is not None :
            sale_price_int = int(sale_price.replace(',',''))
        else :
            sale_price = orgin_price
            sale_price_int = int(sale_price.replace(',',''))

        #실질적인 판매가 곱하기 마진율
        if sale_price != None :
            sale_price2 = int(sale_price_int * margin_rate) # 샵플링 판매가
        
        # 올림하기 위해 1의 자리가 5보다 적을 떄 올려줌 
        if sale_price2 % 10 < 5 :
            sale_price2 += 5

        # 1번째 자리에서 반올림
        sale_price2 = round(sale_price2,-1)  

        #making not having , in cost
        # 가격에 , 없애 주는 장치 
        orgin_price = sale_price_int
        sale_price = sale_price_int

        #making option
        result = mo.options_request(dict) # 전체 옵션에 대한 조합을 저장한 값
        options_value = mo.getting_options(dict,result,sale_price,margin_rate,Onsale) # 옵션에 대한 정보들을 가져 오는 것

        # about essentials + details + delivery_cost
        es = me.making_es(products_id,items_id,vendor_id) 
        #es 0은 필수 고시내용 제목 es 1은 필수 고시내용 내용 es 2는 detail이 저장되어 있다. es 3는 배송비 저장

        #using essentials
        category = me.making_kategorie(products_id,vendor_id) #카테고리 정보
        category_finish = "SMALL_00012=@"+ category # 쿠팡 카테고리 저장 정보
        maker_nm = me.making_maker_nm(es) #제조자
        orgin_nm = me.making_origin_nm(es) #제조국,생산지,원산지

        # using div_code
        compare_things = md.making_containers() #분류하기 위한 값 저장 list 
        div_code = md.making_divcode(compare_things,es) #분류 코드
        attr_list = md.making_attri(compare_things,div_code,es) # 현재 파악 가능한 상세 정보 리스트(속성코드)
        default_list = md.making_default_attri(compare_things,div_code) # 그외의 부분은 default 값 넣어줌
        print("url : " + url)
        for j in range(0,len(attr_list[0])) :
            i = attr_list[0][j]
            if i in default_list[0] :
                temp_index = default_list[0].index(i) # index를 저장할 temp_index
                default_list[1][temp_index] = attr_list[1][j]

        # making safety in api 
        # ',/ make xml problem
        # so change the things
        maker_nm = maker_nm.replace("'","") 
        maker_nm = maker_nm.replace("\\","")
        products_title = products_title.replace("'","")
        products_title = products_title.replace("\\","")
        category_finish = category_finish.replace("'","") 
        category_finish = category_finish.replace("\\","")
        orgin_nm = orgin_nm.replace("'","")
        orgin_nm = orgin_nm.replace("\\","")

        #상세 정보중 실제 정보를 저장하는 내용이 들어감
        for a in es[1] : 
            a = a.replace("'","")
            a = a.replace("\\","") 
        
        # sending to make a details in api
        
        #품절이 아닌 경우는 등록
        if options_value[4] != 0 :
            rx.setting_goods_info(node_api,category_finish,
            products_title,orgin_price,sale_price,Onsale,
            orgin_nm,maker_nm,es,dict,div_code,default_list,ptn_goods_cd,url,sale_price2,options_value)

        #품절인 경우는 등록 X
        else :
            msg = "wrong"
            return [msg,url]
        
        #xml 인간 친화적으로 변경
         
        rx.indent(root)
        
        #만들어진 xml을 샵플링으로 전송
        datas = rx.sending_api(root)
        #return으로 결과 값을 받음
        
        #return으로 받은 결과 값을 이용해
        #등록 , 수정 등의 성공 실패 여부 리턴
        msg = sending_datas(datas)

    except json.decoder.JSONDecodeError :
        msg = "wrong"
    
    # Shopling 처리 결과 값을 최종 함수로 리턴 
    return [msg,url]
  