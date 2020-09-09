import time
import openpyxl

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from urllib.request import urlretrieve
import ssl
ssl._create_default_https_context =ssl._create_unverified_context

##############################################################################################################################

start = time.time()
imgNum = 0  # 0-449, 각 페이지에서 총 450개 수집
urlCode = [[1001, 1010, 1011, 1002, 1003, 1005, 1004, 1006, 1008],
            [2022, 2001, 2002, 2017, 2003, 2020, 2019, 2006, 2018, 2004, 2008, 2007, 2009, 2013, 2012, 2016, 2021, 2014, 2015],
            [20006, 20007, 20008, 20002],
            [3002, 3007, 3008, 3004, 3009, 3005, 3006],
            [22001, 22002, 22003]]  # 세부 카테고리 별 url #

# container : div.list-box.box > ul > li
# image : div.list_img > a > img (src)
# detailUrl : div.list_img > a (href)
# brand : div.article_info > p.item_title > a
# product : p.list_info > a
# price : p.price ( string -> int 필요 )

wb = openpyxl.Workbook()
sheet = wb.active
sheet.append(["대 카테고리", "세부 카테고리", "브랜드 명", "제품 명", "가격", "상세 주소"])

driver = webdriver.Chrome("./chromedriver")

end = time.time()
print("time: ", end-start)

wb.save("collected/datasheet.xlsx")
driver.close()
