from NCAI import left_wing_bias, right_wing_bias, netural_bias
import json





def generate_model_for_bias():
    dataset = {
        'left_wing': left_wing_bias(),
        'right_wing': right_wing_bias(),
        'netural':  netural_bias(),
    }

    with open('news_sentiment_dataset.json', 'w', encoding='UTF-8') as f:
        json.dump(dataset, f, indent=4, nsure_ascii=False)



generate_model_for_bias()