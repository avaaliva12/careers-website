from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///user.db"

db = SQLAlchemy(app)

class User(db.Model):
    sno = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(250), nullable= False)
    password = db.Column(db.String(10), nullable= False)
    datetime = db.Column(db.DateTime,  default=datetime.utcnow)

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    all_users=User.query.all()
    return render_template('index.html', all_users = all_users)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/register", methods = ["GET", "POST"])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        new_user =User(
            username = username,
            password = password
        )
        db.session.add(new_user)
        db.session.commit()
    return render_template('register.html')

if __name__ == "__main__":
    app.run(debug=True)