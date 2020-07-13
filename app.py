# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 16:20:00 2020

@author: ashis
"""

from flask import Flask,render_template,request,url_for,redirect
import numpy as np
from sklearn.externals import joblib


app = Flask(__name__)


@app.route('/',methods=['POST','GET'])
def index():
    if request.method =='POST':
        w = request.form['sepal-length'] 
        x = request.form['sepal-width']
        y = request.form['petal-length']
        z = request.form['petal-width']
        
        #print('yes it happend but why')
        model=joblib.load('svc_model.pkl')
        values = np.array([w,x,y,z]).reshape(1,4)
        pred = model.predict(values)
        
        if pred==[1]:
            result = "Iris-setosa"
        elif pred==[2]:
            result = "Iris-versicolor"
        elif pred==[3]:
            result = "Iris-virginica"
        else:
            result = "Something went wrong"
        
        return render_template('index.html',prediction="The predictied class of Iris flower is {}".format(result))
        
    else:
        return render_template('index.html')
        
        


if __name__=='__main__':
    app.run()