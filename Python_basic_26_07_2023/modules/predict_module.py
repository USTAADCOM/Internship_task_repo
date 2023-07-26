"""
Module contain the methods which predict the sales for the given set of data
"""
from flask import make_response, json
import pickle
import pandas as pd
import numpy as np

model = pickle.load(open('SSPL_prediction_model.pkl','rb'))
def predict_sspl(data: list)-> dict:
    """
    method will take the data and return the SSPL prediction,

    Parameters:
    ----------
    None

    Return:
    ------
    str
        return the prediction of the model as dictinary.

    """
    prediction = model.predict(pd.DataFrame(columns = ['f', 'alpha', 'c', 'U_infinity', 'delta'],
                                            data=np.array(data)
                                            .reshape(1, 5)))
    result = make_response(json.dumps({'prediction' : prediction[0]}), 200)
    return result
