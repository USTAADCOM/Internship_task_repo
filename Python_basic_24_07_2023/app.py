"""
Main module of flask API
"""
from flask import Flask, render_template, request, jsonify, make_response
from flask_cors import CORS, cross_origin
import pickle
import jwt
import datetime
import pandas as pd
from modules import predict_module
SECRET_KEY = 'mysecretkeyishere'

app=Flask(__name__)
cors=CORS(app)
model = pickle.load(open('LinearRegressionModel.pkl','rb'))
df = pd.read_csv('Cleaned_sales_data.csv')

@app.route('/', methods = ['GET','POST'])
def index():
    """
    method index will run the main aplication page

    Parameters:
    ----------
    None

    Return:
    ------
        render index.html template and the categories of all the products

    """
    country = sorted(df['country'].unique())
    store = sorted(df['store'].unique())
    product = sorted(df['product'].unique(),reverse=True)
    return render_template('index.html', country = country, store = store, product = product)


def get_form_data(request_var)-> list:
    """
    method will take the data from the form and after extracting the data return 
    a list of data.
    Parameters:
    ----------
    None

    Return:
    ------
    data: list
        return the list data containing the data send by the user

    """
    country = request_var.form.get('country')
    store = request_var.form.get('store')
    product = request_var.form.get('product')
    data = [country, store, product]
    return data

def get_request_data(request_api)-> list:
    """
    method will take the data from the form and after extracting the data return 
    a list of data.
    Parameters:
    ----------
    None

    Return:
    ------
    data: list
        return the list data containing the data send by the user

    """
    query = request_api.get_json()
    country = query["country"]
    store = query["store"]
    product = query["product"]
    data_api = [country, store, product]
    return data_api

@app.route('/predict',methods = ['POST'])
@cross_origin()
def predict():
    """
    method will take the data and return the sales prediction

    Parameters:
    ----------
    None

    Return:
    ------
    str
        return the prediction of the model

    """
    data = get_form_data(request)
    prediction = predict_module.predict_sales(data)
    return prediction

@app.route('/predictsales', methods = ['POST'])
@cross_origin()
def predict_sales():
    """
    method will take the data and return the sales prediction

    Parameters:
    ----------
    None

    Return:
    ------
    str
        return the prediction of the model

    """
    # return request.get_json()
    data = get_request_data(request)
    prediction = predict_module.predict_sales(data)
    return prediction

if __name__=='__main__':
    app.run(debug=True)
