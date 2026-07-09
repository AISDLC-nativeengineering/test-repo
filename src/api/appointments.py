# Implementation of booking features for appointments
from flask import Flask, request, jsonify

app = Flask(__name__)

appointments = []  # Temporary storage for appointments
slots = [
    {"slotId": "s1", "date": "2026-07-10", "time": "09:00", "available": True},
    {"slotId": "s2", "date": "2026-07-10", "time": "14:00", "available": True}
]

# POST /appointments/book
@app.route('/appointments/book', methods=['POST'])
def book_appointment():
    data = request.json
    slot = next((s for s in slots if s['slotId'] == data['slotId'] and s['available']), None)
    if not slot:
        return jsonify({"status": "error", "message": "Slot unavailable"}), 400

    appointment = {
        "appointmentId": f"a{len(appointments) + 1}",
        "userId": data['userId'],
        "deviceId": data['deviceId'],
        "slotId": data['slotId'],
        "date": slot['date'],
        "time": slot['time'],
        "provider": "Provider A"
    }
    appointments.append(appointment)
    slot['available'] = False
    return jsonify({"status": "success", "appointmentId": appointment['appointmentId'], "details": appointment}), 200

# GET /appointments/:id
@app.route('/appointments/<appointmentId>', methods=['GET'])
def get_appointment(appointmentId):
    appointment = next((a for a in appointments if a['appointmentId'] == appointmentId), None)
    if not appointment:
        return jsonify({"status": "error", "message": "Appointment not found"}), 404

    return jsonify(appointment), 200

# DELETE /appointments/:id
@app.route('/appointments/<appointmentId>', methods=['DELETE'])
def cancel_appointment(appointmentId):
    appointment = next((a for a in appointments if a['appointmentId'] == appointmentId), None)
    if not appointment:
        return jsonify({"status": "error", "message": "Appointment not found"}), 404

    slot = next((s for s in slots if s['slotId'] == appointment['slotId']), None)
    if slot:
        slot['available'] = True
    appointments.remove(appointment)
    return jsonify({"status": "success", "message": "Appointment canceled"}), 200

if __name__ == '__main__':
    app.run(debug=True)