import wikipedia
from textblob import TextBlob
from Bio import Entrez

def wiki(name="Duke University", length=3):
    """This is a wikipedia fetcher for the basic information of reseach"""

    my_wiki = wikipedia.summary(name, length)
    return my_wiki

def search_wiki(name):
    """Search for something you are interested at wikipedia"""

    results = wikipedia.search(name)
    return results

def phrase(name):
    """Returns related phrases for your research resuts from wikipedia"""

    page = wiki(name)
    blob = TextBlob(page)
    return blob.noun_phrases


def search_pub(query):
    Entrez.email = 'your.email@example.com'
    handle = Entrez.esearch(db='pubmed', 
                            sort='relevance', 
                            retmax='20',
                            retmode='xml', 
                            term=query)
    results1 = Entrez.read(handle)
    return results1

def fetch_details(id_list):
    ids = ','.join(id_list)
    Entrez.email = 'your.email@example.com'
    handle = Entrez.efetch(db='pubmed',
                           retmode='xml',
                           id=ids)
    results2 = Entrez.read(handle)
    return results2