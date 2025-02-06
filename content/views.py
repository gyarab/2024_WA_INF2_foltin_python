from django.shortcuts import render
from django.http import HttpResponse

import requests
import json

# data = [
#     {
#         'title': 'web Gymnazia Arabska',
#         'link': 'https://gyarab.cz',
#     },
#     {
#         'title': 'web jutub',
#         'link': 'https://youtube.com',
#     },
# ]

def homepage(request):
    with open('articles.json', encoding='utf-8') as f:
        articles = json.load(f)

    article_html = ''
    i=0
    for article in articles:
        title = article['title']
        image = article['image']
        article_html += f'<a href="/article/{i}"><h2>{title}</h2></a>'
        article_html += f'<img src="{image}" alt="{title}">'
        i+=1

    return HttpResponse(article_html)

def article(request, id):
    with open('articles.json', encoding='utf-8') as f:
        articles = json.load(f)

    article = articles[id]
    title = article['title']
    perex = article['perex']
    image = article['image']

    return HttpResponse(f"""
                        <h2>{title}</h2>
                        <img src="{image}" alt="{title}">
                        <p>{perex}</p>
                        <a href="/">Zpět na úvodní stránku</a>
                        """)

def hello(request, name):
    return HttpResponse(f'Ahoj {name}')

def vynasob(request, a, b):
    return HttpResponse(f'{a} * {b} = {a*b}')
