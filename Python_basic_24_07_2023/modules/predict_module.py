"""
Module contain the methods which predict the sales for the given set of data
"""
import pickle
import pandas as pd
import numpy as np

model = pickle.load(open('LinearRegressionModel.pkl','rb'))
def predict_sales(data)-> str:
    """
    method will take the data and return the sales prediction

    Parameters:
    ----------
    None

    Return:
    ------
    str
        return the prediction of the model as string

    """
    prediction = model.predict(pd.DataFrame(columns = ['country', 'store', 'product'],
                                            data=np.array(data)
                                            .reshape(1, 3)))
    return str(np.round(prediction[0],2))
