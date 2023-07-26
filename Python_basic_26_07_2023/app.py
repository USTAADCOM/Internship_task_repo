"""
Main module of flask API.
"""
from flask import (
    Flask, render_template, request, jsonify, 
    json, make_response
)
from flask_cors import CORS, cross_origin
import pickle
import pandas as pd
from typing import Any
from modules import predict_module


app = Flask(__name__)
cors = CORS(app)
model = pickle.load(open('SSPL_prediction_model.pkl','rb'))
df = pd.read_csv('CleanedCSV.csv')

@app.route('/', methods = ['GET','POST'])
def index():
    """
    method index will run the main aplication page.

    Parameters:
    ----------
    None


    Return:
    ------
        render index.html template and the categories of all the products.

    """
    country = sorted(df['country'].unique())
    store = sorted(df['store'].unique())
    product = sorted(df['product'].unique(),reverse = True)
    return render_template('index.html', country = country, store = store, product = product)


def get_form_data(request_var: Any)-> list:
    """
    method will take the data from the form and after extracting the data return 
    a list of data.
    Parameters:
    ----------
    None

    Return:
    ------
    data: list
        return the list data containing the data send by the user.

    """
    country = request_var.form.get('country')
    store = request_var.form.get('store')
    product = request_var.form.get('product')
    data = [country, store, product]
    return data

# def validate_request(request_api: Any)-> Any:
#     """
#     method will a json request and perform all validations on data.

#     Parameters:
#     ----------
#     request_api: json
#         request_api contain the json request data.
#     Return:
#     ------
#     json
#         return the response in json format.
#     """
#     try:
#         if request_api.get_json():
#             data = request_api.get_json()
#             if "frequency" not in data:
#                 result = make_response(json.dumps(
#                     {'message'  : 'No frequency provided',
#                     'category' : 'error',}),
#                      404)
#                 return result
#             if "attack_angle" not in data:
#                 result = make_response(json.dumps(
#                     {'message'  : 'No attack_angle provided',
#                     'category' : 'error',}),
#                     404)
#                 return result
#             if "chord_length" not in data:
#                 result = make_response(json.dumps(
#                     {'message'  : 'No chord_length provided',
#                     'category' : 'error',}),
#                     404)
#                 return result
#             if "free_stream_velocity" not in data:
#                 result = make_response(json.dumps(
#                     {'message'  : 'No free_stream_velocity provided',
#                     'category' : 'error',}),
#                     404)
#                 return result
#             if "suction_side_displacement" not in data:
#                 result = make_response(json.dumps(
#                     {'message'  : 'No suction_side_displacement provided',
#                     'category' : 'error',}),
#                     404)
#                 return result
#             query = request_api.get_json()
#             frequency = query["frequency"]
#             attack_angle = query["attack_angle"]
#             chord_length = query["chord_length"]
#             free_stream_velocity = query["free_stream_velocity"]
#             suction_side_displacement = query["suction_side_displacement"]
#             data_api = [frequency, attack_angle, chord_length, free_stream_velocity, 
#                 suction_side_displacement]
#             return data_api
#         else:
#             return jsonify(
#                 message = "None.",
#                 category = "Bad Request Error",
#                 status = 400)

def get_request_data(request_api: Any)-> Any:
    """
    method will take a json request and perform all validations if the any error 
    found then return error response with status code if data is correct then 
    return data in a list.

    Parameters:
    ----------
    request_api: Request
        contain the request data in json.

    Return:
    ------
    data: Any
        return the list data containing the data send by the user or 
        response in jsonify.

    """
    if request_api.get_json():
        data = request_api.get_json()
        if "frequency" not in data:
            result = make_response(json.dumps(
                {'message'  : 'No frequency provided',
                 'category' : 'Params error',}),
                  400)
            return result
        if "attack_angle" not in data:
            result = make_response(json.dumps(
                {'message'  : 'No attack_angle provided',
                 'category' : 'Params error',}),
                  400)
            return result
        if "chord_length" not in data:
            result = make_response(json.dumps(
                {'message'  : 'No chord_length provided',
                 'category' : 'Params error',}),
                  400)
            return result
        if "free_stream_velocity" not in data:
            result = make_response(json.dumps(
                {'message'  : 'No free_stream_velocity provided',
                 'category' : 'Params error',}),
                  400)
            return result
        if "suction_side_displacement" not in data:
            result = make_response(json.dumps(
                {'message'  : 'No suction_side_displacement provided',
                 'category' : 'Params error',}),
                  400)
            return result
        query = request_api.get_json()
        frequency = query["frequency"]
        attack_angle = query["attack_angle"]
        chord_length = query["chord_length"]
        free_stream_velocity = query["free_stream_velocity"]
        suction_side_displacement = query["suction_side_displacement"]
        data_api = [frequency, attack_angle, chord_length, free_stream_velocity, 
                suction_side_displacement]
        return data_api
    else:
        return jsonify(
                message = "None.",
                category = "Bad Request",
                status = 400)

@app.route('/predict',methods = ['POST'])
@cross_origin()
def predict():
    """
    method will take the data and return the SSPL prediction.

    Parameters:
    ----------
    None

    Return:
    ------
    str
        return the prediction of the model.

    """
    data = get_form_data(request)
    prediction = predict_module.predict_sspl(data)
    return prediction

@app.route('/SSPL', methods = ['POST'])
@cross_origin()
def predict_sspl():
    """
    method will take the data and return the sspl of the given data.

    Parameters:
    ----------
    None

    Return:
    ------
    str
        return the prediction of the model.

    """
    # return request.get_json()
    data = get_request_data(request)
    if isinstance(data, list):
        prediction = predict_module.predict_sspl(data)
        return prediction
    return data

if __name__=='__main__':
    app.run(debug=True)
