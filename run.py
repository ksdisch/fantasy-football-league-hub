# This imports the Flask instance, app, that we created in the __init__.py file.
from gov_bowl_app import app

# Again, if this script is run directly, start the Flask development server.
if __name__ == "__main__":
    app.run(debug=True)
