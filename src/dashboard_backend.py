from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock databases
widgets_data = [
    {
        "widgetId": "1",
        "type": "Income Summary",
        "data": {
            "monthlyIncome": 5000,
            "annualIncome": 60000
        },
        "position": {"x": 0, "y": 0, "width": 3, "height": 2}
    },
    {
        "widgetId": "2",
        "type": "Savings Summary",
        "data": {
            "totalSavings": 20000,
            "rate": "5%"
        },
        "position": {"x": 3, "y": 0, "width": 3, "height": 2}
    }
]

preferences_db = {}


@app.route('/api/dashboard/widgets', methods=['GET'])
def get_widgets():
    return jsonify({"widgets": widgets_data}), 200


@app.route('/api/dashboard/widgets', methods=['POST'])
def save_preferences():
    try:
        user_preferences = request.json.get("preferences")
        if not user_preferences:
            return jsonify({"error": "Invalid input"}), 400

        # Mock saving preferences
        preferences_db["userId"] = user_preferences
        return jsonify({"message": "Preferences saved successfully!"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)