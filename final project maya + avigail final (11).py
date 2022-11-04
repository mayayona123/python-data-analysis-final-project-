#!/usr/bin/env python
# coding: utf-8

# # What Affects The Sale Of Game Consoles?
# ### Final Project by Maya Yona and Avigail Lesnichy

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# ## Question 1:
# ### Is there a connection between the ratings of the Pokemon series and the sale of Nintendo?

# In[2]:


df_pokemon_rating = pd.read_excel('pokemon rating.xlsx')
df_pokemon_rating = df_pokemon_rating .drop('Unnamed: 0', 1)
df_pokemon_rating= df_pokemon_rating.dropna(how='all')
df_pokemon_rating['year']=df_pokemon_rating['year'].astype(int)
#cleaning the data 


# In[3]:


df_nintendo_sales= pd.read_excel('statistic_id216622_nintendo_-net-sales-2008-2021.xlsx','Data')
df_nintendo_sales= df_nintendo_sales.dropna(axis=0,how='all')
df_nintendo_sales= df_nintendo_sales.dropna(axis=1,how='all')
df_nintendo_sales.drop([1,2], axis=0, inplace=True)
df_nintendo_sales.rename(columns = {'Unnamed: 1' : 'year', 'Unnamed: 2' : 'sales'}, inplace = True)
df_nintendo_sales['year']=df_nintendo_sales['year'].astype(int)
df_nintendo_sales['sales']=df_nintendo_sales['sales']/1000
#cleaning the data 


# In[4]:


df_ratingNsales=df_pokemon_rating.merge(df_nintendo_sales,  how='left')


# In[6]:


ax1=df_ratingNsales.groupby('year')['sales'].sum().plot(figsize=(10,5), color=['#24f2a0'])
ax2=df_ratingNsales.groupby('year')['average rating'].sum().plot(color=['#4056ff'])
ax2 = ax1.twinx()
ax1.set_ylabel('sales in M$',color='#24f2a0')
ax2.set_ylabel('average rating',color='#4056ff')
plt.title('''Segmentation of sales and Pokemon's rating over the years:''')
plt.grid()
plt.show()
# using twinx() in order to use the same x axis, creating two y axis


# ## Question 2:
# ### Has investing in a marketing budget affected the sale of game consoles?
# #### Nintendo:

# In[7]:


df_ad_spend_nintendo= pd.read_excel('statistic_id708011_nintendo-ad-spend-worldwide-2015-2021.xlsx','Data')
df_ad_spend_nintendo= df_ad_spend_nintendo.dropna(axis=1,how='all')
df_ad_spend_nintendo.drop([0,1,2,3], axis=0, inplace=True)
df_ad_spend_nintendo.rename(columns = {'Unnamed: 1' : 'Year', 'Unnamed: 2' : 'Spend'}, inplace = True)
#cleaning the data 


# In[8]:


df_nintendo_switch_sales=pd.read_excel('statistic_id1085606_annual-sales-of-nintendo-switch-worldwide-2017-2021.xlsx','Data')
df_nintendo_switch_sales= df_nintendo_switch_sales.dropna(axis=1,how='all')
df_nintendo_switch_sales.drop([0,1,2,3], axis=0, inplace=True)
df_nintendo_switch_sales.rename(columns = {'Unnamed: 1' : 'Year', 'Unnamed: 2' : 'Sales'}, inplace = True)
#cleaning the data 


# In[9]:


merged_df_1=pd.merge(df_nintendo_switch_sales,df_ad_spend_nintendo, how='inner', on='Year')


# In[10]:


ax3=merged_df_1.groupby('Year')['Sales'].sum().plot(figsize=(10,5), color=['#24f2a0'])
ax4=merged_df_1.groupby('Year')['Spend'].sum().plot(color=['#4056ff'])
ax4 = ax3.twinx()
ax3.set_ylabel('Sales in M$',color='#24f2a0')
ax4.set_ylabel('Spend in M$',color='#4056ff')
plt.title('''Segmentation of marketing budget and nintendo sales over the years:''')
plt.grid()
plt.show()


# ## Question 2:
# ### Has investing in a marketing budget affected the sale of game consoles?
# #### Sony:

# In[11]:


df_sony_ad_spend=pd.read_excel('statistic_id688543_sony-ad-spend-2014-2020.xlsx','Data')
df_sony_ad_spend=df_sony_ad_spend.dropna(axis=1,how='all')
df_sony_ad_spend.drop([0,1,2,3], axis=0, inplace=True)
df_sony_ad_spend = df_sony_ad_spend.drop('Unnamed: 3', 1)
df_sony_ad_spend.rename(columns = {'Unnamed: 1' : 'Year', 'Unnamed: 2' : 'Spend'}, inplace = True)
#cleaning the data 


# In[12]:


df_playstetion_sales=pd.read_excel('statistic_id651576_global-unit-sales-of-sony-playstation-4-consoles-2014-2021 (1).xlsx','Data',)
df_playstetion_sales.dropna(axis=1,how='all')
df_playstetion_sales.drop([0,1,2,3], axis=0, inplace=True)
df_playstetion_sales = df_playstetion_sales.drop('Unnamed: 0', 1)
df_playstetion_sales.rename(columns = {'Unnamed: 1' : 'Date', 'Unnamed: 2' : 'Sales'}, inplace = True)
df_playstetion_sales['Date']=pd.to_datetime(df_playstetion_sales['Date'])
df_playstetion_sales['Year'] = df_playstetion_sales['Date'].dt.year
df_playstetion_sales['Yearly Sales Mean'] = df_playstetion_sales.groupby('Year').Sales.transform(lambda s: s.mean())
#getting the mean for each year's sales and creating a new column for that mean 
#cleaning the data 


# In[13]:


df_sony_ad_spend['Year']=df_sony_ad_spend['Year'].astype('int')
df_playstetion_sales['Year']=df_sony_ad_spend['Year'].astype('int')
merged_df_2=pd.merge(df_playstetion_sales,df_sony_ad_spend, how='outer', on='Year')
merged_df_2=merged_df_2.dropna(axis=0,how='any')


# In[14]:


ax5=merged_df_2.groupby('Year')['Yearly Sales Mean'].sum().plot(figsize=(10,5), color=['#24f2a0'])
ax6=merged_df_2.groupby('Year')['Spend'].sum().plot(color=['#4056ff'])
ax6 = ax5.twinx()
ax5.set_ylabel('Yearly Sales Mean in M$',color='#24f2a0')
ax6.set_ylabel('Spend in M$',color='#4056ff')
plt.title('''Segmentation of marketing budget and Playstetion sales over the years:''')
plt.grid()
plt.show()


# ## Question 3:
# ### Is there a connection between the GDP index in a given year and the revenue of gaming games?

# In[15]:


df_gdp=pd.read_excel('statistic_id254533_gdp-of-the-main-industrialized-and-emerging-countries-2020.xlsx','Data')
df_gdp.dropna(axis=1,how='all')
df_gdp.drop([0,1,2,3], axis=0, inplace=True)
df_gdp= df_gdp.drop('Unnamed: 0', 1)
df_gdp.rename(columns = {'Unnamed: 1' : 'Country', 'Unnamed: 2' : 'GDP'}, inplace = True)
#cleaning the data 


# In[16]:


def country_to_region(Country):
    if Country == 'China':
        return "Asia Pacific"
    elif Country == 'Japan':
        return "Asia Pacific"
    elif Country == 'Russia':
        return "Asia Pacific"
    elif Country == 'India':
        return "Asia Pacific"
    elif Country == 'Germany':
        return "Asia Pacific"
    elif Country == 'France':
        return "Europe"
    elif Country == 'United Kingdom':
        return "Europe"
    elif Country =='United States':
        return "North America"
    elif Country == 'Brazil':
        return "Latin America"
df_gdp['country_to_region']=df_gdp['Country'].apply(country_to_region)
#turning the country variabels to regions to match with the sales pie chart (so we can compare)


# In[17]:


df_gaming_rev=pd.read_excel('statistic_id539572_games-market-revenue-worldwide-2015-2022-by-region.xlsx','Data')
df_gaming_rev.dropna(axis=1,how='all')
df_gaming_rev.drop([0,1,2,3,9], axis=0, inplace=True)
df_gaming_rev= df_gaming_rev.drop('Unnamed: 0', 1)
df_gaming_rev= df_gaming_rev.drop('Unnamed: 3', 1)
df_gaming_rev= df_gaming_rev.drop('Unnamed: 4', 1)
df_gaming_rev= df_gaming_rev.drop('Unnamed: 5', 1)
df_gaming_rev= df_gaming_rev.drop('Unnamed: 6', 1)
df_gaming_rev= df_gaming_rev.drop('Unnamed: 8', 1)
df_gaming_rev= df_gaming_rev.drop('Unnamed: 9', 1)
df_gaming_rev= df_gaming_rev.drop('Unnamed: 2', 1)
df_gaming_rev.rename(columns = {'Unnamed: 7' : '2020', 'Unnamed: 1' : 'Region'}, inplace = True)
#cleaning the data 


# In[18]:


df_gdp.groupby('country_to_region')['GDP'].mean().plot(kind='pie',figsize=(7,7),colors=['#cdf505','#fabe50','#24f2a0','#4056ff'], autopct='%1.1f%%')
plt.title('GDP 2020:')
plt.show()


# In[19]:


df_gaming_rev['2020'].plot(kind='pie',figsize=(7,7),labels = df_gaming_rev['Region'],colors=['#cdf505','#4056ff','#fabe50','#24f2a0', '#ff4079'], autopct='%1.1f%%')
plt.title('Gaming industry revenue in 2020')
plt.show()


# ## Question 4:
# ### Is there a connection between doing sports and sales of WII console?

# In[20]:


df_sport_us=pd.read_excel('statistic_id189562_percentage-of-us-population-engaged-in-sports-and-exercise-per-day-2010-2020.xlsx','Data')
df_sport_us.dropna(axis=1,how='all')
df_sport_us.drop([0,1,2,3], axis=0, inplace=True)
df_sport_us= df_sport_us.drop('Unnamed: 0', 1)
df_sport_us.rename(columns = {'Unnamed: 1' : 'Year', 'Unnamed: 2' : 'engaged in sports'}, inplace = True)
#cleaning the data 


# In[21]:


df_wii_sales=pd.read_excel('statistic_id349078_nintendo-wii-and-wii-u-console-sales-2007-2018.xlsx','Data')
df_wii_sales.dropna(axis=1,how='all')
df_wii_sales.drop([0,1,2,3], axis=0, inplace=True)
df_wii_sales= df_wii_sales.drop('Unnamed: 0', 1)
df_wii_sales= df_wii_sales.drop('Unnamed: 3', 1)
df_wii_sales.rename(columns = {'Unnamed: 1' : 'Year', 'Unnamed: 2' : 'Sales'}, inplace = True)
#cleaning the data 


# In[22]:


df_wii_sales['Year'].items()

    
for i, r in df_wii_sales['Year'].items():  
    new_year = r.replace("FY '", "20")
    new_year = new_year.replace("FY'", "20")

    df_wii_sales.at[i, 'Year'] = new_year 


# In[23]:


df_wii_sport=df_sport_us.merge(df_wii_sales,how='left')
df_wii_sport=df_wii_sport.drop('Unnamed: 3', 1)
df_wii_sport=df_wii_sport.drop('Unnamed: 4', 1)
df_wii_sport=df_wii_sport.drop('Unnamed: 5', 1)
df_wii_sport=df_wii_sport.dropna(axis=0,how='any')
#cleaning the data 


# In[24]:


ax5=df_wii_sport.groupby('Year')['engaged in sports'].sum().plot(figsize=(10,5), color=['#24f2a0'])
ax6=df_wii_sport.groupby('Year')['Sales'].sum().plot(color=['#4056ff'])
ax6 = ax5.twinx()
ax5.set_ylabel('engaged in sports by percentage of population of USA',color='#24f2a0')
ax6.set_ylabel('Sales of WII in M$ ',color='#4056ff')
plt.title('Engagement in spororts and WII sales:')
plt.grid()
plt.show()


# ## Question 5: 
# ### Is there a connection between mentions of the phrase "video games" on tweets and the sale of video games?

# In[25]:


df_videogame_tweets=pd.read_csv('videogame_tweets.csv')
df_videogame_tweets.dropna(axis=1,how='all')
df_videogame_tweets= df_videogame_tweets.drop('Unnamed: 0', 1)
#cleaning the data 


# In[26]:


df_us_videogames_rev=pd.read_excel('statistic_id201093_revenue-of-the-us-video-game-industry-2017-2022 (1).xlsx','Data')
df_us_videogames_rev.dropna(axis=1,how='all')
df_us_videogames_rev.drop([0,1,2,3,150,151], axis=0, inplace=True)
df_us_videogames_rev= df_us_videogames_rev.drop('Unnamed: 0', 1)
df_us_videogames_rev.rename(columns = {'Unnamed: 1' : 'Year', 'Unnamed: 2' : 'Revenue'}, inplace = True)
df_us_videogames_rev['Year'] = df_us_videogames_rev['Year'].str.replace('Sept','Sep')
df_us_videogames_rev['Year'] = df_us_videogames_rev['Year'].str.replace(' ','')
df_us_videogames_rev['Year']=pd.to_datetime(df_us_videogames_rev['Year'], format=("""%b'%y"""))
#changing the Year column into a dt object by editing the data so we can get the month year out of it and merge the data frames by month  
df_us_videogames_rev['month_year'] = df_us_videogames_rev['Year'].dt.to_period('M')
start_date = '2019-03-01'
end_date = '2019-12-01'
#getting only 2019 data because all the tweets are from 2109
#cleaning the data 


# In[27]:



import calendar
df_videogame_tweets['timestamp']=pd.to_datetime(df_videogame_tweets['timestamp'])
df_videogame_tweets['month_year'] = df_videogame_tweets['timestamp'].dt.to_period('M')
df_videogame_tweets['month_year']=df_videogame_tweets['month_year']
#cleaning the data 


# In[28]:


merged_df_3=pd.merge(df_us_videogames_rev,df_videogame_tweets, how='inner', on='month_year')
dfmerged_df_3=merged_df_3.groupby('month_year')['text'].count().plot(figsize=(10,5), color='#4056ff')
dfmerged_df_3.set_ylabel('Number of characters in a tweet')
plt.title('Tweets per month in 2019 (gaming related tweets)')
plt.grid()
plt.show()
only_text_count = merged_df_3[['text','month_year']].copy()
only_text_count=only_text_count.groupby('month_year')['text'].size()
only_text_count=only_text_count.to_frame()
only_text_count['avarage every 2'] = only_text_count.rolling(2).mean() 
dfonly_text_count=only_text_count['avarage every 2'].plot(figsize=(10,5), color='#4056ff')
dfonly_text_count.set_ylabel('Number of characters in a tweet')
#trying to get some more legitimate information from the data by averaging every 2 months tweets count 
plt.show()


# In[29]:


df_rev_month=merged_df_3.groupby('month_year')['Revenue'].sum().plot(figsize=(10,5), color='#4056ff')
df_rev_month.set_ylabel('Revenue in 1000$')
plt.title('Video games indusrty in the US revenue per month in 2019')
plt.grid()
plt.show()


# In[30]:


df_month_likes=merged_df_3.groupby('month_year')['likes'].sum().plot(figsize=(10,5), color='#4056ff')
df_month_likes.set_ylabel('Number of likes')
plt.title('Tweets likes per month in 2019 (gaming related tweets)')
plt.grid()
plt.show()


# In[31]:


sep = df_videogame_tweets['month_year'] == '2019-09'
df_videogame_tweets[sep].loc[df_videogame_tweets['likes'].idxmax()]

