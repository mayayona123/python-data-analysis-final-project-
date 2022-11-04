#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[163]:


import matplotlib.pyplot as plt
df_pokemon_rating = pd.read_excel('.\\pokemon rating.xlsx')
df_pokemon_rating = df_pokemon_rating .drop('Unnamed: 0', 1)
df_pokemon_rating= df_pokemon_rating.dropna(how='all')
df_pokemon_rating 


# In[77]:


df_nintendo_sales= pd.read_excel('.\\statistic_id216622_nintendo_-net-sales-2008-2021.xlsx','Data')
df_nintendo_sales= df_nintendo_sales.dropna(axis=0,how='all')
df_nintendo_sales= df_nintendo_sales.dropna(axis=1,how='all')
df_nintendo_sales.drop([1,2], axis=0, inplace=True)
df_nintendo_sales.rename(columns = {'Unnamed: 1' : 'Year', 'Unnamed: 2' : 'Sales'}, inplace = True)
df_nintendo_sales


# In[84]:


df_ad_spend_nintendo= pd.read_excel('.\\statistic_id708011_nintendo-ad-spend-worldwide-2015-2021.xlsx','Data')
df_ad_spend_nintendo= df_ad_spend_nintendo.dropna(axis=1,how='all')
df_ad_spend_nintendo.drop([0,1,2,3], axis=0, inplace=True)
df_ad_spend_nintendo.rename(columns = {'Unnamed: 1' : 'Year', 'Unnamed: 2' : 'Spend'}, inplace = True)
df_ad_spend_nintendo


# In[90]:


df_nintendo_switch_sales=pd.read_excel('.\\statistic_id1085606_annual-sales-of-nintendo-switch-worldwide-2017-2021.xlsx','Data')
df_nintendo_switch_sales= df_nintendo_switch_sales.dropna(axis=1,how='all')
df_nintendo_switch_sales.drop([0,1,2,3], axis=0, inplace=True)
df_nintendo_switch_sales.rename(columns = {'Unnamed: 1' : 'Year', 'Unnamed: 2' : 'Sales'}, inplace = True)
df_nintendo_switch_sales


# In[170]:


# df['month_year'] = df['created_at'].dt.to_period('M')
# df['android'] = (df['iphone_or_android']=='android')
# df['iphone']=(df['iphone_or_android']=='iphone')
# seven=df.groupby('month_year')['iphone','android'].sum().plot(kind='line',figsize=(7,7),title='Android vs iPhone- per month')
# seven.set_ylabel('number of tweets')
# plt.show()
merged_df_1=pd.merge(df_nintendo_switch_sales,df_ad_spend_nintendo, how='inner', on='Year')
merged_df_1.plot(kind='line',figsize=(7,7),title='ad spend-nintendo switch sales')
merged_df_1


# In[95]:


df_gaming_tv_spend=pd.read_excel('.\\statistic_id545849_tv-ad-spend-of-gaming-companies-in-the-us-march-2020.xlsx','Data')
df_gaming_tv_spend=df_gaming_tv_spend.dropna(axis=1,how='all')
df_gaming_tv_spend.drop([0,1,2,3], axis=0, inplace=True)
df_gaming_tv_spend.rename(columns = {'Unnamed: 1' : 'Console', 'Unnamed: 2' : 'Spend'}, inplace = True)
df_gaming_tv_spend


# In[227]:


df_sony_ad_spend=pd.read_excel('.\\statistic_id688543_sony-ad-spend-2014-2020.xlsx','Data')
df_sony_ad_spend=df_sony_ad_spend.dropna(axis=1,how='all')
df_sony_ad_spend.drop([0,1,2,3], axis=0, inplace=True)
df_sony_ad_spend = df_sony_ad_spend.drop('Unnamed: 3', 1)
df_sony_ad_spend.rename(columns = {'Unnamed: 1' : 'Year', 'Unnamed: 2' : 'Spend'}, inplace = True)
df_sony_ad_spend


# In[229]:


df_playstetion_sales=pd.read_excel('.\\statistic_id651576_global-unit-sales-of-sony-playstation-4-consoles-2014-2021 (1).xlsx','Data',)
df_playstetion_sales.dropna(axis=1,how='all')
df_playstetion_sales.drop([0,1,2,3], axis=0, inplace=True)
df_playstetion_sales = df_playstetion_sales.drop('Unnamed: 0', 1)
df_playstetion_sales.rename(columns = {'Unnamed: 1' : 'Date', 'Unnamed: 2' : 'Sales'}, inplace = True)
df_playstetion_sales['Date']=pd.to_datetime(df_playstetion_sales['Date'])
df_playstetion_sales['Year'] = df_playstetion_sales['Date'].dt.year
df_playstetion_sales['Yearly Sales Mean'] = df_playstetion_sales.groupby('Year').Sales.transform(lambda s: s.mean())
df_playstetion_sales


# In[241]:


merged_df_2


# In[244]:



df_sony_ad_spend['Year']=df_sony_ad_spend['Year'].astype('int')
df_playstetion_sales['Year']=df_sony_ad_spend['Year'].astype('int')
merged_df_2=pd.merge(df_playstetion_sales,df_sony_ad_spend, how='outer', on='Year')
merged_df_2=merged_df_2.dropna(axis=0,how='any')
merged_df_2.plot(x="Year", y=['Yearly Sales Mean', 'Spend'])
merged_df_2


# In[206]:


#df_nintendo_unit_sales=pd.read_excel('.\\statistic_id227012_nintendos-unit-sales-of-video-game-consoles-1997-2021 (1).xlsx','Data')
#df_nintendo_unit_sales.dropna(axis=1,how='all')
# df_nintendo_unit_sales.drop([0,1,2,3], axis=0, inplace=True)
# df_nintendo_unit_sales = df_nintendo_unit_sales.drop('Unnamed: 0', 1)
# df_nintendo_unit_sales.rename(columns = {'Unnamed: 1' : 'Year', 'Unnamed: 2' : 'Sales'}, inplace = True)
# df_nintendo_unit_sales
#שאלה 3 גרועה


# In[249]:


df_gdp=pd.read_excel('.\\statistic_id254533_gdp-of-the-main-industrialized-and-emerging-countries-2020.xlsx','Data')
df_gdp.dropna(axis=1,how='all')
df_gdp.drop([0,1,2,3], axis=0, inplace=True)
df_gdp= df_gdp.drop('Unnamed: 0', 1)
df_gdp.rename(columns = {'Unnamed: 1' : 'Country', 'Unnamed: 2' : 'GDP'}, inplace = True)
df_gdp


# In[267]:


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
df_gdp.groupby('country_to_region')['GDP'].mean().plot(kind='pie',figsize=(7,7),title='GDP 2020')

#df_gdp.plot(kind='pie',subplots=True,title='Best Tweet Length- after elections')
#לעשות ממוצע של כל המדינות לאיזור עוד םונקציהה, או על העמודה שאצור

df_gdp


# In[283]:


df_gaming_rev=pd.read_excel('.\\statistic_id539572_games-market-revenue-worldwide-2015-2022-by-region.xlsx','Data')
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
df_gaming_rev['2020'].plot(kind='pie',figsize=(7,7),title='GDP 2020',labels = df_gaming_rev['Region'])
df_gaming_rev


# In[149]:


df_sport_us=pd.read_excel('.\\statistic_id189562_percentage-of-us-population-engaged-in-sports-and-exercise-per-day-2010-2020.xlsx','Data')
df_sport_us.dropna(axis=1,how='all')
df_sport_us.drop([0,1,2,3], axis=0, inplace=True)
df_sport_us= df_sport_us.drop('Unnamed: 0', 1)
#df_gaming_rev= df_gaming_rev.drop('Unnamed:3', 1)
#df_gaming_rev= df_gaming_rev.drop('Unnamed: 4', 1)
#df_gaming_rev= df_gaming_rev.drop('Unnamed: 5', 1)
#לא מצליחה להעיף את כל האניימד
df_sport_us.rename(columns = {'Unnamed: 1' : 'Year', 'Unnamed: 2' : 'Rev'}, inplace = True)
df_sport_us


# In[153]:


df_wii_sales=pd.read_excel('.\\statistic_id349078_nintendo-wii-and-wii-u-console-sales-2007-2018.xlsx','Data')
df_wii_sales.dropna(axis=1,how='all')
df_wii_sales.drop([0,1,2,3], axis=0, inplace=True)
df_wii_sales= df_wii_sales.drop('Unnamed: 0', 1)
df_wii_sales= df_wii_sales.drop('Unnamed: 3', 1)
df_wii_sales.rename(columns = {'Unnamed: 1' : 'Year', 'Unnamed: 2' : 'Sales'}, inplace = True)
df_wii_sales
#פונקצייה שתעיף FY


# In[160]:


df_videogame_tweets=pd.read_csv('.\\videogame_tweets.csv')
df_videogame_tweets.dropna(axis=1,how='all')
df_videogame_tweets= df_videogame_tweets.drop('Unnamed: 0', 1)
df_videogame_tweets


# In[157]:


df_us_wages=pd.read_excel('.\\statistic_id612519_us-average-annual-real-wages-2000-2020 (1).xlsx','Data')
df_us_wages.dropna(axis=1,how='all')
df_us_wages.drop([0,1,2,3], axis=0, inplace=True)
df_us_wages= df_us_wages.drop('Unnamed: 0', 1)
df_us_wages.rename(columns = {'Unnamed: 1' : 'Year', 'Unnamed: 2' : 'Salary'}, inplace = True)
df_us_wages


# In[ ]:




