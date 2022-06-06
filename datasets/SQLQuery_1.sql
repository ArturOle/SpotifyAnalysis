

CREATE TABLE Revenues(
    song_id int,
    song_prop_id int,
    pricing_id int,
    artist_id int,
    profit int,
    streams int,
    song_name varchar(32),

    FOREIGN KEY (song_prop_id) REFERENCES SongProps(song_prop_id),
    FOREIGN KEY (song_id) REFERENCES Tops(song_id),
    FOREIGN KEY (pricing_id) REFERENCES Pricing(pricing_id),
    FOREIGN KEY (artist_id) REFERENCES Artists(artist_id)
)

CREATE TABLE Artists(
    artist_id int not null,
    artist_name varchar(32) not null,
    main_genre varchar(16) not null,
    PRIMARY KEY (artist_id)
)

CREATE TABLE SongProps(
    song_prop_id int not NULL,
    nrgy int(4),
    dnce int(4),
    dB int(4),
    live int(4),
    bmp int(4),
    val int(4),
    acous int(4),
    spch int(4),
    pop int(4),
    dur int(4),
    ensemble varchar(10),


    genre_1 varchar(16) not NULL,
    genre_2 varchar(16),
    genre_3 varchar(16),
    release_year year,
    top_year year,
    PRIMARY KEY (song_prop_id)
)

CREATE TABLE Tops(
    song_id int not null,
    song_position int not null,
    creation_date datetime,
    PRIMARY KEY (song_id)
)

CREATE TABLE Pricing(
    pricing_id int not null,
    price_per_stream FLOAT,
    year int,
    PRIMARY KEY (pricing_id)
)
