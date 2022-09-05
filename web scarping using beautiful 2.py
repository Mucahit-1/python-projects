from bs4 import BeautifulSoup
import requests

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.7"
}
url = "https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.61529005957031%2C%22east%22%3A-122.25136794042969%2C%22south%22%3A37.65307462630367%2C%22north%22%3A37.89730657544827%7D%2C%22mapZoom%22%3A11%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"

response = requests.get(url , headers=header)
web_page = response.text
soup = BeautifulSoup(web_page , "html.parser")

all_addresses = soup.find_all(name="address", class_="list-card-addr")
all_prices = soup.find_all("div", {"class": "list-card-price"})
all_links = soup.find_all("a", {"class": "list-card-link"})

links_list = []
for link in all_links:
    href = link["href"]
    if "http" not in href:
        links_list.append(f"https://www.zillow.com{href}")
    else:
        links_list.append(href)

addresses_list = [address.get_text().split(" | ")[-1] for address in all_addresses]
prices_list = [price.getText().split("+")[0] for price in all_prices if "$" in price.text]

print(addresses_list)
print(prices_list)
print(links_list)