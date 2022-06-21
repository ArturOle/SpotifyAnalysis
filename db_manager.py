import sqlite3
from sqlite3 import Error
import pandas as pd


class NotConnectedError(Exception):
    def info(self):
        return 'Error: "You are not connected to the database"\n'


class Server:
    def __init__(self, db_name):
        self._db_name = db_name
        self.connection = None

    def connect(self):
        try:
            self.connection = sqlite3.connect(self._db_name)
            print("Connected")
        except Error as err:
            print(err)

    def query_script(self, query_script_name):
        query_string = None

        with open(query_script_name, 'r') as file:
            query_string = ''.join(file.readlines())
        
        if query_string:
            self.query(query_string)
        else:
            print("An problem occured")

    def query(self, query_code):
        if self.connection:
            cur = self.connection.cursor()
            cur.execute(query_code)
            rows = cur.fetchall()
            for row in rows:
                print(row)
        else:
            raise NotConnectedError

    def load_xlsx(self, xlsx_name="database.xlsx"):
        excel_file = pd.ExcelFile(xlsx_name)
        for i in excel_file.sheet_names:
            excel_file.parse(sheet_name=i).to_sql(i, self.connection, if_exists="replace")

    def load_csv(self, csv_name, separator=','):
        csv_file = pd.read_csv(csv_name, sep=separator)
        csv_file.to_sql(csv_name[:-4], self.connection, if_exists="replace")

    def export_json(self, table_name):
        pass

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("Disconnected")

    def __delete__(self):
        self.disconnect()


if __name__ == '__main__':
    server = Server("spotify.db")
    server.connect()
    # server.query(
    # """
    #     CREATE TABLE Revenues(
    #         song_id int,
    #         song_prop_id int,
    #         artist_id int,
    #         year int,
    #         profit int,
    #         streams int,
    #         song_name varchar(32),
            

    #         FOREIGN KEY (song_prop_id) REFERENCES SongProps(song_prop_id),
    #         FOREIGN KEY (song_id) REFERENCES Tops(song_id),
    #         FOREIGN KEY (year) REFERENCES Pricing(year),
    #         FOREIGN KEY (artist_id) REFERENCES Artists(artist_id)
    #     );
    # """
    # )
    # server.query(
    # """        
    #     CREATE TABLE Artists(
    #         artist_id int not null,
    #         artist_name varchar(32) not null,
    #         main_genre varchar(16) not null,
    #         PRIMARY KEY (artist_id)
    #     );
    # """
    # )
    # server.query(
    # """
    #     CREATE TABLE SongProps(
    #         song_prop_id int not NULL,
    #         nrgy int(4),
    #         dnce int(4),
    #         dB int(4),
    #         live int(4),
    #         bmp int(4),
    #         val int(4),
    #         acous int(4),
    #         spch int(4),
    #         pop int(4),
    #         dur int(4),
    #         ensemble varchar(10),


    #         genre_1 varchar(16) not NULL,
    #         genre_2 varchar(16),
    #         genre_3 varchar(16),
    #         release_year year,
    #         top_year year,
    #         PRIMARY KEY (song_prop_id)
    #     );
    # """
    # )
    # server.query(
    # """
    #     CREATE TABLE Tops(
    #         song_id int not null,
    #         song_position int not null,
    #         creation_date datetime,
    #         PRIMARY KEY (song_id)
    #     );
    # """
    # )
    # server.query(
    # """
    #     CREATE TABLE Pricing(
    #         year int not null,
    #         price_per_stream FLOAT,
    #         PRIMARY KEY (year)
    #     );
    # """
    # )
    # server.query(
    # """
    #     SELECT * FROM Pricing
    # """
    # )

