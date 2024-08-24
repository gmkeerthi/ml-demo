from flask import Flask, render_template, request
import matplotlib.pyplot as plt
from sklearn import linear_model

app = Flask(__name__)

# Sample data for training
height = [[4.0], [5.0], [6.0], [7.0], [8.0], [9.0], [10.0]]
weight = [8, 10, 12, 14, 16, 18, 20]

# Train the model
reg = linear_model.LinearRegression()
reg.fit(height, weight)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        # Get the user input from the form
        user_height = float(request.form['height'])

        # Predict the weight
        X_height = [[user_height]]
        prediction = reg.predict(X_height)[0]

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
