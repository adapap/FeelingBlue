import requests
from selenium import webdriver
from bs4 import BeautifulSoup as bs
from util import *

def fetch_data(limit):
    reviews = []
    # Consumer Affairs
    base_url = 'https://www.consumeraffairs.com/travel/jetblue.html?page={}#sort=recent&filter=none'
    for i in range(5 if limit else 50):
        url = base_url.format(i + 1)
        html = requests.get(url).text
        soup = bs(html, 'html.parser')
        divs = soup.find_all('div', class_='rvw-bd ca-txt-bd-2')
        for div in divs:
            review = div.find_all('p')
            if len(review) > 1:
                review = review[1].text
                reviews.append(clean_text(review))
    
    # Airline Quality
    base_url = 'https://www.airlinequality.com/airline-reviews/jetblue-airways/page/{}/?sortby=post_date%3ADesc&pagesize=100'
    for i in range(1 if limit else 8):
        url = base_url.format(i + 1)
        html = requests.get(url).text
        soup = bs(html, 'html.parser')
        divs = soup.find_all('div', attrs={'itemprop': 'reviewBody'})
        for div in divs:
            review = clean_text(div.contents[-1])
            reviews.append(review)
    
    # TripAdvisor
    driver = webdriver.Chrome(executable_path=r'C:\Users\debom\Downloads\Installers\Selenium Drivers\chromedriver_win32\chromedriver.exe')
    base_url = 'https://www.tripadvisor.com/Airline_Review-d8729099-Reviews-or{}-JetBlue'
    for i in range(0, 15 if limit else 500, 5):
        driver.implicitly_wait(7.5)
        driver.get(base_url.format(i) + '?filterLang=en')
        elem = driver.find_element_by_xpath("//span[starts-with(@class, 'location-review-review-list-parts-ExpandableReview__cta')]")
        elem.click()
        "location-review-review-list-parts-ExpandableReview__cta--2mR2g"
        elems = driver.find_elements_by_xpath("//q[starts-with(@class, 'location-review-review-list-parts-ExpandableReview__reviewText')]")
        for elem in elems:
            review = elem.find_element_by_css_selector('span').text
            reviews.append(clean_text(review))
    driver.quit()
    
    # Kayak
    base_url = 'https://www.kayak.com/JetBlue.B6.airline.html'
    html = requests.get(base_url).text
    soup = bs(html, 'html.parser')
    for review in soup.find_all('p', class_='reviewText'):
        a = review.contents[2]
        if len(review.contents) > 6:
            b = review.contents[6]
            reviews.append(clean_text(b))
        reviews.append(clean_text(a))
    # Write to file
    return reviews