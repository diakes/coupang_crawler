"""
옵션 정보 관련 내용 

dict를 almost_done.py에서 넘겨 받아서 
option  관련된 부분 처리

2021-06-18 kdi 개발 

"""
import requests
import re
from bs4 import BeautifulSoup
import json
from setuptools.package_index import HREF
from selenium import webdriver
from openpyxl import load_workbook # 파일 불러오기
from openpyxl import Workbook

# 옵션 수집에 필요한 정보 구현을 위해 필요한것 
def options_request(dict) : 
    result = list() # 가능한 옵션 값들을 저장 할 리스트
    
    # 단품
    if dict['options'] is None :
        result.append("단품")
    #옵션 존재
    else :
        option_save = list()
        # 옵션 1개
        # 옵션 1개에 대한 것을 저장함 
        if len(dict['options']['optionRows']) == 1 :
            for j in dict['options']['optionRows'][0]['attributes']:
                option_save.append(j['valueId'])
            result = option_save
        #옵션 2개 이상
        else :
            #옵션 첫번째 정보 수집후
            for i in range(0,len(dict['options']['optionRows'])) :
                option_save1 = list()
                for j in dict['options']['optionRows'][i]['attributes']:
                    option_save1.append(j['valueId'])
                option_save.append(option_save1)

            # 옵션 두번쨰 이후 것 수집
            for i in range(0,len(option_save)) : # option의 valueId에 저장된 값을 쓴다.
                for j in range(0,len(option_save[i])) : # 옵션이 여러개 존재 할떄를 대비해서 사용함 
                    if i+1 == len(option_save) : # 옵션 마지막 것이 길이를 넘어가는 경우를 방지 하기 위해서 사용
                        break
                    for k in range(0,len(option_save[i+1])) :
                        result.append(option_save[i][j]+":"+option_save[i+1][k])

            # 쿠팡은 옵션 : 옵션으로 개별 옵션으로 구성 

    return result

# 세부적인 옵션 값을 크롤링
def getting_options(dict,result,sale_price,margin_rate,Onsale):
    canSold = "" #옵션별 판매 가능여부
    optOrgAmt = ""
    optAmt = ""
    #사이에 , 가 있는 숫자 값을 일반 숫자로 변형 시킴
    if result[0] == "단품" :
        #Onsale 에서 E 판매 종료된 상품은 팔수 없도록 처리 
        if Onsale == 'E' :
            canSold += "C"+","
        #판매 가능한 여부 판별
        elif str(dict['soldOut']) == 'false' :
            canSold += "B"+","
        else :
            canSold += "C"+","
    # 옵션이 여러개 존재 할때
    #result 에 있는 값을 이용해서 사용 함 
    else :
        for i in range(0,len(result)):
            try :
                if Onsale == 'E' :
                    canSold += "C"+","
                elif dict['options']['attributeVendorItemMap'][result[i]]['soldOut'] == False:
                    canSold += "B"+","
                else :
                    canSold += "C"+","
            except KeyError : # 이건 json 에 존재 하지 않는 경우 즉 품절 혹은 판매 자체 하지 않는 것
                canSold += "C"+","
        for i in range(0,len(result)):
            try : 
                if dict['options']['attributeVendorItemMap'][result[i]]['quantityBase'][0]['price']['salePrice'] is not None : 
                    diff_price = int(dict['options']['attributeVendorItemMap'][result[i]]['quantityBase'][0]['price']['salePrice'].replace(',','')) - sale_price
                else :
                    diff_price = int(dict['options']['attributeVendorItemMap'][result[i]]['quantityBase'][0]['price']['originPrice'].replace(',','')) - sale_price
            except (KeyError,TypeError) : # 이건 json 에 존재 하지 않는 경우 즉 품절 혹은 판매 자체 하지 않는 것
                diff_price = 0
             
            round(diff_price,-2) 
            optOrgAmt += str(diff_price) + ","#추가 금액  
            
            optAmt_price = round(diff_price * margin_rate , -2) #100의 자리까지 반올림
            optAmt_price = int(optAmt_price) # 이후 정수형으로 바꿈 
            optAmt += str(optAmt_price) + ","
    optQty_value = "" #옵션별로 가능한 양
    totalQty = 0
    #CanSold를 이용해서 총 판매 가능한 갯수와 옵션별로 판매 가능한 가상 재고를 넣음 
    for i,value in enumerate(canSold) :
        if value == 'B':
            optQty_value += "999" #옵션별 가능한 판매값을 임의로 저장한 값 
            totalQty += 999
        elif value == 'C' :
            optQty_value += "0"  #품절이기 떄문에 0으로 넣어준다.
            totalQty += 0
        else :
            optQty_value += ","

    # options 즉 옵션에 대한 정보를 리턴 
    options = [canSold,optOrgAmt,optAmt,optQty_value,totalQty]
    
    return options