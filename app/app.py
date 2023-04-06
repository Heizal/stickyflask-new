from . import notes, simple_pages
from flask import Flask, redirect, url_for, render_template
from app.extensions.database import db, migrate

def create_app():
    app = Flask(__name__)
    #app.config.from_object('app.config')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

    register_blueprints(app)
    register_extensions(app)

    return app



# Blueprints
def register_blueprints(app:Flask):
    app.register_blueprint(notes.routes.blueprint)
    app.register_blueprint(simple_pages.routes.blueprint)

def register_extensions(app: Flask):
  db.init_app(app)
  migrate.init_app(app, db, compare_type=True)