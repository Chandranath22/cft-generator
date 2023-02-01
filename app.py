# Entry point to the api
from flask import Flask, request
import json
from controller.get_parameters import read_yaml_file
from controller.generate_cft import create_cloudformation_stack

app = Flask(__name__)

# Define routes

# Test route


@app.route('/')
def home():
    return ('Working container')

# Get params for S3 cloudformation template


@app.route('/params')
def params():
    res = {}
    res['params'] = read_yaml_file()
    return (json.dumps(res))

# Sample request data
# {
#     "BucketName":"cft-generator-bucket"
# }


@app.route('/create', methods=["POST"])
def create_stack():
    data = request.get_json()
    res = {}
    res['result'] = create_cloudformation_stack(data)
    return json.dumps((res))


if __name__ == '__main__':
    app.run()
