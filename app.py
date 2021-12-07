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

@app.route('/api/utilisateur/ban/<int:user_id>', methods=['PUT'])
def ban_user(user_id):
    try:
        database.banUser(user_id)
        return jsonify({'item': 'utilisateur banni'}), 201
    except (Exception) as e:
        return jsonify({e.args[0]: e.args[1]}), 500

if __name__ == '__main__':
    app.run(debug=True)
