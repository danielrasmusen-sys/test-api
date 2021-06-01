from flask import Flask, request
from flask.wrappers import Request
from flask_sqlalchemy import SQLAlchemy 
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

#her bygger vi en class til at python kan læse sql
class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120))
    varenr = db.Column(db.String(80), unique=True)

    def __repr__(self) -> str:
        return f"{self.name} - {self.description} - {self.varenr}"

#her laver vi bare web routes til API'en
#første side er bare en test
@app.route('/')
def index():
    return 'LAGERBOI - Dette er start siden til din lagerstyring, request gerne allwines istedet'
#anden side som hedder all wines, er her hvor vi kan se alle vine.
@app.route('/allwines')
def get_drinks():
    drinks = Drink.query.all()
    output = []
    for drink in drinks:
        drink_data = {'name': drink.name, 'description': drink.description, 'varenr': drink.varenr}
        output.append(drink_data)

    return {"drinks": output} 
#her laver vi, id' til vine og kan print/returne dem hvis man vil via ID nummeret.
@app.route('/allwines/<id>')
def get_drink(id):
    drink = Drink.query.get_or_404(id)
    return {"name": drink.name, "description": drink.description}

@app.route('/allwines', methods=['POST'])
def add_drink():
    drink = Drink(name=request.json['name'], description=request.json['description'])
    db.session.add(drink)
    db.session.commit()
    return {'id': drink.id}