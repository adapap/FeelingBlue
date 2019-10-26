import json
import re

with open('tokens.json') as f:
    tokens = json.load(f)
    
def clean_text(text):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^#0-9A-Za-z\' \t])|(\w+:\/\/\S+)", " ", re.sub('\’', '\'', text)).split())