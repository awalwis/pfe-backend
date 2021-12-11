import psycopg2


def initialiseConnection():
    try:
        connection = psycopg2.connect(
            user="bscjhiup",
            password="StvgARUvcUaIyUO93QDagYX2dcsnJ8FR",
            host="abul.db.elephantsql.com",
            database="bscjhiup",
            port="5432")

        """connection = psycopg2.connect(user="postgres",
                                      password="azerty",
                                      host="localhost",
                                      database="PFE",
                                      port="5432")"""

        print("DATABASE CONNECTED")
        return connection
    except (Exception, psycopg2.DatabaseError) as e:
        print("DATABASE NOT CONNECTED")
        print("CONNECTION Error: %s" % str(e))
        return None

# USERS


def getUsers():
    connection = initialiseConnection()
    cursor = connection.cursor()
    sql = "SELECT * FROM pfe.users"
    resultsExportUsers = []
    try:
        cursor.execute(sql)
        connection.commit()
        results = cursor.fetchall()
        for row in results:
            user = {
                "id_user": row[0],
                "email": row[1],
                "last_name": row[2],
                "first_name": row[3],
                "password": row[4],
                "campus": row[5],
                "role": row[6]
            }
            resultsExportUsers.append(user)
        return resultsExportUsers
    except (Exception, psycopg2.DatabaseError) as e:
        try:
            print("SQL Error [%d]: %s" % (e.args[0], e.args[1]))
            raise Exception from e
        except IndexError:
            print("SQL Error: %s" % str(e))
            raise Exception from e
    finally:
        cursor.close()
        connection.close()


def getUser(id):
    connection = initialiseConnection()
    cursor = connection.cursor()
    sql = "SELECT * FROM pfe.users WHERE id_user = %i" % (id)
    try:
        cursor.execute(sql)
        connection.commit()
        result = cursor.fetchone()
        user = {
            "id_user": result[0],
            "email": result[1],
            "last_name": result[2],
            "first_name": result[3],
            "password": result[4],
            "campus": result[5],
            "role": result[6]
        }
        return user
    except (Exception, psycopg2.DatabaseError) as e:
        try:
            print("SQL Error [%d]: %s" % (e.args[0], e.args[1]))
            raise Exception from e
        except IndexError:
            print("SQL Error: %s" % str(e))
            raise Exception from e
    finally:

        cursor.close()
        connection.close()


def getUserByEmail(email):
    connection = initialiseConnection()
    cursor = connection.cursor()
    sql = "SELECT * FROM pfe.users WHERE email = '%s'" % (email)
    try:
        cursor.execute(sql)
        connection.commit()
        result = cursor.fetchone()
        user = {
            "id_user": result[0],
            "email": result[1],
            "last_name": result[2],
            "first_name": result[3],
            "password": result[4],
            "campus": result[5],
            "role": result[6]
        }
        return user
    except (Exception, psycopg2.DatabaseError) as e:
        try:
            print("SQL Error [%d]: %s" % (e.args[0], e.args[1]))
            raise Exception(e.args[1])
        except IndexError:
            print("SQL Error: %s" % str(e))
            raise Exception(e.args[1])
    finally:

        cursor.close()
        connection.close()


def createUser(user):
    connection = initialiseConnection()
    cursor = connection.cursor()
    sql = "INSERT INTO pfe.users VALUES (DEFAULT,'%s','%s','%s','%s','%s',DEFAULT)" % (
        user['email'], user['last_name'], user['first_name'], user['password'], user['campus'])
    try:
        cursor.execute(sql)
        connection.commit()
    except (Exception, psycopg2.DatabaseError) as e:
        try:
            print("SQL Error [%d]: %s" % (e.args[0], e.args[1]))
            raise Exception from e
        except IndexError:
            connection.rollback()
            print("SQL Error: %s" % str(e))
            raise Exception from e
    finally:
        cursor.close()
        connection.close()


def updateUser(user, id):
    connection = initialiseConnection()
    cursor = connection.cursor()
    sql = "UPDATE pfe.users SET email = '%s', last_name = '%s', first_name = '%s', password = '%s', campus = '%s', role='%s' WHERE id_user = %i" % (
        user['email'], user['last_name'], user['first_name'], user['password'], user['campus'], user['role'], id)
    try:
        cursor.execute(sql)
        connection.commit()
    except (Exception, psycopg2.DatabaseError) as e:
        try:
            print("SQL Error [%d]: %s" % (e.args[0], e.args[1]))
            raise Exception from e
        except IndexError:
            connection.rollback()
            print("SQL Error: %s" % str(e))
            raise Exception from e
    finally:
        cursor.close()
        connection.close()


def deleteUser(id):
    connection = initialiseConnection()
    cursor = connection.cursor()
    sql = "DELETE FROM pfe.users WHERE id_user = %i" % (id)
    try:
        cursor.execute(sql)
        connection.commit()
    except (Exception, psycopg2.DatabaseError) as e:
        try:
            print("SQL Error [%d]: %s" % (e.args[0], e.args[1]))
            raise Exception from e
        except IndexError:
            connection.rollback()
            print("SQL Error: %s" % str(e))
            raise Exception from e
    finally:
        cursor.close()
        connection.close()

# ADS


def getAds():
    connection = initialiseConnection()
    cursor = connection.cursor()
    sql = "SELECT * FROM pfe.ads WHERE state='available'"
    resultsExportAds = []
    try:
        cursor.execute(sql)
        connection.commit()
        results = cursor.fetchall()
        for row in results:
            ad = {
                "id_ad": row[0],
                "title": row[1],
                "description": row[2],
                "price": row[3],
                "date": row[4],
                "state": row[5],
                "type": row[6],
                "displayed_picture": row[7],
                "id_user": row[8],
                "id_category": row[9]
            }
            resultsExportAds.append(ad)
        return resultsExportAds
    except (Exception, psycopg2.DatabaseError) as e:
        try:
            print("SQL Error [%d]: %s" % (e.args[0], e.args[1]))
            raise Exception from e
        except IndexError:
            print("SQL Error: %s" % str(e))
            raise Exception from e
    finally:
        cursor.close()
        connection.close()


def getAdsWithCategory(id_category):
    connection = initialiseConnection()
    cursor = connection.cursor()
    sql = "SELECT * FROM pfe.ads WHERE state='available' AND id_category=%i" % (
        id_category)
    resultsExportAds = []
    try:
        cursor.execute(sql)
        connection.commit()
        results = cursor.fetchall()
        for row in results:
            ad = {
                "id_ad": row[0],
                "title": row[1],
                "description": row[2],
                "price": row[3],
                "date": row[4],
                "state": row[5],
                "type": row[6],
                "displayed_picture": row[7],
                "id_user": row[8],
                "id_category": row[9]
            }
            resultsExportAds.append(ad)
        return resultsExportAds
    except (Exception, psycopg2.DatabaseError) as e:
        try:
            print("SQL Error [%d]: %s" % (e.args[0], e.args[1]))
            raise Exception from e
        except IndexError:
            print("SQL Error: %s" % str(e))
            raise Exception from e
    finally:
        cursor.close()
        connection.close()


def getAdsWithSort(sort):
    connection = initialiseConnection()
    cursor = connection.cursor()
    sql = "SELECT * FROM pfe.ads WHERE state='available' ORDER BY price %s" % (
        sort)
    resultsExportAds = []
    try:
        cursor.execute(sql)
        connection.commit()
        results = cursor.fetchall()
        for row in results:
            ad = {
                "id_ad": row[0],
                "title": row[1],
                "description": row[2],
                "price": row[3],
                "date": row[4],
                "state": row[5],
                "type": row[6],
                "displayed_picture": row[7],
                "id_user": row[8],
                "id_category": row[9]
            }
            resultsExportAds.append(ad)
        return resultsExportAds
    except (Exception, psycopg2.DatabaseError) as e:
        try:
            print("SQL Error [%d]: %s" % (e.args[0], e.args[1]))
            raise Exception from e
        except IndexError:
            print("SQL Error: %s" % str(e))
            raise Exception from e
    finally:
        cursor.close()
        connection.close()


def getAdsByPrice(priceMin, priceMax):
    connection = initialiseConnection()
    cursor = connection.cursor()
    sql = "SELECT * FROM pfe.ads WHERE state='available' AND price BETWEEN %i AND %i" % (
        priceMin, priceMax)
    resultsExportAds = []
    try:
        cursor.execute(sql)
        connection.commit()
        results = cursor.fetchall()
        for row in results:
            ad = {
                "id_ad": row[0],
                "title": row[1],
                "description": row[2],
                "price": row[3],
                "date": row[4],
                "state": row[5],
                "type": row[6],
                "displayed_picture": row[7],
                "id_user": row[8],
                "id_category": row[9]
            }
            resultsExportAds.append(ad)
        return resultsExportAds
    except (Exception, psycopg2.DatabaseError) as e:
        try:
            print("SQL Error [%d]: %s" % (e.args[0], e.args[1]))
            raise Exception from e
        except IndexError:
            connection.rollback()
            print("SQL Error: %s" % str(e))
            raise Exception from e
    finally:
        cursor.close()
        connection.close()


def getAdsByCategoryAndSort(id_category, sort):
    connection = initialiseConnection()
    cursor = connection.cursor()
    sql = "SELECT * FROM pfe.ads WHERE state='available' AND id_category=%i ORDER BY price %s" % (
        id_category, sort)
    resultsExportAds = []
    try:
        cursor.execute(sql)
        connection.commit()
        results = cursor.fetchall()
        for row in results:
            ad = {
                "id_ad": row[0],
                "title": row[1],
                "description": row[2],
                "price": row[3],
                "date": row[4],
                "state": row[5],
                "type": row[6],
                "displayed_picture": row[7],
                "id_user": row[8],
                "id_category": row[9]
            }
            resultsExportAds.append(ad)
        return resultsExportAds
    except (Exception, psycopg2.DatabaseError) as e:
        try:
            print("SQL Error [%d]: %s" % (e.args[0], e.args[1]))
            raise Exception from e
        except IndexError:
            connection.rollback()
            print("SQL Error: %s" % str(e))
            raise Exception from e
    finally:
        cursor.close()
        connection.close()


def getAdsByCategoryAndPrice(id_category, prixMin, prixMax):
    connection = initialiseConnection()
    cursor = connection.cursor()
    sql = "SELECT * FROM pfe.ads WHERE state='available' AND id_category=%i AND price BETWEEN %i AND %i" % (
        id_category, prixMin, prixMax)
    resultsExportAds = []
    try:
        cursor.execute(sql)
        connection.commit()
        results = cursor.fetchall()
        for row in results:
            ad = {
                "id_ad": row[0],
                "title": row[1],
                "description": row[2],
                "price": row[3],
                "date": row[4],
                "state": row[5],
                "type": row[6],
                "displayed_picture": row[7],
                "id_user": row[8],
                "id_category": row[9]
            }
            resultsExportAds.append(ad)
        return resultsExportAds
    except (Exception, psycopg2.DatabaseError) as e:
        try:
            print("SQL Error [%d]: %s" % (e.args[0], e.args[1]))
            raise Exception from e
        except IndexError:
            connection.rollback()
            print("SQL Error: %s" % str(e))
            raise Exception from e
    finally:
        cursor.close()
        connection.close()


def getAdsBySortAndPrice(sort, prixMin, prixMax):
    connection = initialiseConnection()
    cursor = connection.cursor()
    sql = "SELECT * FROM pfe.ads WHERE state='available' AND price BETWEEN %i AND %i ORDER BY price %s" % (
        prixMin, prixMax, sort)
    resultsExportAds = []
    try:
        cursor.execute(sql)
        connection.commit()
        results = cursor.fetchall()
        for row in results:
            ad = {
                "id_ad": row[0],
                "title": row[1],
                "description": row[2],
                "price": row[3],
                "date": row[4],
                "state": row[5],
                "type": row[6],
                "displayed_picture": row[7],
                "id_user": row[8],
                "id_category": row[9]
            }
            resultsExportAds.append(ad)
        return resultsExportAds
    except (Exception, psycopg2.DatabaseError) as e:
        try:
            print("SQL Error [%d]: %s" % (e.args[0], e.args[1]))
            raise Exception from e
        except IndexError:
            print("SQL Error: %s" % str(e))
            raise Exception from e
    finally:
        cursor.close()
        connection.close()


def getAdsByCategoryAndSortAndPrice(id_category, sort, prixMin, prixMax):
    connection = initialiseConnection()
    cursor = connection.cursor()
    sql = "SELECT * FROM pfe.ads WHERE state='available' AND id_category=%i AND price BETWEEN %i AND %i ORDER BY price %s" % (
        id_category, prixMin, prixMax, sort)
    resultsExportAds = []
    try:
        cursor.execute(sql)
        connection.commit()
        results = cursor.fetchall()
        for row in results:
            ad = {
                "id_ad": row[0],
                "title": row[1],
                "description": row[2],
                "price": row[3],
                "date": row[4],
                "state": row[5],
                "type": row[6],
                "displayed_picture": row[7],
                "id_user": row[8],
                "id_category": row[9]
            }
            resultsExportAds.append(ad)
        return resultsExportAds
    except (Exception, psycopg2.DatabaseError) as e:
        try:
            print("SQL Error [%d]: %s" % (e.args[0], e.args[1]))
            raise Exception from e
        except IndexError:
            print("SQL Error: %s" % str(e))
            raise Exception from e
    finally:
        cursor.close()
        connection.close()


def getAllAds():
    connection = initialiseConnection()
    cursor = connection.cursor()
    sql = "SELECT * FROM pfe.ads"
    resultsExportAds = []
    try:
        cursor.execute(sql)
        connection.commit()
        results = cursor.fetchall()
        for row in results:
            ad = {
                "id_ad": row[0],
                "title": row[1],
                "description": row[2],
                "price": row[3],
                "date": row[4],
                "state": row[5],
                "type": row[6],
                "displayed_picture": row[7],
                "id_user": row[8],
                "id_category": row[9]
            }
            resultsExportAds.append(ad)
        return resultsExportAds
    except (Exception, psycopg2.DatabaseError) as e:
        try:
            print("SQL Error [%d]: %s" % (e.args[0], e.args[1]))
            raise Exception from e
        except IndexError:
            print("SQL Error: %s" % str(e))
            raise Exception from e
    finally:
        cursor.close()
        connection.close()


def getAd(id):
    connection = initialiseConnection()
    cursor = connection.cursor()
    sql = "SELECT * FROM pfe.ads WHERE id_ad = %i" % (id)
    try:
        cursor.execute(sql)
        connection.commit()
        result = cursor.fetchone()
        ad = {
            "id_ad": result[0],
            "title": result[1],
            "description": result[2],
            "price": result[3],
            "date": result[4],
            "sate": result[5],
            "type": result[6],
            "displayed_picture": result[7],
            "id_user": result[8],
            "id_category": result[9]
        }
        return ad
    except (Exception, psycopg2.DatabaseError) as e:
        try:
            print("SQL Error [%d]: %s" % (e.args[0], e.args[1]))
            raise Exception from e
        except IndexError:
            print("SQL Error: %s" % str(e))
            raise Exception from e
    finally:
        cursor.close()
        connection.close()


def createAd(ad):
    connection = initialiseConnection()
    cursor = connection.cursor()
    sql = "SELECT pfe.addAds('%s','%s',%i,'%s','%s','%s',%i,%i,%i)" % (
        ad['title'], ad['description'], ad['price'], ad['date'], ad['state'], ad['type'], ad['displayed_picture'], ad['id_user'], ad['id_category'])
    try:
        cursor.execute(sql)
        connection.commit()
        result = cursor.fetchone()
        ad = {
            "id_ad": result[0]
        }
        return ad
    except (Exception, psycopg2.DatabaseError) as e:
        try:
            print("SQL Error [%d]: %s" % (e.args[0], e.args[1]))
            raise Exception from e
        except IndexError:
            connection.rollback()
            print("SQL Error: %s" % str(e))
            raise Exception from e
    finally:
        cursor.close()
        connection.close()


def deleteAd(id):
    connection = initialiseConnection()
    cursor = connection.cursor()
    sql = "DELETE FROM pfe.ads WHERE id_ad = %i" % (id)
    try:
        cursor.execute(sql)
        connection.commit()
    except (Exception, psycopg2.DatabaseError) as e:
        try:
            print("SQL Error [%d]: %s" % (e.args[0], e.args[1]))
            raise Exception from e
        except IndexError:
            connection.rollback()
            print("SQL Error: %s" % str(e))
            raise Exception from e
    finally:
        cursor.close()
        connection.close()


def updateAd(ad, id):
    connection = initialiseConnection()
    cursor = connection.cursor()
    sql = "UPDATE pfe.ads SET title = '%s', description = '%s', price = %i, date = '%s', state = '%s', type = '%s', displayed_picture = %i, id_user = %i, id_category= %i WHERE id_ad = %i" % (
        ad['title'], ad['description'], ad['price'], ad['date'], ad['state'], ad['type'], ad['displayed_picture'], ad['id_user'], ad['id_category'], id)
    try:
        cursor.execute(sql)
        connection.commit()
    except (Exception, psycopg2.DatabaseError) as e:
        try:
            print("SQL Error [%d]: %s" % (e.args[0], e.args[1]))
            raise Exception from e
        except IndexError:
            connection.rollback()
            print("SQL Error: %s" % str(e))
            raise Exception from e
    finally:
        cursor.close()
        connection.close()

# CATEGORIES


def getCategoryByName(name_category):
    connection = initialiseConnection()
    cursor = connection.cursor()
    sql = "SELECT * FROM pfe.categories WHERE name='%s'" % (name_category)
    try:
        cursor.execute(sql)
        connection.commit()
        result = cursor.fetchone()
        category = {
            "id_category": result[0],
            "name": result[1],
            "parent_category": result[2]
        }
        return category
    except (Exception, psycopg2.DatabaseError) as e:
        try:
            print("SQL Error [%d]: %s" % (e.args[0], e.args[1]))
            raise Exception from e
        except IndexError:
            print("SQL Error: %s" % str(e))
            raise Exception from e
    finally:
        cursor.close()
        connection.close()


def getCategories():
    connection = initialiseConnection()
    cursor = connection.cursor()
    sql = "SELECT * FROM pfe.categories"
    resultCategories = []
    try:
        cursor.execute(sql)
        connection.commit()
        results = cursor.fetchall()
        for row in results:
            category = {
                "id_category": row[0],
                "name": row[1],
                "parent_category": row[2]
            }
            resultCategories.append(category)
        return resultCategories
    except (Exception, psycopg2.DatabaseError) as e:
        try:
            print("SQL Error [%d]: %s" % (e.args[0], e.args[1]))
            raise Exception from e
        except IndexError:
            print("SQL Error: %s" % str(e))
            raise Exception from e
    finally:
        cursor.close()
        connection.close()


def getCategoryById(id):
    connection = initialiseConnection()
    cursor = connection.cursor()
    sql = "SELECT * FROM pfe.categories WHERE id_category = %i" % (
        id
    )
    try:
        cursor.execute(sql)
        connection.commit()
        result = cursor.fetchone()
        category = {
            "id_category": result[0],
            "name": result[1],
            "parent_category": result[2]
        }
        return category
    except (Exception, psycopg2.DatabaseError) as e:
        try:
            print("SQL Error [%d]: %s" % (e.args[0], e.args[1]))
            raise Exception from e
        except IndexError:
            print("SQL Error: %s" % str(e))
            raise Exception from e
    finally:
        cursor.close()
        connection.close()


def createCategory(category):
    connection = initialiseConnection()
    cursor = connection.cursor()
    if(category['parent_category'] != 0):
        sql = "INSERT INTO pfe.categories VALUES(DEFAULT, '%s', %i)" % (
            category['name'], category['parent_category']
        )
    else:
        sql = "INSERT INTO pfe.categories VALUES(DEFAULT, '%s', NULL)" % (
            category['name']
        )
    try:
        cursor.execute(sql)
        connection.commit()
    except (Exception, psycopg2.DatabaseError) as e:
        try:
            print("SQL Error [%d]: %s" % (e.args[0], e.args[1]))
            raise Exception from e
        except IndexError:
            connection.rollback()
            print("SQL Error: %s" % str(e))
            raise Exception from e
    finally:
        cursor.close()
        connection.close()

# MEDIAS


def getMedias():
    connection = initialiseConnection()
    cursor = connection.cursor()
    sql = "SELECT * FROM pfe.medias"
    resultMedias = []
    try:
        cursor.execute(sql)
        connection.commit()
        results = cursor.fetchall()
        for row in results:
            media = {
                "id_media": row[0],
                "type": row[1],
                "url": row[2],
                "id_ad": row[3]
            }
            resultMedias.append(media)
        return resultMedias
    except (Exception, psycopg2.DatabaseError) as e:
        try:
            print("SQL Error [%d]: %s" % (e.args[0], e.args[1]))
            raise Exception from e
        except IndexError:
            print("SQL Error: %s" % str(e))
            raise Exception from e
    finally:
        cursor.close()
        connection.close()


def getMediaById(media_id):
    connection = initialiseConnection()
    cursor = connection.cursor()
    sql = "SELECT * FROM pfe.medias WHERE id_media = %i" % (media_id)
    try:
        cursor.execute(sql)
        connection.commit()
        results = cursor.fetchone()
        media = {
            "id_media": results[0],
            "type": results[1],
            "url": results[2],
            "id_ad": results[3]
        }
        return media
    except (Exception, psycopg2.DatabaseError) as e:
        try:
            print("SQL Error [%d]: %s" % (e.args[0], e.args[1]))
            raise Exception from e
        except IndexError:
            print("SQL Error: %s" % str(e))
            raise Exception from e
    finally:
        cursor.close()
        connection.close()


def getMediaByIdAd(ad_id):
    connection = initialiseConnection()
    cursor = connection.cursor()
    sql = "SELECT * FROM pfe.medias WHERE id_ad = %i" % (ad_id)
    resultMedias = []
    try:
        cursor.execute(sql)
        connection.commit()
        results = cursor.fetchall()
        for row in results:
            media = {
                "id_media": row[0],
                "type": row[1],
                "url": row[2],
                "id_ad": row[3]
            }
            resultMedias.append(media)
        return resultMedias
    except (Exception, psycopg2.DatabaseError) as e:
        try:
            print("SQL Error [%d]: %s" % (e.args[0], e.args[1]))
            raise Exception from e
        except IndexError:
            print("SQL Error: %s" % str(e))
            raise Exception from e
    finally:
        cursor.close()
        connection.close()


def deleteMedia(id):
    connection = initialiseConnection()
    cursor = connection.cursor()
    sql = "DELETE FROM pfe.medias WHERE id_media = %i" % (id)
    try:
        cursor.execute(sql)
        connection.commit()
    except (Exception, psycopg2.DatabaseError) as e:
        try:
            print("SQL Error [%d]: %s" % (e.args[0], e.args[1]))
            raise Exception from e
        except IndexError:
            connection.rollback()
            print("SQL Error: %s" % str(e))
            raise Exception from e
    finally:
        cursor.close()
        connection.close()


def createMedia(media):
    connection = initialiseConnection()
    cursor = connection.cursor()
    sql = "INSERT INTO pfe.medias VALUES(DEFAULT, '%s', '%s', %i)" % (
        media['type'], media['url'], media['id_ad']
    )
    try:
        cursor.execute(sql)
        connection.commit()
    except (Exception, psycopg2.DatabaseError) as e:
        try:
            print("SQL Error [%d]: %s" % (e.args[0], e.args[1]))
            raise Exception from e
        except IndexError:
            connection.rollback()
            print("SQL Error: %s" % str(e))
            raise Exception from e
    finally:
        cursor.close()
        connection.close()


def deleteMedia(id):
    connection = initialiseConnection()
    cursor = connection.cursor()
    sql = "DELETE FROM pfe.medias WHERE id_media = %i" % (id)
    try:
        cursor.execute(sql)
        connection.commit()
    except (Exception, psycopg2.DatabaseError) as e:
        try:
            print("SQL Error [%d]: %s" % (e.args[0], e.args[1]))
            raise Exception from e
        except IndexError:
            connection.rollback()
            print("SQL Error: %s" % str(e))
            raise Exception from e
    finally:
        cursor.close()
        connection.close()
