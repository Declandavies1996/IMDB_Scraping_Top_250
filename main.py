import requests
from bs4 import BeautifulSoup

# Downloading imdb top 250 movie's data
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
url = 'https://www.imdb.com/chart/top'
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
movies = soup.find_all(
    "li", class_="ipc-metadata-list-summary-item sc-bca49391-0 eypSaE cli-parent")
for x in movies:
    print(x.h3.text)