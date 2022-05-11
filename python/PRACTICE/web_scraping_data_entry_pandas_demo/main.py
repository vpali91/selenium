from bs4 import BeautifulSoup
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas
import openpyxl

# Ide másold be a saját google form linked
GOOGLE_FORM_LINK = 'https://forms.gle/5wPX4iVJnY969bUo9'

# ZILLOW_LINK = 'https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D'

# Ezek a beautiful souphoz kellenek
HEADER = {"Accept-Language": "en-GB,en;q=0.9,ar-AE;q=0.8,ar;q=0.7,en-US;q=0.6",
          "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
          }
#Itt testre tudod szabni az url-ben, hogy pontosan mire akarsz rákeresni
ZILLOW_LINK = 'https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState={' \
              '"pagination":{},' \
              '"usersSearchTerm":null,' \
              '"mapBounds":{' \
              '"west":-122.56276167822266,' \
              '"east":-122.30389632177734,' \
              '"south":37.69261345230467,' \
              '"north":37.857877098316834' \
              '},' \
              '"isMapVisible":true,' \
              '"filterState":{' \
              '"fr":{"value":true},' \
              '"fsba":{"value":false},' \
              '"fsbo":{"value":false},' \
              '"nc":{"value":false},' \
              '"cmsn":{"value":false},' \
              '"auc":{"value":false},' \
              '"fore":{"value":false},' \
              '"pmf":{"value":false},' \
              '"pf":{"value":false},' \
              '"mp":{"max":2000},' \
              '"price":{"max":872627},' \
              '"beds":{"min":1}' \
              '},' \
              '"isListVisible":true,' \
              '"mapZoom":12' \
              '}'

options = Options()

# Itt a számítógépen található path-re át kell írni, fontos, hogy csak akkor fog helyesen lefutni, ha minden böngészőablakot bezársz előtte
# Azt a felhasználót fogja használni a selenium, amibe éppen be vagy jelentkezve. Javasolt játszós fiók használata, vagy kijelentkezés a fiókból
options.add_argument('user-data-dir=C:/Users/viczj/AppData/Local/Google/Chrome/User Data')

s = Service("D:/chromedriver.exe")

# Seleniummal kerül megnyitásra a böngésző, hogy a beautiful soup teljesen használható legyen ezen a védett oldalon
# A beautiful soup selenium nélkül is működik, de akkor csak 9 adatot enged letölteni
driver = webdriver.Chrome(service=s, options=options)

print('Görgess végig manuálisan a céloldalon, hogy minden link és kép az ingatlanokról betöltsön. Egyébként enélkül csak 9 adatot sikerülne letölteni')

driver.get(ZILLOW_LINK)

# Kb 40 másodperc elegendő arra, hogy végiggörgess az oldalon. e.
# Ezt a részt is lehetne automatizálni.

sleep(40)

html_source = driver.page_source

sleep(5)

# Ez a funkció lementi a html oldalt és a későbbiekben innen kerülnek beolvasásra az adatok.
with open('file.html', mode="w", encoding="utf-8") as fp:
    fp.write(html_source)

with open('file.html', mode="r", encoding="utf-8") as fp:
    content = fp.read()

soup = BeautifulSoup(content, 'html.parser')

# Itt jönnek létre a listák, amik a szükséges adatokat tartalmazzák(beautiful soup)
addresses = soup.find_all(name='address', class_="list-card-addr")

prices = soup.find_all(name='div', class_='list-card-price')

addresses_ = [address.get_text() for address in addresses]

prices_ = [price.get_text().split('/')[0].split('+')[0] for price in prices]

links = [a["href"] for a in soup.find_all(name="a", class_='list-card-link', tabindex="0")]

# Van néhány rosszul tagolt link...
# Ezeknél nem a teljes elérési link van, így az alábbi módon kerül korrigálásra.
#   pl: '/b/1450-castro-st-san-francisco-ca-5YVg2f/'
#        Ez lesz belőle 'https://www.zillow.com/b/1450-castro-st-san-francisco-ca-5YVg2f/'
for index in range(len(links)):
    if not links[index].startswith("http"):
        links[index] = 'https://www.zillow.com' + links[index]

#Ellenőrző kiíratások
print(len(addresses_), len(prices_), len(links))

print(addresses_)
print(prices_)
print(links)

# Kiíratás excel táblába. Ez pillanatok alatt kész van, a pandas hasznosságának demonstrációja miatt beleraktam
excel_writer = "D:/table.xlsx"
pandas.DataFrame({"address":addresses_, "price":prices_, "link":links}).to_excel(excel_writer, sheet_name='Sheet1', na_rep='', float_format=None, columns=None, header=True, index=True, index_label=None, startrow=0, startcol=0, engine=None, merge_cells=True, encoding=None, inf_rep='inf', verbose=True, freeze_panes=None, storage_options=None)

# Itt kezdődik a google form kitöltős selenium kód
driver.get(GOOGLE_FORM_LINK)

for i in range(len(prices_)):
    sleep(2)
    addr = driver.find_element(By.XPATH,
                               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price = driver.find_element(By.XPATH,
                                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element(By.XPATH,
                               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    addr.send_keys(addresses_[i])
    price.send_keys(prices_[i])
    link.send_keys(links[i])
    driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span').click()
    driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a').click() 
