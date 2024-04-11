#A Class for getting data from our database

import mysql.connector

class DatabaseManager:
    def __init__(self, database_name = None):
        self.host = "localhost"
        self.user = "root"
        self.password = ""
        self.database_name = database_name
        
        
        if database_name is None:
            self.connect_controller()
            self.database_name = "media_platform_database"
            self.mycursor.execute(f"CREATE DATABASE {self.database_name}")
        
        self.connect_controller()
        self.initial_table_setup()
        

    def connect_controller(self):
        self.mydb = mysql.connector.connect(
        host=self.host,
        user=self.user,
        password=self.password,
        database=self.database_name)
        
        self.mycursor = self.mydb.cursor()
    
    def initial_table_setup(self):
        self.mycursor.execute("""
                            CREATE TABLE IF NOT EXISTS user(
                                Id INT NOT NULL AUTO_INCREMENT,
                                Username VARCHAR(32) NOT NULL,
                                DisplayName VARCHAR(32) NOT NULL,
                                Description VARCHAR(500),
                                PasswordHash VARCHAR(256) NOT NULL,
                                CreationDate INT NOT NULL,
                                EmailAddress VARCHAR(256) NOT NULL,
                                Server VARCHAR(128) NOT NULL,
                                PRIMARY KEY (Id)
                            ) ENGINE = InnoDB
""")
        #Medie(~MedieID[ASCII]~, MedieNavn[Unicode], Beskrivelse[Unicode], OprettelsesDato[Timestamp])
        self.mycursor.execute("""
                            CREATE TABLE IF NOT EXISTS media(
                                Id INT NOT NULL AUTO_INCREMENT,
                                MediaName VARCHAR(32) NOT NULL,
                                Description VARCHAR(500),
                                CreationDate INT NOT NULL,
                                PRIMARY KEY (Id)
                            ) ENGINE = InnoDB
""")      #Tags(~ID[ASCII], Content[Unicode]~)
        self.mycursor.execute("""
                                CREATE TABLE IF NOT EXISTS tag(
                                    Id INT NOT NULL AUTO_INCREMENT,
                                    Content VARCHAR(128),
                                    PRIMARY KEY (Id)
                                ) ENGINE = InnoDB
""") 
        #TagRelation(~TagID[ASCII], MedieID[ASCII]~)
        self.mycursor.execute("""
                                CREATE TABLE IF NOT EXISTS tagrelation(
                                    MediaId INT NOT NULL,
                                    TagId INT NOT NULL,
                                    PRIMARY KEY (MediaId, TagId)
                                ) ENGINE = InnoDB
""")
    def create_user(self, username, password, email):
        pass

DatabaseManager("media_platform_database")