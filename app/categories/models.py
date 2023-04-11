from app.extensions.database import db

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    categoryName = db.Column(db.String(80))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))