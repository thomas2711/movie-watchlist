from bs4 import BeautifulSoup
import requests
import re

rt_prefix = "https://www.rottentomatoes.com/m/"

def get_rt_score(title, year):
    rt_url_a = rt_prefix + title.replace(' ','_').replace("'", '').replace(':','').replace('.','').lower()

    rt_rating = rt_score_helper(title, year, rt_url_a)
    if rt_rating != -1:
        return rt_rating
    else:
        rt_url_b = rt_url_a + '_' + str(year)
        rt_rating = rt_score_helper(title, year, rt_url_b)
        return rt_rating 

def rt_score_helper(title, year, url):
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'html.parser')
    #print(soup.prettify())  

    rt_rating = soup.find("span", class_="meter-value")
    
    if rt_rating == None:
        return -1
    else:
        rt_rating = rt_rating.contents[0].string
        return rt_rating

#print(get_rt_score('Dunkirk', 2017))