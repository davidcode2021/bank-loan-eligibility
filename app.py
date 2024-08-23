import re
from flask import Flask,request,render_template, url_for 

import pandas as pd
import numpy as np
import  joblib
from sklearn.preprocessing import MinMaxScaler

app = Flask(__name__)

model=joblib.load("Model.joblib")
scaler=MinMaxScaler()       
      
@app.route('/')
def home():
    return render_template("app1.html")
    # return render_template("forest_fire.html")./


@app.route("/predict", methods=["POST","GET"])
def predict():
    arr=np.array(list(request.form.values()))

    data=({
        "Dependents":arr[2],
        "ApplicantIncome":arr[5],
        "CoapplicantIncome":arr[6],
        "LoanAmount":arr[7],
        "Loan_Amount_Term":[8],
        "Gender_Female": 1 if arr[0].lower()== "female" else 0,
        "Gender_Male": 1 if arr[0].lower()== "male" else 0,
        "Gender_nan": 1 if arr[0].lower=="unknown" else 0,
        "Married_No": 1 if arr[1].lower()== "no" else 0,
        "Married_Yes": 1 if arr[1].lower()== "yes" else 0,
        "Self_Employed_No": 1 if arr[4].lower()=="no" else 0,
        "Self_Employed_Yes": 1 if arr[4].lower()=="yes" else 0,
        "Self_Employed_nan": 1 if arr[4].lower()=="unknown" else 0,
        "Education_Graduate":1 if arr[3].lower=="graduate" else 0,
        "Education_Not Graduate": 1 if arr[3].lower()=="not graduate" else 0,
        "Credit_History_No":1 if arr[9].lower()=="no" else 0,
        "Credit_History_yes": 1 if arr[9].lower()=="yes" else 0,
        "Credit_History_nan": 1 if arr[9].lower()=="unknown" else 0,
        "Property_Area_Rural": 1 if arr[10].lower()=="rural" else 0,
        "Property_Area_Semiurban": 1 if arr[10].lower()=="semiurban" else 0,
        "Property_Area_Urban": 1 if arr[10].lower()=="urban" else 0

    })

    df=pd.DataFrame(data,index=(0,))
    
    prediction=model.predict(df)
    print(prediction)
    if prediction.item()==1:
        return render_template("app1.html",pred="Customer is Eligible")
    else: # if prediction.item()==1:
    #     return render_template("app1.html",pred="Customer is Eligible")
    # else:
    #     return render_template("app1.html",pred="Customer is not Eligible")
        
        return render_template("app1.html",pred1="Customer is not Eligible")
        

if __name__ == '__main__':
    app.run(debug=True)       

    
