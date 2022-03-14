import requests
from bs4 import BeautifulSoup

def get_html():
	url = "https://www.caa.ca/gas-prices/"
	html = BeautifulSoup(requests.get(url).content, "html.parser")
	return (html)

def get_gaz_prices(html):
	prices = {}

	table = html.find(class_ = "provinces_table")
	table_rows = table.find_all("tr")
	for row in table_rows:
		row_data = row.find_all("td")
		prices[row_data[0].text] = row_data[1].text[:-2]
	return (prices)

html = get_html()
gaz_prices = get_gaz_prices(html)
print(gaz_prices)
