import plotly.express as px
import plotly
from gov_bowl_app import db
from gov_bowl_app.models.owner_stat_models import Owner, OwnerStatTotal
from gov_bowl_app.db_queries.owners_table import get_owner_id

full_column_names = [column.key for column in OwnerStatTotal.__table__.columns]
data_column_names = full_column_names[2:]

def fetch_all_totals():
    owners = db.session.query(Owner).all()
    all_time_stats_dict = {}
    for row in owners:
        owner_name = row.name.title().replace("  ", " ")
        all_time_stats_dict[row.id] = {'owner_name': owner_name}
    stats = db.session.query(OwnerStatTotal).all()
    stat_labels = [column.key for column in OwnerStatTotal.__table__.columns if column.key != 'id' and column.key != 'owner_id']
    for row in stats:
        for label in stat_labels:
            all_time_stats_dict[row.owner_id][label] = getattr(row, label)

    return(all_time_stats_dict)

def fetch_owner_totals(owner):
    owner_id_ = get_owner_id(owner)
    owner_row = db.session.query(OwnerStatTotal).filter(OwnerStatTotal.owner_id == owner_id_).first()
    owner_stats = [getattr(owner_row, column_name) for column_name in data_column_names]

    return owner_stats