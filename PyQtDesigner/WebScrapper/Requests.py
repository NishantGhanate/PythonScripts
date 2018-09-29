import requests
from lxml import html
import string

url = "https://www.reddit.com/r/popular/?geo_filter=US"
page = requests.get(url)
tree = html.fromstring(page.content)

token = tree.xpath('//a[@href]')
print(token)