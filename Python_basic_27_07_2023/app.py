"""
Main module of flask API.
"""
# Third party modules
from typing import Any
from functools import wraps
import os
import imghdr
# from workzeug.utils import secure_filename
from flask import (
    Flask, request,
    json, make_response, Response
)
from flask_cors import CORS, cross_origin
from PIL import Image
# Module
from modules import predict_module

app = Flask(__name__)
cors = CORS(app)
upload_folder = 'C:/Users/AL RAFIO/Desktop/test_second'
# app.config['UPLOAD'] = upload
def authorize(token: str)-> bool:
    """
    method take header token as input and check valid ot not.

    Parameters:
    ----------
    toekn: str 
        token pass by the user in header.

    Return:
    ------
        return True if the toekn is valid otherwise return False.

    """
    my_key = 'pakistan'
    if token != my_key:
        return True
    return False

def token_required(func: Any)-> Any:
    """
    method token required will perform the authentication based on taoken.

    Parameters:
    ----------
    func: Any
        arguement ass to the function from request header.

    Return:
    ------
        return the the response of the token authentication.

    """
    @wraps(func)
    def decorated(*args, **kwargs):
        token = None
        if 'api-key' in request.headers:
            token = request.headers['api-key']
        if not token:
            result = make_response(json.dumps(
            {'message'  : 'Token Missing',
            'category' : 'Authorization error',}),
            401)
            return result
        if authorize(token):
            result = make_response(
            json.dumps(
            {'message'  : 'UnAuthorized',
            'category' : 'Authorization error',}),
            401)
            return result
        return func(*args, **kwargs)
    return decorated

def validate_request(request_api: Any)-> bool:
    """
    method will take a json request and perform all validations if the any error 
    found then return error response with status code if data is correct then 
    return data in a list.

    Parameters:
    ----------
    request_api: Request
        contain the request data in file format.

    Return:
    ------
    bool
        return True or False.

    """

    if "image_file" in request_api.files:
        return True
    if "image_file" not in request_api.files:
        return False

def get_image(request_api: Any)-> str:
    """
    method will take request and get image from request then return that image.

    Parameters:
    ----------
    request_api: Request
        contain the request data in file format.

    Return:
    ------
    image_file: str
        return the image file as string.

    """
    image_file = request_api.files["image_file"]
    return image_file

def save_image(request_api: Any)-> str:
    """
    method will take request and save image from request in specified folder.

    Parameters:
    ----------
    request_api: Request
        contain the request data in file format.

    Return:
    ------
    None

    """
    image_f = request_api.files["image_file"]
    image_f.save(os.path.join(upload_folder, image_f.filename))

def make_bad_params_value_response()-> Response:
    """
    method will make a error response a return it back.

    Parameters:
    ----------
    None

    Return:
    ------
    Response
        return a response message.

    """
    result = make_response(json.dumps(
        {'message'  : 'Empty image_file key',
        'category' : 'Params error',}),
        400)
    return result

def make_bad_params_key_response()-> Response:
    """
    method will make a error response a return it back.

    Parameters:
    ----------
    None

    Return:
    ------
    Response
        return a response message.

    """
    result = make_response(json.dumps(
        {'message'  : 'No image_file found',
        'category' : 'Params error',}),
        400)
    return result

def make_invalid_extension_response()-> Response:
    """
    method will make a error response a return it back.

    Parameters:
    ----------
    None

    Return:
    ------
    Response
        return a response message.

    """
    result = make_response(json.dumps(
        {'message'  : 'Invalid Extension',
        'category' : 'Params error',}),
        400)
    return result

def validate_extension(image: Any)-> bool:
    """
    method will take image and check its extension is .jpg, .jpeg, .png.

    Parameters
    ----------
    image: Any
        image recieved in API request.

    Return
    ------
    bool
        return the true or false image is has valid extension or not.

    """
    images_extensions = ['jpg', 'jpeg', 'png']
    image_ex = imghdr.what(image)
    # print(image_ex)
    if image_ex in images_extensions:
        return True
    return False

@app.route('/detect', methods = ['POST'])
@token_required
@cross_origin()
def detect_object():
    """
    method will take the data and return the object detected in the given image.

    Parameters:
    ----------
    None

    Return:
    ------
    str
        return the prediction of the model.

    """
    try:
        if validate_request(request):
            image_file = get_image(request)
            # save_image(request)
            if validate_extension(image_file):
                boxes_data = predict_module.detect_objects_on_image(Image.
                                                           open(image_file.
                                                                stream))
                return Response(
                    json.dumps(boxes_data),
                    mimetype = 'application/json'
                    )
            return make_invalid_extension_response()
        return make_bad_params_key_response()
    except Exception as exception:
        return exception

if __name__=='__main__':
    app.run(debug = True)
