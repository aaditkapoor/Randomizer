import requests
import os
import random
import json
from typing import List

BASE_URL = "https://damp-plains-56068.herokuapp.com"


class Movie:
    def __init__(self, image, title):
        self.image = image
        self.title = title
    def __repr__(self):
        return "<Movie: {}>".format(self.title)
    def to_dict(self):
        return {"image": self.image, "title": self.title}

def encode(s):  
    return "+".join(s.split())

class Scraper:
    def __init__(self, search_term: str):
        self.search_term = encode(search_term)
        self.movies = []
    def search(self) -> str:
        results = requests.get(BASE_URL + "/search/" + self.search_term)
        data = json.loads(results.text)
        print(results)
        for i in data:
            print(f"Loaded {i['title']}")
            self.movies.append(Movie(i['image'], i['title']))
    def pick_movie(self, n = 6) -> List[Movie]:
        return random.sample(self.movies, n)


s = Scraper("star wars")
s.search()
print(s.pick_movie())

