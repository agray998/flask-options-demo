from flask import Flask, request, render_template, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField

global_stuff = []

class DemoForm(FlaskForm):
    demo = SelectField("Choose all that apply", choices=[('A', 'A'), ('B', 'B'), ('C', 'C')])
    submit = SubmitField("Add Choice")

app = Flask(__name__)
app.config['SECRET_KEY'] = 'KVBVBVBSJVJFVBFBVBV'

@app.route('/', methods=['GET', 'POST'])
def index():
    global global_stuff
    global_stuff = []
    form = DemoForm()
    selections = list(dict(request.args).values())
    add_url = url_for('add') + '?' + '&'.join(f"choice_{i}={item}" for i, item in enumerate(selections))
    if request.method == 'POST':
        selections.append(form.demo.data)
        return redirect(url_for('index') + '?' + '&'.join(f"choice_{i}={item}" for i, item in enumerate(selections)))
    return render_template('home_2.html', form=form, selections=selections, add_url = add_url)

@app.route('/add')
def add():
    selections = list(dict(request.args).values())
    global_stuff.extend(selections)
    return render_template('view.html', all=global_stuff)

if __name__ == '__main__':
    app.run(debug=True)