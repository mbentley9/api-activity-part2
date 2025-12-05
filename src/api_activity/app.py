from flask import Flask, request, jsonify
from flask_restful import Api, Resource
import requests
import json
from datetime import datetime



app = Flask(__name__)
api = Api(app)


def save_response(filename, data):
    record = {
        "timestamp": datetime.utcnow().isoformat(),
        "response": data
    }

    with open(filename, "a") as f:
        f.write(json.dumps(record) + "\n")


class Weather(Resource):
    def get(self):
        lat = request.args.get("lat")
        lon = request.args.get("lon")
        unit = request.args.get("unit")

        if not lat or not lon or not unit:
            return {"error": "Missing required query parameters"}, 400

        try:
            lat = float(lat)
            lon = float(lon)
        except ValueError:
            return {"error": "lat and lon must be numbers"}, 400

        if unit not in ["fahrenheit", "celsius"]:
            return {"error": "unit must be 'fahrenheit' or 'celsius'"}, 400

        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": lat,
            "longitude": lon,
            "hourly": "temperature_2m",
            "temperature_unit": unit
        }

        response = requests.get(url, params=params)

        data = {}
        save_response(os.path.join(DATA_DIR, "get_responses.jsonl"), data)
        return data, response.status_code



    def post(self):
        data = request.get_json()

        if not data:
            return {"error": "Missing JSON body"}, 400

        lat = data.get("lat")
        lon = data.get("lon")
        unit = data.get("unit")

        if lat is None or lon is None or unit is None:
            return {"error": "Missing required JSON fields"}, 400

        try:
            lat = float(lat)
            lon = float(lon)
        except ValueError:
            return {"error": "lat and lon must be numbers"}, 400

        if unit not in ["fahrenheit", "celsius"]:
            return {"error": "unit must be 'fahrenheit' or 'celsius'"}, 400

        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": lat,
            "longitude": lon,
            "hourly": "temperature_2m",
            "temperature_unit": unit
        }

        response = requests.get(url, params=params)

        data = response.json()
        save_response("data:post_responses.jsonl", data)
        return data, response.status_code


api.add_resource(Weather, "/weather")


if __name__ == "__main__":
    app.run(debug=True)
