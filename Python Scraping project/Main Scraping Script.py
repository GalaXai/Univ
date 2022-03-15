#Using beatifullsoup4 and requests library
#Doc https://www.crummy.com/software/BeautifulSoup/bs4/doc/
#Imports
"""TODO
    ADD Flask + Make it object
"""
from bs4 import BeautifulSoup
import requests
import json
#Code
product_id = 117205811 # for testing 55742508
url =f"https://www.ceneo.pl/{product_id}/opinie-1"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")
#print(doc.prettify) #raw html

#check for error 
""" TODO
    if error == 404:
    return bad_id()
    elif error == 500 :
    exited_id()
"""

#Top price
#top_Product = doc.find(["div"] , class_="layout-wrapper product-top__wrapper")
#test = top_Product.find(["span"], class_="price-format nowrap")



reviews = doc.find(["div"] ,class_="score-extend__review")
# Ammount of opinions
reviews.contents
print((reviews.contents))
# Max 50 pages of opinions

#Declaring Tabales for Data
id = []
author_name = []
stars = []
recomend = []
purchase = []
opinion_date = []
bought_date = []
review_up =[]
review_down = []
message = []
cons = []
pros = []

#Scaraping the data
count = 0
error = False
#Scraping Data Function
for count in range(1,51):
    url =f"https://www.ceneo.pl/{product_id}/opinie-{count}"
    result =requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")
    test = doc.find(["div"],class_="js_product-reviews")
    " check if there are opinons if test == [] then return error / break + error        TODO" 
    opinions = doc.find_all(["div"],class_="user-post user-post__card js_product-review")
    for x in opinions:
        #id
        id.append(x["data-entry-id"])
        if x["data-entry-id"] == id[0] and len(id)>1:
            error = True
            id.pop(-1)
            break
        #Author name 
        name = x.find(["span"],class_="user-post__author-name")
        author_name.append(name.contents[0].strip()) # strip to remove newline from ex.'\nm...1'
        #Recomend
        recom = x.find(["em"],class_="recommended")
        try:
            recomend.append(recom.contents[0])
        except AttributeError:
            recomend.append(None)


        #Stars
        star = x.find(["span"],class_="user-post__score-count")
        stars.append(star.contents[0])
        #Date + Opinion
        purch = x.find(["div"], class_="review-pz")
        if purch != []:
            purchase.append("True") 
            date= x.find(["span"],class_="user-post__published")
            opinion_date.append(date.time["datetime"])
            bought_date.append(date.contents[-2]["datetime"])
        else:
            purchase.append("False")
            date= x.find(["span"],class_="user-post__published")
            opinion_date.append(date.time["datetime"])
            bought_date.append("")
        #up and down 
        up = x.find(["div"],class_="js_product-review-usefulness vote")
        review_up.append(up.find_all(["span"])[0].contents[0])
        review_down.append(up.find_all(["span"])[1].contents[0])
        #content
        mess = x.find(["div"],class_="user-post__text")
        word = ""
        for i in range (0,len(mess.contents),2):
            word+= mess.contents[i].strip()
        message.append(word)
        #pros and cons
        pro = x.find(["div"], class_="review-feature__col")
        list= []
        try:
            if len(pro)== 2:
                for i in range(len(pro)):
                    for x in range (0,len(pro[i]),2):
                        list.append(pro[i].contents[x].contents[0])
                    if list[0] == 'Zalety':
                        list.pop(0)
                        pros.append(list)
                    else:
                        list.pop(0)
                        cons.append(list)   
            else:
                z = pro.find_all(["div"], class_="review-feature__item")
                for x in range(len(z)):
                    list.append(z[x].contents[0])
                pros.append(list)
                cons.append([])
        except TypeError:
            pros.append([])
            cons.append([])

    if error == True:
        break
    else:
        continue


#for i in range(len(id)):
#    print(f"id {id[i]} author {author_name[i]} {stars[i]} {recomend[i]} {purchase[i]} {opinion_date[i]} {bought_date[i]} {review_up[i]} {review_down[i]} \n {message[i]} Wady {cons[i]} Zalety {pros[i]} ")

#Saving to Files
data = {
    'Opinie': [
    ]
}
#Loading and sving data fuction
for i in range(len(id)):
    data['Opinie'].append({'id': id[i],'Author':author_name[i],'Ocena': stars[i],
    'Poleca' :recomend[i],'Kupił': purchase[i], 'Data wystawienia opini': opinion_date[i],
    'Data kupna': bought_date[i],'Przydatna opinia': review_up[i],
    'Nieprzdatna opnia': review_down[i],'Treść wiadomości':  message[i],
    'Wady': cons[i], 'Zalety': pros[i]})
print(data)
with open(f'json_data{product_id}.json',"w", encoding="utf-8") as json_file:
    json.dump(data,json_file,indent=True,ensure_ascii=False)
    print(data)
