import requests
import bs4

url = 'https://en.wikipedia.org/wiki/Jonas_Salk'

def grab_title():
    result = requests.get(url)
    soup = bs4.BeautifulSoup(result.text, 'lxml')
    title = soup.select('title')[0].getText()
    return title

def grab_classes():
    result = requests.get(url)
    soup = bs4.BeautifulSoup(result.text, "lxml")
    
    for item in soup.select('.toctext'):
        yield item.text

def grab_image():
    result = requests.get(url)
    soup = bs4.BeautifulSoup(result.text, 'lxml')

    for element in soup.select('.thumbimage'):
        src = element['src']
        link = 'https:' + src

        image_link = requests.get(link)

        # raw content of the actual image
        # binary file
        print(image_link.content)

        # save file
        # write binary
        with open('image.jpg', 'wb') as f:
            f.write(image_link.content)

        break

def get_book_titles():
    base_url = 'http://books.toscrape.com/catalogue/page-{}.html'

    for page in range(1, 6):
        print('\nScrap Page {}\n'.format(page))

        scrape_url = base_url.format(page)
        response = requests.get(scrape_url)

        soup = bs4.BeautifulSoup(response.text, 'lxml')
        
        counter = 1
        for book_element in iter(soup.select('.product_pod')):
            if len(book_element.select('.star-rating.Two')) > 0:
                book_title = book_element.select('a')[1]['title']
                yield (page, counter, book_title)

                counter += 1

if __name__ == '__main__':
    # title = grab_title()
    # print(title)

    # for text in grab_classes():
    #     print(text)

    # grab_image()

    print('All 2 stars books')
    for page, index, title in get_book_titles():
        print('Page {}: #{} - {}'.format(page, index, title))