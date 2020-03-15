
from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests
from splinter import Browser
import pandas as pd
import pymongo

conn= 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

db=client.mars_db

# db.items.drop()


collection = db.items

app=Flask(__name__)

@app.route("/scrape")
def scrape():

    

  

    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'

    response=requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    # print(soup.prettify())

    title=soup.find(class_="content_title").text
    # print(title)
    paragraph=soup.find('div',class_="rollover_description_inner").text
    # print(paragraph)

  


    featured_image_url=  'https://www.jpl.nasa.gov/spaceimages/images/wallpaper/PIA17044-1600x1200.jpg'

  

    url = 'https://twitter.com/MarsWxReport/status/1236756368335519745'

    response=requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    # print(soup.prettify())

    mars_weather=soup.find('div',class_="js-tweet-text-container").text
 

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
    mars_dict={
    "title":title,
    "paragraph":paragraph,
    "featured_image_url":"https://www.jpl.nasa.gov/spaceimages/images/wallpaper/PIA17044-1600x1200.jpg",
    "weather":mars_weather,
    "facts":df,
    "hemisphere_img":hemisphere_image_url

    }

    
    return(mars_dict)
    collection.insert(mars_dict)
    print(mars_dict)

@app.route("/")
def index():
    all_items=list(db.collection.find())
    print(all_items)
    return render_template("index.html", all_items=all_items)

if __name__=="__main__":
    app.run(debug=True)
    