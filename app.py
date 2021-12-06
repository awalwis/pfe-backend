import warnings

import subprocess

import database

from flask import Flask, jsonify, request, abort

warnings.filterwarnings("ignore")

app = Flask(__name__)


items = []


@app.route('/api/users', methods=['GET'])
def get_users():
    result = database.getusers()
    print(result)
    return jsonify({'item': result}), 201


@app.route('/api/user', methods=['POST'])
def add_user():
    database.createUser(request.json)
    return jsonify({'item': 'user created'}), 201


if __name__ == '__main__':
    app.run(debug=True)
