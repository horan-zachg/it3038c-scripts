import requests, re
from bs4 import BeautifulSoup

data = requests.get ('https://www.footlocker.com/product/nike-air-max-plus-mens/J2029001.html').content

soup = BeautifulSoup(data, "html.parser")
span = soup.find("span", {"class":"ProductName-primary"})
title = span.text
span = soup.find("div", {"class":"ProductPrice"})
price = span.text

print("The item '%s' cost %s" % (title,price))

