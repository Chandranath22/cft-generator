# Entry point to the api
from flask import Flask

app = Flask(__name__)

# Define routes

# Test route
@app.route('/')
def home():
    return ('Working container')

if __name__ == '__main__':
    app.run()