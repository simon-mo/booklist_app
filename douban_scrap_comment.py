from bs4 import BeautifulSoup
import requests

def search_page(name, n=0):
    """Input a search title, return a url"""
    name = ''.join([char if char != ' ' else '%20' for char in str(name)])
    search_url = 'http://book.douban.com/subject_search?search_text={}&cat=1002'.format(name)
    search = requests.get(search_url).text
    soup = BeautifulSoup(search, "lxml")
    link = soup.find("li", "subject-item")
    if link:
        print("Book title: {}".format(link.find("h2","").find("a").get("title")))
        print("Showing comments for following edition: {}".format(link.find("div", "pub").contents[0]))
        return link.find("a", "nbg").get('href')
    else:
        print("Can't find anything!!!")
        return None

def print_comment(url):
    """Scrap Short comment from douban url"""
    test = requests.get(url).text
    soup = BeautifulSoup(test, "lxml")
    comment = soup.find_all("p", "comment-content", limit = 10)
    for item in set(comment):
        print("-", item.contents[0])
    if not comment:
        print("There's no comment.")
    return

def read_print_loop():
    """Read a douban book number and return the comment"""
    recent_input = ""
    while True:
        try:
            src = input('Book> ')
            if src == "Q":
                return None
            elif src == "^[[A" :
                src = search_page(recent_input)
                print_comment(src)
            elif src:
                recent_input = src
                src = search_page(src)
                print_comment(src)
            print(" ")
        except (AttributeError, EOFError):
            read_print_loop()

read_print_loop()
