from flask import Flask
from api.routes import api
# from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from database.db_manager import db

migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.register_blueprint(api, url_prefix='/api')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://saad:saad@localhost:5432/watch'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    return app