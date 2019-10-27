## Challenge: Crawl Any/All public domain/social media data to get customer’s sentiments of JetBlue.

*What we are looking for:*
· Define your hypothesis.
· Prove it using the data found in public domain and social media (what insight/learning the data show)
· Area of Recommendations for JetBlue

Prize: JetBlue vacation package including round-trip flight travel certificate and hotel stay for $1000 credit.


Hypothesis:

Data Analysis:

Recommendation:



Tools:
- Vue.js (frontend)
- Flask (backend)
  - Sentiment analysis Python
- GraphQL (parsing JSON/queries)

Links:
https://finance.yahoo.com/quote/JBLU/community/

https://monkeylearn.com/sentiment-analysis/

# Customer Reviews

https://www.consumeraffairs.com/travel/jetblue.html?#sort=top_reviews&filter=none +
https://www.airlinequality.com/airline-reviews/jetblue-airways/ +
https://www.tripadvisor.com/Airline_Review-d8729099-Reviews-JetBlue +
https://www.kayak.com/JetBlue.B6.airline.html + 

https://opensourceforu.com/2016/12/analysing-sentiments-nltk/


# Output Format

[
    {
        "source": "twitter",
        "content": "...",
        "sentiment": "positive/negative/neutral"
    }
]