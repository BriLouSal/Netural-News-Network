from NCAI import left_wing_bias, right_wing_bias, netural_bias
import json






from sklearn.feature_extraction.text  import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split
import json



from anthropic import AnthropicVertex
from anthropic import Anthropic

import os
from dotenv import load_dotenv




load_dotenv()




def generate_universal_dataset():
    """Generate one dataset for all stocks using fictional company data."""
    dataset = {
        "Left_wing": left_wing_bias(),
        "Neutral":  netural_bias(),
        "Right_wing": right_wing_bias()
    }

    with open('sentiment_dataset_of_stocks.json', "w", encoding="utf-8") as f:
        json.dump(dataset, f, indent=4)


generate_universal_dataset()