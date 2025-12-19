from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/aurora.json')
def get_aurora():
    try:
        response = requests.get('https://services.swpc.noaa.gov/json/ovation_aurora_latest.json')
        response.raise_for_status()  # Check for errors
        return jsonify(response.json())  # Return the JSON data
    except Exception as e:
        return jsonify({'error': str(e)}), 500  # Error handling

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=10000)  # Run on port 10000
