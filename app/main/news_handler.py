from requests import get # http 'get' requests
from requests.exceptions import ConnectionError, MissingSchema, ReadTimeout
from bs4 import BeautifulSoup # html parsing
from gensim.summarization.summarizer import summarize # extractive text summarization
from gensim.summarization import keywords
from requests.models import MissingSchema # get keywords from summary
from app.models import Article
from app import db
import random


def extract_headlines(urlList):
    hlList = []
    for url in urlList:
        print("Extracting Stories ...")
        response = get(url)
        content = response.content
        soup = BeautifulSoup(content, "lxml")

        for tag in soup.find_all("td", attrs={"class": "title", "valign": ""}):
            if (link_url := tag.a["href"])[:4] != "http":
                link_url = "https://news.ycombinator.com/" + link_url

            hlList.append([link_url, tag.a.text])
    
    return hlList[:-1]

def generate_summaries(hlList):

    def get_only_text(url):
        try:
            page = get(url, timeout=10)
            soup = BeautifulSoup(page.content, "lxml")
            text = ' '.join(map(lambda p: p.text.strip(), soup.find_all('p')))
            title = "Default Title" if not soup.title else ' '.join(soup.title.stripped_strings)

        except (ConnectionError, MissingSchema, ReadTimeout) as e:
            title, text = None, e

        return title, text

    for hl in hlList:
        title, text = get_only_text(hl[0])
    
        if title is None:
            print(f"Error : {hl[0]} : {text}")
            continue

        k_l_words = keywords(text, lemmatize=True)

        try:
            summary = summarize(repr(text), ratio=0.1)
            summary = ' '.join(c for c in summary.split() if c.isalnum())
        except ValueError:
            summary = "Inadequate text structure.  This text cannot be summarized.  This is default text.  This might be summarized."
        print(k_l_words)
        db.session.add(Article(title=hl[1], summary=' '.join(summary.split()[:100]), keywords=' '.join(random.sample(k_l_words.split(), int(len(k_l_words.split()) * .20))) if len(k_l_words.split()) >= 5 else k_l_words, link=hl[0]))
        db.session.commit()
