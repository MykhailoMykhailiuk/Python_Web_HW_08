
import json
from datetime import datetime
from mongoengine import connect

from models import Authors, Quotes

URI = "mongodb+srv://misamihajluk1:A03LBdqNq5xiqcmw@testmongo.rvxofnn.mongodb.net/?retryWrites=true&w=majority&appName=TestMongo"

connect(host=URI)


def load_authors(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        authors = json.load(file)
        for a in authors:
            author = Authors(
                full_name=a['fullname'],
                born_date=datetime.strptime(a['born_date'], '%B %d, %Y'),
                born_location=a['born_location'],
                description=a['description']
            ).save()


def load_guotes(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        quotes = json.load(file)
        for q in quotes:
            author = Authors.objects(full_name=q['author']).first()
            if author:
                quote = Quotes(
                    tags=q['tags'],
                    author=author,
                    quote=q['quote']
                ).save()


if __name__ == '__main__':
    load_authors('authors.json')
    load_guotes('qoutes.json')