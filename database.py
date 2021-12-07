import psycopg2

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

    cursor = connection.cursor()

    # USERS

    def getUsers():
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
                    "isadmin": row[6],
                    "isbanned": row[7]
                }
                resultsExportUsers.append(user)
            return resultsExportUsers
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

    def getUser(id):
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
                "isadmin": result[6],
                "isbanned": result[7]
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
        sql = "INSERT INTO pfe.users VALUES (DEFAULT,'%s','%s','%s','%s','%s','%s','%s')" % (
            user['email'], user['last_name'], user['first_name'], user['password'], user['campus'], user['isAdmin'], user['isBanned'])
        try:
            cursor.execute(sql)
            connection.commit()
        except (Exception, psycopg2.DatabaseError) as e:
            try:
                print("SQL Error [%d]: %s" % (e.args[0], e.args[1]))
                raise Exception(e.args[1])
            except IndexError:
                connection.rollback()
                print("SQL Error: %s" % str(e))
                raise Exception(e.args[1])
            finally:
                cursor.close()
                connection.close()

    def updateUser(user, id):
        sql = "UPDATE pfe.users SET email = '%s', last_name = '%s', first_name = '%s', password = '%s', campus = '%s', isAdmin = '%s', isBanned = '%s' WHERE id_user = %i" % (
            user['email'], user['last_name'], user['first_name'], user['password'], user['campus'], user['isAdmin'], user['isBanned'], id)
        try:
            cursor.execute(sql)
            connection.commit()
        except (Exception, psycopg2.DatabaseError) as e:
            try:
                print("SQL Error [%d]: %s" % (e.args[0], e.args[1]))
                raise Exception(e.args[1])
            except IndexError:
                connection.rollback()
                print("SQL Error: %s" % str(e))
                raise Exception(e.args[1])
            finally:
                cursor.close()
                connection.close()

    def deleteUser(id):
        sql = "DELETE FROM pfe.users WHERE id_user = %i" % (id)
        try:
            cursor.execute(sql)
            connection.commit()
        except (Exception, psycopg2.DatabaseError) as e:
            try:
                print("SQL Error [%d]: %s" % (e.args[0], e.args[1]))
                raise Exception(e.args[1])
            except IndexError:
                connection.rollback()
                print("SQL Error: %s" % str(e))
                raise Exception(e.args[1])
            finally:
                cursor.close()
                connection.close()

    def banUser(user_id):
        sql = "UPDATE pfe.users SET isBanned = NOT isBanned WHERE id_user = %i" % (
            user_id
        )
        try:
            cursor.execute(sql)
            connection.commit()
        except(Exception, psycopg2.DatabaseError) as e:
            try:
                print("SQL Error [%d]: %s" % (e.args[0], e.args[1]))
                return None
            except IndexError:
                connection.rollback()
                print("SQL Error: %s" % str(e))
                return None
            finally:
                cursor.close()
                connection.close()

    # ADS

    def getAds():
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
                    "id_user": row[7],
                    "id_category": row[8]
                }
                resultsExportAds.append(ad)
            return resultsExportAds
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

    def getAdsWithCategory(id_category):
        sql = "SELECT * FROM pfe.ads WHERE id_category=%i" % (id_category)
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
                    "id_user": row[7],
                    "id_category": row[8]
                }
                resultsExportAds.append(ad)
            return resultsExportAds
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

    def getAdsWithSort(sort):
        sql = "SELECT * FROM pfe.ads ORDER BY price %s" % (sort)
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
                    "id_user": row[7],
                    "id_category": row[8]
                }
                resultsExportAds.append(ad)
            return resultsExportAds
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

    def getAdsByPrice(priceMin, priceMax):
        sql = "SELECT * FROM pfe.ads WHERE price BETWEEN %i AND %i" % (
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
                    "id_user": row[7],
                    "id_category": row[8]
                }
                resultsExportAds.append(ad)
            return resultsExportAds
        except (Exception, psycopg2.DatabaseError) as e:
            try:
                print("SQL Error [%d]: %s" % (e.args[0], e.args[1]))
                raise Exception(e.args[1])
            except IndexError:
                connection.rollback()
                print("SQL Error: %s" % str(e))
                raise Exception(e.args[1])
            finally:
                cursor.close()
                connection.close()

    def getAdsByCategoryAndSort(id_category, sort):
        sql = "SELECT * FROM pfe.ads WHERE id_category=%i ORDER BY price %s" % (
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
                    "id_user": row[7],
                    "id_category": row[8]
                }
                resultsExportAds.append(ad)
            return resultsExportAds
        except (Exception, psycopg2.DatabaseError) as e:
            try:
                print("SQL Error [%d]: %s" % (e.args[0], e.args[1]))
                raise Exception(e.args[1])
            except IndexError:
                connection.rollback()
                print("SQL Error: %s" % str(e))
                raise Exception(e.args[1])
            finally:
                cursor.close()
                connection.close()

    def getAdsByCategoryAndPrice(id_category, prixMin, prixMax):
        sql = "SELECT * FROM pfe.ads WHERE id_category=%i AND price BETWEEN %i AND %i" % (
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
                    "id_user": row[7],
                    "id_category": row[8]
                }
                resultsExportAds.append(ad)
            return resultsExportAds
        except (Exception, psycopg2.DatabaseError) as e:
            try:
                print("SQL Error [%d]: %s" % (e.args[0], e.args[1]))
                raise Exception(e.args[1])
            except IndexError:
                connection.rollback()
                print("SQL Error: %s" % str(e))
                raise Exception(e.args[1])
            finally:
                cursor.close()
                connection.close()

    def getAdsBySortAndPrice(sort, prixMin, prixMax):
        sql = "SELECT * FROM pfe.ads WHERE price BETWEEN %i AND %i ORDER BY price %s" % (
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
                    "id_user": row[7],
                    "id_category": row[8]
                }
                resultsExportAds.append(ad)
            return resultsExportAds
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

    def getAdsByCategoryAndSortAndPrice(id_category, sort, prixMin, prixMax):
        sql = "SELECT * FROM pfe.ads WHERE id_category=%i AND price BETWEEN %i AND %i ORDER BY price %s" % (
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
                    "id_user": row[7],
                    "id_category": row[8]
                }
                resultsExportAds.append(ad)
            return resultsExportAds
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

    def getAd(id):
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
                "id_user": result[7],
                "id_category": result[8]
            }
            return ad
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

    def createAd(ad):
        sql = "INSERT INTO pfe.ads VALUES (DEFAULT,'%s','%s',%i,'%s','%s','%s',%i ,%i)" % (
            ad['title'], ad['description'], ad['price'], ad['date'], ad['state'], ad['type'], ad['id_user'], ad['id_category'])
        try:
            cursor.execute(sql)
            connection.commit()
        except (Exception, psycopg2.DatabaseError) as e:
            try:
                print("SQL Error [%d]: %s" % (e.args[0], e.args[1]))
                raise Exception(e.args[1])
            except IndexError:
                connection.rollback()
                print("SQL Error: %s" % str(e))
                raise Exception(e.args[1])
            finally:
                cursor.close()
                connection.close()

    def deleteAd(id):
        sql = "DELETE FROM pfe.ads WHERE id_ad = %i" % (id)
        try:
            cursor.execute(sql)
            connection.commit()
        except (Exception, psycopg2.DatabaseError) as e:
            try:
                print("SQL Error [%d]: %s" % (e.args[0], e.args[1]))
                raise Exception(e.args[1])
            except IndexError:
                connection.rollback()
                print("SQL Error: %s" % str(e))
                raise Exception(e.args[1])
            finally:
                cursor.close()
                connection.close()

    def updateUser(ad, id):
        sql = "UPDATE pfe.ads SET title = '%s', description = '%s', price = %i, date = '%s', state = '%s', type = '%s', id_user = %i, id_category= %i WHERE id_ad = %i" % (
            ad['title'], ad['description'], ad['price'], ad['date'], ad['state'], ad['type'], ad['id_user'], ad['id_category'], id)
        try:
            cursor.execute(sql)
            connection.commit()
        except (Exception, psycopg2.DatabaseError) as e:
            try:
                print("SQL Error [%d]: %s" % (e.args[0], e.args[1]))
                raise Exception(e.args[1])
            except IndexError:
                connection.rollback()
                print("SQL Error: %s" % str(e))
                raise Exception(e.args[1])
            finally:
                cursor.close()
                connection.close()

    # CATEGORIES

    def getCategoryByName(name_category):
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
                raise Exception(e.args[1])
            except IndexError:
                print("SQL Error: %s" % str(e))
                raise Exception(e.args[1])
            finally:
                cursor.close()
                connection.close()

except (Exception, psycopg2.DatabaseError) as e:
    print("DATABASE NOT CONNECTED")
    print("CONNECTION Error: %s" % str(e))
