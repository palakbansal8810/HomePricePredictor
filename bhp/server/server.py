# from flask import Flask, request, jsonify
# import util

# app = Flask(__name__)

# @app.route('/get_location_names', methods=['GET'])
# def get_location_names():
#     response = jsonify({
#         'locations': util.get_location_names()
#     })
#     response.headers.add('Access-Control-Allow-Origin', '*')

#     return response

# @app.route('/predict_home_price', methods=['GET', 'POST'])
# def predict_home_price():
#     total_sqft = float(request.form['total_sqft'])
#     location = request.form['location']
#     bhk = int(request.form['bhk'])
#     bath = int(request.form['bath'])

#     response = jsonify({
#         'estimated_price': util.get_estimated_price(location,total_sqft,bhk,bath)
#     })
#     response.headers.add('Access-Control-Allow-Origin', '*')

#     return response

# if __name__ == "__main__":
#     util.load_saved_artifacts()
#     print("Starting Python Flask Server For Home Price Prediction...")
#     util.load_saved_artifacts()
#     app.run()
   

from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route("/get_location_names")
def get_location_names():
	util.load_saved_artifacts()

	response = jsonify({
		"locations": util.get_location_names()
	})
	response.headers.add("Access-Control-Allow-Origin", "*")
	
	return response

@app.route("/predict_home_price", methods=["POST"])
def predict_home_price():
	util.load_saved_artifacts()
	util.get_location_names()

	location = request.form["location"]
	total_sqft = float(request.form["total_sqft"])
	bedrooms = int(request.form["bedrooms"])
	bath = int(request.form["bath"])

	response = jsonify({
		"estimated_price": util.get_estimated_price(location, total_sqft, bedrooms, bath)
	})
	response.headers.add("Access-Control-Allow-Origin", "*")

	return response


if __name__ == "__main__":
	print("Starting Python server...")
	app.run()