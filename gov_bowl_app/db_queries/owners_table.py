import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from gov_bowl_app import create_app, db
from gov_bowl_app.models.owner_stat_models import Owner, OwnerStatTotal


def get_owners_list():
    app = create_app()

    with app.app_context():
        # Query all owners
        owners = db.session.query(Owner).all()
        owners_list = [owner.name for owner in owners]

    return(owners_list)

def get_owner_id(owner):
    owner_id = db.session.query(Owner).filter(Owner.name == owner).first().id
    return(owner_id)

def get_owner_name(owner_ident):
    owner_name = db.session.query(Owner).filter(Owner.id == owner_ident).first().name
    return(owner_name)