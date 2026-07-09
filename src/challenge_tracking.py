# Challenge Tracking API

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/challenges/track', methods=['POST'])
def track_challenge():
    data = request.json

    challenge_id = data.get("challengeId")
    user_id = data.get("userId")
    progress_level = data.get("progressLevel")

    if not challenge_id or not user_id or progress_level is None:
        return jsonify({"error": "Missing required field(s)"}), 400

    # Simulate metrics update
    updated_metrics = {
        "userProgress": 70,  # Example updated progress
        "teamRanking": 3     # Example new ranking
    }

    return jsonify({"success": True, "updatedMetrics": updated_metrics})

if __name__ == "__main__":
    app.run(debug=True)