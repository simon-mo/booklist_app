from bs4 import BeautifulSoup
import requests

def search_page(name):
    """Input a search title, return a url"""
    name = ''.join([char if char != ' ' else '%20' for char in str(name)])
    search_url = 'http://book.douban.com/subject_search?search_text={}&cat=1002'.format(name)
    search = requests.get(search_url).text
    soup = BeautifulSoup(search, "lxml")
    link = soup.find("li", "subject-item")
    print("Showing comments for: {}".format(link.find("div", "pub").contents[0]))
    return link.find("a", "nbg").get('href')

def print_comment(url):
    """Scrap Short comment from douban url"""
    test = requests.get(url).text
    soup = BeautifulSoup(test, "lxml")
    comment = soup.find_all("p", "comment-content", limit = 10)
    for item in comment:
        print("-", item.contents[0])
    return

def read_print_loop():
    """Read a douban book number and return the comment"""
    while True:
        try:
            src = input('Book> ')
            print_comment(search_page(src))
            print(" ")
        except (EOFError):
            return

read_print_loop()
