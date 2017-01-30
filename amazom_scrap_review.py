from bs4 import BeautifulSoup
import requests

"""This is not happening becuase amazon blocked srapping"""


def search_page(name, n=0):
    """Input a search title, return a url"""
    name = ''.join([char if char != ' ' else '%20' for char in str(name)])
    search_url ='https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Dstripbooks&field-keywords={}&rh=n%3A283155%2Ck%3A{}'.format(name,name)
    search = requests.get(search_url).text
    soup = BeautifulSoup(search, "lxml")
    link = soup.find("div", id = "searchTemplate").find("li", "s-result-item celwidget",id = "result_0")
    if link:
        print("Book title: {}".format(link.find("a","a-link-normal s-access-detail-page  a-text-normal").get("title")))
        return link.find("a","a-link-normal s-access-detail-page a-text-normal").get("href")
    else:
        print("Can't find anything!!!")
        return None

def print_comment(url):
    """Scrap Short comment from amazon url"""
    test = requests.get(url).text
    soup = BeautifulSoup(test, "lxml")
    comment = soup.find("div", id="revMHRL").find_all("div", "a-row a-spacing-small")
    for item in set(comment):
        print("-", item.find("div", "a-section").contents[0])
    if not comment:
        print("There's no comment.")
    return

def read_print_loop():
    """Read a Amazon book Name and return the comment"""
    while True:
        try:
            src = input('Book> ')
            if src == "Q":
                return None
            src = search_page(src)
            if src:
                print_comment(src)
            print(" ")
        except (AttributeError, EOFError):
            read_print_loop()

read_print_loop()

