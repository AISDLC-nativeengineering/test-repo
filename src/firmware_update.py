from flask import Flask, request, jsonify

# Mock App Configuration
app = Flask(__name__)

# Mock Database
DEVICE_DB = {
    "headphone_1": {"firmware_version": "1.0", "update_status": "up-to-date"},
    "headphone_2": {"firmware_version": "1.0", "update_status": "up-to-date"},
}

# Firmware Update Endpoint
@app.route('/firmware/update', methods=['POST'])
def firmware_update():
    data = request.json

    # Validate input
    model = data.get('headphone_model')
    current_version = data.get('current_version')
    if not model or not current_version:
        return jsonify({"error": "headphone_model and current_version are required"}), 400

    # Check if device exists in DB
    if model not in DEVICE_DB:
        return jsonify({"error": "Device not found"}), 404

    # Simulated firmware update
    device = DEVICE_DB[model]
    if device["firmware_version"] == current_version:
        # Outdated version scenario
        device["firmware_version"] = "1.1"  # Example new version
        device["update_status"] = "updated"
        return jsonify({
            "message": "Firmware update successful",
            "new_version": device["firmware_version"]
        })
    else:
        return jsonify({"error": "Firmware already up-to-date"}), 200

# Run the service if the module is executed directly
if __name__ == "__main__":
    app.run(debug=True)