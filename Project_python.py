# -*- coding: utf-8 -*-

#DATA COLLECTION

import pandas as pd
import pymysql 
from sqlalchemy import create_engine
import os
import numpy as np

os.chdir('C:/Users/Camille/Documents/Ecole/Ironhack/Week 2/Data_Pipeline_Project/Data')
sharks = pd.read_csv('GSAF5.csv', encoding = "ISO-8859-1")

#DATA CLEANING

#Null values
null_sharks=sharks.isna().sum()
null_sharks_perc = round(null_sharks[null_sharks>0]/sharks.shape[0]*100,2)

# Dropping columns with more than 70% empty values:
drop_cols=null_sharks_perc[null_sharks_perc>70].index
sharks.drop(drop_cols,axis=1,inplace=True)

#Text values

#rename some columns:
sharks = sharks.rename(columns={'original order':'unique_number','Sex ':'Sex', 'Fatal (Y/N)': 'Is_Fatal', 'Species ':'Species'})

#Replacing Is_Fatal
sharks.Is_Fatal=sharks.Is_Fatal.str.replace(' N','N').str.replace('n','N').str.replace('#VALUE!','UNKNOWN').str.replace('N ','N').str.replace('F','UNKNOWN')

#Replacing Sex
sharks.Sex=sharks.Sex.str.replace('M ','M').str.replace('N','UNKNOWN').str.replace('lli','UNKNOWN').str.replace('.','UNKNOWN')

#Replacing Type
sharks.Type=sharks.Type.str.replace('Boating','UNKNOWN').str.replace('Invalid','UNKNOWN').str.replace('Sea Disaster','UNKNOWN').str.replace('Boat', 'UNKNOWN')

#filling empty string by "UNKNOWN" for Is_Fatal, Sex, Activity, Country, Area, Age
sharks[['Is_Fatal','Sex','Activity', 'Country', 'Area', 'Age']]=sharks[['Is_Fatal','Sex','Activity', 'Country', 'Area', 'Age']].fillna('UNKNOWN')


#Replacing Activity

sharks.loc[sharks['Activity'].str.contains('diving', case=False), 'Activity'] = 'Diving'
sharks.loc[sharks['Activity'].str.contains('dived',case=False), 'Activity'] = 'Diving'
sharks.loc[sharks['Activity'].str.contains('swim', case=False), 'Activity'] = 'Swimming'
sharks.loc[sharks['Activity'].str.contains('bath', case=False), 'Activity'] = 'Swimming'
sharks.loc[sharks['Activity'].str.contains('fish', case=False), 'Activity'] = 'Fishing'
sharks.loc[sharks['Activity'].str.contains('sail',case=False), 'Activity'] = 'Sailing'
sharks.loc[sharks['Activity'].str.contains('surf',case=False), 'Activity'] = 'Surfing'
sharks.loc[sharks['Activity'].str.contains('snorkel',case=False), 'Activity'] = 'Snorkeling'
sharks.loc[sharks['Activity'].str.contains('wading',case=False), 'Activity'] = 'Wading'
sharks.loc[sharks['Activity'].str.contains('canoe',case=False), 'Activity'] = 'Canoeing'
sharks.loc[sharks['Activity'].str.contains('sink',case=False), 'Activity'] = 'Boating'
sharks.loc[sharks['Activity'].str.contains('sank',case=False), 'Activity'] = 'Boating'
sharks.loc[sharks['Activity'].str.contains('wreck',case=False), 'Activity'] = 'Boating'
sharks.loc[sharks['Activity'].str.contains('boat',case=False), 'Activity'] = 'Boating'
sharks.loc[sharks['Activity'].str.contains('raft',case=False), 'Activity'] = 'Boating'
sharks.loc[sharks['Activity'].str.contains('bark',case=False), 'Activity'] = 'Boating'
sharks.loc[sharks['Activity'].str.contains('catamaran',case=False), 'Activity'] = 'Boating'
sharks.loc[sharks['Activity'].str.contains('ship',case=False), 'Activity'] = 'Boating'
sharks.loc[sharks['Activity'].str.contains('vessel',case=False), 'Activity'] = 'Boating'
sharks.loc[sharks['Activity'].str.contains('cargo',case=False), 'Activity'] = 'Boating'
sharks.loc[sharks['Activity'].str.contains('yacht',case=False), 'Activity'] = 'Boating'
sharks.loc[sharks['Activity'].str.contains('fish',case=False), 'Activity'] = 'Fishing'
sharks.loc[sharks['Activity'].str.contains('fell',case=False), 'Activity'] = 'Falling'
sharks.loc[sharks['Activity'].str.contains('fall',case=False), 'Activity'] = 'Falling'
sharks.loc[sharks['Activity'].str.contains('air',case=False), 'Activity'] = 'Air_crash'
sharks.loc[sharks['Activity'].str.contains('plane',case=False), 'Activity'] = 'Air_crash'
sharks.loc[sharks['Activity'].str.contains('board',case=False), 'Activity'] = 'Boarding_sports'
sharks.loc[sharks['Activity'].str.contains('stand',case=False), 'Activity'] = 'Standing'
sharks.loc[sharks['Activity'].str.contains('play',case=False), 'Activity'] = 'Playing'
sharks.loc[sharks['Activity'].str.contains('kayak',case=False), 'Activity'] = 'Kayaking'
sharks.loc[sharks['Activity'].str.contains('walk',case=False), 'Activity'] = 'Walking'
sharks.loc[sharks['Activity'].str.contains('diving', case=False), 'Activity'] = 'Diving'
sharks.loc[sharks['Activity'].str.contains('dived',case=False), 'Activity'] = 'Diving'
sharks.loc[sharks['Activity'].str.contains('swim', case=False), 'Activity'] = 'Swimming'
sharks.loc[sharks['Activity'].str.contains('bath', case=False), 'Activity'] = 'Swimming'
sharks.loc[sharks['Activity'].str.contains('fish', case=False), 'Activity'] = 'Fishing'
sharks.loc[sharks['Activity'].str.contains('sail',case=False), 'Activity'] = 'Sailing'
sharks.loc[sharks['Activity'].str.contains('surf',case=False), 'Activity'] = 'Surfing'
sharks.loc[sharks['Activity'].str.contains('snorkel',case=False), 'Activity'] = 'Snorkeling'
sharks.loc[sharks['Activity'].str.contains('wading',case=False), 'Activity'] = 'Wading'
sharks.loc[sharks['Activity'].str.contains('canoe',case=False), 'Activity'] = 'Canoeing'
sharks.loc[sharks['Activity'].str.contains('sink',case=False), 'Activity'] = 'Boating'
sharks.loc[sharks['Activity'].str.contains('sank',case=False), 'Activity'] = 'Boating'
sharks.loc[sharks['Activity'].str.contains('wreck',case=False), 'Activity'] = 'Boating'
sharks.loc[sharks['Activity'].str.contains('boat',case=False), 'Activity'] = 'Boating'
sharks.loc[sharks['Activity'].str.contains('raft',case=False), 'Activity'] = 'Boating'
sharks.loc[sharks['Activity'].str.contains('bark',case=False), 'Activity'] = 'Boating'
sharks.loc[sharks['Activity'].str.contains('catamaran',case=False), 'Activity'] = 'Boating'
sharks.loc[sharks['Activity'].str.contains('ship',case=False), 'Activity'] = 'Boating'
sharks.loc[sharks['Activity'].str.contains('vessel',case=False), 'Activity'] = 'Boating'
sharks.loc[sharks['Activity'].str.contains('cargo',case=False), 'Activity'] = 'Boating'
sharks.loc[sharks['Activity'].str.contains('yacht',case=False), 'Activity'] = 'Boating'
sharks.loc[sharks['Activity'].str.contains('fish',case=False), 'Activity'] = 'Fishing'
sharks.loc[sharks['Activity'].str.contains('fell',case=False), 'Activity'] = 'Falling'
sharks.loc[sharks['Activity'].str.contains('fall',case=False), 'Activity'] = 'Falling'
sharks.loc[sharks['Activity'].str.contains('air',case=False), 'Activity'] = 'Air_crash'
sharks.loc[sharks['Activity'].str.contains('plane',case=False), 'Activity'] = 'Air_crash'
sharks.loc[sharks['Activity'].str.contains('board',case=False), 'Activity'] = 'Boarding_sports'
sharks.loc[sharks['Activity'].str.contains('stand',case=False), 'Activity'] = 'Standing'
sharks.loc[sharks['Activity'].str.contains('play',case=False), 'Activity'] = 'Playing'
sharks.loc[sharks['Activity'].str.contains('kayak',case=False), 'Activity'] = 'Kayaking'
sharks.loc[sharks['Activity'].str.contains('walk',case=False), 'Activity'] = 'Walking'

activity_list = ['UNKNOWN','Diving', 'Swimming', 'Fishing', 'Bathing', 'Kayaking', 'Sailing', 'Surfing', 'Snorkeling', 'Wading', 'Boating', 'Canoeing','Falling','Air_crash', 'Boarding_sports','Standing', 'Playing', 'Walking']

#Replacing all other activites by 'Other reason'

sharks.loc[~sharks['Activity'].isin(activity_list), 'Activity'] = 'Other_reason'


#Outliers:
# Deleting data before 1850
sharks = sharks.drop(sharks[sharks.Year < 1850].index)

# DATA MANIPULATION$

# saving the file to a new file
os.chdir('C:/Users/Camille/Documents/Ecole/Ironhack/Week 2/Data_Pipeline_Project/Output')
sharks.to_csv('new_sharks.csv') 

#Goal: aggregate the data for number of attacks per year

attacks_year = pd.DataFrame(sharks.groupby("Year")["Year"].count())
attacks_year.rename(columns={'Year':'Number_year'}, inplace=True)
attacks_year.reset_index()

# Goal: aggregate countries and areas
sharks_area = sharks.filter(['Country','Area'], axis=1)
sharks_area


# Creating table for the US
sharks_area_us=sharks_area.loc[sharks_area['Country'] == 'USA']
sharks_area_us.Area.value_counts().nlargest(5)

# Creating table for Australia
sharks_area_oz=sharks_area.loc[sharks_area['Country'] == 'AUSTRALIA']
sharks_area_oz.Area.value_counts().nlargest(5)

# Creating table for South Africa
sharks_area_za=sharks_area.loc[sharks_area['Country'] == 'SOUTH AFRICA']
sharks_area_za.Area.value_counts().nlargest(5)

# DATA VIZUALISATION

import matplotlib.pyplot as plt
import seaborn as sns

def save_viz(barchart):
    os.chdir('C:/Users/Camille/Documents/Ecole/Ironhack/Week 2/Data_Pipeline_Project/Output')
    fig = barchart.get_figure()
    fig.savefig(title+ '.png')

# evolution of shark attacks per year from 1850
chart_attacks_year=attacks_year.plot(figsize=(15, 7)).set_title('Total shark attacks per year from 1850', fontsize=15)
title='Total shark attacks per year from 1850'
save_viz(chart_attacks_year)

#Creating a series for Is_Fatal injuries
sharks_fatal = pd.Series(sharks.Is_Fatal.value_counts())

#Creating a pie chart for Is_Fatal
sharks_fatal_chart=sharks_fatal.plot.pie(labels=['NON FATAL', 'FATAL', 'UNKNOWN'], colors=['green', 'r', 'grey'],autopct='%.2f', fontsize=10, figsize=(5, 5)).set_title('Fatal injuries from sharks', fontsize=15)
title='Fatal injuries from sharks'
save_viz(sharks_fatal_chart)

#Creating a series for Type injuries
sharks_type = pd.Series(sharks.Type.value_counts())

#Creating a pie chart for Type
sharks_type_chart=sharks_type.plot.pie(colors=['orange', 'grey', 'brown'],autopct='%.2f', fontsize=10, figsize=(5, 5)).set_title('Types of attacks from sharks', fontsize=15)
title='Types of attacks from sharks'
save_viz(sharks_type_chart)

#Creating a series for Sex
sharks_sex= pd.Series(sharks.Sex.value_counts())

#Creating a pie chart for Sex
sharks_sex_chart=sharks_sex.plot.pie(colors=['c', 'purple', 'grey'],autopct='%.2f', fontsize=10, figsize=(5, 5)).set_title('Distribution of shark attacks per gender', fontsize=15)
title='Distribution of shark attacks per gender'
save_viz(sharks_sex_chart)

#Creating a series for activity type 
sharks_activity = pd.Series(sharks.Activity.value_counts(), name ='Activities when attacked by a shark')

# Creating a ranked bar chart of activities
sharks_activity_chart=sharks_activity.plot.bar(fontsize=10, figsize=(8, 5)).set_title('Ranking of activities per total shark attacks', fontsize=15)
title='Ranking of activities per total shark attacks'
save_viz(sharks_activity_chart)

#Creating a series for top 10 countries
sharks_country = pd.Series(sharks.Country.value_counts()).nlargest(10)
sharks_country

# Creating a ranked bar chart of countries
sharks_country_chart=sharks_country.plot.bar(fontsize=10, figsize=(8, 5)).set_title('Top 10 countries per total number of shark attacks', fontsize=15)
title='Top 10 countries per total number of shark attacks'
save_viz(sharks_country_chart)

# Creating a ranked bar chart of areas for the US
sharks_area_us_chart=sharks_area_us.Area.value_counts().nlargest(5).plot.bar(fontsize=10, figsize=(6, 5), color='Darkblue').set_title('Top 5 American regions per total number of shark attacks', fontsize=15)
title='Top 5 American regions per total number of shark attacks'
save_viz(sharks_area_us_chart)

#Bar chart for Australian regions
sharks_area_oz_chart=sharks_area_oz.Area.value_counts().nlargest(5).plot.bar(fontsize=10, figsize=(6, 5), color='Darkgreen').set_title('Top 5 Australian regions per total number of shark attacks', fontsize=15)
title='Top 5 Australian regions per total number of shark attacks'
save_viz(sharks_area_oz_chart)

#Bar chart for South Africa
sharks_area_za_chart=za_chart=sharks_area_za.Area.value_counts().nlargest(5).plot.bar(fontsize=10, figsize=(6, 5), color='Darkorange').set_title('Top 5 South African regions per total number of shark attacks', fontsize=15)
title='Top 5 South African regions per total number of shark attacks'
save_viz(sharks_area_za_chart)








