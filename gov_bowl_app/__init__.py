# File purpose: Intialize Flask application and SQLAlchemy
from flask import Flask
from dotenv import load_dotenv
import os
from flask_sqlalchemy import SQLAlchemy # SQLAlchemy is a SQL toolkit and object relational mapper (ORM).
from flask_bootstrap import Bootstrap

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    bootstrap = Bootstrap(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./governors_bowl.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)

    from gov_bowl_app.routes.main import main 
    app.register_blueprint(main)

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)

# app = Flask(__name__) # Creates a new Flask web server instance
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./governors_bowl.db'# Tells Flask-SQLAlchemy where the database is located

# db = SQLAlchemy(app) # Creates a new SQLAlchemy instance, which is our ORM


# from gov_bowl_app.routes.main import main # This line imports the main blueprint from your routes module. A blueprint is a way to organize a group of related routes and other code.

# app.register_blueprint(main)
# # This line registers the blueprint with the Flask application.
# # Now the routes defined in the blueprint will be part of the application.

# if __name__ == "__main__":
#     app.run(debug=True)
# # If this script is run directly (not imported), start the Flask development server.


