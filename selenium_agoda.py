from selenium.webdriver import Chrome
import time
import requests
from datetime import datetime
from bs4 import BeautifulSoup
import os
import json

resource_path = r'E:\專題\agoda'
if not os.path.exists(resource_path):
    os.mkdir(resource_path)

driver = Chrome('./chromedriver')

# 北部各縣市搜尋網址
url_taipei = 'https://www.agoda.com/zh-tw/search?asq=u2qcKLxwzRU5NDuxJ0kOF8dmq7Ztgl2%2FfOEj7KAaspCTIbIpW83e1VFmJssp8bOXEzrTs7PF4tDRSVBAE1arGohHkxI9jvuYE1HkfyDsP3wyvzhpqnZ39XQafsUKr5aLDTvhW%2FXI5O%2FOPNGClRgpGEhl1cAoVYNrB%2FiHVEE5cv3V%2Fi0y0KRQ5wboBBIWaS5iNHHIKlUAdluuZpieL9PNJw%3D%3D&city=4951&tick=637222427500&languageId=20&userId=55f96f07-2b98-4ab5-bfbc-60d14af2d5a6&sessionId=loyzsspwm0ytkpxcrbnm4qdk&pageTypeId=103&origin=TW&locale=zh-TW&cid=-1&aid=130243&currencyCode=TWD&htmlLanguage=zh-tw&cultureInfoName=zh-TW&memberId=32611396&ckuid=55f96f07-2b98-4ab5-bfbc-60d14af2d5a6&prid=0&checkIn=2020-04-12&checkOut=2020-04-13&rooms=1&adults=2&children=0&priceCur=TWD&los=1&textToSearch=%E5%8F%B0%E5%8C%97%E5%B8%82&productType=-1&travellerType=1&familyMode=off'
url_keelung = 'https://www.agoda.com/zh-tw/search?asq=u2qcKLxwzRU5NDuxJ0kOF5rT4E79GdB8XCNi2zL6G6TPl9oPTUOKmNi0UWoJlvaM0LgSVK8pmZX1%2FEU7tkByuwQOYS3849Ndvqb1bJ1CZlft%2BXyB8OpN1h2WP%2BnBM%2FwNizgaSuFVpMSkebRuVasLYVQ%2F3qMt0vT4DBXU4dF7rHHilpMPlUermwV1UKIKfuyeFI2UM%2BfKqngoERJD%2FAJa%2BA%3D%3D&city=17048&tick=637222352679&languageId=20&userId=55f96f07-2b98-4ab5-bfbc-60d14af2d5a6&sessionId=loyzsspwm0ytkpxcrbnm4qdk&pageTypeId=1&origin=TW&locale=zh-TW&cid=-1&aid=130243&currencyCode=TWD&htmlLanguage=zh-tw&cultureInfoName=zh-TW&memberId=32611396&ckuid=55f96f07-2b98-4ab5-bfbc-60d14af2d5a6&prid=0&checkIn=2020-02-12&checkOut=2020-02-13&rooms=1&adults=2&children=0&priceCur=TWD&los=1&textToSearch=%E5%9F%BA%E9%9A%86%E5%B8%82&travellerType=1&familyMode=off&productType=-1&sort=agodaRecommended'
url_taoyuan = 'https://www.agoda.com/zh-tw/search?asq=u2qcKLxwzRU5NDuxJ0kOFz9MdCPdzde%2Fz6OXwHjbQ8qdk%2F7cv0xAPWRx86BvaOo9EzrTs7PF4tDRSVBAE1arGohHkxI9jvuYE1HkfyDsP3wyvzhpqnZ39XQafsUKr5aLDTvhW%2FXI5O%2FOPNGClRgpGEhl1cAoVYNrB%2FiHVEE5cv3V%2Fi0y0KRQ5wboBBIWaS5iOLZLTAf2SRMlxeUuV7rM7g%3D%3D&city=8453&tick=637222427860&languageId=20&userId=55f96f07-2b98-4ab5-bfbc-60d14af2d5a6&sessionId=loyzsspwm0ytkpxcrbnm4qdk&pageTypeId=103&origin=TW&locale=zh-TW&cid=-1&aid=130243&currencyCode=TWD&htmlLanguage=zh-tw&cultureInfoName=zh-TW&memberId=32611396&ckuid=55f96f07-2b98-4ab5-bfbc-60d14af2d5a6&prid=0&checkIn=2020-04-12&checkOut=2020-04-13&rooms=1&adults=2&children=0&priceCur=TWD&los=1&textToSearch=%E6%A1%83%E5%9C%92%E5%B8%82&productType=-1&travellerType=1&familyMode=off'
url_hsinchu = 'https://www.agoda.com/zh-tw/search?asq=u2qcKLxwzRU5NDuxJ0kOF8ORcEUphkefHpyRX0GKg%2FJypeXaGht5OGeMtyD%2F0W5j0LgSVK8pmZX1%2FEU7tkByuwQOYS3849Ndvqb1bJ1CZlft%2BXyB8OpN1h2WP%2BnBM%2FwNizgaSuFVpMSkebRuVasLYVQ%2F3qMt0vT4DBXU4dF7rHHilpMPlUermwV1UKIKfuyeN1%2F%2BRxJEsIe5fo5YpkFtJA%3D%3D&city=12711&tick=637222428493&languageId=20&userId=55f96f07-2b98-4ab5-bfbc-60d14af2d5a6&sessionId=loyzsspwm0ytkpxcrbnm4qdk&pageTypeId=103&origin=TW&locale=zh-TW&cid=-1&aid=130243&currencyCode=TWD&htmlLanguage=zh-tw&cultureInfoName=zh-TW&memberId=32611396&ckuid=55f96f07-2b98-4ab5-bfbc-60d14af2d5a6&prid=0&checkIn=2020-04-12&checkOut=2020-04-13&rooms=1&adults=2&children=0&priceCur=TWD&los=1&textToSearch=%E6%96%B0%E7%AB%B9%E7%B8%A3&productType=-1&travellerType=1&familyMode=off'
url_yilan = 'https://www.agoda.com/zh-tw/search?asq=u2qcKLxwzRU5NDuxJ0kOF%2BQPSTWnnU2he7kPIKBU02whudZRSNZwodFw5l4muZJj0LgSVK8pmZX1%2FEU7tkByuwQOYS3849Ndvqb1bJ1CZlft%2BXyB8OpN1h2WP%2BnBM%2FwNizgaSuFVpMSkebRuVasLYVQ%2F3qMt0vT4DBXU4dF7rHHilpMPlUermwV1UKIKfuye1wYDtb%2BoWilsfXJMZzLD4Q%3D%3D&city=88773&tick=637222429019&languageId=20&userId=55f96f07-2b98-4ab5-bfbc-60d14af2d5a6&sessionId=loyzsspwm0ytkpxcrbnm4qdk&pageTypeId=103&origin=TW&locale=zh-TW&cid=-1&aid=130243&currencyCode=TWD&htmlLanguage=zh-tw&cultureInfoName=zh-TW&memberId=32611396&ckuid=55f96f07-2b98-4ab5-bfbc-60d14af2d5a6&prid=0&checkIn=2020-04-12&checkOut=2020-04-13&rooms=1&adults=2&children=0&priceCur=TWD&los=1&textToSearch=%E5%AE%9C%E8%98%AD%E7%B8%A3&productType=-1&travellerType=1&familyMode=off'

# 欲搜尋之縣市網址 (url)
url = url_yilan
#滾動到最底部
#js1 = 'return document.body.scrollHeight'
#js2 = 'window.scrollTo(0, document.body.scrollHeight)'
old_scroll_height = 0
n = 10  #設定抓取頁數 (每頁約有100筆，此處可先至agoda搜尋確切頁數)
driver.get(url)
#driver.set_window_size(1680, 1050) # 可自行設置大小(太小會點不到換頁鍵)
driver.maximize_window()
time.sleep(10)
for i in range(1,n+1):
    #while driver.execute_script(js1) >= old_scroll_height:
    a = datetime.now()
    count = 0
    while True:
        count= count+1
        print(count)
        driver.execute_script("window.scrollBy(0,500)")
        #old_scroll_height = driver.execute_script(js1)
        #driver.execute_script(js2)
        time.sleep(2)
        #print(datetime.now())
        if (datetime.now() - a).seconds > 120 :
            break
    try:
        htmltext = driver.page_source
        soup = BeautifulSoup(htmltext,'html.parser')
        #print(soup.prettify())
        artitle_url = soup.select('li[data-selenium="hotel-item"] a ')
        driver.execute_script("window.open()")
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(1)
        for each_artitle_url in artitle_url:
            try:
                each_artitle_url = 'https://www.agoda.com'+ each_artitle_url['href']
                print(each_artitle_url)
                driver.get(each_artitle_url)
                time.sleep(2)
                soup = BeautifulSoup(driver.page_source,'html.parser')
                artitle_title = soup.select_one('h1[class="HeaderCerebrum__Name"]').text
                print(artitle_title)
                artitle_address = soup.select_one('span[class="HeaderCerebrum__Address"]').text
                print(artitle_address)
                artitle_store = soup.select_one('span[class="ReviewScore-Number"]').text
                #artitle_store = artitle_store.text
                print(artitle_store)
                article_json = {
                            '酒店名稱': artitle_title,
                            '酒店地址': artitle_address,
                            '酒店評分': artitle_store,
                            '縣市': '宜蘭縣',    #自行替換
                            '網址': each_artitle_url,
                            '留言': 'NA'
                }
                acticle_js = json.dumps(article_json, ensure_ascii=False, indent=1)
                try:
                    if not os.path.exists(resource_path + '\\' + '宜蘭縣'):   #自行替換
                        os.mkdir(resource_path + '\\' + '宜蘭縣')
                    with open(r'%s/%s.json' % (resource_path + '\\' + '宜蘭縣', artitle_title), 'w',
                              encoding='utf-8') as w:
                        w.write(acticle_js)
                except:
                    print("==========")
                    print("寫入檔案錯誤")
                    print("==========")
                time.sleep(1)
            except:
                print("==========")
                print("網頁錯誤")
                print("==========")

        print('第'+ str(i) +'頁完成')
        driver.close()
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(2)
        driver.find_element_by_id('paginationNext').click()
        time.sleep(10)
    except :
        print("==========")
        print("其他錯誤")
        print("==========")

print('宜蘭縣' + " complete")  #自行替換訊息


