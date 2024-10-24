import requests
import pprint
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.titleline a')
subtext = soup.select('.subtext')

def sort_stories_by_votes(list):
    return sorted(list, key = lambda k:k['votes'], reverse = True)

def crete_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(subtext):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        vote = item.select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 150:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)

pprint.pprint(crete_custom_hn(links, subtext))