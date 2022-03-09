#Using beatifullsoup4 and requests library
#Doc https://www.crummy.com/software/BeautifulSoup/bs4/doc/
#Imports
from bs4 import BeautifulSoup
from matplotlib.pyplot import text
import requests
import re
#Code
product_id = 117205811
url = f"https://www.ceneo.pl/{product_id}"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")
#print(doc.prettify) #raw html
#top_Product = doc.find(["div"] , class_="layout-wrapper product-top__wrapper")

#test = top_Product.find(["span"], class_="price-format nowrap")
#print(test)
#cena wyswietlana na top

reviews = doc.find(["div"] ,class_="score-extend__review")
#for test in opinions:
#    print(test)
# ilość opinii
reviews.contents
#for test in reviews:
#    print(test)
print((reviews.contents))
# 9-10 opini na strone max 50 stron
#tabele do danych
id = []
nickname = []
stars = []
recomend = []
purchase = []
opinion_date = []
boght_date = []
review_up =[]
review_down = []
message = []
cons = []
pros = []

for count in range(1,51):
    url_2 =f"https://www.ceneo.pl/{product_id}/opinie-{count}"
    result_2 =requests.get(url_2)
    doc = BeautifulSoup(result_2.text, "html.parser")
    test = doc.find(["div"],class_="js_product-reviews")
    opinions = doc.find_all(["div"],class_="user-post user-post__card js_product-review")
    for x in opinions:
        id.append(x["data-entry-id"])
print(id)
print(len(id) + "max 500 opinii potem sie wraca do 1 strony")