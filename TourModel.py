from pandas import to_datetime
import pymysql
from pymysql import connections
from pymysql import cursors

from ViewClasses import Tours


class TourModel:
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

    def get_alloftours(self):
        try:
            if self.connection != None:
                tourslist = []
                cursor = self.connection.cursor()
                cursor.execute(
                    "select * from tours"
                )
                tours = cursor.fetchall()
                for t in tours:
                    print(t)
                    rev = Tours(t_id=t[0], h_id=t[1], img=[t[2], t[3], t[4]], t_title=t[5], t_description=t[6], t_location=t[7], t_days=t[8], t_capacity=t[9],
                                t_price_default=t[10], t_price_delux=t[11], t_describe_default=t[12],
                                t_decribe_delux=t[13], t_start_date=t[14], t_end_date=t[15])
                    tourslist.append(rev)
                    print(rev)
                return tourslist
        except Exception as e:
            print("Exception in TourGetting", str(e))
        finally:
            if cursor != None:
                cursor.close()

    def getcardoftours(self):
        try:
            if self.connection != None:
                tourslist = []
                cursor = self.connection.cursor()
                cursor.execute(
                    "select tour_img1  tour_title tour_location tour_days tour_price_default tour_capacity from tours"
                )
                tours = cursor.fetchall()
                for t in tours:
                    print(t)
                    rev = Tours()
                    rev.addinit(tour_img1=t[0], tour_title=t[1], tour_location=t[2],
                                tour_days=t[3], tour_price_default=t[4], tour_capacity=t[5])
                    tourslist.append(rev)
                return tourslist
        except Exception as e:
            print("Exception in Tour Getting", str(e))
        finally:
            if cursor != None:
                cursor.close()

    def getdatabyid(self, tourid):
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                cursor.execute(
                    "select host_id,tour_img1,tour_img2,tour_img3,tour_title,tour_description,tour_location,tour_days,tour_capacity,tour_price_default,tour_describe_default, tour_start_date, tour_end_date from tours where tour_id = %s", tourid)
                tour = cursor.fetchall()
                print("njncjff")
                print(tour)
                rev = Tours(h_id=tour[0][0], img=[
                    tour[0][1], tour[0][2], tour[0][3]],
                    t_title=tour[0][4], t_description=tour[0][5],
                    t_location=tour[0][6], t_days=tour[0][7],
                    t_capacity=tour[0][8], t_price_default=tour[0][9],
                    t_decribe_delux=0,
                    t_id=tourid,
                    t_price_delux=0,
                    t_describe_default=tour[0][10],
                    t_start_date=tour[0][11],
                    t_end_date=tour[0][12])
                return rev
        except Exception as e:
            print("Exception in Single Tour Getting", str(e))
        finally:
            if cursor != None:
                cursor.close()

    def insert_tour(self, tour):
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                query = "INSERT INTO tours (host_id,tour_img1,tour_img2,tour_img3,tour_title,tour_description,tour_location,tour_days,tour_capacity,tour_price_default,tour_price_delux,tour_describe_default,tour_describe_delux, tour_start_date, tour_end_date) values (%s, %s, %s, %s, %s, %s ,%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                args = (tour.hostId,
                        tour.tour_img1,
                        tour.tour_img2,
                        tour.tour_img3,
                        tour.tour_title,
                        tour.tour_description,
                        tour.tour_location,
                        tour.tour_days,
                        tour.tour_capacity,
                        tour.tour_price_default,
                        tour.tour_price_delux,
                        tour.tour_describe_default,
                        tour.tour_describe_delux,
                        tour.tour_start_date,
                        tour.tour_end_date)
                print(args)
                cursor.execute(query, args)
                self.connection.commit()
                return True
        except Exception as e:
            print("Exception in tour add tour", str(e))
        finally:
            if cursor != None:
                cursor.close()
