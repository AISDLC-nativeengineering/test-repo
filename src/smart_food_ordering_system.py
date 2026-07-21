# Smart Food Ordering System Implementation

# API Endpoints
# GET /restaurants: Fetch restaurant list with filtering options
# POST /orders: Submit customized orders
# PUT /deliveries: Update delivery timings based on traffic/weather changes

from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy data
restaurants = [
    {"id": 1, "name": "Pizza Palace", "cuisine": "Italian", "price_range": "$$", "rating": 4.5},
    {"id": 2, "name": "Sushi Square", "cuisine": "Japanese", "price_range": "$$$", "rating": 4.7},
]
menu_items = {
    1: [
        {"id": 1, "name": "Margherita Pizza", "price": 10.99, "add_ons": ["Extra Cheese", "Mushrooms"], "customization": "Cheeseburst"}
    ],
    2: [
        {"id": 2, "name": "California Roll", "price": 12.99, "add_ons": ["Avocado", "Spicy Mayo"], "customization": "No Wasabi"}
    ]
}

# Endpoint: Fetch restaurants
@app.route('/restaurants', methods=['GET'])
def get_restaurants():
    cuisine = request.args.get('cuisine')
    price_range = request.args.get('price_range')
    filtered_restaurants = [r for r in restaurants if (not cuisine or r['cuisine'] == cuisine) \
                            and (not price_range or r['price_range'] == price_range)]
    return jsonify(filtered_restaurants)

# Endpoint: Submit order
@app.route('/orders', methods=['POST'])
def post_order():
    data = request.json
    order = {
        "restaurantId": data.get("restaurantId"),
        "items": data.get("items"),
        "customerId": data.get("customerId"),
        "scheduleTime": data.get("scheduleTime")
    }
    return jsonify({"status": "Order submitted successfully", "order": order}), 201

# Endpoint: Update delivery timings
@app.route('/deliveries', methods=['PUT'])
def put_delivery():
    data = request.json
    delivery_time = data.get('delivery_time') # Updated due to traffic/weather
    return jsonify({"status": "Delivery timing updated", "updated_delivery_time": delivery_time})

if __name__ == '__main__':
    app.run(debug=True)