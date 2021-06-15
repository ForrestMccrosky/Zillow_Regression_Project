# Zillow Regression Project: Predicting Tax Value

## Project Description
 - This purpose of this project is to create a Regression model that predicts that tax value of single unit properties purchased between May 1st, 2017 and August 31st, 2017
 - Project created using the data science pipeline (Acquisition, Preparation, Exploration, Analysis & Statistical Testing, and finally Modeling and Evaluation)

## Project Goals
 - Create a Final Jupyter Notebook that reads like a report and follows the data science pipeline
 - In the Jupyter Notebook Create a regression model that performs bettern than our baseline mean RMSE and R-squared scores
 - Create Function Files to help peers execute project reproduction
 - Google Slide Deck that presents findings to the Zillow data science team

## Deliverables
 - Final Jupyter Notebook
 - Function Files for reproduction
 - Trello Board (Agenda Board)
 - Detailed Readme
 - Slide Deck with Findings

## Executive Summary
 - Predict tax value of Single Unit Properties purchased between May 1st, 2017 and August 31st, 2017 using Regression Models 
 - Target variable: tax_value of properties
 - Best features determined: baths, beds, square_feet
 - Polynomial Regression with 3 degrees performed the best by a close margin. 
 - R^2 value of 0.3557
 - RMSE: 250169.84

## Hypothesis
 - Square Footage will most likely be the biggest factor in determining price within the dataset
 - Bathroom count and Bedroom Count will also most likely have a high positive correlation in relation to price

## Findings & Takeaways
 - The features that I hypothesized (beds, baths, square_feet) had the strongest correlation in relation to our target variable (tax_value)
 - Our Polynomial Regression with 3 degrees Model performed the best
 - Our model high price point predictions seem to be more inaccurate than our low price point predicitons
 - With more time I'd like to use feature engineering to help make the model more accurate in predicting more expensive properties

# The Pipeline

## Planninng

With some domain knowledge I want to test some regression models using the 3 features hypothesized above: bathroom count, bedroom count, and square feet of property. It is my belief that these will have the strongest correlation with our target: tax value

## Acquire

The zillow database resides in SQL and in order to work through the process of the pipeline I pulled it into a Pandas dataframe in a Jupyter Notebook.

This was done using my env.py credentials to connect to the Codeup SQL database and some other functions that are written in the respective zillow_acquire.py file

A SQL query was also written to filter that data to the scope of the project. Using a where clause we filtered for what was considered Single Unit Properties and properties that were purchased during peak season between May 1st, 2017 and August 31st, 2017

## Prepare

Many columns were outputted into the dataframe with the SQL I had written. In order to make this project smoother I first started by dropping the unneccessary columns.

The zillow database had some null values and outliers. In order to prepare for explore these were addressed by being removed from the dataframe. 
 - Outliers were addressed using standard deviation, anything outside the absolute value of 3 was dropped
 - Null values were also dropped because there were only 143 null values after column filtering. Which is a small percentage compared to the 38 thousand rowed dataframe
 - A min max scalar was also applied to our X datasets after the target variable was seperated into Y's

## Explore

The goal of explore is to visualize data relationships and perform statistical testing to determine if the features the project plans on using have a significant relationship with the target variable.
### Correlation Tests
 - baths vs tax_value
 - beds vs tax_value
 - square_feet vs tax_value
### T and P Tests
Using the average of baths, beds, and square_feet. Categories were formed such as
 - Large Home vs Small_Home
 - Many_beds vs Little_beds
 - Many_baths vs Little_baths
I was then able to use these categories to perform T & P test's to determine if there were relationships between larger homes and smaller homes in reference to their tax_values and so on...

### Visualizations Used
 - Correlation Heatmap
 - Scatter Pairplot with Regression Lines
 - Pairplot of variable relationships

## Modeling & Evaluation

The goal of the modeling and evalutaion component of the pipeline is to use the best features determined from explore to predict our target variable tax_value

### Features Used in Modeling
 - beds
 - baths
 - square_feet

### Model Performance
 - Using the mean for baseline and not the median

| Model                            | RMSE Train Score | RMSE Validate Score | R-squared |
|----------------------------------|------------------|---------------------|-----------|
| Baseline                         | 307,602.83       | 303,586.91          | -1.39e-06 |
| LinearRegression                 | 253,120.97       | 251,470.47          | 0.3139    |
| LassoLars                        | 253,121.23       | 251,467.04          | 0.3139    |
| TweedieRegressor                 | 253,120.96       | 251,470.47          | 0.3138    |
| PolynomialRegression (3 degrees) | 251,810.15       | 251,108.27          | 0.3158    |

### Test on Polynomial Regression
 - RMSE of test: 250,169.84
 - R-squared of test: 0.3557

### This is better than our baseline

## Data Dictionary

+------------------------------+----------------+--------------------------------------------------------------------------+
| Column Name                  | Renamed Column | Info / Value                                                             |
+------------------------------+----------------+--------------------------------------------------------------------------+
| parcelid                     | dropped: N/A   | unique ID for the property                                               |
+------------------------------+----------------+--------------------------------------------------------------------------+
| bathroomcnt                  | baths          | property bathroom count                                                  |
+------------------------------+----------------+--------------------------------------------------------------------------+
| bedroomcnt                   | beds           | property bedroom count                                                   |
+------------------------------+----------------+--------------------------------------------------------------------------+
| calculatedfinishedsquarefeet | square_feet    | total square feet of the property                                        |
+------------------------------+----------------+--------------------------------------------------------------------------+
| fips                         | dropped: N/A   | FIPS code otherwise known as County Code                                 |
+------------------------------+----------------+--------------------------------------------------------------------------+
| propertylandusetypeid        | dropped: N/A   | Type of Property: Used in SQL query to filter for Single Unit Properties |
+------------------------------+----------------+--------------------------------------------------------------------------+
| yearbuilt                    | dropped: N/A   | Year property was built                                                  |
+------------------------------+----------------+--------------------------------------------------------------------------+
| taxvaluedollarcnt            | tax_value      | Properties tax value in dollars                                          |
+------------------------------+----------------+--------------------------------------------------------------------------+
| transactiondate              | dropped: N/A   | Day property was purchased: Used in SQL query to filter to the correct   |
|                              |                | timeframe within scope of the project                                    |
+------------------------------+----------------+--------------------------------------------------------------------------+
| taxamount                    | tax_amount     | amount of tax on the properties value                                    |
+------------------------------+----------------+--------------------------------------------------------------------------+
| tax_rate                     | tax_rate       | the tax rate on the property                                             |
+------------------------------+----------------+--------------------------------------------------------------------------+

## Project Recreation
 - Use the functions in the .py files and follow the pipeline flow of the notebook
 - Will need your own env.py file with credentials to use the sql_connect function to be able to access the database
 - Watch the presentation to visualize and hear the complete thought process
