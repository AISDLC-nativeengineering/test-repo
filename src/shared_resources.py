# Shared Resources API

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/resources/pdf', methods=['GET'])
def fetch_shared_pdfs():
    # Simulated response of PDF resources
    resources = [
        {"url": "https://resources.example.com/pdf1", "title": "Wellness Tips 2023"},
        {"url": "https://resources.example.com/pdf2", "title": "Balanced Nutrition Guide"}
    ]

    if not resources:
        return jsonify({"error": "No resources found"}), 404

    return jsonify(resources)

if __name__ == "__main__":
    app.run(debug=True)