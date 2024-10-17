### Database

```
docker-compose up -d
```

### Migration

```
flask --app main.py db migrate -m <MESSAGE>
flask --app main.py db upgrade
```

### Run the application

Run the scraper

```
python3 amazon_scraper.py
```

Run the flask app

```
python3 main.py
```
