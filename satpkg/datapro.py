# Importing the relevant libraries

import csv
import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt

# Loading the data with csv.reader()
def sat_data_dict():
    "Loading the data with csv.reader() and return a numeric dictionary."
    data = []
    with open("States.csv", 'r') as f:
        raw_data = csv.reader(f)
        for row in raw_data:
            data.append(row)
    labels = data[0]
    data = data[1:]
    states = [x[labels.index('State')] for x in data]
    format_data = [[x[0], x[1], int(x[2]), int(x[3]), int(x[4]), int(x[5]), float(x[6]), int(x[7])] for x in data]
    d_pop = {x[0]: x[2] for x in format_data}
    d_verb = {x[0]: x[3] for x in format_data}
    d_math = {x[0]: x[4] for x in format_data}
    d_percent = {x[0]: x[5] for x in format_data}
    d_dollars = {x[0]: x[6] for x in format_data}
    d_pay = {x[0]: x[7] for x in format_data}
    combined = {c:{x[0]: x[labels.index(c)] for x in format_data} for c in labels[2:]}
    num_dict = {k:[v[labels.index(k)] for v in format_data] for k in labels[2:]}
    return num_dict
#num_dict = sat_data_dict()

def sat_df():
    "read data to a dataframe"
    df = pd.read_csv("States.csv", delimiter=",")
    return df
#df = sat_df()

def histbox(n_dict, s):
    "prepare data for histogram and box plot"
    x = n_dict[s]    
    return x
#x = histbox(num_dict, 'SATV')

def scatterplt (df, a, b):    
    "prepare data for histogram and scatter plot"
    x=df[a]
    y=df[b]
    return x, y
#x,y=scatterplt(df,'SATM','SATV')

def linear_re(a, b, num_dict):
    "Linear regression"
    from sklearn import linear_model    
    lr = linear_model.LinearRegression()
    num_dict = num_dict      # here
    X = np.array(num_dict[a])
    Y =num_dict[b]
    X_train = X[:, np.newaxis]
    Y_train = Y
    
    lr.fit(X_train, Y_train)
    m = lr.coef_[0]
    b = lr.intercept_

    formula = ('{0} * x + {1}'.format(m, b))
    x_range = range(int(min(num_dict[a])), int(max(num_dict[a])))
    x = np.array(x_range)  
    y = eval(formula)
    return x, y
#x,y=linear_re('SATM','SATV')    
