# IMDb Top 250 Movies Scraper

This Python script demonstrates how to scrape data from the IMDb website's top 250 movies list using the `requests` and `BeautifulSoup` libraries. The main goal of this code is to provide an example of web scraping in Python and to extract the movie titles from the IMDb Top 250 list.

## Requirements

- Python 3.x
- `requests` library
- `BeautifulSoup` library

You can install the required libraries using the following commands:

```bash
pip install requests
pip install beautifulsoup4
```

## How It Works

1. Import the necessary libraries:

```python
from bs4 import BeautifulSoup
import requests
```

2. Set up the User-Agent header to mimic a web browser to avoid being blocked by the website's anti-scraping measures:

```python
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
}
```

3. Define the URL of the IMDb Top 250 list and send a GET request using the `requests` library:

```python
url = 'https://www.imdb.com/chart/top'
response = requests.get(url, headers=headers)
```

4. Create a BeautifulSoup object to parse the HTML content of the webpage:

```python
soup = BeautifulSoup(response.text, "html.parser")
```

5. Locate the elements containing movie data using the appropriate class name. In this case, we are searching for `li` elements with the class name `"ipc-metadata-list-summary-item sc-bca49391-0 eypSaE cli-parent"`:

```python
movies = soup.find_all(
    "li", class_="ipc-metadata-list-summary-item sc-bca49391-0 eypSaE cli-parent")
```

6. Loop through the extracted movie elements and print the title of each movie:

```python
for x in movies:
    print(x.h3.text)
```

## Usage

1. Make sure you have Python 3.x installed.

2. Install the required libraries using the commands provided above.

3. Copy and paste the script into a Python file (e.g., `imdb_scraper.py`).

4. Run the script using the command:

```bash
python imdb_scraper.py
```

## Learning Objectives

By studying this code, I learned the following:

- How to send HTTP requests using the `requests` library.
- How to parse HTML content using the `BeautifulSoup` library.
- How to locate and extract specific elements from a webpage using CSS selectors.
- How to mimic a web browser's User-Agent header to avoid anti-scraping measures.
- How to loop through and process scraped data.

Remember that web scraping practices might need to be adjusted depending on the website's structure and any changes made to the website's design or layout. Additionally, always make sure to follow the website's terms of use and guidelines when scraping data.
