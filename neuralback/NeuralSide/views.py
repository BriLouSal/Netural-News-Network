from django.shortcuts import render

from anthropic import AnthropicVertex
from anthropic import Anthropic
from dotenv import load_dotenv

import os

# Side AI Core Goals: News API

# Json

import json
from json import JSONDecodeError

from gnews import GNews
import requests
# Json Parse

load_dotenv()

API_NEWS= os.getenv('NEWS_API')


news = GNews()



# Create your views here.


def data_synthsize():
    url = (
        f"https://gnews.io/api/v4/top-headlines?"
        f"category=general&lang=en&country=us&max=10&apikey={API_NEWS}"
    )

    get_news = requests.get(url)


    # world_news = news.get_top_news()
    dict_data_news = get_news.json()
    

    articles = dict_data_news.get('articles', [])
    info_list = []

    for news in articles:
        info_list.append({
            'title': news.get('title'),
            'images': news.get('images'),
            'description': news.get('description'),
            'source': news.get('source'),

            
        })

    return info_list





def home(request):
    context = {'info': data_synthsize()}
    return render('base/home.html', context)




data_synthsize()