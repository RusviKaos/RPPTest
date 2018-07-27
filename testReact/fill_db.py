import psycopg2
from psycopg2 import sql
from pprint import pprint
import settings
class DatabaseConnection:
    def __init__(self):
        try:
            self.connection = psycopg2.connect("dbname='test_db' user='medeni' host='localhost' password='tester23' port='5432'")
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
            pprint("Coneccted")
        except:
            pprint("Cannot connect to database")
    def create_table(self, data):
        create_table_command = "CREATE TABLE Products(Id INTEGER PRIMARY KEY AUTO, Name VARCHAR(20), Price INT)"
        self.cursor.execute(create_table_command)
        self.connection.close()
    def insert_into_table(self, data):
        self.cursor.execute(sql.SQL("insert into {} values (%s, %s)")
        .format(sql.Identifier(data["Table"])),
        [data["Name"], data["Price"]])
        self.connection.close()
       # self.cursor.execute("INSERT INTO Products VALUES(" + data.id + "," + data.Name + "," + data.Price + ")")
    def show_table(self):
        self.cursor.execute("SELECT * FROM products")
        prods = self.cursor.fetchall()
        for prod in prods:
            pprint("product : {0}".format(prod))
        self.connection.close()
    def delete_record(self, data):
        self.cursor.execute(sql.SQL("delete from {} where id=%s")
        .format(sql.Identifier(data["Table"])),
        [data["id"]])
        self.connection.close()
    def delete_table(self, data):
        self.cursor.execute(sql.SQL("drop table {}")
        .format(sql.Identifier(data["Table"])),
        [])
        self.connection.close()

       #if __name__ == '__main__':
    
#    database_connection = DatabaseConnection()
    #database_connection.insert_into_table_products(data)