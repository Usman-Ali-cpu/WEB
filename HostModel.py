import pymysql
from pymysql import connections
from pymysql import cursors

from ViewClasses import Hosts


class HostModel:
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

    def check_host_exist(self, host):
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                cursor.execute("select host_name from hosts")
                hosts = cursor.fetchall()
                for u in hosts:
                    if u[0] == host.name:
                        print(u[0])
                        print(host.name)
                        return True
                return False
        except Exception as e:
            print("Exception in checkHostExist", str(e))
        finally:
            if cursor != None:
                cursor.close()

    def add_host(self, host):
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                query = "INSERT INTO hosts (user_id,host_name, host_img , host_describe) values (%s, %s, %s, %s)"
                args = (host.user_id, host.name, host.host_img, host.describe)
                cursor.execute(query, args)
                self.connection.commit()
                return True
        except Exception as e:
            print("Exception in add host", str(e))
        finally:
            if cursor != None:
                cursor.close()

    def gethostid(self, username):
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                cursor.execute(
                    "select host_id , host_name from hosts")
                users = cursor.fetchall()
                for u in users:
                    print(str(u))
                    if u[1] == username:
                        return int(u[0])
                return -1
        except Exception as e:
            print("Exception in Login User", str(e))
        finally:
            if cursor != None:
                cursor.close()

    def gethostobjbyid(self, id):
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                cursor.execute(
                    "select host_describe , host_name from hosts where host_id= %s", id)
                users = cursor.fetchall()
                hostobj = Hosts("", 1, 1, 1, 1)
                hostobj.settter(users[0][0], users[0][0])
                return hostobj
        except Exception as e:
            print("Exception in Login User", str(e))
        finally:
            if cursor != None:
                cursor.close()
