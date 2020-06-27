from Scrap import Scrap_PageNo, Scrap_Content, GetTitleList, GetPriceList, ExtendInfo
from Save import save_to_file

lastPage = Scrap_PageNo()

contentList = Scrap_Content(lastPage)

titleList = GetTitleList(contentList)

priceList = GetPriceList(contentList)

info = ExtendInfo(titleList, priceList)

save_to_file(info)