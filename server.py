# -- Load library --
from flask import json, jsonify, request
from __init__ import app
import log
from classifier import classify

# -- Logger --
logger = log.setup_custom_logger('root')


# -- Classification request --
@app.route('/api/classify', methods=['POST'])
def handle_classify():
    if request.headers['Content-Type'] == 'application/json' \
            or request.headers['Content-Type'].lower() == 'application/json; charset=utf-8':
        __json = json.loads(json.dumps(request.json))

        label, prob = classify(__json)

        if (type(label) == NameError):
            return not_found(404, "Could not load the data")
        else:
            _resp = jsonify({"label": str(label), "probability": str(prob)})
            _resp.status_code = 200
            return _resp
    else:
        return not_found(404, "Invalid Request")


# -- Error Message --
@app.errorhandler(404)
def not_found(code=None, error=None):
    if code:
        message = {
            'status': code,
            'message': error
        }
    else:
        code = 404
        message = {
            'status': 404,
            'message': 'Not Found: ' + request.url
        }
    resp = jsonify(message)
    resp.status_code = code
    return resp
    # -- // Error Message --
