import requests
import bs4

url = 'https://en.wikipedia.org/wiki/Jonas_Salk'

def grab_title():
    result = requests.get(url)
    soup = bs4.BeautifulSoup(result.text, 'lxml')
    title = soup.select('title')[0].getText()
    return title
    
if __name__ == '__main__':
    title = grab_title()
    print(title)