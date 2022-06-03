CREATE TABLE Revenue(
    song_id int,
    song_prop_id int,
    pricing_id int,
    date_id int,
    artist_id int,

    profit int,  
    streams int,
    song_name VARCHAR,

    FOREIGN KEY (song_prop_id) REFERENCES SongProps(song_prop_id),
    FOREIGN KEY (date_id) REFERENCES Dates(date_id),
    FOREIGN KEY (song_id) REFERENCES Tops(song_id),
    FOREIGN KEY (pricing_id) REFERENCES Pricing(pricing_id),
    FOREIGN KEY (artist_id) REFERENCES Artists(artist_id)
)

CREATE TABLE Artists(
    artist_id int not null,
    artist_name varchar,
    main_genre varchar,
    PRIMARY KEY (artist_id)
)

CREATE TABLE SongProps(
    song_prop_id int not NULL,
    nrgy int,
    dnce int,
    dB int,
    live int,
    bmp int,
    genre_1 varchar not NULL,
    genre_2 varchar,
    genre_3 VARCHAR,
    PRIMARY KEY (song_prop_id)
)

CREATE TABLE Dates(
    date_id int NOT NULL,
    year int,
    month int,
    day int,
    PRIMARY KEY (date_id)
)

CREATE TABLE Tops(
    song_id int not null,
    song_position int,
    region varchar,
    creation_date datetime,
    PRIMARY KEY (song_id)
)

CREATE TABLE Pricing(
    pricing_id int not null,
    price_per_stream FLOAT,
    year int,
    PRIMARY KEY (pricing_id)
)
