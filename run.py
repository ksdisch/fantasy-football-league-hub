# This imports the Flask instance, app, that we created in the __init__.py file.
from gov_bowl_app import app
# run.py
from gov_bowl_app import create_app, db
# from gov_bowl_app.models.new_owner_stat_models import OwnerT

app = create_app()

@app.before_first_request
def create_tables():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)

# Again, if this script is run directly, start the Flask development server.
if __name__ == "__main__":
    app.run(debug=True)
