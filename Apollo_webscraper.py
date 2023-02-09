import requests
from bs4 import BeautifulSoup as soup


def searchApollo(medicine):
    header = {
        'Origin': 'https://www.netmeds.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
    }
    url = 'https://www.apollopharmacy.in/search-medicines/' + medicine
    html = requests.get(url=url, headers=header)

    bsobj = soup(html.content, "html.parser")
    product_price = []
    for price in bsobj.findAll('div', {"class": "ProductCard_priceGroup__V3kKR"}):
        if (len(product_price)) == 0:
            price_string = price.text
            rs_index = price_string.rfind('₹') + 1
            price_string = price_string[rs_index:]
            product_price.append(price_string)
        else:
            break

    return product_price[0], url
