coupang_crawler
================
국내 최대 오픈 마켓인 쿠팡에 등록된 상품의 정보를 수집 하는 크롤러
Python 라이브러리 Selenium 및 BS4을 이용하여 크롤링 

쿠팡 웹 크롤링 프로그램
--------------------------------------------
### 개발 환경 설정 
<img src = "https://img.shields.io/pypi/pyversions/Beautiful">
	
	pip install selenium
	pip install requests
	pip install Beautifulsoup4
	pip install chromedriver_autoinstaller
	pip install openpyxl
	pip install lxml
-------------------------------------------	

### 사용 버전
- python 3.8.5 - [[Link]](https://www.python.org/downloads/release/python-385/excutalbe)

------------------------------------------

### 메인 실행 파일
- #### Shopling_product_registration.py
coupang 아이콘을 클릭 시 크롬 창 실행 시 성공 

-------------------------------------

### Shopling_registration3 구조

```bash
├── img
│   ├── img1.PNG
│   ├── img2.PNG
│   ├── img3.PNG
│   ├── img4.PNG
│   ├── img5.PNG
│   ├── img6.PNG
│   ├── img7.PNG
│   ├── img8.PNG
│   └── img9.PNG
│
├── Selenium_Function
│   ├── 89
│      └── chormedriver.exe
│   └── open.py
│
├── dist
│   ├── (google_chrome driver file version이 기록됨) ex) 89,90,91
│   ├── img
│   ├── img2
│   ├── shopling.ico
│   └── Shopling_product_registration3.exe
│
├── code
│   ├── Shopling_Product_registration3.py
│   ├── almost_done.py
│   ├── making_essential.py
│   ├── making_goodsAttri.py
│   ├── making_option.py
│   └── requesting_xml.py
│
├── shopling.ico
├── file_verion_info.txt
├── Shopling_product_registration3.spec
└── run.sh
``` 
img 파일
-------------
![image](https://user-images.githubusercontent.com/85141446/123568594-9caabe80-d7ff-11eb-9c96-c41e8f40101f.png)

- 1번 부터 img1.PNG
- 최종적으로 9번이 img9.PNG

Selenium Function
--------------------

### open.py

- open_Shopping class 을 통한 사이트 오픈 

```python
class open_Shopping:
    def retrieval(self):
        
        try:
            shutil.rmtree(r"c:\chrometemp") 
        except FileNotFoundError:
            pass
        #쿠키 / 캐쉬파일 삭제
	 
        try :
            subprocess.Popen(r'C:\Program Files\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\chrometemp"') # 64 bit인 경우
        except FileNotFoundError :
            subprocess.Popen(r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\chrometemp"') #32 bit인 경우
        # Google driver 처리
        
	#port 9222로 실행 
        option = Options()
        option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        option.add_argument("disable-gpu")
        
        chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
        global driver
        try:
	# 기본적으로 옵션이 맞으면 실행
            driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe',options=option)
        except:
            chromedriver_autoinstaller.install(True)#맞는 버전 선택
            driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)
	   # 맞는 버전 directory 생성
	  
        driver.implicitly_wait(10)
	
        driver.set_window_size(940,1050)
	# window 사이즈 설정
        
	driver.set_window_position(-10,0)
        #window 실행 사이즈 선택 
	
        return driver
```
실행 파일 제작
-------------------

#### python pyinstaller 라이브러리 사용

```python
pyinstaller -w -F --icon=shopling.ico --version-file file_version_info.txt Shopling_product_registration3.py
```

이러면 exe 파일이 /dist 파일 밑에 생성되게 됨

dist 파일 밑에 있는 img,img2,shopling.ico은

Shopling_product_registration3.exe 실행에 필수(없으면 실행 안 됨)

참조 

- pyinstaller 오류 없이 실행 하기 https://umnoni.com/18 
- pyinstaller 버전 관리 https://nick2ya.tistory.com/7

버전 관리 
------------------- 
- version 1.0.0.0 - 배포

- version 1.0.0.1 - windows 32bit 버전 google chorme.exe 안 열리는 버그 수정

- version 1.0.0.2 - 리스트 전체 삭제 후 다시 수집한 상품 등록 안되는 버그 수정

- version 1.0.0.3 - 리스트 수집 후 샵플링에 등록 되지 않는 상품이 리스트에서 삭제 안되는 버그 수정


버전 관리 파일
--------------------
file_verion_info.txt 이용

```
# UTF-8
#
VSVersionInfo(
  ffi=FixedFileInfo(
# filevers and prodvers should be always a tuple with four items: (1, 2, 3, 4)
# Set not needed items to zero 0.
filevers=(1, 0, 0, 2),
prodvers=(1, 0, 0, 2),
# Contains a bitmask that specifies the valid bits 'flags'r
mask=0x3f,
# Contains a bitmask that specifies the Boolean attributes of the file.
flags=0x0,
# The operating system for which this file was designed.
# 0x4 - NT and there is no need to change it.
OS=0x4,
# The general type of file.
# 0x1 - the file is an application.
fileType=0x1,
# The function of the file.
# 0x0 - the function is not defined for this fileType
subtype=0x0,
# Creation date and time stamp.
date=(0, 0)
),
  kids=[
StringFileInfo(
  [
  StringTable(
    u'040904B0',
    [StringStruct(u'CompanyName', u''),
    StringStruct(u'FileDescription', u'Shopling_Product_registration3'),
    StringStruct(u'FileVersion', u'1.0.0.2'),
    StringStruct(u'InternalName', u''),
    StringStruct(u'LegalCopyright', u''),
    StringStruct(u'OriginalFilename', u''),
    StringStruct(u'ProductName', u'Shopling_Product_registration3.exe'),
    StringStruct(u'ProductVersion', u'1.0.0.2')])
  ]), 
VarFileInfo([VarStruct(u'Translation', [1033, 1200])])
  ]
)

```

- filevers=(버전명),
- prodvers=(버전명),
- StringStruct(u'FileDescription', u'실행 파일 directory'),
- StringStruct(u'FileVersion', u'버전명')
- StringStruct(u'ProductName', u'실행파일명.exe')
- StringStruct(u'ProductVersion', u'버전명')])

프로그램 구조
--------------------
 
        	Shopling_proudct_registration3.py(최상단)
                        	|
                        	▼
                	almost_done.py(핵심 부위)
                        	|
                       	▼
	making_goodAttri.py,making_essential.py,making_option.py,requesting_xml.py (함수 호출 사용)

Shopling_proudct_registration3.py
-------------------------------

GUI 세팅 부분 , 이벤트 처리 
if __name__ = '__main__' 
여기에서 GUI 세팅을 해줌,
그 외의 부분은 이벤트 처리 함수 부분

almost_done.py
-----------------

샵플링 인증 확인 , 상품 수집 정보, 수집된 상품 전송을 하는 파일

실제 중추적인 역할을 수행하는 파일 

필요한 함수들이 있는 py 파일들을 import 해서 사용함
```python

import making_option as mo
import making_goodsAttri as md
import making_essential as me
import requesting_xml as rx
import xml.etree.ElementTree as elemTree

```

#### 샵플링 인증 확인

```python
# to connect id
def responing_id(shopling_id,company_id,api_auth_key):
    test_root = rx.get_root()
    root = rx.making_test_api(test_root,shopling_id,company_id,api_auth_key) #rx는 requesting_xml -> test_api의 xml을 리턴 받는다.
    text = rx.sending_test_api(root) sending_test_api 보내줌 
    
    return text
```
text는 샵플링에 의해서 리턴 받은 값으로 실패시 기본적으로 "등록 실패"를 리턴

성공할시 샵플링 상품 Q&a 수집 결과를 지정된 xml 형태로 가져 오게 됨

#### 상품 정보 수집 

```python
def making_things(url,shopling_id,company_id,api_auth_key) :
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
	#쿠팡 과 쿠팡에서 제공하는 items_id를 조합해서 사용함

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
```

정규 식을 이용해 가장 첫번째로 나오는 exports.sdp = 뒤에 있는 json 값을 파싱

json 파싱시 dict으로 받아와 원하는 기본 정보들을 수집, 

option관련 부분 - mo.options_request,mo.getting_options 이용 수집

상세 정보, 카테고리, 제조사, 제조국은 me.making_es, me.making_kategorie, me.making_maker_nm, me.making_origin_nm 이용 수집

분류코드, 상세 고시 의무 정보는 md.making_containers, md.making_divcode, md.making_attri, md.making_default_attri 이용 수집

',/이 들어 있는 글자를 전송시 php로 구성된 서버에서 에러 발생  그러므로 수정이 필요, 가장 뒤에 있는 부분이 글자를 수정하는 부분 

#### 등록을 위한 전송 관련 부분
```python
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
```
rx.setting_goods_info에 수집된 정보를 넣어, 그 정보를 가지고 xml 파일 생성

rx.indent(root)를 이용해 사람이 생각하는 xml 파일로 변형

datas = rx.sending_api(root)을 통해서 datas에 리턴값 저장

msg = sending_datas(datas) 이 부분을 통해 성공 실패 여부를 받아와 msg에 저장

return [msg,url]을 통해 Shopling_Product_registration에 결과 리턴 실행 도중 나온 결과를 리스트에 반영 


exe파일 사용 방법 
---------------------

![04](https://user-images.githubusercontent.com/85141446/122140065-40ea4800-ce85-11eb-91eb-9dac354501a9.png)

	1. 쿠팡 버튼 클릭 (쿠팡 창 실행) 방화벽 경고 창 허용

	2. 인증키 검사 수행 (샵플링 로그인 id, company id(고객사 번호) , 샵플링 api 인증키 입력 후 인증키 검사 버튼 클릭)

	3. 쿠팡 팝업 창에서 원하는 상품 검색
	
	4. 원하는 수집  페이지 수 선택 후, 수집 버튼 클릭 

	5. 원하는 마진율 최소 20%이상 입력

	6. 수집된 상품의 선택 or 전체 샵플링 등록 버튼 클릭
 
   ![05](https://user-images.githubusercontent.com/85141446/122140095-56f80880-ce85-11eb-85c1-30df3f72f745.png)
   
   * 가. 원하는 상품 쿠팡 창에서 검색 
   
   * 나. 기본 값으로는 현재 페이지 , 페이지 변경을 원할 시 원하는 페이지 클릭 하여 원하는 페이지 이동
   
   * 다. 페이지 수집 버튼 클릭 시 원하는 페이지 정보가 수집
  
※ 주의 사항
----------------
	1. 실행된 쿠팡 창 종료 시, 프로그램 재 실행 필요 
	
	2. 프로그램을 오래 실행 시 access denied 발생 가능
	
	3. access denied 발생 시 프로그램과 쿠팡 창 종료 후 잠시 대기 후 사용
	
	4. 검색 창이 뜨면 무시하고 진행
	
	5. 페이지 재 수집 후, 샵플링 전체 등록 버튼 클릭 시 샵플링 등록 진행
	
	6. 페이지 번호 선택 시 원하는 페이지 수집
	
	7. 현재 URL은 페이지 번호 1 
	
	8. 실행 하고 쿠팡 버튼을 클릭 시 반응이 없을 시 웹사이트 종료
	
	9. 이상 발생 시 Shopling_product_registration3.exe 종료 후 재실행
