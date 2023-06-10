import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from gov_bowl_app import create_app, db
from gov_bowl_app.models.owner_stat_models import Owner, OwnerStatTotal, AllTimeStatRank
from gov_bowl_app.db_queries.owners_table import get_owners_list, get_owner_name

def fetch_owner_stat_ranks():
    owner_ranks_rows = db.session.query(AllTimeStatRank).all()
    stat_labels = [column.name for column in OwnerStatTotal.__table__.columns]
    owners = get_owners_list
    owner_stat_ranks_dict = {}
    for i in range(13):
        try:
            owner_name = get_owner_name(i).title().replace("  ", " ")
            owner_stat_ranks_dict[i] = {'owner_name': owner_name}
        except AttributeError:
            print('error in fetch_owner_stat_ranks(), continuing...')
            

    for row in owner_ranks_rows:
        owner_stat_ranks_dict[row.owner_id][row.stat_name] = row.rank



    return(owner_stat_ranks_dict)   
    


# Structure it 