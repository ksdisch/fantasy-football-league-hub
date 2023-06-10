# import sys
# import os
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

# from gov_bowl_app import create_app, db
# from gov_bowl_app.models.owner_stat_models import Owner, OwnerStatTotal
# from gov_bowl_app.db_queries.owners_table import get_owner_name

# app = create_app()

# with app.app_context():

#     column_names = [column.name for column in OwnerStatTotal.__table__.columns]
#     owner_all_time_stats = {}
#     for column in column_names [2:]:
#         owner_all_time_stats[column] = {}
#     # Query all owners
#     all_time_stats = OwnerStatTotal.query.all()
#     for row in all_time_stats:
#         owner_name = get_owner_name(row.owner_id)

#         for column in column_names[2:]:
#             owner_all_time_stats[column][owner_name] = getattr(row, column)

# owner_all_time_stats = {
#     # your data here
# }

# for stat, owners in owner_all_time_stats.items():
#     sorted_stats = sorted(owners.items(), key=lambda x: x[1], reverse=True)
#     print(f"\nRankings for {stat}:")
#     for rank, (owner, score) in enumerate(sorted_stats, start=1):
#         print(f"Rank {rank}: {owner} with score {score}")


import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from gov_bowl_app import create_app, db
from gov_bowl_app.models.owner_stat_models import Owner, OwnerStatTotal
from gov_bowl_app.db_queries.owners_table import get_owner_name

app = create_app()

with app.app_context():

    column_names = [column.name for column in OwnerStatTotal.__table__.columns]
    owner_all_time_stats = {}
    for column in column_names [1:]:
        owner_all_time_stats[column] = {}
    # Query all owners
    all_time_stats = OwnerStatTotal.query.all()
    for row in all_time_stats:
        owner_name = get_owner_name(row.owner_id)

        for column in column_names[1:]:
            owner_all_time_stats[column][owner_name] = getattr(row, column)

items_list = list(owner_all_time_stats.items())
# Dictionary of owner names as keys and values
owner_id_numbers = items_list[0]
print(f"First item: {owner_id_numbers}")

for stat, owners in items_list[1:]:
    sorted_stats = sorted(owners.items(), key=lambda x: x[1], reverse=True)
    print(f"\nRankings for {stat}:")
    for rank, (owner, score) in enumerate(sorted_stats, start=1):
        print(f"Rank {rank}: {owner} with score {score}")


# app = create_app()

# with app.app_context():

#     column_names = [column.name for column in OwnerStatTotal.__table__.columns]
#     owner_all_time_stats = {}
#     for column in column_names [1:]:
#         owner_all_time_stats[column] = {}
#     # Query all owners
#     all_time_stats = OwnerStatTotal.query.all()
#     for row in all_time_stats:
#         owner_name = get_owner_name(row.owner_id)

#         for column in column_names[1:]:
#             owner_all_time_stats[column][owner_name] = getattr(row, column)

# items_list = list(owner_all_time_stats.items())
# owner_id = 
# for stat, owners in items_list[1:]:
#     sorted_stats = sorted(owners.items(), key=lambda x: x[1], reverse=True)
#     print(f"\nRankings for {stat}:")
#     for rank, (owner, score) in enumerate(sorted_stats, start=1):
#         print(f"Rank {rank}: {owner} with score {score}")
