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

if __name__ == '__main__':
    # title = grab_title()
    # print(title)

    # for text in grab_classes():
    #     print(text)

    grab_image()