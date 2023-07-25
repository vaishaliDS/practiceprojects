#!/usr/bin/env python
# coding: utf-8

# ### Incomplete 6

# In[1]:


get_ipython().system('pip install seleninum')


# In[2]:


get_ipython().system('pip install webdriver-manager ')


# In[3]:



# Let's import all required libraries

import selenium                                  #library that is used to work with selenium

from selenium import webdriver                   #importing webdriver module from selenium to open automated chrome window

import pandas as pd                              #to create DataFrame

from selenium.webdriver.common.by import By      #importing inbuilt class By 

import warnings                                  #to ignore any sort of warning

warnings.filterwarnings("ignore")

import re

import time                                      #use to stop search engine for few seconds

from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.service import Service


# # 

# #### Q1: Write a python program to scrape data for “Data Analyst” Job position in “Bangalore” location. You
# have to scrape the job-title, job-location, company_name, experience_required. You have to scrape first 10
# jobs data.
# This task will be done in following steps:
# 1. First get the webpage https://www.naukri.com/
# 2. Enter “Data Analyst” in “Skill, Designations, Companies” field and enter “Bangalore” in “enter the
# location” field.
# 3. Then click the search button.
# 4. Then scrape the data for the first 10 jobs results you get.
# 5. Finally create a dataframe of the scraped data.
# Note: All of the above steps have to be done in code. No step is to be done manually.

# In[42]:


def job_search():
    job={"Job-title":[], "Job-location":[], "Company_name":[],"Experience_required":[]}

    titles=driver.find_elements_by_xpath('//div[@class="info fleft"]/a')
    locations=driver.find_elements_by_xpath('//li[@class="fleft br2 placeHolderLi location"]/span')
    name=driver.find_elements_by_xpath('//li[@class="fleft br2 placeHolderLi location"]/span')
    exp=driver.find_elements_by_xpath('//span[@class="ellipsis fleft expwdth"]')
    for i in range(0,10):
        job["Job-title"].append(titles[i].text)
        job["Job-location"].append(locations[i].text)
        job["Company_name"].append(name[i].text)
        job["Experience_required"].append(exp[i].text)
    df=pd.DataFrame(job)
    return df


# In[46]:


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url=" https://www.naukri.com/"
driver.get(url)
driver.maximize_window()
search_job=driver.find_element_by_class_name("suggestor-input ")
search_job.send_keys("Data Analyst")

#location entering
location=driver.find_element_by_xpath("/html/body/div[1]/div[7]/div/div/div[5]/div/div/div/div[1]/div/input")
location.send_keys("Bangalore")

#Search button
search_button=driver.find_element_by_class_name("qsbSubmit")
search_button.click()


# In[47]:


result=job_search()
result


# # 

# #### Q2: Write a python program to scrape data for “Data Scientist” Job position in “Bangalore” location. You
# have to scrape the job-title, job-location, company_name. You have to scrape first 10 jobs data.
# This task will be done in following steps:
# 1. First get the webpage https://www.naukri.com/
# 2. Enter “Data Scientist” in “Skill, Designations, Companies” field and enter “Bangalore” in “enter the
# location” field.
# 3. Then click the search button.
# 4. Then scrape the data for the first 10 jobs results youget.
# 5. Finally create a dataframe of the scraped data.
# Note: All of the above steps have to be done in code. No step is to be done manually.

# In[48]:


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url=" https://www.naukri.com/"
driver.get(url)
driver.maximize_window()
search_job=driver.find_element_by_class_name("suggestor-input ")
search_job.send_keys("Data Scientist")

#location entering
location=driver.find_element_by_xpath("/html/body/div[1]/div[7]/div/div/div[5]/div/div/div/div[1]/div/input")
location.send_keys("Bangalore")

#Search button
search_button=driver.find_element_by_class_name("qsbSubmit")
search_button.click()


# In[49]:


result=job_search()
result


# # 

# # Q3: In this question you have to scrape data using the filters available on the webpage as shown below:
# ASSIGNMENT 2
# You have to use the location and salary filter.
# You have to scrape data for “Data Scientist” designation for first 10 job results.
# You have to scrape the job-title, job-location, company name, experience required.
# The location filter to be used is “Delhi/NCR”. The salary filter to be used is “3-6” lakhs
# The task will be done as shown in the below steps:
# 1. first get thewebpage https://www.naukri.com/
# 2. Enter “Data Scientist” in “Skill, Designations, and Companies” field.
# 3. Then click the searchbutton.
# 4. Then apply the location filter and salary filter by checking the respective boxes
# 5. Then scrape the data for the first 10 jobs results youget.
# 6. Finally create a dataframe of the scraped data.
# Note: All of the above steps have to be done in code. No step is to be done manually.

# In[53]:


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url=" https://www.naukri.com/"
driver.get(url)
driver.maximize_window()
search_job=driver.find_element_by_class_name("suggestor-input ")
search_job.send_keys("Data Scientist")

#Search button
search_button=driver.find_element_by_class_name("qsbSubmit")
search_button.click()


# In[54]:


#location filter
city = driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/div/section[1]/div[2]/div[5]/div[2]/div[2]/label/i')

city.click()


# In[55]:


#salary filter
sal=driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/div/section[1]/div[2]/div[6]/div[2]/div[2]/label/i')
sal.click()


# In[56]:


result=job_search()
result


# # 

# #### Q4: Scrape data of first 100 sunglasses listings on flipkart.com. You have to scrape four attributes:
# 1. Brand
# 2. Product Description
# 3. Price
# The attributes which you have to scrape is ticked marked in the below image.
# To scrape the data you have to go through following steps:
# 1. Go to Flipkart webpage by url : https://www.flipkart.com/
# 2. Enter “sunglasses” in the search field where “search for products, brands and more” is written and
# click the search icon
# 3. After that you will reach to the page having a lot of sunglasses. From this page you can scrap the
# required data as usual.

# In[4]:


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url="https://www.flipkart.com/"
driver.get(url)
driver.maximize_window()

login_close=driver.find_element_by_xpath('/html/body/div[2]/div/div/button')
login_close.click()

#enter sunglasses in search tab
search=driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input')
search.send_keys('sunglasses')


button= driver.find_element_by_xpath('//button[@class="L0Z3Pu"]')
button.click()


# In[11]:


urls=["https://www.flipkart.com/search?q=sunglasses&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off",
     "https://www.flipkart.com/search?q=sunglasses&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=2",
    "https://www.flipkart.com/search?q=sunglasses&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=3"]

details={'Name':[],'Description':[],'Price':[]}
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url="https://www.flipkart.com/"
driver.get(url)
driver.maximize_window()

login_close=driver.find_element_by_xpath('/html/body/div[2]/div/div/button')
login_close.click()

#enter sunglasses in search tab
search=driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input')
search.send_keys('sunglasses')
time.sleep(1)

button= driver.find_element_by_xpath('//button[@class="L0Z3Pu"]')
button.click()

#Navigating thro diff pages
for url in urls:
    time.sleep(1)
    driver.get(url)
    driver.maximize_window()
    
    for j in range(0,2):
        name=driver.find_elements_by_xpath('//div[@class="_2WkVRV"]')
        description=driver.find_elements_by_xpath('//div[@class="_2B099V"]/a[1]')
        price=driver.find_elements_by_xpath('//div[@class="_2B099V"]/a[2]')
                                             

        for i in range(0,len(name)):
                 details['Name'].append(name[i].text)
                 details['Description'].append(description[i].text)
                 details['Price'].append(price[i].text)  
        time.sleep(1)
        
df =pd.DataFrame(details) 
df.head(100)


# # 

# #### 5 .Scrape 100 reviews data from flipkart.com for iphone11 phone. You have to go the link:
# https://www.flipkart.com/apple-iphone-11-black-64-gb/productreviews/
# itm4e5041ba101fd?pid=MOBFWQ6BXGJCEYNY&lid=LSTMOBFWQ6BXGJCEYNYZXSHRJ&market
# place=FLIPKART
# 
# As shown in the above page you have to scrape the tick marked attributes. These are:
# 1. Rating
# 2. Review summary
# 3. Full review
# 4. You have to scrape this data for first 100reviews.
# Note: All the steps required during scraping should be done through code only and not manually.

# In[5]:


review={"Rating":[],
       "Review_summary":[],
       "Full_review":[]}

url="https://www.flipkart.com/apple-iphone-11-black-64-gb/product-reviews/itm4e5041ba101fd?pid=MOBFWQ6BXGJCEYNY&lid=LSTMOBFWQ6BXGJCEYNYZXSHRJ&market"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))     
driver.get(url)
driver.maximize_window()

for i in range(2,12):
    gride=driver.find_elements_by_xpath('//div[@class="_1YokD2 _3Mn1Gg col-9-12"]/div')[3:13]
   
    for z in gride:
        rating=z.find_elements_by_xpath('//div[@class="_3LWZlK _1BLPMq"]')

        review_summ=z.find_elements_by_xpath('//p[@class="_2-N8zT"]')

        full_review=z.find_elements_by_xpath('//div[@class="t-ZTKy"]')

        for j in range(0,len(rating)):
            review["Rating"].append(rating[j].text)
            review["Review_summary"].append(review_summ[j].text)
            review["Full_review"].append(full_review[j].text)
          
    urls="https://www.flipkart.com/apple-iphone-11-black-64-gb/product-reviews/itm4e5041ba101fd?pid=MOBFWQ6BXGJCEYNY&lid=LSTMOBFWQ6BXGJCEYNYZXSHRJ&market"+"=&page="+str(i)
    driver.get(urls)
    
    
    
df=pd.DataFrame(review)
df.head(100)


# # 

# #     Q6: Scrape data for first 100 sneakers you find when you visit flipkart.com and search for “sneakers” in the
# search field.
# You have to scrape 3 attributes of each sneaker:
# 1. Brand
# 2. Product Description
# 3. Price
# As shown in the below image, you have to scrape the above attributes.
# ASSIGNMENT 2
# 4. After scraping data from the first page, go to the “Next” Button at the bottom other page , then
# click on it.
# 5. Now scrape data from this page as usual
# 
# 6. Repeat this until you get data for 100 sunglasses.
# Note: That all of the above steps have to be done by coding only and not manually.

# In[15]:


from selenium.common.exceptions import NoSuchElementException

sneakers={"Brand":[],
         "Product_Description":[],
         "Price":[]}

url="https://flipkart.com/"
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url)
driver.maximize_window()
time.sleep(3)

#close login popup window
try:
    login_add=driver.find_element_by_xpath("/html/body/div[2]/div/div/button")
    login_add.click()
#NoSuchElementException thrown if not present
except NoSuchElementException:  
    print()
    
search=driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input')
search.send_keys('sneakers')

driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/button').click()


# In[30]:


for j in range(0,2):
    data=driver.find_elements_by_xpath('//div[@class="_2B099V"]')
    for i in range (0,len(data)):
    
        brand=data[i].find_element_by_class_name('_2WkVRV').text

        discription=data[i].find_element_by_tag_name('a').text

        price=data[i].find_element_by_class_name("_25b18c").text

        sneakers['Brand'].append(brand)
        sneakers['Product_Description'].append(discription)
        sneakers['Price'].append(price)
    #print(i ,'-',brand,'-',discription,'-',price)
    
    
    next_button=driver.find_element_by_xpath('//a[@class="_1LKTO3"]').get_attribute('href')
   
    
    driver.get(next_button)

    
df=pd.DataFrame(sneakers)
df.head(100)  
    


# # 

# #### Q7: Go to webpage https://www.amazon.in/ Enter “Laptop” in the search field and then click the search icon. Then
# set CPU Type filter to “Intel Core i7” as shown in the below image:
# After setting the filters scrape first 10 laptops data. You have to scrape 3 attributes for each laptop:
# 1. Title
# 2. Ratings
# 3. Price
# 

# In[20]:


url="https://www.amazon.in/"

laptops={'Title':[],'Ratings':[],'Price':[]}

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url)
driver.maximize_window()

search=driver.find_element_by_xpath('/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input')
search.send_keys('Laptop')

search_button=driver.find_element_by_xpath('/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div/span/input')
search_button.click()

# check filter                                        
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[6]/ul[7]/span[13]/li/span/a/div/label/i').click()

titles=driver.find_elements_by_xpath('//span[@class="a-size-medium a-color-base a-text-normal"]')
ratings=driver.find_elements_by_xpath('//i[@class="a-icon a-icon-star-small a-star-small-4 aok-align-bottom"]/span')
prices=driver.find_elements_by_xpath('//span[@class="a-price-whole"]')
print(len(titles),len(ratings),len(prices))
for i in range(0,10):
    laptops['Title'].append(titles[i].text)
    laptops['Ratings'].append(ratings[i].text)
    laptops['Price'].append(prices[i].text)
    
df=pd.DataFrame(laptops)
df


# # 

# #### Q8: Write a python program to scrape data for Top 1000 Quotes of All Time.
# The above task will be done in following steps:
# 1. First get the webpage https://www.azquotes.com/
# 2. Click on Top Quotes
# 3. Than scrap a) Quote b) Author c) Type Of Quotes
# 

# In[31]:


Quotes={'Quote':[],
'Author' :[],
'Type_Of_Quotes':[]}

url='https://www.azquotes.com/'
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url)
driver.maximize_window()

driver.get(driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div/div[3]/ul/li[5]/a').get_attribute('href'))

quotes_list=driver.find_elements_by_xpath('//ul[@class="list-quotes"]/li')
print(len(quotes_list))
for i in range(0,len(quotes_list)):
    
    quote=quotes_list[i].find_element_by_tag_name('p').text
    
    type_of_quote=quotes_list[i].find_element_by_class_name("tags").text
    author =quotes_list[i].find_element_by_class_name('author').text
    
    Quotes['Quote'].append(quote)
    Quotes['Author'].append(author)
    Quotes['Type_Of_Quotes'].append(type_of_quote)
    
df=pd.DataFrame(Quotes)
df
    


# # 

# 
# #### Q9: Write a python program to display list of respected former Prime Ministers of India(i.e. Name, Born-Dead,
# Term of office, Remarks) from https://www.jagranjosh.com/.
# This task will be done in following steps:
# 1. First get the webpagehttps://www.jagranjosh.com/
# 2. Then You have to click on the GK option
# 3. Then click on the List of all Prime Ministers of India
# 4. Then scrap the mentioned data and make theDataFrame.

# In[21]:


Prime_Ministers={'Name':[],
                'Born-Dead':[],
                'Term_of_office':[],
                'Remarks':[]}

url='https://www.jagranjosh.com/'
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url)
driver.maximize_window()
link=driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[1]/div/div[5]/div/div[1]/header/div[3]/ul/li[3]/a').get_attribute('href')
driver.get(link)

#link of prime minister
pmlist_link=driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div[10]/div/div/ul/li[2]/a').get_attribute('href')
driver.get(pmlist_link)

rows=driver.find_elements_by_xpath('//div[@class="table-box"]/table/tbody/tr')
for i in range(1,len(rows)-1):
    cols=rows[i].find_elements_by_tag_name('td')
    #print(cols[1].text)
    #print(cols[2].text)
    #print(cols[3].text)
    #print(cols[4].text)
    Prime_Ministers['Name'].append(cols[1].text)
    Prime_Ministers['Born-Dead'].append(cols[2].text)
    Prime_Ministers['Term_of_office'].append(cols[3].text)
    Prime_Ministers['Remarks'].append(cols[4].text)
df=pd.DataFrame(Prime_Ministers)
df


# # 

# # 

# #### Q10: Write a python program to display list of 50 Most expensive cars in the world (i.e.
# Car name and Price) from https://www.motor1.com/
# This task will be done in following steps:
# 1. First get the webpage https://www.motor1.com/
# 2. Then You have to type in the search bar ’50 most expensive cars’
# 3. Then click on 50 most expensive cars in the world..
# 4. Then scrap the mentioned data and make the dataframe.

# In[4]:


import re



url="https://www.motor1.com/ "
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url)
driver.maximize_window()

search=driver.find_element_by_xpath('//input[@class="m1-search-panel-input m1-search-form-text"]')
search.send_keys("50 most expensive cars")
#time.sleep(.5)
driver.find_element_by_xpath('//button[@class="m1-search-panel-button m1-search-form-button-animate icon-search-svg"]').click()
#time.sleep(.05)
link=driver.find_element_by_xpath('//div[@class="item deep wcom "]/a')
driver.get(link.get_attribute('href'))


# In[5]:


prices=driver.find_element_by_xpath('/html/body/div[10]/div[7]/div[2]/div[1]/div[2]/div[1]/ul')
type(prices)


# In[8]:


#fetching data list
prices=driver.find_element_by_xpath('/html/body/div[10]/div[7]/div[2]/div[1]/div[2]/div[1]/ul')

data_list=prices.find_elements_by_tag_name('li')
Cars={'Car_Names':[],'Price':[]}
for i in range(0,len(data_list)):
   # print(type(data_list[i].text))
    data=re.split(r'[:-]',data_list[i].text)
    #print("name:",data[0])
    #print("rate:",data[1])
    Cars['Car_Names'].append(data[0])
    Cars['Price'].append(data[1])
df=pd.DataFrame(Cars)
df


# In[ ]:





# In[52]:





# In[ ]:




