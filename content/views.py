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
    return render(request, 'content/article.html', {'article': article})
