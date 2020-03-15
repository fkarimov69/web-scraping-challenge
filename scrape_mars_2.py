    # ---
    # jupyter:
    #   jupytext:
    #     text_representation:
    #       extension: .py
    #       format_name: light
    #       format_version: '1.5'
    #       jupytext_version: 1.4.0
    #   kernelspec:
    #     display_name: Python 3
    #     language: python
    #     name: python3
    # ---
from flask import Flask
import pymongo
from bs4 import BeautifulSoup
import requests
from splinter import Browser
import pandas as pd


# conn='mongodb://localhost:27017'
# client=pymongo.MongoClient(conn)

# db=client.mars_db
# collection=db.mars_db

app=Flask(__name__)


conn='mongodb://localhost:27017'
client=pymongo.MongoClient(conn)

db=client.mars_db
collection=db.collection

    




@app.route("/scrape")
def scrape():
    

    # +
    #NASA Mars News
    # -

    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'

    response=requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    # print(soup.prettify())

    title=soup.find(class_="content_title").text
    # print(title)
    paragraph=soup.find('div',class_="rollover_description_inner").text
    # print(paragraph)

    # +
    #JPL Mars Space Images - Featured Image
    # -

    # executable_path = {'executable_path': 'chromedriver.exe'}
    # browser = Browser('chrome', **executable_path, headless=False)

    # url='https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars' 
    # browser.visit(url) 

    featured_image_url=  'https://www.jpl.nasa.gov/spaceimages/images/wallpaper/PIA17044-1600x1200.jpg'

    # +
    #Mars Weather
    # -

    url = 'https://twitter.com/MarsWxReport/status/1236756368335519745'

    response=requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    # print(soup.prettify())

    mars_weather=soup.find('div',class_="js-tweet-text-container").text
    # tag=soup.span
    # print(tag)
    # tag.name
    # print(mars_weather)
    # paragraph=soup.find('div',class_="rollover_description_inner").text
    # print(paragraph)

    # +
    #Mars Facts
    # -

    url="https://space-facts.com/mars/"

    tables=pd.read_html(url)
    # tables

    # type(tables)

    df=tables[0]
    df.columns = ['Fact','Value']
    df=df.to_dict('records')

    #

    hemisphere_image_url= []
    hemisphere_image_url.append({"img_url":"https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg","title":"Cerebrus Hemisphere"})
    hemisphere_image_url.append({"img_url":"https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg","title":"Schiaparelli Hemisphere"})
    hemisphere_image_url.append({"img_url":"https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg","title":"Syrtis Major Hemisphere"})
    hemisphere_image_url.append({"img_url":"https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg","title":"Valles Marineris Hemisphere"})
    # hemisphere_image_url
    mars_dict = {
    "title":title,
    "paragraph":paragraph,
    "featured_image_url":"https://www.jpl.nasa.gov/spaceimages/images/wallpaper/PIA17044-1600x1200.jpg",
    "weather":mars_weather,
    "facts":df,
    "hemisphere_img":hemisphere_image_url

    }
    collection.insert(mars_dict)
    return(mars_dict)
    
# conn='mongodb://localhost:27017'
# client=pymongo.MongoClient(conn)

# db=client.mars_db
# collection=db.mars_db

# collection.insert_one(mars_dict)
    
if __name__=="__main__":
    app.run(debug=True)

# print(mars_dict)

# results = db.collection.find()
# for result in results:
#     print(result)

    # +
    # # initializing dictionary 
    # test_dict = { "Rash" : [1, 3], "Manjeet" : [1, 4], "Akash" : [3, 4] } 

    # # printing original dictionary 
    # print ("The original dictionary is : " + str(test_dict)) 

    # # using list comprehension 
    # # to convert dictionary of list to  
    # # list of dictionaries 
    # res = [{key : value[i] for key, value in test_dict.items()} 
    #          for i in range(2)] 
    # -
# scrape()