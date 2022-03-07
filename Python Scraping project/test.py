#Using beatifullsoup4 and requests library
#Doc https://www.crummy.com/software/BeautifulSoup/bs4/doc/
#Imports
from random import betavariate
from bs4 import BeautifulSoup
from matplotlib.pyplot import text
import requests
#Code
url = "https://www.ceneo.pl/117205812"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")
#print(doc.prettify) #raw html
top_Product = doc.find(["div"] , class_="layout-wrapper product-top__wrapper")

test = top_Product.find(["span"], class_="price-format nowrap")
print(test)
#print(top_Product)