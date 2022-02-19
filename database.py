import psycopg2 as pg
import csv


class DatabaseDB:
    
    
    def _init_(self):
        self.filename = 'filename'
        self.conn = None

    def connection(self):
        try:
            self.conn = pg.connect(
                host="localhost",
                database="teyematics",
                user="decagon",
                port="5432",
                password="Adewale@dec"
            )
            cursor = self.conn.cursor()
            print("working")
            return {"cursor": cursor, "conn": self.conn}
        except (Exception, pg.Error) as e:
            print(str(e))
        

    def create_table(self):
        # self.connection()
        sql_comm = '''
                CREATE TABLE IF NOT EXISTS posts(
                    userId INT NOT NULL, 
                    id INT NOT NULL, 
                    title VARCHAR(50) NOT NULL, 
                    body VARCHAR(255) NOT NULL, 
                    PRIMARY KEY (id) 
                    );
                '''

        my_connect = self.connection()
        cursor = my_connect["cursor"]
        self.conn = my_connect["conn"]
        cursor.execute(sql_comm)
        self.conn.close()

    def open_file(self):
        pass

    def insert_many(self):
        try:
            with open(self.filename, 'r') as f:
                reader = csv.reader(f)
                next(reader)  # This skips the 1st row which is the header.
        except Exception as e:
            print(str(e))

        my_connect = self.connection()
        self.open_file()
        cursor = my_connect["cursor"]
        conn = my_connect["conn"]
        sql_insert = """INSERT INTO posts(userId, id, title,
                        body)
                        VALUES(%s, %s, %s, %s)"""

        cursor.executemany(sql_insert, f)
        conn.commit()


db_connect = DatabaseDB()
db_connect.create_table()

