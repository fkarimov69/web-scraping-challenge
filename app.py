
from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests
from splinter import Browser
import pandas as pd
import pymongo
from flask_pymongo import PyMongo

# conn= 'mongodb://localhost:27017'
# client = pymongo.MongoClient(conn)


app=Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_db"
mongo = PyMongo(app)


# db=client.mars_db

# db.items.drop()


# collection = db.items



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

    df=tables[1]
    df.columns = ['Fact','Value']
    df=df.to_dict('records')

    #

    hemisphere_image_url= []
    hemisphere_image_url.append({"img_url":"https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg","title":"Cerebrus Hemisphere"})
    hemisphere_image_url.append({"img_url":"https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg","title":"Schiaparelli Hemisphere"})
    hemisphere_image_url.append({"img_url":"https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg","title":"Syrtis Major Hemisphere"})
    hemisphere_image_url.append({"img_url":"https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg","title":"Valles Marineris Hemisphere"})
    # hemisphere_image_url

    mars_dict={
    "title":title,
    "paragraph":paragraph,
    "featured_image_url":"https://www.jpl.nasa.gov/spaceimages/images/wallpaper/PIA17044-1600x1200.jpg",
    "weather":mars_weather,
    "facts":df,
    "hemisphere_img":hemisphere_image_url
    }
    marsdb = mongo.db.mars_db
    marsdb.update({}, mars_dict, upsert=True)
    return(mars_dict)

    


@app.route("/")
def index():
    all_items=list(mongo.db.mars_db.find())
    # print(all_items)
    return render_template("index.html", all_items=all_items)

if __name__=="__main__":
    app.run(debug=True)
    
