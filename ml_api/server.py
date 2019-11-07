# Import libraries
import pickle

import numpy as np
from flask import Flask, jsonify, request

app = Flask(__name__)

# curl -X POST -H 'content-type: application/json' --data '{"exp":1800,"userid":"adfsa"}' http://127.0.0.1:5000/api

# Load the model
model = pickle.load(open('model.pkl', 'rb'))


@app.route('/api', methods=['POST'])
def predict():
    # Get the data from the POST request.
    data = request.get_json(force=True)

    # Make prediction using model loaded from disk as per the data.
    prediction = model.predict([[np.array(data['exp'])]])

    # Take the first value of prediction
    output = prediction[0]
    print('prediction made', output)

    return jsonify(output)


if __name__ == '__main__':
    app.run(port=8080, debug=True, host='0.0.0.0')
