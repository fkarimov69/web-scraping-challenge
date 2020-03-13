# !/usr/bin/env python
# coding: utf-8

# In[1]:
# import pymongo





def scrape():

    #  return (
    from bs4 import BeautifulSoup
    import requests
    from splinter import Browser
    import pandas as pd



    # from bs4 import BeautifulSoup
    # import requests
    # from splinter import Browser
    # import pandas as pd


    # In[2]:


    #NASA Mars News


    # In[3]:


    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'


    # In[4]:


    response=requests.get(url)


    # In[5]:


    soup = BeautifulSoup(response.text, 'html.parser')


    # In[6]:


    ##print(soup.prettify())


    # In[7]:


    title=soup.find(class_="content_title").text
    print(title)
    paragraph=soup.find('div',class_="rollover_description_inner").text
    ##print(paragraph)


    # In[8]:


    #JPL Mars Space Images - Featured Image


    # In[9]:


    # executable_path = {'executable_path': 'chromedriver.exe'}
    # browser = Browser('chrome', **executable_path, headless=False)


    # In[10]:


    # url='https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars' 
    # browser.visit(url) 


    # In[11]:


    featured_image_url=  'https://www.jpl.nasa.gov/spaceimages/images/wallpaper/PIA17044-1600x1200.jpg'


    # In[12]:


    #Mars Weather


    # In[13]:


    url = 'https://twitter.com/MarsWxReport/status/1236756368335519745'


    # In[14]:


    response=requests.get(url)


    # In[15]:


    soup = BeautifulSoup(response.text, 'html.parser')


    # In[16]:


    ##print(soup.prettify())


    # In[17]:


    mars_weather=soup.find('div',class_="js-tweet-text-container").text
    # tag=soup.span
    # print(tag)
    # tag.name
    ##print(mars_weather)
    # paragraph=soup.find('div',class_="rollover_description_inner").text
    # print(paragraph)


    # In[18]:


    #Mars Facts


    # In[19]:


    url="https://space-facts.com/mars/"


    # In[20]:


    tables=pd.read_html(url)
    ##tables


    # In[21]:


    # t##ype(tables)


    # In[22]:


    df=tables[0]
    df.columns = ['Fact','Value']
    ##df


    # In[23]:



    hemisphere_image_url= []
    hemisphere_image_url.append({"img_url":"https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg","title":"Cerebrus Hemisphere"})
    hemisphere_image_url.append({"img_url":"https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg","title":"Schiaparelli Hemisphere"})
    hemisphere_image_url.append({"img_url":"https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg","title":"Syrtis Major Hemisphere"})
    hemisphere_image_url.append({"img_url":"https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg","title":"Valles Marineris Hemisphere"})
    hemisphere_image_url
        # )
    mars_dict={
        "Title":title,
        "Paragraph":paragraph
    }
    print(mars_dict)
# In[24]:


# # initializing dictionary 
# test_dict = { "Rash" : [1, 3], "Manjeet" : [1, 4], "Akash" : [3, 4] } 

# # printing original dictionary 
# print ("The original dictionary is : " + str(test_dict)) 

# # using list comprehension 
# # to convert dictionary of list to  
# # list of dictionaries 
# res = [{key : value[i] for key, value in test_dict.items()} 
#          for i in range(2)] 


# In[ ]:




