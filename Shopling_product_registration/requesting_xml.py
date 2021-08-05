"""
수집 된 정보를 이용하여 xml 파일 생성

lxml 를 이용하여 etree 구조로 xml 생성

만들어진 xml을 almost_done.py로 전송함 

test_api () 
<?xml version="1.0" encoding="UTF-8"?>
<reqst>
   <apiQnaReplyReg>
    <login_id><![CDATA[shoppling]]></login_id>
    <company_id>S001</company_id>
    <api_auth_key>fgsddfgfkdgdkfgk</api_auth_key>
    <qnaReplyInfo>
       <qna_key>105987</qna_key>
       <reply><![CDATA[해당 상품은 품절되었습니다.]]></reply>
    </qnaReplyInfo>
    <qnaReplyInfo>
       <qna_key>105986</qna_key>
       <reply><![CDATA[해당 상품은 3일 후에 배송예정입니다.]]></reply>
    </qnaReplyInfo>
  </apiQnaReplyReg>
</reqst>

데이터 
<?xml version="1.0" encoding="UTF-8"?>
<reqst>
   <apiProdMdy>
    <login_id><![CDATA[shoppling]]></login_id>
    <company_id>S001</company_id>
    <api_auth_key>fgsddfgfkdgdkfgk</api_auth_key>

    <goodsInfo>
      <goods_key>100051</goods_key>
      <ptn_goods_cd><![CDATA[A1000045]]></ptn_goods_cd>
      <prod_tp><![CDATA[A]]></prod_tp>
      <prod_nm><![CDATA[수정상품명]]></prod_nm>
      <org_price><![CDATA[45000]]></org_price>
      <sale_price><![CDATA[60000]]></sale_price>
      <list_price><![CDATA[80000]]></list_price>
      <tax_tp><![CDATA[A]]></tax_tp>
      <sex_tp><![CDATA[해당없음]]></sex_tp>
      <sale_area><![CDATA[수도권]]></sale_area>
      <sale_status><![CDATA[B]]></sale_status>
      <origin_nm><![CDATA[국산]]></origin_nm>
      <dtl_desc><![CDATA[상세설명]]></dtl_desc>
      <img_0><![CDATA[http://img.aaa.co.kr/aaa.jpg]]></img_0>
      <img_19><![CDATA[http://img.aaa.co.kr/aaa.jpg]]></img_19>

      <options>
         <optList>
            <title><![CDATA[색상]]></title>
            <value><![CDATA[파랑,검정]]></value>
         </optList>
         <optList>
            <title><![CDATA[사이즈]]></title>
            <value><![CDATA[대,중,소]]></value>
         </optList>
         <optStatus>B,B,B,B,B,B</optStatus>
         <optQty>50,51,52,53,54,55</optQty>
         <optVrtlQty>500,500,500,500,500,500</optVrtlQty>
         <optAmt>2500,2000,2500,3000,5000,5000</optAmt>
      </options>

      <goodsAttri>
         <attriList>
            <code><![CDATA[03]]></code>
            <a002><![CDATA[3일]]></a002>
            <a003><![CDATA[파랑색과 검정색]]></a003>
            <a005><![CDATA[행복물산 / 국산]]></a005>
            <a006><![CDATA[대한민국]]></a006>
            <a009><![CDATA[상세설명참조]]></a009>
            <a010><![CDATA[AS번호 : 080-000-0000]]></a010>
            <a011><![CDATA[비뚤어짜기 금지]]></a011>
            <a012><![CDATA[상세설명참조]]></a012>
            <a013><![CDATA[소가죽]]></a013>
            <a014><![CDATA[가로30cm, 세로20cm]]></a014>
         </attriList>
      </goodsAttri>
    </goodsInfo>

    <goodsInfo>
      <goods_key>100052</goods_key>
      <ptn_goods_cd><![CDATA[A1000046]]></ptn_goods_cd>
      <prod_tp><![CDATA[A]]></prod_tp>
      <prod_nm><![CDATA[수정상품명]]></prod_nm>
      <org_price><![CDATA[45000]]></org_price>
      <sale_price><![CDATA[60000]]></sale_price>
      <list_price><![CDATA[80000]]></list_price>
      <tax_tp><![CDATA[A]]></tax_tp>
      <sex_tp><![CDATA[해당없음]]></sex_tp>
      <sale_area><![CDATA[수도권]]></sale_area>
      <sale_status><![CDATA[B]]></sale_status>
      <origin_nm><![CDATA[국산]]></origin_nm>
      <dtl_desc><![CDATA[상세설명]]></dtl_desc>
      <img_0><![CDATA[http://img.aaa.co.kr/aaa.jpg]]></img_0>
      <img_19><![CDATA[http://img.aaa.co.kr/aaa.jpg]]></img_19>

      <options>
         <optList>
            <title><![CDATA[색상]]></title>
            <value><![CDATA[파랑,검정]]></value>
         </optList>
         <optList>
            <title><![CDATA[사이즈]]></title>
            <value><![CDATA[대,중,소]]></value>
         </optList>
         <optStatus>B,B,B,B,B,B</optStatus>
         <optQty>50,51,52,53,54,55</optQty>
         <optVrtlQty>500,500,500,500,500,500</optVrtlQty>
         <optAmt>2500,2000,2500,3000,5000,5000</optAmt>
      </options>

      <goodsAttri>
         <attriList>
            <code>03</code>
            <a002><![CDATA[3일]]></a002>
            <a003><![CDATA[파랑색과 검정색]]></a003>
            <a005><![CDATA[행복물산 / 국산]]></a005>
            <a006><![CDATA[대한민국]]></a006>
            <a009><![CDATA[상세설명참조]]></a009>
            <a010><![CDATA[AS번호 : 080-000-0000]]></a010>
            <a011><![CDATA[비뚤어짜기 금지]]></a011>
            <a012><![CDATA[상세설명참조]]></a012>
            <a013><![CDATA[소가죽]]></a013>
            <a014><![CDATA[가로30cm, 세로20cm]]></a014>
         </attriList>
      </goodsAttri>
    </goodsInfo>

  </apiProdMdy>
</reqst>

etree를 사용해야 CDATA를 쉽게 처리 가능함 
"""

from lxml import etree
import requests
from datetime import date,timedelta
global count 
count = 0
def get_root() : # make the root

    root = etree.Element("reqst")
    return root

# 샵플링 api 정보가 제대로 들어갔는지 확인 위한 xml 파일 생성을 위한 node_api
def making_test_api(root,shopling_id,company_id,api_auth_key) : # make node_api
    
    test_node_api = etree.Element("apiQnaGather")
    login_id = etree.Element("login_id")
    login_id.text = etree.CDATA(shopling_id)
    test_node_api.append(login_id)
    etree.SubElement(test_node_api,"company_id").text = f'{company_id}'
    etree.SubElement(test_node_api,"api_auth_key").text = f'{api_auth_key}'
    yesterday = date.today() - timedelta(1)
    start_dt = str(yesterday.strftime("%Y%m%d"))
    etree.SubElement(test_node_api,"start_dt").text = f'{start_dt}'
    end_dt = str(date.today().strftime("%Y%m%d"))
    etree.SubElement(test_node_api,"end_dt").text = f'{end_dt}'
    qna_fields = etree.SubElement(test_node_api,"qna_fields")
    qna_fields.text = etree.CDATA("qna_key")

    root.append(test_node_api)
    return root

# api를 정보를 보낼 함수 
def sending_test_api(root) :
    #make xml
    tree = etree.ElementTree(root)

    datas = etree.tostring(tree,encoding='utf-8', xml_declaration=True)
       
    url ='http://api.shopling.co.kr/qna/qna_gather_api.phtml?mode=2'
    
    # datas를 url 로 전송
    try :
        reponse = requests.post(url, data =  datas) #geting respon
        return reponse.text
    
    # timeout 오류 나게 되면 처리  
    except requests.exceptions.Timeout:
        timeoutMessage = "Time out"
        return timeoutMessage
    

#node_api를 만드는 함수 
def making_node_api(root,shopling_id,company_id,api_auth_key) : # make node_api
    node_api = etree.Element("apiProdMdy")
    login_id = etree.SubElement(node_api,"login_id")
    login_id.text = etree.CDATA(shopling_id)
    etree.SubElement(node_api,"company_id").text = f'{company_id}'
    etree.SubElement(node_api,"api_auth_key").text = f'{api_auth_key}'
    root.append(node_api)

    return node_api


def setting_goods_info(node_api,category_finish,
products_title,orgin_price,sale_price,Onsale,
orgin_nm,maker_nm,es,dict,div_code,attr_list,ptn_goods_cd,url,sale_price2,options_value) : # goods_info 이거 반복 가능
    
    node_goodsInfo = etree.Element("goodsInfo")
    etree.SubElement(node_goodsInfo,"goods_key").text = ''#f"{goods_key}" # goods_key를 몰라서 처리 X
    etree.SubElement(node_goodsInfo,"mall_cate_all_nm").text = etree.CDATA(category_finish)
    etree.SubElement(node_goodsInfo,"ptn_goods_cd").text = etree.CDATA(ptn_goods_cd)
    etree.SubElement(node_goodsInfo,"prod_tp").text = etree.CDATA("A") #상품
    etree.SubElement(node_goodsInfo,"prod_nm").text = etree.CDATA(products_title) #상품 제목
    etree.SubElement(node_goodsInfo,"org_price").text = etree.CDATA(str(sale_price)) #원가
    etree.SubElement(node_goodsInfo,"sale_price").text = etree.CDATA(str(sale_price2)) #샴플링 판매가
    etree.SubElement(node_goodsInfo,"list_price").text = etree.CDATA(str(orgin_price))#소비자 값
    etree.SubElement(node_goodsInfo,"tax_tp").text = etree.CDATA('A') #f"![CDATA[{tax_tp}]]"
    # 과세 여부는 A로 표시 
    #etree.SubElement(node_goodsInfo,"sex_tp").text = f'<![CDATA[{ad.sex_tp}]]>'#f"![CDATA[{sex_tp}]]"
    # 성별 표시여부는 관계 없어서 처리 X
    etree.SubElement(node_goodsInfo,"sale_status").text = etree.CDATA(Onsale)
    #es[3] 배송비, 배송비가 0이 아니면 착불 
    if es[3] != 0 :
        etree.SubElement(node_goodsInfo,"dlvy_tp").text = etree.CDATA('C')
    # 그외는 배송비가 0이므로 무료로 처리 
    else :
        etree.SubElement(node_goodsInfo,"dlvy_tp").text = etree.CDATA('A')
    #배송비가 있으면 es[3]으로 처리함 
    etree.SubElement(node_goodsInfo,"dlvy_cost").text = etree.CDATA(str(es[3]))
    # 제조국
    etree.SubElement(node_goodsInfo,"origin_nm").text = etree.CDATA(orgin_nm)#f"![CDATA[{}]]"
    # 제조사
    etree.SubElement(node_goodsInfo,"maker_nm").text = etree.CDATA(maker_nm)
    #상세 설명 
    for i in es[2] :
        etree.SubElement(node_goodsInfo,"dtl_desc").text = etree.CDATA(i)
    # 상세 설명 3 에 URL 저장
    etree.SubElement(node_goodsInfo,"dtl_add3_desc").text = etree.CDATA(url)
    img_count = 1
    
    #필수 이미지 image_0, image_19
    etree.SubElement(node_goodsInfo,"img_0").text = etree.CDATA(f"http:{dict['images'][0]['origin']}")
    etree.SubElement(node_goodsInfo,"img_19").text = etree.CDATA(f"http:{dict['images'][0]['origin']}")
    
    #그외는 5개 넘으면 더 이상 넣지 않음 
    for i in dict['images'] :
        if img_count == 5 : 
            break
        etree.SubElement(node_goodsInfo,f"img_{img_count}").text = etree.CDATA(f"http:{i['detailImage']}")
        img_count +=1

    #goodInfo를 추가 
    node_api.append(node_goodsInfo)

    #option 태그 
    options = etree.Element("options")

    if dict['options'] is None : #단품 처리
        optList= etree.Element("optList")
        etree.SubElement(optList,"title").text = etree.CDATA("단품")
        etree.SubElement(optList,"value").text = etree.CDATA("단품")
        options.append(optList)
        
    else : # 그외의 경우
        for i in range(0,len(dict['options']['optionRows'])) :
            optLists = etree.Element("optList")
            etree.SubElement(optLists,"title").text = etree.CDATA(dict['options']['optionRows'][i]['name'])
            option_value = ""
            option_image = ""
            
            for j in dict['options']['optionRows'][i]['attributes']:
                option_value = option_value + str(j['name']) + "," # img가 없는 부분에 처리 할 방법을 찾아야함
                if j['image'] is not None:
                    option_image = option_image + str(j['image']) + ","
                else : 
                    continue 
            etree.SubElement(optLists,"value").text = etree.CDATA(option_value[0:-1])
            if option_image != "" :
                etree.SubElement(optLists,"image").text = etree.CDATA(option_image[0:-1])
            options.append(optLists)
    Cansold = options_value[0]
    etree.SubElement(options,"optStatus").text = Cansold[0:-1]
    optVrtlQty = options_value[3]
    etree.SubElement(options,"optVrtlQty").text = optVrtlQty[0:-1]#f"{canSold[0:-1]}"
    optOrgAmt = options_value[1]
    etree.SubElement(options,"optOrgAmt").text = optOrgAmt[0:-1] # 쿠팡 옵션 차이값
    optAmt = options_value[2]
    etree.SubElement(options,"optAmt").text = optAmt[0:-1] # 샵플링 옵션 차이값
    node_goodsInfo.append(options)

    goodsAttri = etree.Element("goodsAttri")
    attriList = etree.Element("attriList")
    # dive_code 만들기 
    etree.SubElement(attriList,"code").text = etree.CDATA(div_code)
    # 속성 넣기 
    for i in range(0,len(attr_list[0])) :
        etree.SubElement(attriList,f"{attr_list[0][i]}").text = etree.CDATA(attr_list[1][i])
    goodsAttri.append(attriList)
    node_goodsInfo.append(goodsAttri)

#indent xml 순서 정렬
def indent(elem, level=0): 
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

#만들어진 api 전송
def sending_api(root) :
    #make xml
    tree = etree.ElementTree(root)
    # utf-8, xml_declaration=True로 xml 생성 한것을 datas 변수에 저장 
    datas = etree.tostring(tree,encoding='utf-8', xml_declaration=True)
    
    url ='http://api.shopling.co.kr/prod/prod_modify_api2.phtml?mode=2'
   
    # send 
    try :
        reponse = requests.post(url, data = datas) #geting respon
        return reponse.text
    except requests.exceptions.Timeout:
        timeoutMessage = "Time out"
        return timeoutMessage

