# To run the application, use the following commands in your terminal:
# $env:FLASK_APP = "application.py"
# $env:FLASK_ENV = "development"  
# flask run

from flask import Flask
app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy
from flask import request, jsonify

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///valorant.db'
db = SQLAlchemy(app)

class Valorant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    role = db.Column(db.String(120), unique=False, nullable=False)

    def __repr__(self):
        return f'<Valorant {self.name} : {self.role}>'

@app.route('/')
def index():
    return "Hello from Flask!"


@app.route('/add', methods=['POST'])
def add_agent():
    data = request.get_json()  # get JSON body from request

    name = data.get('name')
    role = data.get('role')

    # basic validation
    if not name or not role:
        return jsonify({'error': 'Missing name or role'}), 400

    # create new agent object
    new_agent = Valorant(name=name, role=role)

    # add to DB
    db.session.add(new_agent)
    db.session.commit()

    return jsonify({'message': f'Added {name} with role {role}'}), 201


@app.route('/agents', methods=['GET'])
def get_agents():
    agents = Valorant.query.all()  # get all rows from Valorant table
    output = []

    for agent in agents:
        output.append({
            'id': agent.id,
            'name': agent.name,
            'role': agent.role
        })

    return jsonify(output)





@app.cli.command("create-db")
def create_db():
    db.create_all()
    print("Database created successfully!")