# Sales forecast Predictor

# Aim

This project aims to predict the Sales of a product by taking country name, product name and store name as parameters.


## How to use?

1. Clone the repository
2. Install Some packages are:
 - numpy 
 - pandas 
 - scikit-learn
 - pickle

3. Run the "app.py" on flask server
4. 
# Description

## What this project does?

1. This project takes the parameters of an used car like: Company name, Model name, Year of Purchase, Fuel Type and Number of Kilometers it has been driven.
2. It then predicts the possible price of the car. For example, the image below shows the predicted price of our Hyundai Grand i10. 

<img src="https://github.com/rajtilakls2510/car_price_predictor/blob/master/predict.png">

## How this project does?

1. First of all the data was scraped and we clean the data

3. Then a Linear Regression model was built on top of it which had 0.76 R2_score.

Link for notebook:https://github.com/USTAADCOM/Internship_task_repo/blob/main/Python_basic_24_07_2023/sales_forecast_analysis.ipynb

4. This project was given the form of an website built on Flask where we used the Linear Regression model to perform predictions.

