from  flask import Flask
app = Flask(__name__)
from flask_sqlalachemy import SQLAlchemy 

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

#her bygger vi en class til at python kan læse sql
class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120))

    def __repr__(self) -> str:
        return f"{self.name} - {self.description}"

#her laver vi bare web routes til API'en
#første side er bare en test
@app.route('/'):
def index():
    return 'HELLOOOO!'
#anden side som hedder all wines, er her hvor vi kan se alle vine.
@app.route('/allwines')
def get_allwines():
    return drinks