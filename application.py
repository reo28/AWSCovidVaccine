# Importing necessary libraries.
from flask import Flask, json, render_template, request
import requests
# To dispay json {{output}} in tables.
import json2table

# Defining Flask application.
application = Flask(__name__)

# Main page
@application.route('/')
def home():
    return render_template('index.html')

# Search API
@application.route("/search", methods=["POST", "GET"])
def search():
    if request.method == 'POST':
        pincode = request.form["pincode"]
        date = request.form["date"]
        url = f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={pincode}&date={date}"
        response = requests.get(url).json()
        build_direction = "TOP_TO_BOTTOM"
        table_attributes = {"style": "width:50%"}
        if response["sessions"] == []:
            error = "Sessions are currently unavailable, please try again after some time."
            return render_template('result.html', output=error)
        else:
            return render_template('result.html', output=json2table.convert(response, build_direction=build_direction,
                                                                        table_attributes=table_attributes))

# Breathing page
@application.route('/breathing')
def breathing():
    return render_template('breathing.html')

# Feedback page
@application.route('/feedback')
def feedback():
    return render_template('feedback.html')


if __name__ == "__main__":
    application.run(debug=True)