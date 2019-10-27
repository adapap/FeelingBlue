import json
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob import TextBlob

def sentiment_scores(sentence):
    # Create a SentimentIntensityAnalyzer object.
    sid_obj = SentimentIntensityAnalyzer()
    
    # polarity_scores method of SentimentIntensityAnalyzer
    # oject gives a sentiment dictionary.
    # which contains pos, neg, neu, and compound scores.
    sentence = sentence.replace('\n', '')
    text_blob = TextBlob(sentence)
    polarity = text_blob.polarity
    subjectivity = text_blob.subjectivity
    #d = sid_obj.polarity_scores(sentence)
    #Overall sentiment dictionary is : "+ sentiment_dict +\
    #output = f'Sentence: {sentence}\nNegative: {d["neg"] * 100}% | Neutral: {d["neu"] * 100}% | Positive: {d["pos"] * 100}%'
    #output = f'Sentence: {sentence}\nPolartiy: {polarity}% | Subjectivity: {subjectivity}%'
    return (polarity, subjectivity)

with open('input.json') as f:
    data = json.load(f)
    output = {}
    count = 0
    total = sum(len(x) for x in data.values())
    for source, sentences in data.items():
        results = []
        for sentence in sentences:
            polarity, subjectivity = sentiment_scores(sentence)
            result = {
                'sentence': sentence,
                'polarity': polarity,
                'subjectivity': subjectivity
            }
            results.append(result)
            count += 1
            if count % 500 == 0:
                print(f'{count / total * 100:.2f}%')
        output[source] = results
with open('output.json', 'w') as f:
    json.dump(output, f)