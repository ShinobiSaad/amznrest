from database.db_manager import db


class Page(db.Model):
    last_page_scraped = db.Column(db.Integer, primary_key=True)

class Product(db.Model):
    __tablename__ = 'product'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    brand = db.Column(db.String)
    model = db.Column(db.String)
    price = db.Column(db.Float)
    image_url = db.Column(db.String)
    specifications = db.Column(db.String)
    ratings = db.Column(db.String)


class Review(db.Model):
    __tablename__ = 'review'

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer)
    rating = db.Column(db.Float)
    review_text = db.Column(db.String)
    reviewer_name = db.Column(db.String)
    review_date = db.Column(db.String)

