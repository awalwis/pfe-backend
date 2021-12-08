import sys
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
        result = database.getUsers()
        return jsonify({'users': result}), 201
    except (Exception) as e:
        return jsonify({e.args[0]: e.args[1]}), 500


@app.route('/api/utilisateurs/<int:user_id>', methods=['GET'])
def get_user(user_id):
    try:
        result = database.getUser(user_id)
        return jsonify({'user': result}), 201
    except (Exception) as e:
        return jsonify({e.args[0]: e.args[1]}), 500


@app.route('/api/utilisateurs', methods=['POST'])
def add_user():
    try:
        database.createUser(request.json)
        return jsonify({'user': 'user created'}), 201
    except (Exception) as e:
        return jsonify({e.args[0]: e.args[1]}), 500


@app.route('/api/utilisateurs/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    try:
        database.updateUser(request.json, user_id)
        return jsonify({'user': 'user update'}), 201
    except (Exception) as e:
        return jsonify({e.args[0]: e.args[1]}), 500


@app.route('/api/utilisateurs/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        database.deleteUser(user_id)
        return jsonify({'user': 'user deleted'}), 201
    except (Exception) as e:
        return jsonify({e.args[0]: e.args[1]}), 500

# ROUTES AD


@app.route('/api/annonces', methods=['GET'])
def get_ads():
    try:
        result = None
        if(not request.args.get('categorie') and not request.args.get('tri') and not request.args.get('prixMin') and not request.args.get('prixMax')):
            result = database.getAds()
        elif(request.args.get('categorie') and not request.args.get('tri') and not request.args.get('prixMin') and not request.args.get('prixMax')):
            category = database.getCategoryByName(
                request.args.get('categorie'))
            result = database.getAdsWithCategory(category['id_category'])
        elif(not request.args.get('categorie') and request.args.get('tri') and not request.args.get('prixMin') and not request.args.get('prixMax')):
            result = database.getAdsWithSort(request.args.get('tri'))
        elif(not request.args.get('categorie') and not request.args.get('tri') and request.args.get('prixMin') and not request.args.get('prixMax')):
            result = database.getAdsByPrice(
                int(request.args.get('prixMin')), sys.maxsize)
        elif(not request.args.get('categorie') and not request.args.get('tri') and not request.args.get('prixMin') and request.args.get('prixMax')):
            result = database.getAdsByPrice(
                0, int(request.args.get('prixMax')))
        elif(not request.args.get('categorie') and not request.args.get('tri') and request.args.get('prixMin') and request.args.get('prixMax')):
            result = database.getAdsByPrice(int(request.args.get(
                'prixMin')), int(request.args.get('prixMax')))
        elif(request.args.get('categorie') and request.args.get('tri') and not request.args.get('prixMin') and not request.args.get('prixMax')):
            category = database.getCategoryByName(
                request.args.get('categorie'))
            result = database.getAdsByCategoryAndSort(
                category['id_category'], request.args.get('tri'))
        elif(request.args.get('categorie') and not request.args.get('tri') and request.args.get('prixMin') and not request.args.get('prixMax')):
            category = database.getCategoryByName(
                request.args.get('categorie'))
            result = database.getAdsByCategoryAndPrice(
                category['id_category'], int(request.args.get('prixMin')), sys.maxsize)
        elif(request.args.get('categorie') and not request.args.get('tri') and not request.args.get('prixMin') and request.args.get('prixMax')):
            category = database.getCategoryByName(
                request.args.get('categorie'))
            result = database.getAdsByCategoryAndPrice(
                category['id_category'], 0, int(request.args.get('prixMax')))
        elif(request.args.get('categorie') and not request.args.get('tri') and request.args.get('prixMin') and request.args.get('prixMax')):
            category = database.getCategoryByName(
                request.args.get('categorie'))
            result = database.getAdsByCategoryAndPrice(
                category['id_category'], int(request.args.get('prixMin')), int(request.args.get('prixMax')))
        elif(not request.args.get('categorie') and request.args.get('tri') and request.args.get('prixMin') and not request.args.get('prixMax')):
            result = database.getAdsBySortAndPrice(request.args.get(
                'tri'), int(request.args.get('prixMin')), sys.maxsize)
        elif(not request.args.get('categorie') and request.args.get('tri') and not request.args.get('prixMin') and request.args.get('prixMax')):
            result = database.getAdsBySortAndPrice(
                request.args.get('tri'), 0, int(request.args.get('prixMax')))
        elif(not request.args.get('categorie') and request.args.get('tri') and request.args.get('prixMin') and request.args.get('prixMax')):
            result = database.getAdsBySortAndPrice(request.args.get(
                'tri'), int(request.args.get('prixMin')), int(request.args.get('prixMax')))
        elif(request.args.get('categorie') and request.args.get('tri') and request.args.get('prixMin') and not request.args.get('prixMax')):
            category = database.getCategoryByName(
                request.args.get('categorie'))
            result = database.getAdsByCategoryAndSortAndPrice(category['id_category'], request.args.get(
                'tri'), int(request.args.get('prixMin')), sys.maxsize)
        elif(request.args.get('categorie') and request.args.get('tri') and not request.args.get('prixMin') and request.args.get('prixMax')):
            category = database.getCategoryByName(
                request.args.get('categorie'))
            result = database.getAdsByCategoryAndSortAndPrice(
                category['id_category'], request.args.get('tri'), 0, int(request.args.get('prixMax')))
        else:
            category = database.getCategoryByName(
                request.args.get('categorie'))
            result = database.getAdsByCategoryAndSortAndPrice(category['id_category'], request.args.get(
                'tri'), int(request.args.get('prixMin')), int(request.args.get('prixMax')))
        return jsonify({'ads': result}), 201
    except (Exception) as e:
        return jsonify({e.args[0]: e.args[1]}), 500


@app.route('/api/annonces/<int:ad_id>', methods=['GET'])
def get_ad(ad_id):
    try:
        result = database.getAd(ad_id)
        return jsonify({'ad': result}), 201
    except (Exception) as e:
        return jsonify({e.args[0]: e.args[1]}), 500


@app.route('/api/annonces', methods=['POST'])
def add_ad():
    try:
        database.createAd(request.json)
        return jsonify({'ad': 'ad created'}), 201
    except (Exception) as e:
        return jsonify({e.args[0]: e.args[1]}), 500


@app.route('/api/annonces/<int:ad_id>', methods=['DELETE'])
def delete_ad(ad_id):
    try:
        database.deleteAd(ad_id)
        return jsonify({'ad': 'annonce supprimee'}), 201
    except (Exception) as e:
        return jsonify({e.args[0]: e.args[1]}), 500


@app.route('/api/annonces/<int:ad_id>', methods=['PUT'])
def update_ad(ad_id):
    try:
        database.updateAd(request.json, ad_id)
        return jsonify({'ad': 'annonce update'}), 201
    except (Exception) as e:
        return jsonify({e.args[0]: e.args[1]}), 500

# ROUTE CATEGORIES


@app.route('/api/categories', methods=['GET'])
def get_categories():
    try:
        result = database.getCategories()
        return jsonify({'categories': result}), 201
    except (Exception) as e:
        return jsonify({e.args[0]: e.args[1]}), 500


@app.route('/api/categories/<int:category_id>', methods=['GET'])
def get_category(category_id):
    try:
        result = database.getCategoryById(category_id)
        return jsonify({'category': result}), 201
    except (Exception) as e:
        return jsonify({e.args[0]: e.args[1]}), 500


@app.route('/api/categories', methods=['POST'])
def add_category():
    try:
        database.createCategory(request.json)
        return jsonify({'category': 'category created'}), 201
    except (Exception) as e:
        return jsonify({e.args[0]: e.args[1]}), 500

# ROUTE MEDIAS


@app.route('/api/medias', methods=['GET'])
def get_medias():
    try:
        result = database.getMedias()
        return jsonify({'medias': result}), 201
    except (Exception) as e:
        return jsonify({e.args[0]: e.args[1]}), 500


@app.route('/api/medias/<int:media_id>', methods=['GET'])
def get_media(media_id):
    try:
        result = database.getMediaById(media_id)
        return jsonify({'media': result}), 201
    except (Exception) as e:
        return jsonify({e.args[0]: e.args[1]}), 500


@app.route('/api/medias/ad/<int:ad_id>', methods=['GET'])
def get_media_by_ad_id(ad_id):
    try:
        result = database.getMediaByIdAd(ad_id)
        return jsonify({'medias': result}), 201
    except (Exception) as e:
        return jsonify({e.args[0]: e.args[1]}), 500


@app.route('/api/medias', methods=['POST'])
def add_media():
    try:
        database.createMedia(request.json)
        return jsonify({'media': 'media created'}), 201
    except (Exception) as e:
        return jsonify({e.args[0]: e.args[1]}), 500


@app.route('/api/medias/<int:media_id>', methods=['DELETE'])
def delete_media(media_id):
    try:
        database.deleteMedia(media_id)
        return jsonify({'media': 'media supprimee'}), 201
    except (Exception) as e:
        return jsonify({e.args[0]: e.args[1]}), 500


if __name__ == '__main__':
    app.run(debug=True)
