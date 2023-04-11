from flask import Blueprint, render_template
from app.notes.models import Note

blueprint = Blueprint('categories', __name__)

@blueprint.get('/checkout')
def get_checkout():
  notes = Note.query.all()

  return render_template('categories/category.html', notes = notes)

@blueprint.post('/checkout')
def post_checkout():
  notes = Note.query.all()

  return render_template('categories/category.html', notes = notes)