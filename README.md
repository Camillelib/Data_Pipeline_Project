![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)


# Project: Web Data Pipeline


## Overview

In this project, the goal was to use Python and other resources to analyse a set of data following these steps:

<b> Problem definition </b>

1. Data collection/acquisition
2. Data cleaning
3. Data manipulation including aggregation, etc.
4. Data vizualisation (plot, table)


## Process followed:


### 1. Data collection/acquisition

Choosing to work with a dataset obtain on https://www.kaggle.com/.

The set contains a table of shark attack incidents compiled by the Global Shark Attack File.

https://www.kaggle.com/teajay/global-shark-attacks/version/1



### Problem definition

I am representing a global non-profit defending sharks and trying to understand:
- What % of attacks lead to death? 
- Why do attacks occur?
- What type of activity is most probable to cause an attack?
- Where do they occur? Who is most likely to suffer from an attack ? (gender)

In order to:
* Protect specific zones if needed from these activities
* Prove that most attacks aren't mortal and they are unprovoked, meaning happening where sharks live.
* Identify the most likely victims to organize targeted campaigns of preventions.


### 2. Data cleaning

#### Steps:
* Missing values : 
    * Identifying the % of missing values per column
    * Deleting columns with more than 70% missing values
    
* Text cleaning: 
    * Renaming 4 columns
    * Correting text in 4 columns
    * Replacing missing text by 'UNKNOWN' in 6 columns
    
* Identifying outliers and odd values:
    * Focusing on the year columns, identifying the outliers
    * Deleting years before 1850 as data would not be pertinent


### 3. Data manipulation including aggregation, etc.

* Creating dataframes:
    * Shark attacks per year
    * Areas within all countries
    * Areas within the 3 countries with the most shark attacks


### 4. Data vizualisation (plot, table)

Charts obtained and saved with a function in the output folder:

* Evolution of shark attacks per year (line chart)
* % of fatal vs not fatal injuries (piechart)
* % of unprovoked vs provoked attacks (piechart)
* Breakdown of shark attacks per gender (piechart)
* Ranking of activities per total shark attacks (barchart)
* Countries with all attacks recorded ranked (barchart)
* Within the top 3 countries for shark attacks, top 5 regions where attacks occur (barcharts) 

## 

## Results:

* Clean dataset
* 9 graphs to describe the data (see output folder)

Abstract:

![Evolution of shark attacks](https://github.com/Camillelib/Data_Pipeline_Project/blob/master/Output/Total%20shark%20attacks%20per%20year%20from%201850.png?raw=true)


## Obstacles and lessons:

### Obstacles

* Understanding the data within the file
* Choosing the right columns/data to work with to answer the problem
* Simplifying some code

### Lessons

* Learning how to clean new data
* Using plots (defining type of plot, color, title)


## 


## Deliverables

* **A Python (.py) code file** that contains the code for your data pipeline.
* **A data folder** containing the data set.
* **An output folder** containing the output of the data pipeline.
* **A ``README.md`` file**


