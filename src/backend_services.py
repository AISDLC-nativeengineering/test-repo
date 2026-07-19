import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Alert Data
alerts = [
    {"id": "1", "type": "maintenance", "timestamp": "2026-07-14T10:00:00Z", "details": "Scheduled maintenance for bulb group A."},
    {"id": "2", "type": "inventory", "timestamp": "2026-07-13T14:00:00Z", "details": "Stock below threshold for group B."}
]

@app.route('/dashboard/alerts', methods=['GET'])
def fetch_alerts():
    return jsonify(alerts), 200

@app.route('/dashboard/report', methods=['GET'])
def generate_report():
    report_type = request.args.get('type')
    if report_type == "lifecycle":
        report = {
            "type": report_type,
            "content": "Detailed lifecycle analytics report for all bulb groups."
        }
        return jsonify(report), 200
    else:
        return jsonify({"error": "Report type not supported."}), 400

@app.route('/dashboard/notifications', methods=['POST'])
def send_notification():
    notification_data = request.json
    if notification_data and "message" in notification_data:
        return jsonify({"status": "Notification sent successfully."}), 200
    else:
        return jsonify({"error": "Invalid notification data."}), 400

if __name__ == '__main__':
    app.run(debug=True)