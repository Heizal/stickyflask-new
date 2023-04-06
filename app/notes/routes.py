from .models import Note
from flask import Blueprint, render_template

blueprint = Blueprint('notes', __name__)

# Notes route
@blueprint.route('/notes')
def notes():
    all_notes = Note.query.all()
    return render_template('notes/notes.html' , notes=all_notes)

@blueprint.route('/notes/<slug>')
def note(slug):
    # return slug
    note = Note.query.filter_by(slug=slug).first()
    #x = note_data[slug]
    return render_template('notes/tasks.html', note=note)
