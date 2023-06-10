import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from gov_bowl_app import create_app, db
from gov_bowl_app.models.owner_stat_models import Owner, OwnerStatTotal, Matchup


# def get_owner_weekly_results(owner):
#     owner_id = db.session.query(Owner).filter(Owner.name == owner).first().id
#     owner_weekly_results = db.session.query(Matchup).filter(Matchup.owner_id == owner_id).all()
#     # with app.app_context():
#     #     # Query all owners
#     #     owners = db.session.query(Owner).all()
#     #     owners_list = [owner.name for owner in owners]

#     return(owner_weekly_results)
