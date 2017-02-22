from urllib.request import urlopen
from bs4 import BeautifulSoup
import yaml
import re

html = urlopen("http://www.marktplaats.nl/verkopers/15321101.html?view=gv")
bsObj = BeautifulSoup(html.read(), "html5lib")

case_list = {}
x = 0

for child in bsObj.find("div", {"class":"card-grid"}).findAll("div", {"class":"card card--rich"}):

    testgeld = child.find("span",{"class":"price-new"}).get_text()
    geld = str(re.sub(r'[^\x00-\x7F]+',' ', testgeld).strip())
    pattern = re.compile("^[0-9]")
    if pattern.match(geld):
        geld = ''.join(('&euro; ', geld))

    case = {'price': geld,
            # remove tracking tags 
            'link': child.a.attrs['href'].split('?', 1)[0], 
            'img': ''.join(('http:', child.img.attrs['src'])),
            'title': child.img.attrs['alt']}
            
    idx=''.join(('id_', str(x)))

    case_ids = {idx: case}
    case_list.update(case_ids)

    x = x+1

cases = {'items' : case_list} 

with open('data.yml', 'w') as outfile:
            yaml.dump(cases, outfile, default_flow_style=False)
