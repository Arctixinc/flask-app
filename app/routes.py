import json
import requests
from flask import Blueprint, request, Response

api = Blueprint('api', __name__)

@api.route('/data', methods=['GET'])
def get_data():
    json_url = request.args.get('json_url')
    start = request.args.get('start')
    end = request.args.get('end')
    limit = request.args.get('limit')

    response = requests.get(json_url)
    json_data = json.loads(response.text)

    if start:
        start = int(start)
    else:
        start = 0

    if end:
        end = int(end)
    else:
        end = len(json_data)

    if limit:
        limit = int(limit)
        end = start + limit

    response_data = json_data[start:end]
    response = Response(json.dumps(response_data), mimetype='application/json')
    return response
