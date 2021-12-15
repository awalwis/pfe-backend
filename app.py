from os import error
import sys
import warnings

import jwt

import database

from flask import Flask, jsonify, request, abort
from flask_cors import CORS

warnings.filterwarnings("ignore")

app = Flask(__name__)
"""cors = CORS(app, resources={
            r"/api/*": {"origins": "http://pfe-market-vinci.herokuapp.com"}})"""
CORS(app)

# ROUTES USER


@app.route('/api/utilisateurs', methods=['GET'])
def get_users():
    try:
        decodedToken = jwt.decode(request.headers.get(
            'Authorization'), "sdkfh5464sdfjlskdjfntmdjfhskjfdhs", algorithms=["HS256"])
        if(decodedToken['role'] != "admin"):
            raise ValueError("NOT AUTHORIZED")

        result = database.getUsers()
        return jsonify({'users': result}), 200
    except (jwt.InvalidTokenError) as e:
        return jsonify({e.__class__.__name__: "INVALID TOKEN"}), 500
    except (Exception) as e:
        return jsonify({e.__class__.__name__: e.args[0]}), 500


@app.route('/api/utilisateurs/<int:user_id>', methods=['GET'])
def get_user(user_id):
    try:
        decodedToken = jwt.decode(request.headers.get(
            'Authorization'), "sdkfh5464sdfjlskdjfntmdjfhskjfdhs", algorithms=["HS256"])
        if(decodedToken['role'] != "admin"):
            if(user_id != decodedToken['id_user']):
                raise ValueError("NOT AUTHORIZED")

        result = database.getUser(user_id)
        return jsonify({'user': result}), 200
    except (jwt.InvalidTokenError) as e:
        return jsonify({e.__class__.__name__: "INVALID TOKEN"}), 500
    except (Exception) as e:
        return jsonify({e.__class__.__name__: e.args[0]}), 500


@app.route('/api/utilisateurs/<email>', methods=['GET'])
def get_user_by_email(email):
    try:
        result = database.getUserByEmail(email)
        return jsonify({'user': result}), 200
    except (Exception) as e:
        return jsonify({e.args[0]: e.args[1]}), 500


@app.route('/api/utilisateurs', methods=['POST'])
def add_user():
    try:
        database.createUser(request.json)
        return jsonify({'user': 'user created'}), 201
    except (Exception) as e:
        return jsonify({e.__class__.__name__: e.args[0]}), 500


@ app.route('/api/utilisateurs/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    try:
        decodedToken = jwt.decode(request.headers.get(
            'Authorization'), "sdkfh5464sdfjlskdjfntmdjfhskjfdhs", algorithms=["HS256"])
        if(decodedToken['role'] != "admin"):
            if(user_id != decodedToken['id_user']):
                raise ValueError("NOT AUTHORIZED")

        database.updateUser(request.json, user_id)
        return jsonify({'user': 'user update'}), 200
    except (jwt.InvalidTokenError) as e:
        return jsonify({e.__class__.__name__: "INVALID TOKEN"}), 500
    except (Exception) as e:
        return jsonify({e.__class__.__name__: e.args[0]}), 500


@ app.route('/api/utilisateurs/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        decodedToken = jwt.decode(request.headers.get(
            'Authorization'), "sdkfh5464sdfjlskdjfntmdjfhskjfdhs", algorithms=["HS256"])
        if(decodedToken['role'] != "admin"):
            if(user_id != decodedToken['id_user']):
                raise ValueError("NOT AUTHORIZED")

        database.deleteUser(user_id)
        return jsonify({'user': 'user deleted'}), 200
    except (jwt.InvalidTokenError) as e:
        return jsonify({e.__class__.__name__: "INVALID TOKEN"}), 500
    except (Exception) as e:
        return jsonify({e.__class__.__name__: e.args[0]}), 500

# ROUTES AD


@ app.route('/api/annonces', methods=['GET'])
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
        return jsonify({'ads': result}), 200
    except (Exception) as e:
        return jsonify({e.__class__.__name__: e.args[0]}), 500


@ app.route('/api/annonces/all', methods=['GET'])
def get_all_ads():
    try:
        decodedToken = jwt.decode(request.headers.get(
            'Authorization'), "sdkfh5464sdfjlskdjfntmdjfhskjfdhs", algorithms=["HS256"])
        if(decodedToken['role'] != "admin"):
            raise ValueError("NOT AUTHORIZED")

        result = database.getAllAds()
        return jsonify({'ads': result}), 200
    except (jwt.InvalidTokenError) as e:
        return jsonify({e.__class__.__name__: "INVALID TOKEN"}), 500
    except (Exception) as e:
        return jsonify({e.__class__.__name__: e.args[0]}), 500


@ app.route('/api/annonces/user/<int:id_user>', methods=['GET'])
def get_all_ads_idUser(id_user):
    try:
        decodedToken = jwt.decode(request.headers.get(
            'Authorization'), "sdkfh5464sdfjlskdjfntmdjfhskjfdhs", algorithms=["HS256"])
        if(decodedToken['role'] != "admin"):
            if(id_user != decodedToken['id_user']):
                raise ValueError("NOT AUTHORIZED")

        result = database.getAdWithIdUser(id_user)
        return jsonify({'ads': result}), 200
    except (jwt.InvalidTokenError) as e:
        return jsonify({e.__class__.__name__: "INVALID TOKEN"}), 500
    except (Exception) as e:
        return jsonify({e.__class__.__name__: e.args[0]}), 500


@ app.route('/api/annonces/<int:ad_id>', methods=['GET'])
def get_ad(ad_id):
    try:
        jwt.decode(request.headers.get(
            'Authorization'), "sdkfh5464sdfjlskdjfntmdjfhskjfdhs", algorithms=["HS256"])

        result = database.getAd(ad_id)
        return jsonify({'ad': result}), 200
    except (jwt.InvalidTokenError) as e:
        return jsonify({e.__class__.__name__: "INVALID TOKEN"}), 500
    except (Exception) as e:
        return jsonify({e.__class__.__name__: e.args[0]}), 500


@ app.route('/api/annonces', methods=['POST'])
def add_ad():
    try:
        jwt.decode(request.headers.get('Authorization'),
                   "sdkfh5464sdfjlskdjfntmdjfhskjfdhs", algorithms=["HS256"])

        result = database.createAd(request.json)
        return jsonify(result), 201
    except (jwt.InvalidTokenError) as e:
        return jsonify({e.__class__.__name__: "INVALID TOKEN"}), 500
    except (Exception) as e:
        return jsonify({e.__class__.__name__: e.args[0]}), 500


@ app.route('/api/annonces/<int:ad_id>', methods=['DELETE'])
def delete_ad(ad_id):
    try:
        decodedToken = jwt.decode(request.headers.get(
            'Authorization'), "sdkfh5464sdfjlskdjfntmdjfhskjfdhs", algorithms=["HS256"])
        if(decodedToken['role'] != "admin"):
            ad = database.getAd(ad_id)
            if(ad['id_user'] != decodedToken['id_user']):
                raise ValueError("NOT AUTHORIZED")

        database.deleteAd(ad_id)
        return jsonify({'ad': 'annonce supprimee'}), 200
    except (jwt.InvalidTokenError) as e:
        return jsonify({e.__class__.__name__: "INVALID TOKEN"}), 500
    except (Exception) as e:
        return jsonify({e.__class__.__name__: e.args[0]}), 500


@ app.route('/api/annonces/<int:ad_id>', methods=['PUT'])
def update_ad(ad_id):
    try:
        decodedToken = jwt.decode(request.headers.get(
            'Authorization'), "sdkfh5464sdfjlskdjfntmdjfhskjfdhs", algorithms=["HS256"])
        if(decodedToken['role'] != "admin"):
            ad = database.getAd(ad_id)
            print("USER ID : ", ad['id_user'])
            print("USER TOKEN : ", decodedToken['id_user'])
            if(ad['id_user'] != decodedToken['id_user']):
                raise ValueError("NOT AUTHORIZED")

        database.updateAd(request.json, ad_id)
        return jsonify({'ad': 'annonce update'}), 200
    except (jwt.InvalidTokenError) as e:
        return jsonify({e.__class__.__name__: "INVALID TOKEN"}), 500
    except (Exception) as e:
        return jsonify({e.__class__.__name__: e.args[0]}), 500

# ROUTE CATEGORIES


@ app.route('/api/categories', methods=['GET'])
def get_categories():
    try:
        result = database.getCategories()
        return jsonify({'categories': result}), 200
    except (Exception) as e:
        return jsonify({e.__class__.__name__: e.args[0]}), 500


@ app.route('/api/categories/<int:category_id>', methods=['GET'])
def get_category(category_id):
    try:
        result = database.getCategoryById(category_id)
        return jsonify({'category': result}), 200
    except (Exception) as e:
        return jsonify({e.__class__.__name__: e.args[0]}), 500


@ app.route('/api/categories', methods=['POST'])
def add_category():
    try:
        decodedToken = jwt.decode(request.headers.get(
            'Authorization'), "sdkfh5464sdfjlskdjfntmdjfhskjfdhs", algorithms=["HS256"])
        if(decodedToken['role'] != "admin"):
            raise ValueError("NOT AUTHORIZED")

        database.createCategory(request.json)
        return jsonify({'category': 'category created'}), 201
    except (jwt.InvalidTokenError) as e:
        return jsonify({e.__class__.__name__: "INVALID TOKEN"}), 500
    except (Exception) as e:
        return jsonify({e.__class__.__name__: e.args[0]}), 500


@ app.route('/api/categories/<int:category_id>', methods=['DELETE'])
def delete_category(category_id):
    try:
        decodedToken = jwt.decode(request.headers.get(
            'Authorization'), "sdkfh5464sdfjlskdjfntmdjfhskjfdhs", algorithms=["HS256"])
        if(decodedToken['role'] != "admin"):
            raise ValueError("NOT AUTHORIZED")
        database.deleteCategory(category_id)
        return jsonify({'category': 'category '+str(category_id)+' supprimee'}), 200
    except (jwt.InvalidTokenError) as e:
        return jsonify({e.__class__.__name__: "INVALID TOKEN"}), 500
    except (Exception) as e:
        return jsonify({e.__class__.__name__: e.args[0]}), 500

# ROUTE MEDIAS


@ app.route('/api/medias', methods=['GET'])
def get_medias():
    try:
        result = database.getMedias()
        return jsonify({'medias': result}), 200
    except (jwt.InvalidTokenError) as e:
        return jsonify({e.__class__.__name__: "INVALID TOKEN"}), 500
    except (Exception) as e:
        return jsonify({e.__class__.__name__: e.args[0]}), 500


@ app.route('/api/medias/<int:media_id>', methods=['GET'])
def get_media(media_id):
    try:
        result = database.getMediaById(media_id)
        return jsonify({'media': result}), 200
    except (Exception) as e:
        return jsonify({e.__class__.__name__: e.args[0]}), 500


@ app.route('/api/medias/ad/<int:ad_id>', methods=['GET'])
def get_media_by_ad_id(ad_id):
    try:
        jwt.decode(request.headers.get(
            'Authorization'), "sdkfh5464sdfjlskdjfntmdjfhskjfdhs", algorithms=["HS256"])

        result = database.getMediaByIdAd(ad_id)
        return jsonify({'medias': result}), 200
    except (jwt.InvalidTokenError) as e:
        return jsonify({e.__class__.__name__: "INVALID TOKEN"}), 500
    except (Exception) as e:
        return jsonify({e.__class__.__name__: e.args[0]}), 500


@ app.route('/api/medias', methods=['POST'])
def add_media():
    try:
        jwt.decode(request.headers.get(
            'Authorization'), "sdkfh5464sdfjlskdjfntmdjfhskjfdhs", algorithms=["HS256"])

        database.createMedia(request.json)
        return jsonify({'media': 'media created'}), 201
    except (jwt.InvalidTokenError) as e:
        return jsonify({e.__class__.__name__: "INVALID TOKEN"}), 500
    except (Exception) as e:
        return jsonify({e.__class__.__name__: e.args[0]}), 500


@ app.route('/api/medias/<int:media_id>', methods=['DELETE'])
def delete_media(media_id):
    try:
        decodedToken = jwt.decode(request.headers.get(
            'Authorization'), "sdkfh5464sdfjlskdjfntmdjfhskjfdhs", algorithms=["HS256"])
        if(decodedToken['role'] != "admin"):
            media = database.getMediaById(media_id)
            ad = database.getAd(media['id_ad'])
            if(ad['id_user'] != decodedToken['id_user']):
                raise ValueError("NOT AUTHORIZED")

        database.deleteMedia(media_id)
        return jsonify({'media': 'media supprimee'}), 200
    except (jwt.InvalidTokenError) as e:
        return jsonify({e.__class__.__name__: "INVALID TOKEN"}), 500
    except (Exception) as e:
        return jsonify({e.__class__.__name__: e.args[0]}), 500

# ROUTES NOTIFICATIONS~


@app.route('/api/notifications/<int:user_id>', methods=['GET'])
def get_notifications_from_user(user_id):
    try:

        decodedToken = jwt.decode(request.headers.get(
            'Authorization'), "sdkfh5464sdfjlskdjfntmdjfhskjfdhs", algorithms=["HS256"])
        if(user_id != decodedToken['id_user']):
            raise ValueError("NOT AUTHORIZED")

        result = database.getAllNotificationsById(user_id)
        return (jsonify({'notifications': result}))
    except (jwt.InvalidTokenError) as e:
        return jsonify({e.__class__.__name__: "INVALID TOKEN"}), 500
    except (Exception) as e:
        return jsonify({e.__class__.__name__: e.args[0]}), 500


@ app.route('/api/notification', methods=['POST'])
def create_notification():
    try:
        decodedToken = jwt.decode(request.headers.get(
            'Authorization'), "sdkfh5464sdfjlskdjfntmdjfhskjfdhs", algorithms=["HS256"])
        if(decodedToken['role'] != "admin"):
            raise ValueError("NOT AUTHORIZED")

        result = database.createNotification(request.json)
        return jsonify(result), 201
    except (jwt.InvalidTokenError) as e:
        return jsonify({e.__class__.__name__: "INVALID TOKEN"}), 500
    except (Exception) as e:
        return jsonify({e.__class__.__name__: e.args[0]}), 500


@ app.route('/api/notifications/<int:notification_id>', methods=['DELETE'])
def deleteNotification(notification_id):
    try:
        decodedToken = jwt.decode(request.headers.get(
            'Authorization'), "sdkfh5464sdfjlskdjfntmdjfhskjfdhs", algorithms=["HS256"])
        if(request.user_id != decodedToken['id_user']):
            raise ValueError("NOT AUTHORIZED")
        database.deleteMedia(notification_id)
        return jsonify({'notification': 'notification supprimee'}), 200
    except (jwt.InvalidTokenError) as e:
        return jsonify({e.__class__.__name__: "INVALID TOKEN"}), 500
    except (Exception) as e:
        return jsonify({e.__class__.__name__: e.args[0]}), 500


@app.route('/api/notifications/<int:id_notification>', methods=['PUT'])
def update_notification(notification_id):
    try:
        decodedToken = jwt.decode(request.headers.get(
            'Authorization'), "sdkfh5464sdfjlskdjfntmdjfhskjfdhs", algorithms=["HS256"])
        if(request.user_id != decodedToken['id_user']):
            raise ValueError("NOT AUTHORIZED")
        database.updateNotification(request.json, notification_id)
        return jsonify({'notification': 'notification update'})
    except (jwt.InvalidTokenError) as e:
        return jsonify({e.__class__.__name__: "INVALID TOKEN"}), 500
    except (Exception) as e:
        return jsonify({e.__class__.__name__: e.args[0]}), 500


if __name__ == '__main__':
    app.run(debug=True)
