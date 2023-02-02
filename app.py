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


# Select service currently only s3 is supported
@app.route('/service')
def getService():
    service_name = request.args.get("name")
    res = {}
    print(service_name)
    res['params'] = read_yaml_file(service_name)
    return (json.dumps(res))


# Sample request data
# {
#     "stack-name": "s3-bucket-creation",
#     "params": {
#         "BucketName": "sample-test-bucket-poc-30873"
#     }
# }


@app.route('/create', methods=["POST"])
def create_stack():
    data = request.get_json()
    res = {}
    print(data)
    res['result'] = create_cloudformation_stack(data)
    return json.dumps((res))


if __name__ == '__main__':
    app.run()
