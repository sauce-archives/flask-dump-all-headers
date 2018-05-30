from werkzeug.contrib.fixers import ProxyFix
from flask import Flask, request, jsonify
from six import string_types, text_type, integer_types
import os

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)


@app.route('/')
def dump():
    environ = {k: v for k, v in request.environ.items()
               if isinstance(v, text_type) or isinstance(v, string_types) or isinstance(v, integer_types)}
    req_data = {}
    req_data['endpoint'] = request.endpoint
    req_data['method'] = request.method
    req_data['cookies'] = request.cookies
    # Is a byte so don't export
    # req_data['data'] = request.data
    req_data['environ'] = dict(environ)
    req_data['headers'] = dict(request.headers)
    req_data['headers'].pop('Cookie', None)
    req_data['args'] = request.args
    req_data['form'] = request.form
    req_data['remote_addr'] = request.remote_addr
    print(req_data)
    return jsonify(req_data)
