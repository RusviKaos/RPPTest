import fill_db as db_controller

#db_controller.DatabaseConnection()

#if __name__ == '__main__':
database_connection = db_controller.DatabaseConnection()
database_connection.delete_table(dataDeleteTable)