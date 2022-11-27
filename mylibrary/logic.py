import arxivscraper
import pandas as pd


def arxiv(name="astro-ph"):
    """Search for something you are interested at Arxiv"""
    scraper = arxivscraper.Scraper(category=name, date_from='2022-05-27',date_until='2022-06-07')
    output = scraper.scrape()
    cols = ('id', 'title', 'categories', 'abstract', 'doi', 'created', 'updated', 'authors')
    df = pd.DataFrame(output,columns=cols)
    return df


