from flask import Flask, render_template, redirect, url_for, flash
import flask_wtf
import wtforms

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
class SubscriptionForm(flask_wtf.FlaskForm):
    name = wtforms.StringField('Ваше імя', validators=[wtforms.validators.DataRequired()])
    surname = wtforms.StringField('Ваше прізвище', validators=[wtforms.validators.DataRequired()])
    submit = wtforms.SubmitField('продовжити')

@app.route('/', methods=['GET', 'POST'])
def web():
    form = SubscriptionForm()
    if form.validate_on_submit():
        name = form.name.data
        surname = form.surname.data
        # Process the form data (e.g., save to database)
        flash('Операція пройшла успішно!', 'success')
        return redirect(url_for('swim'))  # Redirect to avoid form resubmission
    return render_template("swim.html", form=form)

@app.route('/')
def swim():
    return render_template("swim.html")

@app.route('/swim1')
def swim1():
    return render_template("swim1.html")

@app.route('/swim2')
def swim2():
    return render_template("swim2.html")

@app.route('/swim3')
def swim3():
    return render_template("swim3.html")

@app.route('/swim4')
def swim4():
    return render_template("swim4.html")

@app.route('/swim5')
def swim5():
    return render_template("swim5.html")

@app.route('/swim6')
def swim6():
    return render_template("swim6.html")
if __name__ == "__main__":
    app.run(debug=True)