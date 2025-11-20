
#  Main AI Core
from anthropic import AnthropicVertex
from anthropic import Anthropic
from dotenv import load_dotenv

import os

# Side AI Core Goals: News API

# Json

import json
from json import JSONDecodeError

import requests
from gnews import GNews

# Json Parse

load_dotenv()

API_CURRENT = os.getenv('CURRENT_API')

API_NEWS= os.getenv('NEWS_API')



news = GNews()


url = ('https://api.currentsapi.services/v1/latest-news?'
    'language=us&'
    F'apiKey={API_CURRENT}')




response = requests.get(url)
json_response = response.json()









CLAUDE = os.getenv('CLAUDE')
client = Anthropic(api_key=CLAUDE)


MAX_TOKEN_FOR_NEWS_SENTIMENT = os.getenv('MAX_TOKEN_FOR_NEWS_SENTIMENT')

MODEL_AI = os.getenv('MODEL')


def parser():
    pass

def dataset():
    pass



def right_wing_bias():
    right_wing_data = client.messages.create(
    model=MODEL_AI,
    max_tokens=int(MAX_TOKEN_FOR_NEWS_SENTIMENT),
    messages =[
        {"role": "user", 
            "content": f"Generate a news for world-news political that follows the political trend in 2025  that has right wing-bias rating of and create this news that would have major wording that is used in promiennt right-wing news network that would have such as that the bias rating is 1.00-0.90 . Create hundreds of output. The Bias should be formattable in JSON Style, do not incldue any formalities, MAKE IT ONLY JSON VALID DATASET"}
    ],
)
    return right_wing_data.content[0].text.strip()

def left_wing_bias():
    left_wing_data = client.messages.create(
    model=MODEL_AI,
    max_tokens=int(MAX_TOKEN_FOR_NEWS_SENTIMENT),
    messages =[
        {"role": "user", 
            "content": f"Generate a news for world-news political that follows the political trend in 2025  that has left wing-bias rating of and create this news that would have major wording that is used in promiennt left-wing news network that would have such as that the bias rating is from -1.00 to -0.90 . Create hundreds of output. The Bias should be formattable in JSON Style, do not incldue any formalities, MAKE IT ONLY JSON VALID DATASET"}
    ],
)
    return left_wing_data.content[0].text.strip()




def netural_bias():
    netural_wing = client.messages.create(
    model=MODEL_AI,
    max_tokens=int(MAX_TOKEN_FOR_NEWS_SENTIMENT),
    messages =[
        {"role": "user", 
            "content": f"Generate a news for world-news political that follows the political trend in 2025  that has NO BIAS AT ALL rating of and create this news that would have major wording that is used in promiennt left-wing news network that would have such as that the bias rating is 0.00-0.0.5 . Create hundreds of output. The Bias should be formattable in JSON Style, do not incldue any formalities, MAKE IT ONLY JSON VALID DATASET"}
    ],
)
    return netural_wing.content[0].text.strip()






# Recreate a recursive function