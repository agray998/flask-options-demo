from flask import Flask, request, render_template
from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField

choices = ['a', 'b', 'c']

class DemoForm(FlaskForm):
    for choice in choices:
        locals()[choice] = BooleanField(choice.upper())
    submit = SubmitField("Add Choice")

app = Flask(__name__)
app.config['SECRET_KEY'] = 'KVBVBVBSJVJFVBFBVBV'

@app.route('/', methods=['GET', 'POST'])
def index():
    form = DemoForm()
    selections = []
    if request.method == 'POST':
        for choice in ['a', 'b', 'c']:
            selections.append(choice.upper()) if getattr(form, choice).data else ...
        return render_template('view.html', all = selections)
    return render_template('home.html', form = form, fields = [getattr(form, choice) for choice in ['a', 'b', 'c']])

if __name__ == '__main__':
    app.run(debug=True)