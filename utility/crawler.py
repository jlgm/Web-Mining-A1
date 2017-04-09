import requests
from bs4 import BeautifulSoup

number_of_files = 1

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

#function generates different files with content from the given list
def generate_files(texts):
    for item in texts:
        global number_of_files
        filename = "doc" + str(number_of_files)
        myfile = open('./'+filename+'.txt', 'w+')
        myfile.write(item)
        myfile.close()
        number_of_files = number_of_files + 1


#main subjects:
acne = build_content(get_pages('acne'))
insomnia = build_content(get_pages('insomnia'))

#other subjects:
depression = build_content(get_pages('depression'))
pain = build_content(get_pages('pain'))
hepatitisa = build_content(get_pages('hepatitis-a'))
menopausal = build_content(get_pages('menopausal-disorders'))
diarrhea = build_content(get_pages('diarrhea'))
cold = build_content(get_pages('cold-symptoms'))

#generates in total: 200 documents
generate_files(acne)
generate_files(insomnia)
generate_files(depression)
generate_files(pain)
generate_files(hepatitisa)
generate_files(menopausal)
generate_files(diarrhea)
generate_files(cold)
