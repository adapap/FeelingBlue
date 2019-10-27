import json
import re
import random
from collections import defaultdict
with open('output.json') as f:
    data = json.load(f)

categories = defaultdict(lambda: defaultdict(list))
total = defaultdict(int)
sample = [data for group in data.values() for data in group]
for x in sample:
    text = x['sentence'].lower()
    rating = 'positive' if x['polarity'] >= 0 else 'negative'
    match = lambda *tokens: any(re.search(token, text) for token in tokens)
    if match('delay', 'late', 'wait', 'ago', 'busy', 'traffic'):
        categories['delay'][rating].append(text)
    elif match('disable', 'disability', 'aid', 'assist', 'wheelchair', 'crutch', 'bleed', 'stroller'):
        categories['accessibility'][rating].append(text)
    elif match('cancel', 'schedule', 'reschedule', 'change', 'bump'):
        categories['cancel'][rating].append(text)
    elif match('crew', 'pilot', 'attendant', 'employee', 'staff', 'steward', 'supervisor', 'rep ', 'represent'):
        categories['staff'][rating].append(text)
    elif match('website', 'app', 'glitch', 'bug', 'broken', 'tv', 'wifi', 'internet', 'system', 'mechanical', 'failure', 'malfunction'):
        categories['tech'][rating].append(text)
    elif match('fit', 'space', 'comfort', 'loud', 'noise', 'experience', 'service', 'seat', 'parking', 'hot', 'heat', 'no air', 'customer', 'sleep', 'food'):
        categories['experience'][rating].append(text)
    elif match('operations', 'destination', 'location', 'business', 'ban', 'fee', 'price', 'money', 'sell', 'points'):
        categories['business'][rating].append(text)
    elif match('luggage', 'baggage', 'bag', 'lost', 'missing'):
        categories['luggage'][rating].append(text)
    elif match('info', 'information', 'directions', 'rules', 'know', 'can i', 'help', 'trouble', 'question', 'problem'):
        categories['info'][rating].append(text)
    total[rating] += 1

parsed = {}
samples = {}
for k, v in categories.items():
    parsed['total'] = {
        'positive': total['positive'],
        'negative': total['negative']
    }
    parsed[k] = {
        'positive': len(v['positive']),
        'negative': len(v['negative'])
    }
    samples[k] = {
        'positive': random.sample(v['positive'], 20),
        'negative': random.sample(v['negative'], 20)
    }
with open('parsed.json', 'w') as f:
    json.dump(parsed, f)
with open('samples.json', 'w') as f:
    json.dump(samples, f, indent=4)