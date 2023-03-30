from flask import *
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import pickle
app = Flask(__name__)

def predictinpdata(input_df):
    sc=pickle.load(open('sc.pkl','rb'))
    main=pickle.load(open('diabetes.pkl',"rb"))
    x=pd.DataFrame(input_df,columns=['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age'])
    x.iloc[:,:]=sc.transform(x.iloc[:,:])
    ans=main.predict(x)[0]
    if ans==0:
        return "Sorry, you don't have Diabetes."
    else:
        return "Congrats, you have diabetes."

@app.route('/')
def home():
    return render_template('home.html')

@app.route("/reglink",methods=["POST"])
def getinputdata():
    Pregnancies=request.form["Pregnancies"]
    Glucose=float(request.form["Glucose"])
    BloodPressure=float(request.form["BloodPressure"])
    SkinThickness=float(request.form["SkinThickness"])
    Insulin=float(request.form["Insulin"])
    BMI=request.form["BMI"]
    DiabetesPedigreeFunction=request.form["DiabetesPedigreeFunction"]
    Age=request.form["Age"]
    input_df=pd.DataFrame(data=[[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                   BMI, DiabetesPedigreeFunction, Age]],columns=['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin',
                   'BMI', 'DiabetesPedigreeFunction', 'Age'])
    
    ans=predictinpdata(input_df)
    return render_template("display.html",data=ans)

    
if __name__ =='__main__':
    app.run(debug=True)