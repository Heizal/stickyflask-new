from app.extensions.database import db

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(80), unique=True)
    title = db.Column(db.String(80))
    content = db.Column(db.String(250))


# class Category(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     categoryName = db.Column(db.String(80))
#     category_id = db.Column(db.Integer, db.ForeignKey('category.id'))