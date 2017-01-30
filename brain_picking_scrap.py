from bs4 import BeautifulSoup
import requests
from datetime import datetime
print(datetime.now())

h = open('h.html', 'r').read()
count = 0

def render_url(page):
    return 'https://www.brainpickings.org/page/' + str(page) + '/'

def scrap_page(url):
    global count
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'lxml')
    contents = soup.find_all('div', 'post_content')
    for content in contents:
        main = content.find('div')
        new_name = str(count) + '.html'
        f = open('{}'.format(new_name), 'w')
        f.write('<html>')
        f.write(str(h))
        f.write('<body style="margin:20;padding:0">')
        f.write(str(main))
        f.write('</body>')
        f.write('</html>')
        f.close()
        count += 1

for page in range(1605):
    scrap_page(render_url(page))
    print('Done with page {}/1604, {}'.format(page, page/1604))

print(datetime.now())
