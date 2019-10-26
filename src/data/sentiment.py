import json
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob import TextBlob

def sentiment_scores(source, sentence):
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
    output = {"Source" : source, "Sentence " : sentence, "Sentiment": polarity , "Subjectivity": subjectivity}
    return output

with open('reddit.txt') as f:
    lines = f.readlines()
    output1 = [sentiment_scores("Reddit", x) for x in lines]
with open('tweets.txt') as f:
    lines = f.readlines()
    output2 = [sentiment_scores("Twitter", x) for x in lines]
with open('complete_output.txt', 'w') as f:
    output = {key: value for (key, value) in (output1.items() + output2.items())}
    json1 = json.dumps(output)
    f.write('\n'.join(json1))