from splinter import Browser
from bs4 import BeautifulSoup as bs
import requests


# Initiate instance 


def init_browser():

    exec_path = {'executable_path': 'chromedriver'}

    return Browser('chrome', headless=True, **exec_path)


# Visit sites


def scraper():

    url1 = 'https://mars.nasa.gov/news/'

    url2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'

    url3 = 'https://twitter.com/marswxreport?lang=en'

    url4 = 'http://space-facts.com/mars/'

    url5 = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'


    
    # Craete defination 

    mars_collection = {}


    # Craete instance 

    browser = init_browser()

    browser.visit(url1)

    news_title = browser.find_by_css('.content_title').first.text

    news_p = browser.find_by_css('.article_teaser_body').first.text


    # Assign to defication 

    mars_collection['news_title'] = news_title

    mars_collection['news_p'] = news_p


    # Create  second instance 

    browser = init_browser()

    browser.visit(url2)

    browser.find_by_id('full_image').click()

    featured_image_url = browser.find_by_css('.fancybox-image').first['src']


     # assign Image to variable 

    mars_collection['featured_image_url'] = featured_image_url
    

    # Create third instance and get text

    browser = init_browser()

    browser.visit('https://twitter.com/marswxreport?lang=en')

    # for text in browser.find_by_css('.tweet-text'):

    # if text.text.partition(' ')[1] == 'Sol':
    html = browser.html
    soup = bs(html, 'html.parser')

    mars_weather = soup.find_all("p")[5].get_text()
        # mars_weather = text.text

        # break
        
    mars_collection['mars_weather'] = mars_weather

    # Create fact variable

    browser = init_browser()
    browser.visit('http://space-facts.com/mars/')
    response = requests.get('http://space-facts.com/mars/', timeout=10)
    soup = bs(response.content, 'html.parser')
    mars_facts = soup.find_all('table')[1].text
    mars_collection['mars_facts'] = mars_facts

    # Create fourth instance 

    browser = init_browser()

    browser.visit(url5)

    first = browser.find_by_tag('h3')[0].text

    second = browser.find_by_tag('h3')[1].text

    third = browser.find_by_tag('h3')[2].text

    fourth = browser.find_by_tag('h3')[3].text



    browser.find_by_css('.thumb')[0].click()

    first_img = browser.find_by_text('Sample')['href']

    browser.back()



    browser.find_by_css('.thumb')[1].click()

    second_img = browser.find_by_text('Sample')['href']

    browser.back()



    browser.find_by_css('.thumb')[2].click()

    third_img = browser.find_by_text('Sample')['href']

    browser.back()



    browser.find_by_css('.thumb')[3].click()

    fourth_img = browser.find_by_text('Sample')['href']



    hemisphere_image_urls = [

        {'title': first, 'img_url': first_img},

        {'title': second, 'img_url': second_img},

        {'title': third, 'img_url': third_img},

        {'title': fourth, 'img_url': fourth_img}

    ]



    mars_collection['hemisphere_image_urls'] = hemisphere_image_urls



    return mars_collection


if __name__ == '__main__':

    print(scraper())
