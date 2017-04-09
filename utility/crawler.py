import requests
from bs4 import BeautifulSoup

#funcion returns a list of pages for a particular condition
def get_pages(condition):
    page = requests.get("https://www.drugs.com/condition/" + condition + ".html")
    soup = BeautifulSoup(page.content, 'html.parser')
    pages = []
    for item in soup.find_all('a', class_='condition-table__drug-name__link'):
        pages.append(item['href'])
    return pages

#function receives a list of drug pages to visit
#visits all of them and returns a list of strings with information about them
def build_content(pages):
    result = []
    for item in pages:
        page = requests.get("https://www.drugs.com" + item)
        soup = BeautifulSoup(page.content, 'html.parser')
        count = 0
        text = ""
        for p in soup.find_all('p'):
            text = text + p.get_text() + "\n"
            count = count + 1
            if count == 7:
                break
        result.append(text)
    return result

texts = build_content(get_pages('acne'))

for item in texts:
    print item
    print "######################\n"

# page = requests.get("https://www.drugs.com/aconite.html")
#
# soup = BeautifulSoup(page.content, 'html.parser')
#
# #print(soup.prettify())
#
# html = list(soup.children)[2]
#
# body = list(html.children)
#
# #for item in list(body.children):
#     #print item
#     #print "\n######################\n"
#
# count = 0
#
# for p in soup.find_all('p'):
#     print p.get_text()
#     count = count + 1
#     if count == 8:
#         break
