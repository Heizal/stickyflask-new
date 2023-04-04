from flask import Blueprint, render_template

# Notes template dictionary
note_data = {
  'Groceries' : {'content': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Totam sequi error aliquid.', 'createdAt': 'DD/MM/YYYY', 'title':'Groceries'},
  'Class Assignment' : {'content': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Totam sequi error aliquid.', 'createdAt': 'DD/MM/YYYY','title':'Class Assignment'},
  'My thoughts' : {'content': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Totam sequi error aliquid.', 'createdAt': 'DD/MM/YYYY', 'title':'My thoughts'},
  'Class notes for Wednesday' : {'content': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Totam sequi error aliquid.', 'createdAt': 'DD/MM/YYYY', 'title':'Class notes for Wednesday'},
  'To buy on Friday' : {'content': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Totam sequi error aliquid.', 'createdAt': 'DD/MM/YYYY', 'title':'To buy on Friday'},
}

blueprint = Blueprint('notes', __name__)

# Notes route
@blueprint.route('/notes')
def notes():
    return render_template('notes/notes.html' , notes=note_data)

@blueprint.route('/notes/<slug>')
def note(slug):
    # return slug
    x = note_data[slug]
    return render_template('notes/tasks.html', note=x)
