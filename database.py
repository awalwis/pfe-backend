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

    def getusers():
        sql = "SELECT * FROM pfe.users"
        resultsExportEtudiants = []
        try:
            cursor.execute(sql)
            connection.commit()
            results = cursor.fetchall()
            for row in results:
                item = {
                    "id_user": row[0],
                    "email": row[1],
                    "last_name": row[2],
                    "first_name": row[3]
                }
                resultsExportEtudiants.append(item)
            return resultsExportEtudiants
        except (Exception, psycopg2.DatabaseError) as e:
            try:
                print("SQL Error [%d]: %s" % (e.args[0], e.args[1]))
                return None
            except IndexError:
                print("SQL Error: %s" % str(e))
                return None
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
                return None
            except IndexError:
                connection.rollback()
                print("SQL Error: %s" % str(e))
                return None
            finally:
                cursor.close()
                connection.close()

    # ITEMS

except (Exception, psycopg2.DatabaseError) as e:
    print("DATABASE NOT CONNECTED")
    print("CONNECTION Error: %s" % str(e))
