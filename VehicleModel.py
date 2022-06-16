from pandas import to_datetime
import pymysql
from pymysql import connections
from pymysql import cursors

from ViewClasses import Vehicles


class VehicleModel:
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

    def get_allofVehicle(self):
        try:
            if self.connection != None:
                Vehiclelist = []
                cursor = self.connection.cursor()
                cursor.execute(
                    "select * from Vehicles"
                )
                Vehicle = cursor.fetchall()
                for t in Vehicle:
                    print(t)
                    rev = Vehicles(h_id=t[1], img=[t[2], t[3], t[4]], t_title=t[5], t_description=t[6], t_location=t[7], t_days=t[8], t_capacity=t[9],
                                   t_price_default=t[10],  t_describe_default=t[11], t_start_date=t[12], t_end_date=t[13])
                    Vehiclelist.append(rev)
                return Vehiclelist
        except Exception as e:
            print("Exception in Vehicle Getting", str(e))
        finally:
            if cursor != None:
                cursor.close()

    def getcardofVehicle(self):
        try:
            if self.connection != None:
                Vehiclelist = []
                cursor = self.connection.cursor()
                cursor.execute(
                    "select Vehicle_img1  Vehicle_title Vehicle_location Vehicle_days Vehicle_price_default Vehicle_capacity from Vehicles"
                )
                Vehicle = cursor.fetchall()
                for t in Vehicle:
                    print(t)
                    rev = Vehicles()
                    rev.addinit(vehicle_img1=t[0], vehicle_title=t[1], vehicle_location=t[2],
                                vehicle_days=t[3], vehicle_price_default=t[4], vehicle_capacity=t[5])
                    Vehiclelist.append(rev)
                return Vehiclelist
        except Exception as e:
            print("Exception in Vehicle Getting", str(e))
        finally:
            if cursor != None:
                cursor.close()

    def insert_Vehicle(self, Vehicle):
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                query = "INSERT INTO Vehicles (host_id,vehicle_img1,vehicle_img2,vehicle_img3,vehicle_title,vehicle_description,vehicle_location,vehicle_days,vehicle_capacity,vehicle_price_default,vehicle_describe_default, vehicle_start_date, vehicle_end_date, driver_age) values (%s, %s, %s, %s, %s, %s ,%s, %s,  %s, %s, %s, %s, %s, %s)"
                args = (Vehicle.hostId,
                        Vehicle.vehicle_img1,
                        Vehicle.vehicle_img2,
                        Vehicle.vehicle_img3,
                        Vehicle.vehicle_title,
                        Vehicle.vehicle_description,
                        Vehicle.vehicle_location,
                        Vehicle.vehicle_days,
                        Vehicle.vehicle_capacity,
                        Vehicle.vehicle_price_default,
                        Vehicle.vehicle_describe_default,
                        Vehicle.vehicle_start_date,
                        Vehicle.vehicle_end_date,
                        Vehicle.vehicle_age
                        )
                print(args)
                cursor.execute(query, args)
                self.connection.commit()
                return True
        except Exception as e:
            print("Exception in Vehicle add Vehicle", str(e))
        finally:
            if cursor != None:
                cursor.close()
