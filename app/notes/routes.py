from .models import Note
from flask import Blueprint, render_template, request, current_app

blueprint = Blueprint('notes', __name__)

# Notes route
@blueprint.route('/notes')
def notes():
    page_number = request.args.get('page', 1, type=int)
    notes_pagination = Note.query.paginate(page=page_number, per_page=current_app.config['NOTES_PER_PAGE'])
    return render_template('notes/notes.html', notes_pagination=notes_pagination)

@blueprint.route('/notes/<slug>')
def note(slug):
    # return slug
    note = Note.query.filter_by(slug=slug).first()
    #x = note_data[slug]
    return render_template('notes/tasks.html', note=note)

@blueprint.route('/run-seed')
def run_seed():
    if not Note.query.filter_by(slug='Groceries').first():
        import app.scripts.seed
        return 'Database seed completed!'
    else:
        return 'Nothing to run.'