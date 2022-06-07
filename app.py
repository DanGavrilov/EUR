from datetime import datetime

from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask_test.db'
db = SQLAlchemy(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Article %r>' % self.id


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/create-aricle', methods=['POST', 'GET'])
def data_base():
    if request.method == 'POST':
        name = request.form['name']
        article = Article(name=name)

        try:
            db.session.add(article)
            db.session.commit()
            return redirect('/')
        except:
            return "Помилочка..."

    else:
        return render_template('create-aricle.html')


if __name__ == "__main__":
    app.run(debug=True)