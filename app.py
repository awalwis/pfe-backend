import warnings

import subprocess

import database

from flask import Flask, jsonify, request, abort

warnings.filterwarnings("ignore")

app = Flask(__name__)

# ROUTES USER


@app.route('/api/utilisateurs', methods=['GET'])
def get_users():
    try:
        result = database.getusers()
        return jsonify({'item': result}), 201
    except (Exception) as e:
        return jsonify({e.args[0]: e.args[1]}), 500


@app.route('/api/utilisateur/<int:user_id>', methods=['GET'])
def get_user(user_id):
    try:
        result = database.getuser(user_id)
        return jsonify({'item': result}), 201
    except (Exception) as e:
        return jsonify({e.args[0]: e.args[1]}), 500


@app.route('/api/utilisateur', methods=['POST'])
def add_user():
    try:
        database.createUser(request.json)
        return jsonify({'item': 'user created'}), 201
    except (Exception) as e:
        return jsonify({e.args[0]: e.args[1]}), 500


@app.route('/api/utilisateur/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    try:
        database.updateUser(request.json, user_id)
        return jsonify({'item': 'user update'}), 201
    except (Exception) as e:
        return jsonify({e.args[0]: e.args[1]}), 500


@app.route('/api/utilisateur/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        database.deleteUser(user_id)
        return jsonify({'item': 'user deleted'}), 201
    except (Exception) as e:
        return jsonify({e.args[0]: e.args[1]}), 500


@app.route('/api/utilisateur/ban/<int:user_id>', methods=['PUT'])
def ban_user(user_id):
    try:
        database.banUser(user_id)
        return jsonify({'item': 'utilisateur banni'}), 201
    except (Exception) as e:
        return jsonify({e.args[0]: e.args[1]}), 500

# ROUTES ITEM
    
@app.route('/api/annonce', methods=['POST'])
def add_ad():
    try:
        database.createAd(request.json)
        return jsonify({'ad': 'ad created'}), 201
    except (Exception) as e:
        return jsonify({e.args[0]: e.args[1]}), 500

@app.route('/api/annonce/<int:ad_id>', methods=['DELETE'])
def delete_ad(ad_id):
    try:
        database.deleteAd(ad_id)
        return jsonify({'item': 'annonce supprimee'}), 201
    except (Exception) as e:
        return jsonify({e.args[0]: e.args[1]}), 500

if __name__ == '__main__':
    app.run(debug=True)
