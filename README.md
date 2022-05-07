# SpotifyAnalysis

## How to start:

0) Download Python(preferably 3.9.x up), add python to PATH in virtual enviroments and use

```py
pip install virtualenv
or
python -m pip install virtualenv
```

1) Launch create virtual enviroment

```py
virtualenv venv
or
python -m virtualenv venv
```

3) Download all necessary packages

```py
pip install -r requirements.txt
or
python -m pip install -r requirements.txt
```

## Usage:

0) Launch Python in the console

1) Import db_manager as db
```py
>>> import db_manager as db 
```

2) Create server
```py
>>> server = db.Server("spotify.db")
```

3) Load the csv
```py
>>> server.load_csv("#NAME_FOR_TABLE_HERE#", separator="#IF_YOU HAVE CUSTOM SEPARATOR IN THE CSV#")
```

4) Run queries
```py
>>> server.query("#YOUR SQL QUERY HERE#")
or
>>> server.query_script("#path/to/sql/query.sql#")
```

## Datasets in question:

| Name | Link |
| ---- | ---- |
| Spotify daily top 200 (2017-2021) | https://www.kaggle.com/datasets/ivannatarov/spotify-daily-top-200-songs-with-genres-20172021 |
| Spotify top 100 (2015-2019) | https://www.kaggle.com/datasets/muhmores/spotify-top-100-songs-of-20152019?select=Spotify+2010+-+2019+Top+100.csv |
| Exemplary Spotify Recommendations | https://www.kaggle.com/datasets/bricevergnou/spotify-recommendation |
| Spotify Charts | https://www.kaggle.com/datasets/dhruvildave/spotify-charts |


