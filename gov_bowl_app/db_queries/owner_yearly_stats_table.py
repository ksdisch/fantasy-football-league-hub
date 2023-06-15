import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from gov_bowl_app import db
from gov_bowl_app.models.owner_stat_models import OwnerT, OwnerStatTotalT, OwnerYearlyStatsT
from gov_bowl_app.db_queries.owners_table import fetch_owner_id


# def fetch_yearly_stats(owner):
#     owner_yearly_stats = {}
#     owner_id_ = fetch_owner_id(owner)
#     owner_rows = db.session.query(OwnerYearlyStatsT).filter(OwnerYearlyStatsT.owner_id == owner_id_).all()
#     for row in owner_rows:
#         owner_yearly_stats[row.year] = {
#             'wins': row.wins,
#             'losses': row.losses,
#             'ties': row.ties,
#             'points_for': row.points_for,
#             'points_against': row.points_against,
#             'acquisitions': row.acquisitions,
#             'budget_spent': row.budget_spent,
#             'trades': row.trades,
#             'playoff_seed': row.playoff_seed,
#             'final_rank': row.final_rank
#         }

#     return owner_yearly_stats