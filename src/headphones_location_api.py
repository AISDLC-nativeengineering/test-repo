from flask import Flask, request, jsonify
import psycopg2
import os

app = Flask(__name__)

# Database connection configuration
def get_db_connection():
    return psycopg2.connect(
        dbname=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        host=os.getenv('DB_HOST'),
        port=os.getenv('DB_PORT')
    )

@app.route('/headphones/location', methods=['GET'])
def get_location():
    headphone_id = request.args.get('headphone_id')
    if not headphone_id:
        return jsonify({'error': 'headphone_id is required'}), 400

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        query = """
        SELECT latitude, longitude, timestamp
        FROM headphone_locations
        WHERE headphone_id = %s
        ORDER BY timestamp DESC
        LIMIT 1;
        """
        cursor.execute(query, (headphone_id,))
        result = cursor.fetchone()

        conn.close()

        if result:
            latitude, longitude, timestamp = result
            return jsonify({
                'headphone_id': headphone_id,
                'latitude': latitude,
                'longitude': longitude,
                'timestamp': timestamp
            })
        else:
            return jsonify({'message': 'No location data available'}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
