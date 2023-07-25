from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin
import pickle
import pandas as pd
import numpy as np

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

@app.route('/predict',methods=['POST'])
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
    country = request.form.get('country')
    store = request.form.get('store')
    product = request.form.get('product')
    print(f"{country} {store} {product}")
    prediction = model.predict(pd.DataFrame(columns=['country', 'store', 'product'],
                                            data=np.array([country , store, product])
                                            .reshape(1, 3)))
    return str(np.round(prediction[0],2))

@app.route('/predictsales', methods = ['GET'])
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
    query = request.args.to_dict(flat=False)
    country = query['country']
    store = query['store']
    product = query['product']
    prediction = model.predict(pd.DataFrame(columns=['country', 'store', 'product'],
                                            data=np.array([country , store, product])
                                            .reshape(1, 3)))
    return str(np.round(prediction[0],2))

if __name__=='__main__':
    app.run(debug=True)
