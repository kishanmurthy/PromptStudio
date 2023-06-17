import asyncio
import random
import uuid
from urllib.parse import urlencode, urlparse
from mongo_db import save_or_update
from dag_parser import create_dag_object
from prompt_processing import prompt_process
from aioflask import Flask, abort, jsonify, render_template, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

@app.route('/')
def application_start():
    return "Hello"

@app.route('/save', methods=["POST"])
def save_dag():
	dag_arch = request.get_json()
	save_or_update(dag_arch)
	return jsonify({'statusCode':200})

@app.route('/test', methods=["POST"])
def test_dag():
    dag_arch = request.get_json()
    save_or_update(dag_arch)
    node_dict, tp_sort = create_dag_object(dag_arch)
    node_input = dag_arch["input"]
    output_dict, input_dicts = prompt_process(node_input, node_dict, tp_sort)
    return json.dumps(input_dicts)

@app.route('/download', methods=["POST"])
def test_dag_ye():
    dag_arch = request.get_json()
    save_or_update(dag_arch)
    node_dict, tp_sort = create_dag_object(dag_arch)
    node_input = dag_arch["input"]
    output_dict, input_dicts = prompt_process(node_input, node_dict, tp_sort)
    return json.dumps(input_dicts)

if __name__ == '__main__':
   app.run()