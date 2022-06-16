from pandas import to_datetime
import pymysql
from pymysql import connections
from pymysql import cursors
from sympy import im

from ViewClasses import Experiences


class ExperienceModel:
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

    def get_allofexps(self):
        try:
            if self.connection != None:
                experiencelist = []
                cursor = self.connection.cursor()
                cursor.execute(
                    "select * from experiences"
                )
                experience = cursor.fetchall()
                for t in experience:
                    print(t)
                    rev = Experiences(h_id=t[1], img=[t[2], t[3], t[4]], t_title=t[5], t_description=t[7], t_location=t[8], t_days=t[9], t_capacity=t[10],
                                      t_price_default=t[11],  t_describe_default=t[12], t_start_date=t[13], t_end_date=t[14])
                    rev.experience_id = int(t[0])
                    print(rev.experience_id)
                    experiencelist.append(rev)
                return experiencelist
        except Exception as e:
            print("Exception in Experience Getting", str(e))
        finally:
            if cursor != None:
                cursor.close()

    def getcardofexperience(self):
        try:
            if self.connection != None:
                experiencelist = []
                cursor = self.connection.cursor()
                cursor.execute(
                    "select experience_img1  experience_title experience_location experience_days experience_price_default experience_capacity from experiences"
                )
                experience = cursor.fetchall()
                for t in experience:
                    print(t)
                    rev = Experiences()
                    rev.addinit(experience_img1=t[0], experience_title=t[1], experience_location=t[2],
                                experience_days=t[3], experience_price_default=t[4], experience_capacity=t[5])
                    experiencelist.append(rev)
                return experiencelist
        except Exception as e:
            print("Exception in Experience Getting", str(e))
        finally:
            if cursor != None:
                cursor.close()

    def getdatabyid(self, expid):
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                cursor.execute(
                    "select host_id,experience_img1,experience_img2,experience_img3,experience_title,experience_description,experience_location,experience_days,experience_capacity,experience_price_default,experience_describe_default, experience_start_date, experience_end_date, driver_age from experiences where experience_id = %s", expid)
                exp = cursor.fetchall()
                print(exp)
                rev = Experiences(h_id=exp[0][0], img=[
                                  exp[0][1], exp[0][2], exp[0][3]],
                                  t_title=exp[0][4], t_description=exp[0][5],
                                  t_location=exp[0][6], t_days=exp[0][7],
                                  t_capacity=exp[0][8], t_price_default=exp[0][9],
                                  t_describe_default=exp[0][10],
                                  t_start_date=exp[0][11],
                                  t_end_date=exp[0][12])
                return rev
        except Exception as e:
            print("Exception in Single Experience Getting", str(e))
        finally:
            if cursor != None:
                cursor.close()

    def deletedatabyid(self, expid):
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                cursor.execute(
                    "DELETE from experiences where experience_id= % s", expid)
                self.connection.commit()
        except Exception as e:
            print("Exception in Single Experience Getting", str(e))
        finally:
            if cursor != None:
                cursor.close()

    def insert_experience(self, experience):
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                query = "INSERT INTO experiences (host_id,experience_img1,experience_img2,experience_img3,experience_title,experience_description,experience_location,experience_days,experience_capacity,experience_price_default,experience_describe_default, experience_start_date, experience_end_date, driver_age) values (%s, %s, %s, %s, %s, %s ,%s, %s,  %s, %s, %s, %s, %s, %s)"
                args = (experience.hostId,
                        experience.experience_img1,
                        experience.experience_img2,
                        experience.experience_img3,
                        experience.experience_title,
                        experience.experience_description,
                        experience.experience_location,
                        experience.experience_days,
                        experience.experience_capacity,
                        experience.experience_price_default,
                        experience.experience_describe_default,
                        experience.experience_start_date,
                        experience.experience_end_date,
                        experience.experience_age
                        )
                print(args)
                cursor.execute(query, args)
                self.connection.commit()
                return True
        except Exception as e:
            print("Exception in experience add experience", str(e))
        finally:
            if cursor != None:
                cursor.close()
