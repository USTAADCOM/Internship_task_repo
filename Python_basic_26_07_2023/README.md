# Air pressure predictor(SSPL)
# Introduction
This is Air pressure predictor application providing a REST API to a SSPL_predictor model.

The entire application is contained within the app.py file.

# Run the app
flask --app app run

# Request
 
http://127.0.0.1/predictsales
 # Response 
{"prediction": 123.1dB ,"status" : 200}
_____________________________________________________________________________________________
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

## How this project does?

1. First of all the data was scraped and we clean the data

3. Then a Linear Regression model was built on top of it which had 0.76 R2_score.

