from django.shortcuts import render
from django.http import HttpResponse

import requests
import json

def homepage(request):
    with open('articles.json', encoding='utf-8') as f:
        articles = json.load(f)

    return render(request, 'content/homepage.html', {'articles': articles})

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
