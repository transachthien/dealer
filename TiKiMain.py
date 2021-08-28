from TiKiTarget import TikiTarget
import TikiHelper
import requests 
from bs4 import BeautifulSoup

TARGET_FILE = "target_list.txt"
targets = TikiHelper.getTargetFromFile(TARGET_FILE)
for target in targets:
    print(target.info())

#===============target.categoryUrl
headers = {'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Mobile Safari/537.36'}
target = targets[0]
searchLink = target.getSearchLink(1)
print(searchLink)

response = requests.get(searchLink,headers=headers)
bsoup = BeautifulSoup(response.text,"lxml")

listElement = bsoup.findAll("a", {"class":"product-item"})
print(len(listElement))

print(response.text)
# , {"class":"product-item"}
