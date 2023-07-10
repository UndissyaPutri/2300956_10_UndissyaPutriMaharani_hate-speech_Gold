# import pandas as pd
import re

from flask import Flask, jsonify
from flask import request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():
    json_response = {
        'status_code': 200,
        'description': "Menyapa Hello World",
        'data': "Hello World",
    }

    response_data = jsonify(json_response)
    return response_data


@app.route('/text', methods=['GET'])
def text():
    json_response = {
        'status_code': 200,
        'description': "Original Teks",
        'data': "Halo, apa kabar semua?",
    }

    response_data = jsonify(json_response)
    return response_data


@app.route('/text-clean', methods=['GET'])
def text_clean():
    json_response = {
        'status_code': 200,
        'description': "Original Teks",
        'data': re.sub(r'[^a-zA-Z0-9]', ' ', "Halo, apa kabar semua?"),
    }

    # response_data = jsonify(json_response)
    return jsonify(json_response)

@app.route('/text-processing', methods=['POST'])
def text_processing():

    text = request.form.get('text')

    json_response = {
        'status_code': 200,
        'description': "Teks yang sudah diproses",
        'data': re.sub(r'[^a-zA-Z0-9]', ' ', text),
    }

    response_data = jsonify(json_response)
    return response_data


# @app.route('/pandas', methods=['GET'])
# def pandas():
#     df = {"nama": "tedy", "Jenis": "manusia"}
#     json_response = {
#         'status_code': 200,
#         'description': "Original Teks",
#         'data': df,
#     }

    # response_data = jsonify(json_response)
    # return response_data


if __name__ == '__main__':
    app.run()
