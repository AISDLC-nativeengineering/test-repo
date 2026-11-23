from flask import Flask, jsonify, request
import uuid

app = Flask(__name__)

# In-memory database simulation for data sources
data_sources = []

@app.route('/api/data-sources', methods=['GET'])
def get_data_sources():
    """Fetch all linked data sources with their status."""
    return jsonify(data_sources), 200

@app.route('/api/data-sources', methods=['POST'])
def add_data_source():
    """Add a new data source."""
    data = request.json
    if not data or 'name' not in data or 'type' not in data:
        return jsonify({'error': 'Invalid data source format'}), 400

    data_source = {
        'id': str(uuid.uuid4()),
        'name': data['name'],
        'type': data['type'],
        'status': 'Syncing',
        'lastSyncedTime': None
    }
    data_sources.append(data_source)
    return jsonify(data_source), 201

@app.route('/api/data-sources/<string:source_id>', methods=['DELETE'])
def delete_data_source(source_id):
    """Delete an existing data source."""
    global data_sources

    data_sources = [ds for ds in data_sources if ds['id'] != source_id]

    return jsonify({'message': 'Data source deleted'}), 200

if __name__ == '__main__':
    app.run(debug=True)