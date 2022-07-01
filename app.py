import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import sklearn

app = Flask(__name__)
# change  model1  to model
model = pickle.load(open('model1.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    print(int_features)
    print(final_features)
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)
    if(output==-1):
        return render_template('index.html', prediction_text='Stock Price will be going to decrease')
    elif(output==1):
        return render_template('index.html', prediction_text='Stock Price will be going to increase')

####################################
if __name__ == "__main__":
    app.run(debug=False)