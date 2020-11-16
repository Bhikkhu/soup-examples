from bs4 import BeautifulSoup
import requests

with open('simple.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')
print(soup.prettify())

match = soup.find('div', class_ = 'footer')
match = match.find('p')
print(match.text)
