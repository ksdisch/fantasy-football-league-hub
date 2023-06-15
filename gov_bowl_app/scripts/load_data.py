import json
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))


import json
from gov_bowl_app import app, db
from gov_bowl_app.models.owner_stat_models import OwnerT


# def load_owners(file_path):
#     with open(file_path) as f:
#         data = json.load(f)
#     with app.app_context():
#         db.create_all()
#         for year, owners in data.items():
#             for owner_name, owner_data in owners.items():
#                 owner_formatted = owner_name.title().replace("  ", " ")
#                 owner = OwnerT.query.filter_by(name=owner_formatted).first()
#                 if not owner:
#                     owner = OwnerT(name=owner_formatted)
#                     db.session.add(owner)
                
#         db.session.commit()

# load_owners('/Users/kyledisch/Desktop/fantasy-football-league-hub/data_processing/new_league_data.json')  # Replace with the actual path to your JSON file








import json
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from gov_bowl_app import app, db
from gov_bowl_app.models.owner_stat_models import OwnerT, OwnerYearlyStatsT, PlayerT, MatchupT

def load_data(file_path):
    with open(file_path) as f:
        data = json.load(f)

    with app.app_context():
        db.drop_all()
        db.create_all()

        for year, owners in data.items():
            for owner_name, owner_data in owners.items():
                new_owner_name = owner_name.title().replace("  ", " ")
                owner = OwnerT.query.filter_by(name=new_owner_name).first()
                if not owner:
                    owner = OwnerT(name=new_owner_name)
                    db.session.add(owner)

                # Load data into TeamT table
                team_name = owner_data['team_name']
                team = OwnerYearlyStatsT.query.filter_by(team_name=team_name).first()
                if not team:
                    team = OwnerYearlyStatsT(owner_id=owner.owner_id, team_name=owner_data['team_name'], year=year, team_abbrev=owner_data['team_abbrev'], wins=owner_data['wins'], losses=owner_data['losses'], points_for=owner_data['points_for'], points_against=owner_data['points_against'], acquisitions=owner_data['season_acquisitions'], budget_spent=owner_data['season_budget_spent'], trades=owner_data['season_trades'], playoff_seed=owner_data['playoff_seed'], final_rank=owner_data['final_rank'], projected_rank=owner_data['projected_rank'], )
                    db.session.add(team)
                
                else: # Doing this for checking purposes, not best practice
                    team = OwnerYearlyStatsT(owner_id=owner.owner_id, team_name=owner_data['team_name'], year=year, team_abbrev=owner_data['team_abbrev'], wins=owner_data['wins'], losses=owner_data['losses'], points_for=owner_data['points_for'], points_against=owner_data['points_against'], acquisitions=owner_data['season_acquisitions'], budget_spent=owner_data['season_budget_spent'], trades=owner_data['season_trades'], playoff_seed=owner_data['playoff_seed'], final_rank=owner_data['final_rank'], projected_rank=owner_data['projected_rank'], )
                    db.session.add(team)

                # Load data into PlayerT table
                for player_data in owner_data['schedule']:
                    player_name = player_data['name']
                    position = player_data['position']
                    print(position)
                    player = PlayerT.query.filter_by(name=player_name, team_name=owner_data['team_name']).first()
                    if not player:
                        player = PlayerT(name=player_name, position=player_data['position'], team_name=team_name)
                        db.session.add(player)

                # Load data into MatchupT table
                for week_number, week_data in owner_data.items():
                    if type(week_data) is dict:
                        matchup = MatchupT(owner_id=owner.owner_id, year=int(year), week=week_number, score=week_data['score'],
                                        opponent=week_data['opponent'], opponent_score=week_data['opponent_score'], 
                                        result=week_data['result'], result_margin=week_data['mov'])
                        db.session.add(matchup)

        db.session.commit()

load_data('/Users/kyledisch/Desktop/fantasy-football-league-hub/data_processing/reg_seas_data.json')  # Replace with the actual path to your JSON file
