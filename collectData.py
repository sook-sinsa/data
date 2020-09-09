import time
import openpyxl

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from urllib.request import urlretrieve
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

###################################################################################

start = time.time()
imgNum = 0  # 0-449, 각 페이지에서 총 450개 수집
urlCode = [[1001, 1010, 1011, 1002, 1003, 1005, 1004, 1006, 1008],
            [2022, 2001, 2002, 2017, 2003, 2020, 2019, 2006, 2018, 2004, 2008, 2007, 2009, 2013, 2012, 2016, 2021, 2014, 2015],
            [20006, 20007, 20008, 20002],
            [3002, 3007, 3008, 3004, 3009, 3005, 3006],
            [22001, 22002, 22003]]  # 세부 카테고리 별 url #

bigCategory = int(input("Input Big Category Number(0-4) : "))
smallCategory = int(input("Input Small Category Number : "))

if bigCategory > 4 or bigCategory < 0:
    print("Wrong big #")
    exit()
else:
    if smallCategory >= len(urlCode[bigCategory]) or smallCategory < 0:
        print("Wrong small #")
        exit()
    else:
        urlNum = urlCode[bigCategory][smallCategory]
        if bigCategory == 0 or bigCategory == 1 or bigCategory == 3:
            url = "https://store.musinsa.com/app/items/lists/00"+str(urlCode[bigCategory][smallCategory])+"/"
        else:
            url = "https://store.musinsa.com/app/items/lists/0"+str(urlCode[bigCategory][smallCategory])+"/"

# container : div.list-box.box > ul > li
# image : div.list_img > a > img (src)
# detailUrl : div.list_img > a (href)
# brand : div.article_info > p.item_title > a
# product : p.list_info > a
# price : p.price ( string -> int 필요 )

###################################################################################

try:
    wb = openpyxl.load_workbook("collected/datasheet.xlsx")
    sheet = wb.active
    print("불러오기 완료")

except:
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.append(["대 카테고리", "세부 카테고리", "브랜드 명", "제품 명", "가격", "상세 주소"])
    print("새로 파일을 만들었습니다")

# options = webdriver.ChromeOptions()
# options.add_argument("headless")
# driver = webdriver.Chrome("/chromedriver", options=options)
driver = webdriver.Chrome("./chromedriver")

###################################################################################

for page in range(1, 6) :
    driver.get(url+str(page))
    time.sleep(10)

    container = driver.find_elements_by_css_selector("div.list-box.box > ul > li")

    for c in container :
        time.sleep(1)

        brand = c.find_element_by_css_selector("div.article_info > p.item_title > a").text.strip()
        product = c.find_element_by_css_selector("p.list_info > a").text.strip()
        price = c.find_element_by_css_selector("p.price").text.strip().replace(",", "").replace("원", "")
        priceIdx = price.find(" ")
        price = int(price[priceIdx+1:])
        detailUrl = c.find_element_by_css_selector("div.list_img > a").get_attribute("href")

        imgSrc = c.find_element_by_css_selector("div.list_img > a > img").get_attribute("src")
        urlretrieve(imgSrc, 'collected/image/' + str(bigCategory) + '/' + str(smallCategory) + '/' + str(imgNum) + '.png')

        print(priceIdx)
        print(brand, product, price, detailUrl, sep=" / ")

        sheet.append([bigCategory, smallCategory, brand, product, price, detailUrl])
        imgNum += 1

        if imgNum == 5 :
            break
    if page == 1 :
        break

###################################################################################

end = time.time()
print("time: ", end-start)

wb.save("collected/datasheet.xlsx")
driver.close()
