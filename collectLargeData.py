import time
import openpyxl

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from urllib.request import urlretrieve
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

###################################################################################

start = time.time()

urlCode = [[1001, 1010, 1011, 1002, 1003, 1005, 1004, 1006, 1008],
            [2022, 2001, 2002, 2017, 2003, 2020, 2019, 2006, 2018, 2004, 2008, 2007, 2009, 2013, 2012, 2016, 2021, 2014, 2015],
            [20006, 20007, 20008, 20002],
            [3002, 3007, 3008, 3004, 3009, 3005, 3006],
            [22001, 22002, 22003]]  # 세부 카테고리 별 url #

categoryList = [["ssleeve", "lsleeve", "nsleeve", "collar", "hood"],
               ["coat", "jacket", "lpadding", "spadding", "vest", "cardigan"],
               ["jsuit", "dress"],
               ["spants", "lpants"],
               ["skirt"]]

productList = [[[0], [1, 5, 7], [2], [3, 4], [6, 0]],
               [[10, 11, 12], [1, 2, 3, 4, 6, 7, 8, 9, 17], [13], [14], [15, 16], [5]],
               [[3], [0, 1, 2]],
               [[4], [0, 1, 2, 3, 5]],
               [[0, 1, 2]]]

productNumList = [[450, 150, 450, 225, 225],
                  [150, 50, 450, 450, 225, 450],
                  [450, 150],
                  [450, 90],
                  [150]]

###################################################################################

bigCategory = int(input("Input Big Category Number(0-4) : "))
smallCategory = int(input("Input Small Category Number : "))
restartCnt = int(input("Where to restart? : "))

if bigCategory > 4 or bigCategory < 0:
    print("Wrong big #")
    exit()
else:
    if smallCategory >= len(categoryList[bigCategory]) or smallCategory < 0:
        print("Wrong small #")
        exit()

###################################################################################

limitCnt = productNumList[bigCategory][smallCategory]
restartProductListNum = restartCnt // limitCnt
restartPage = restartCnt % limitCnt // 90
restartProductCnt = restartCnt % limitCnt % 90

# container : div.list-box.box > ul > li
# image : div.list_img > a > img (src)
# detailUrl : div.list_img > a (href)
# brand : div.article_info > p.item_title > a
# product : p.list_info > a
# price : p.price ( string -> int 필요 )

###################################################################################

options = webdriver.ChromeOptions()
options.add_argument("headless")
driver = webdriver.Chrome("./chromedriver", options=options)

###################################################################################

for i in range(restartProductListNum, len(productList[bigCategory][smallCategory])):

    cnt = 0
    page = 0
    if i == restartProductListNum:
        page = restartPage

    urlNum = urlCode[bigCategory][productList[bigCategory][smallCategory][i]]
    if bigCategory == 0 or bigCategory == 1 or bigCategory == 3:
        if smallCategory == 4 and i == 1:
            url = "https://store.musinsa.com/app/items/lists/002022/"
        else :
            url = "https://store.musinsa.com/app/items/lists/00"+str(urlNum)+"/"
    else:
        url = "https://store.musinsa.com/app/items/lists/0"+str(urlNum)+"/"
    driver.get(url)

    for p in range(page, 6):

        if i == restartProductListNum and p == page:
            cnt = restartProductCnt + restartPage * 90
        if cnt == limitCnt:
            break

        pageBar = driver.find_elements_by_css_selector("div.pagination.bottom > div.wrapper > *")
        nextBtn = pageBar[p + 2]
        driver.execute_script("arguments[0].click();", nextBtn)

        time.sleep(5)
        container = driver.find_elements_by_css_selector("div.list-box.box > ul > li")

        startPoint = 0
        if i == restartProductListNum and p == page:
            startPoint = restartProductCnt

        for c in range(startPoint, len(container)):
            print("=" * 20)
            print("대카테고리: "+str(bigCategory)+" / 소카테고리: "+str(smallCategory)+"/ 품목번호: "+str(limitCnt)+" "+str(i)+" "+str(cnt)+" => "+str(limitCnt*i+cnt))
            time.sleep(1)

            try:
                wb = openpyxl.load_workbook("datasheet.xlsx")
                sheet = wb.active
                print("불러오기 완료")
            except:
                wb = openpyxl.Workbook()
                sheet = wb.active
                sheet.append(["대 카테고리", "세부 카테고리", "제품 번호", "브랜드 명", "제품 명", "가격", "상세 주소"])
                print("새로 파일을 만들었습니다")

            brand = container[c].find_element_by_css_selector("div.article_info > p.item_title > a").text.strip()
            product = container[c].find_element_by_css_selector("p.list_info > a").text.strip()
            price = container[c].find_element_by_css_selector("p.price").text.strip().replace(",", "").replace("원", "")
            priceIdx = price.find(" ")
            if ' ' in price:
                price = int(price[priceIdx + 1:])
            else:
                price = int(price)

            detailUrl = container[c].find_element_by_css_selector("div.list_img > a").get_attribute("href")
            detailDriver = webdriver.Chrome("./chromedriver", options=options)
            detailDriver.get(detailUrl)
            time.sleep(1)
            imgSrc = detailDriver.find_element_by_css_selector("img#bigimg.plus_cursor").get_attribute("src")
            urlretrieve(imgSrc, 'image/'+str(bigCategory)+'/'+str(smallCategory)+'/'+str(limitCnt*i+cnt)+'.png')
            detailDriver.close()

            # imgSrc = c[i].find_element_by_css_selector("div.list_img > a > img").get_attribute("src")
            # urlretrieve(imgSrc, 'image/' + str(bigCategory) + '/' + str(smallCategory) + '/' + str(cnt) + '.png')

            print(brand, product, price, sep=" / ")

            sheet.append([bigCategory, smallCategory, limitCnt*i+cnt, brand, product, price, detailUrl])
            cnt += 1

            wb.save("datasheet.xlsx")

            if cnt == limitCnt:
                break

###################################################################################

end = time.time()
print("time: ", end-start)

driver.close()
