from bs4 import BeautifulSoup
import requests

r = requests.get('https://www.google.com/search?q=weather&rlz=1C1CHBF_enUS927US927&oq=weather&aqs=chrome..69i57j0i67i433j0i433j0j0i131i433l2j0i433j0i67i433.1135j1j7&sourceid=chrome&ie=UTF-8')
print(r.ok)
soup = BeautifulSoup(r.text, 'lxml')

print(soup.text)
#match = soup.findAll('span')
#print("\n\n", match)
