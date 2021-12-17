from requests import get # http 'get' requests
from requests.exceptions import ConnectionError as RqConnError
from bs4 import BeautifulSoup # html parsing
from gensim.summarization.summarizer import summarize # extractive text summarization
from gensim.summarization import keywords # get keywords from summary
from app.models import Article
from app import db

class NewsHandler():
    def __init__(self, file=None, app=None):
        if file:
            with open(file, 'r') as reader:
                urls = reader.readlines()

        self.urls = urls if file else input('Enter URL: ')
        self.hlList = self.extract_headlines()
        self.app = app

    def extract_headlines(self):
        hlList = []
        print("Extracting Stories ...")
        response = get(self.urls)
        content = response.content
        soup = BeautifulSoup(content, "lxml")

        for tag in soup.find_all("td", attrs={"class": "title", "valign": ""}):
            if (link_url := tag.a["href"])[:4] != "http":
                link_url = "https://news.ycombinator.com/" + link_url
            
            hlList.append(link_url)
        
        return hlList[:-1]

    def generate_summaries(self):

        def get_only_text(url):
            try:
                page = get(url)
                soup = BeautifulSoup(page.content, "lxml")
                text = ' '.join(map(lambda p: p.text.strip(), soup.find_all('p')))
                title = "Default Title" if not soup.title else ' '.join(soup.title.stripped_strings)

            except RqConnError as e:
                title, text = None, e

            return title, text

        for hl in self.hlList:
            title, text = get_only_text(hl)
        
            if title is None:
                print(f"Error : {hl} : {text}")
                continue

            k_l_words = keywords(text, ratio=0.1, lemmatize=True)

            try:
                summary = summarize(repr(text), ratio=0.1)
            except ValueError as e:
                summary = "Inadequate text structure.  This text cannot be summarized.  This is default text.  This might be summarized."

            with self.app.app_context(): 
                db.session.add(Article(title, summary, k_l_words, hl))
                db.session.commit()