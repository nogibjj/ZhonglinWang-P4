import wikipedia
from textblob import TextBlob

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
