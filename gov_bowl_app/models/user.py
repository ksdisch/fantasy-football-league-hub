from gov_bowl_app import db # We're importing the SQLAlchemy instance that we created in __init__.py

# We're defining a new class 'User' that inherits from db.Model
# Each class that inherits from db.Model corresponds to a table in the database.
# Each attribute of the class represents a column in the table.
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username
    



# Get data in this bish