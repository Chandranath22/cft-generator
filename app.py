# Entry point to the api
from flask import Flask
import json
from controller.get_parameters import read_yaml_file

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
    print(res)
    return (json.dumps(res))


if __name__ == '__main__':
    app.run()
