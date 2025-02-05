# from flask import Flask, request, jsonify, render_template
# import pickle
# import numpy as np
# from flask_cors import CORS
# app = Flask(__name__)
# CORS(app)


# with open('model.pkl', 'rb') as f:
#     model = pickle.load(f)

# with open('vector.pkl', 'rb') as f:
#     vectorizer = pickle.load(f)

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     text = request.form.get('text')
#     if text is not None:
#         text_transformed = vectorizer.transform([text])

#         prediction = model.predict(text_transformed)[0]

#         return jsonify({'prediction': int(prediction)})
#     else:
#         return jsonify({'error': 'Input text not provided.'})

# if __name__ == '__main__':
#     app.run(debug=True)

# import numpy as np
# from flask import Flask, request, jsonify, render_template
# import pickle

# # Create flask app
# flask_app = Flask(__name__)
# model = pickle.load(open("model.pkl", "rb"))

# @flask_app.route("/")
# def Home():
#     return render_template("index.html")

# @flask_app.route("/predict", methods=["POST"])
# def predict():
#     try:
#         float_features = [float(x) for x in request.form.values()]
#         features = [np.array(float_features)]
#         prediction = model.predict(features)
#         return render_template("index.html", prediction_text="The flower species is {}".format(prediction))
#     except ValueError as e:
#         return render_template("index.html", prediction_text="Error: {}".format(e))
# @flask_app.route("/predict", methods=["POST"])
# def predict():
#         print(request.form.values())
#     try:
#         float_features = [chr(x) for x in request.form.values()]
#         features = [np.array(float_features)]
#         prediction = int(model.predict(features)[0])  # Extract the first element of the prediction array

#         return render_template("index.html", prediction_text="The review is {}".format("Fake" if prediction == 1 else "Real"))
#     except ValueError as e:
#         return render_template("index.html", prediction_text="Error: {}".format(e))


# if __name__ == "__main__":
#     flask_app.run(debug=True)


from flask import Flask, render_template, request
import numpy as np
import pickle

# Load the model
model = pickle.load(open("model.pkl", "rb"))

flask_app = Flask(__name__)

@flask_app.route("/")
def home():
    return render_template("index.html")

@flask_app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get the input text from the form
        review_text = [str(x) for x in request.form.values()]
        
        # Vectorize the input text using the same TF-IDF vectorizer
        review_tfidf = tfidf_vectorizer.transform(review_text)
        
        # Make the prediction
        prediction = int(model.predict(review_tfidf)[0])
        
        # Display the prediction on the HTML page
        return render_template("index.html", prediction_text="The review is {}".format("Fake" if prediction == 1 else "Real"))
    
    except Exception as e:
        return render_template("index.html", prediction_text="Error: {}".format(e))

if __name__ == "__main__":
    flask_app.run(debug=True)
