import asyncio
import json
import random
import uuid
from urllib.parse import urlencode, urlparse

from aioflask import Flask, abort, jsonify, render_template, request, send_file
from dag_parser import create_dag_object
from flask_cors import CORS
from frontend_to_backend_dag_parser import to_backend_json
from generate_code import generate_python_code
from mongo_db import (find_published_dag_arch, load_frontend, save_or_update,
                      save_or_update_frontend, save_publish_version)
from prompt_processing import prompt_process

app = Flask(__name__)
CORS(app)

@app.route('/')
def application_start():
    return "Hello"

@app.route('/save', methods=["POST"])
def save_dag():
	dag_arch = request.get_json()
	save_or_update_frontend(dag_arch)
	return jsonify({'statusCode':200})

@app.route('/load', methods=["GET"])
def load_dag():
	return load_frontend()

@app.route('/test', methods=["POST"])
def test_dag():
    frontend_dag = request.get_json()
    dag_arch = to_backend_json(frontend_dag)
    save_or_update(dag_arch)
    node_dict, tp_sort = create_dag_object(dag_arch)
    node_input = dag_arch["input"]
    output_dict, input_dicts = prompt_process(node_input, node_dict, tp_sort)
    # print(input_dicts)
    return json.dumps(output_dict)

@app.route('/download', methods=["POST"])
def download_code():
    frontend_dag = request.get_json()
    dag_arch = to_backend_json(frontend_dag)
    save_or_update(dag_arch)
    node_dict, tp_sort = create_dag_object(dag_arch)
    node_input = dag_arch["input"]
    file_path = generate_python_code(dag_arch["flow_name"], dag_arch["version"], node_input, node_dict, tp_sort)
    return send_file(file_path)

@app.route('/published_endpoint/<flow_name>', methods=["GET"])
def published_endpoints(flow_name):
    dag_arch = find_published_dag_arch(flow_name)
    node_dict, tp_sort = create_dag_object(dag_arch)
    node_input = dag_arch["input"]
    output_dict, input_dicts = prompt_process(node_input, node_dict, tp_sort)
    return json.dumps(input_dicts)

@app.route('/publish', methods=["POST"])
def publish_code():
    frontend_dag = request.get_json()
    dag_arch = to_backend_json(frontend_dag)
    save_or_update(dag_arch)
    save_publish_version(dag_arch)
    return jsonify({'statusCode':200})

if __name__ == '__main__':
   app.run()