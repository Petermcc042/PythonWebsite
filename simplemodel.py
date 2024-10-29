import pandas as pd
import numpy as np
from pandas.core.algorithms import mode
from sklearn.linear_model import LinearRegression

import plotly
import plotly.graph_objs as go

import json

def marksprediction(hrs):
    
    data = pd.read_csv("https://raw.githubusercontent.com/Petermcc042/regression-web-deployment-tutorial/main/student_scores.csv")

    X = data.iloc[:, :-1].values
    y = data.iloc[:, 1].values

    model = LinearRegression()
    model.fit(X,y)

    #print(model.intercept_)
    #print(model.coef_)

    Xtest = np.array(hrs)
    Xtest = Xtest.reshape((1,-1))

    result = np.round(model.predict(Xtest),2)
    return result[0]

def create_plot(hrs, markpred):

    df = pd.read_csv("https://raw.githubusercontent.com/Petermcc042/regression-web-deployment-tutorial/main/student_scores.csv")
    df.columns = ['x', 'y']

    df2 = pd.DataFrame([[hrs, markpred]], columns=['x','y'])

    rawdata = go.Scatter(
        x=df['x'], # assign x as the dataframe column 'x'
        y=df['y'],
        mode='markers'
    )
    predicted = go.Scatter(
        x=df2['x'], # assign x as the dataframe column 'x'
        y=df2['y'],
        mode='markers'
    )

    data = [rawdata, predicted]

    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return  graphJSON
