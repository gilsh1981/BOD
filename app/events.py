# events.py
from flask import Blueprint, request, jsonify

events_bp = Blueprint('events', __name__)

events = []  # This will store events in memory for simplicity. You can replace this with a database.

@events_bp.route('/events', methods=['GET'])
def get_events():
    return jsonify(events)

@events_bp.route('/events', methods=['POST'])
def add_event():
    event = request.json
    events.append(event)
    return jsonify(event), 201

@events_bp.route('/events/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
    global events
    events = [event for event in events if event['id'] != event_id]
    return '', 204
