import requests
import bs4
import lxml


url = 'http://quotes.toscrape.com/page/{}'

page_number = 1

res = requests.get(url.format(page_number))

soup = bs4.BeautifulSoup(res.text,'lxml')

authors = set()    
    
while len(soup.select('.quote')) > 0:
    
    page_number += 1
    
    
    
    for name in soup.select('.author'):
        authors.add(name.text)
        
    break

authors
    