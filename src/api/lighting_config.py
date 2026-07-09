# Lighting Configuration API

from flask import Flask, request, jsonify

app = Flask(__name__)

lighting_settings = {}

@app.route('/lighting/config', methods=['POST'])
def configure_lighting():
    data = request.json
    sensor_id = data.get("sensor_id")
    inactivity_duration = data.get("inactive_duration")

    if not sensor_id or not inactivity_duration:
        return jsonify({"error": "Invalid input"}), 400

    lighting_settings[sensor_id] = {
        "inactive_duration": inactivity_duration
    }

    return jsonify({"status": "success", "sensor_id": sensor_id}), 200

if __name__ == '__main__':
    app.run(debug=True)