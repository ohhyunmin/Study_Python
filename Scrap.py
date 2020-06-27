import requests
from bs4 import BeautifulSoup

SCRAP_URL = "https://search.shopping.naver.com/search/all?frm=NVSHATC&pagingSize=50&productSet=total&query=%EB%82%98%EB%B9%84&sort=rel&timestamp=&viewType=list"

def Scrap_PageNo():
  request = requests.get(SCRAP_URL)
  soup = BeautifulSoup(request.text,"html.parser")

  pagination = soup.find("div",{"class":"pagination_num__-IkyP"})

  pages = pagination.find_all("a")
  pageNo = []
  for page in pages:
    pageNo.append(int (page.text))
  
  maxPage = pageNo[-1]
  return maxPage

def Scrap_Content(lastPage):
  contentList = []
  for page in range(0, lastPage):
    request = requests.get(f"{SCRAP_URL}&pagingIndex={page}")
    soup = BeautifulSoup(request.text,"html.parser")
    contentList.append(soup.find("ul",{ "class":"list_basis"}))

  return contentList
  
def GetTitleList(pContentList):
  titleClass = []
  for content in pContentList:
    titleClass.append(content.find_all("div", {"class":"basicList_title__3P9Q7"}))

  titleList = []
  for divTitle in titleClass:
    for title in divTitle:
      titleList.append(title.find("a")["title"])
  
  return titleList

def GetPriceList(pContentList):
  priceClass = []
  for content in pContentList:
    priceClass.append(content.find_all("div", {"class":"basicList_price_area__1UXXR"}))

  priceClassList = []
  for divPrice in priceClass:
    priceClassList.append(divPrice)
  
  priceList = []
  for priceClass in priceClassList:
    for price in priceClass:
      priceList.append(price.find("span").text)
  return priceList
       
info = []
def ExtendInfo(pTitleList, pPriceList):
  for listNo in range(0, len(pTitleList)):
    info.append({
    'TITLE':pTitleList[listNo],
    'PRICE':pPriceList[listNo]
  })

  return info