#A Class for getting data from our database

import mysql.connector
import sys
from mysql.connector import Error


class DatabaseManager:
    def __init__(self, db_name = None):
        self.host_name = "localhost"
        self.username = "root"
        self.user_password = ""
        self.db_name = db_name
        
        
        # try:
        #     self.connect_controller(self.db_name)
        # except:
        #     self.connect_controller()
        #     self.mycursor.execute(f"CREATE DATABASE {self.db_name}")
        #     self.connect_controller(self.db_name)
        self.create_database()
        self.initial_table_setup()
    
    def create_database(self):
        query = f"""
        CREATE DATABASE IF NOT EXISTS `{self.db_name}`;
        """
        self.execute_query(query)

    def execute_query(self, query):
        connection = self.create_connection(self.host_name, self.username, self.user_password, self.db_name)
        cursor = connection.cursor()
        try:
            cursor.execute(query)
            connection.commit()
        except Error:
            pass
        connection.close()
        connection = None
    
    def execute_read_query(self, query):
        connection = self.create_connection(self.host_name, self.username, self.user_password, self.db_name)
        cursor = connection.cursor()
        result = None
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error:
            pass
        connection.close()
        connection = None
    
    def create_connection(self, host_name, username, user_password, db_name=""):
        try:
            return mysql.connector.connect(
                            host=host_name,
                            user=username,
                            passwd=user_password,
                            database=db_name,
                        )
        except Exception as e:
            try:
                # Will be run, if a new database is to be made.
                return mysql.connector.connect(
                    host=host_name,
                    user=username,
                    passwd=user_password,
                )
            except:
                status = "An error occurred while establishing a connnection to the database. Have you started it yet? (See log for more details)"
                print(status)
                sys.exit(0)

    # def connect_controller(self, database_name=None):
        
    #     self.mydb = mysql.connector.connect(
    #     host=self.host_name,
    #     user=self.username,
    #     password=self.user_password,
    #     database=database_name)
        
    #     self.mycursor = self.mydb.cursor()
    
    def initial_table_setup(self):
        self.execute_query("""
        CREATE TABLE IF NOT EXISTS Ids (
            id INT NOT NULL AUTO_INCREMENT,
            user_next_id BIGINT UNSIGNED NOT NULL DEFAULT 1,
            media_next_id BIGINT UNSIGNED NOT NULL DEFAULT 1,
            tag_next_id BIGINT UNSIGNED NOT NULL DEFAULT 1,
            PRIMARY KEY (id)
        ) ENGINE = InnoDB
        
""")

        self.execute_query("""
                            CREATE TABLE IF NOT EXISTS user(
                                Id BIGINT UNSIGNED NOT NULL,
                                Username VARCHAR(32) NOT NULL,
                                DisplayName VARCHAR(32) NOT NULL,
                                Description VARCHAR(500),
                                PasswordHash VARCHAR(256) NOT NULL,
                                Salt VARCHAR(128) NOT NULL,
                                CreationDate BIGINT UNSIGNED NOT NULL,
                                EmailAddress VARCHAR(256) NOT NULL,
                                PRIMARY KEY (Id)
                            ) ENGINE = InnoDB
""")
        
        self.execute_query("""
                            CREATE TABLE IF NOT EXISTS media(
                                Id BIGINT UNSIGNED NOT NULL,
                                MediaName VARCHAR(32) NOT NULL,
                                Description VARCHAR(500),
                                CreationDate INT NOT NULL,
                                PRIMARY KEY (Id)
                            ) ENGINE = InnoDB
""")      #Tags(~ID[ASCII], Content[Unicode]~)
        
        self.execute_query("""
                                CREATE TABLE IF NOT EXISTS tag(
                                    Id BIGINT UNSIGNED NOT NULL,
                                    Content VARCHAR(128),
                                    PRIMARY KEY (Id)
                                ) ENGINE = InnoDB
""") 
        
        self.execute_query("""
                                CREATE TABLE IF NOT EXISTS tagrelation(
                                    MediaId INT NOT NULL,
                                    TagId INT NOT NULL,
                                    PRIMARY KEY (MediaId, TagId)
                                ) ENGINE = InnoDB
""")

        if not self.execute_read_query("SELECT * FROM ids WHERE id = 1"):
            self.execute_query("INSERT INTO Ids () VALUES ()")

manager = DatabaseManager("media_platform_database")