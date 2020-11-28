from flask import request, jsonify

from config import *


def wrap(data):
    return jsonify({PAYLOAD_WRAPPER: data})


def unwrap_request():
    json_data = request.get_json()
    if not json_data or PAYLOAD_WRAPPER not in json_data:
        return None
    else:
        return json_data[PAYLOAD_WRAPPER]
