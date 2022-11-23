import bs4
import requests
from pprint import pprint
from Constants import HEADERS

KEYWORDS = ['язык', 'IT', 'Python', 'Apple']

url = 'https://habr.com'

response = requests.get(url, headers = HEADERS)
text = response.text
soup = bs4.BeautifulSoup(text, features = 'html.parser')
articles = soup.find_all("article")


for article in articles:
    previews = article.find_all(class_ = "tm-article-snippet tm-article-snippet")
    previews = [preview.text.strip() for preview in previews]
    for preview in previews:
        for keyword in KEYWORDS:
            if keyword in preview:   
                href = article.find(class_ = "tm-article-snippet__title-link").attrs['href']
                full_href = f"{url}{href}"
                time = article.find(class_ = "tm-article-snippet__datetime-published").find('time').attrs['title']
                title = article.find('h2').find('span').text
                x = f"{time}  {title} ===> {full_href}"

                pprint(x)