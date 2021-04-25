
# from bs4 import BeautifulSoup

# import requests


# url = "https://www.x-rates.com/calculator/?from=EUR&to=USD&amount=1"

# html_content= requests.get(url).text

# soup = BeautifulSoup(html_content, "lxml")
# usd_container = soup.findAll('span', {"class":"ccOutputRslt"})
# usd = usd_container[0].text
# print(usd)

l = [1,2,3,4,5]

j = [x**2 for x in l]

print(j)