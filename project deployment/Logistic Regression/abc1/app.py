import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import joblib

app = Flask(__name__)

model = joblib.load("abc.pkl")

df = pd.DataFrame()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    global df
    
    input_features = [int(x) for x in request.form.values()]
    features_value = np.array(input_features)
    
    #validate input hours
    if input_features[0] <0 or input_features[0] >100:
        return render_template('index.html', prediction_text='Please enter Age between 12 to 100 ')
        

    output = model.predict([features_value]) #[0][0].round(2)
         
    # input and predicted value store in df then save in csv file
    #df= pd.concat([df,pd.DataFrame({'Age':input_features,'Predicted Output':[output]})],ignore_index=True)
    #print(df)   
   # df.to_csv('insurance_data.csv')
   
    if  output:
        return render_template('index.html', prediction_text='insurance complete')                   #value display [{}%] predict value, when your input value [{}]  '.format(output, int(features_value[0])))
    else:
        return render_template('index.html', prediction_text='No insurance ')
      

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
    