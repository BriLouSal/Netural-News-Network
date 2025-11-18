
#  Main AI Core
from anthropic import AnthropicVertex
from anthropic import Anthropic
from dotenv import load_dotenv



# Side AI Core Goals: News API

# Json

import json
from json import JSONDecodeError

# Json Parse

load_dotenv()






def parser():
    pass

def dataset():
    pass



def left_wing_bias():
    negative_data = client.messages.create(
    model=MODEL_AI,
    max_tokens=int(MAX_TOKEN_FOR_NEWS_SENTIMENT),
    messages =[
        {"role": "user", 
            "content": f"Generate a news for a stock  that has positivety rating of and create this news that would have catalyst such as that the sentiment rating is 0.0-0.50. Create hundreds of output"}
    ],
)
    return negative_data.content[0].text.strip()

def right_wing_bias():
    pass