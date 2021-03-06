import pymysql
from pymysql import connections
from pymysql import cursors

from ViewClasses import Reviews


class ReviewModel:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        try:
            self.connection = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
            )
        except Exception as e:
            print("There is error in connection", str(e))

    def __del__(self):
        if self.connection != None:
            self.connection.close()

    def getreviews(self):
        try:
            if self.connection != None:
                reviewlist = []
                cursor = self.connection.cursor()
                cursor.execute(
                    "select review_id, review_profession, review_desc from reviews"
                )
                reviews = cursor.fetchall()
                for r in reviews:
                    print(r)
                    rev = Reviews(r[1], r[2], r[0])
                    reviewlist.append(rev)
                return reviewlist
        except Exception as e:
            print("Exception in checkUserExist", str(e))
        finally:
            if cursor != None:
                cursor.close()

    # def add_user(self, user):
    #     try:
    #         if self.connection != None:
    #             cursor = self.connection.cursor()
    #             query = "INSERT INTO users (name, email, password) values (%s, %s, %s)"
    #             args = (user.name, user.email, user.password)
    #             cursor.execute(query, args)
    #             self.connection.commit()
    #             return True
    #     except Exception as e:
    #         print("Exception in add user", str(e))
    #     finally:
    #         if cursor != None:
    #             cursor.close()

    # def login_user(self, user):
    #     try:
    #         if self.connection != None:
    #             cursor = self.connection.cursor()
    #             cursor.execute("select name, password from users")
    #             users = cursor.fetchall()
    #             for u in users:
    #                 print(str(u))
    #                 if u[0] == user.name and u[1] == user.password:
    #                     return True
    #             return False
    #     except Exception as e:
    #         print("Exception in Login User", str(e))
    #     finally:
    #         if cursor != None:
    #             cursor.close()
