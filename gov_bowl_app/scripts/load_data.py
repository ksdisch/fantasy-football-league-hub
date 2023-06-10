import os
import sys
import json
from sqlalchemy import create_engine

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))


# We're importing the SQLAlchemy instance that we created in __init__.py
from gov_bowl_app import db, create_app
from gov_bowl_app.models.owner_stat_models import Owner, OwnerStatTotal, Matchup, OwnerYearlyStats, TempMatchup
from gov_bowl_app.db_queries.owners_table import get_owner_id
from gov_bowl_app import db, create_app
from sqlalchemy import exc



# app = create_app()
# with app.app_context():
#     new_owner = Owner(
#         name = 'brantley lohkamp'
#     )

#     db.session.add(new_owner)
#     db.session.commit()

# app = create_app()
# def load_new_yearly_owner_data(path_to_json, year):
#     # load the json data
#     with open(path_to_json, 'r') as f:
#         data = json.load(f)

#     app = create_app()

#     with app.app_context():
#         # create the tables in the database if they don't exist
#         db.create_all()

#         # for each owner in the data
#         for owner_name, owner_data in data.items():
#             print(owner_data)
#             # fetch the owner from the database
#             owner = Owner.query.filter_by(name=owner_name).first()
#             print(owner)
#             # if the owner does not exist, skip this iteration
#             if not owner:
#                 continue

#             # try:
#             new_yearly_stats_entry = OwnerYearlyStats(
#                 owner_id = owner.id,
#                 year = year,
#                 wins = owner_data['season_wins'],
#                 losses = owner_data['season_losses'],
#                 ties = owner_data['season_ties'], 
#                 points_for = owner_data['season_pf'], 
#                 points_against = owner_data['season_pa'],
#                 acquisitions = owner_data['season_acquisitions'],
#                 budget_spent = owner_data['season_budget_spent'],
#                 trades = owner_data['trades']
#             )                
#             db.session.add(new_yearly_stats_entry)
#         db.session.commit()

# if __name__ == "__main__":
#     load_new_yearly_owner_data(path_to_json='/Users/kyledisch/Desktop/gov-bowl-app/gov_bowl_app/data/processed_new_yearly_data.json', year=2022)










def load_matchup_data(path_to_json):
    with open(path_to_json, 'r') as f:
        data = json.load(f)

    app = create_app()

    with app.app_context():
        # assuming 'TableName' is the class of the model you want to drop
        if 'weekly_matchups' in db.metadata.tables:  # replace 'table_name' with your actual table name
            try:
                Matchup.__table__.drop(db.engine)  # try to drop the table
            except exc.SQLAlchemyError:
                db.session.rollback()  # rollback if there is any error
        db.create_all()

        for owner_name, owner_data in data.items():
            print(f'Owner Name: {owner_name}')
            print(f'Owner Data: {owner_data}')
            owner = Owner.query.filter_by(name=owner_name).first()
            print(f'Owner: {owner}')
            if not owner:
                # consider creating a new owner here if it doesn't exist
                # new_owner = Owner(
                #     name = Owner
                # )
                continue

            for year, year_data in owner_data.items():
                if year_data:  # Changed this line
                    print(f'Year: {year}\n')
                    print(f'Year Data: {year_data}')
                    for week, week_data in year_data.items():
                        if week_data:  # Changed this line
                            print(f'Week: {week}')
                            print(f'Week Data: {week_data}')
                            new_matchup = Matchup(
                                owner_id=owner.id,
                                year=year,
                                week=week,
                                score=week_data['score'],
                                opponent=week_data['opponent'],
                                opponent_score=week_data['opponent_score'],
                                result=week_data['result']
                            )
                            db.session.add(new_matchup)
                else:
                    print(f'No data for {owner} for the year {year}')
        db.session.commit()


if __name__ == "__main__":
    load_matchup_data(path_to_json='/Users/kyledisch/Desktop/gov-bowl-app/data_processing/owner_weekly_stats_raw.json')

# NEW WEEKLY MATCHUP DATA FOR NEW YEAR
# def load_new_matchup_data(path_to_json):
#     # load the json data
#     with open(path_to_json, 'r') as f:
#         data = json.load(f)



#     app = create_app()

#     with app.app_context():
#         # create the tables in the database if they don't exist
#         db.create_all()
#         for owner, year_dictionary in data.items():
#             owner_id = get_owner_id(owner)
#             print(f'Owner: {owner}')
#             print(f'Owner ID: {owner_id}\n')
#             for year, next_dict in year_dictionary.items():
#                 print(f'Year: {year}')
#                 print(f'Dict: {next_dict}\n')
#                 for week, matchup_results_dict in next_dict.items():   
#                     new_matchup = Matchup(
#                         owner_id=owner_id,
#                         year=int(year),
#                         week=int(week),
#                         score=matchup_results_dict['score'],
#                         opponent=matchup_results_dict['opponent'],
#                         opponent_score=matchup_results_dict['opponent_score'],
#                         result=matchup_results_dict['result']
#                     )                     
#                     print(f'Week: {week}')
#                     print(f'Matchup Results: {matchup_results_dict}\n')

#                     db.session.add(new_matchup)

#         db.session.commit()

        # # for each owner in the data
        # for owner_name, owner_data in data.items():
        #     # fetch the owner from the database
        #     owner = Owner.query.filter_by(name=owner_name).first()
        #     # if the owner does not exist, skip this iteration
        #     if not owner:
        #         continue
            

        #     # for each year of matchup data for the owner
        #     for year, year_data in owner_data.items():
        #         # for each week of matchup data in the year
        #         for week, week_data in year_data.items():
        #             # necessary_keys = ['score', 'opponet', 'opponent_score', 'result']
        #             # if all(key in week_data for key in necessary_keys):
        #             if len(week_data) > 0:
        #                 # create a new matchup
        #                 new_matchup = Matchup(
        #                     owner_id=owner.id,
        #                     year=year,
        #                     week=week,
        #                     score=week_data['score'],
        #                     opponent=week_data['opponent'],
        #                     opponent_score=week_data['opponent_score'],
        #                     result=week_data['result']
        #                 )
        #                 db.session.add(new_matchup)
        #             # else:
        # db.session.commit()

# if __name__ == "__main__":
#     load_new_matchup_data(path_to_json='/Users/kyledisch/Desktop/gov-bowl-app/data_processing/new_owner_weekly_stats_raw.json')


# def load_new_matchup_data(path_to_json):
#     # load the json data
#     with open(path_to_json, 'r') as f:
#         data = json.load(f)

#     app = create_app()

#     with app.app_context():
#         # create the tables in the database if they don't exist
#         db.create_all()

#         try:
#             for owner, year_dictionary in data.items():
#                 owner_id = get_owner_id(owner)
#                 print(f'Owner: {owner}')
#                 print(f'Owner ID: {owner_id}\n')

#                 for year, next_dict in year_dictionary.items():
#                     print(f'Year: {year}')
#                     print(f'Dict: {next_dict}\n')

#                     for week, matchup_results_dict in next_dict.items():
#                         print(f'Week: {week}')
#                         print(f'Matchup Results: {matchup_results_dict}\n')   
#                         new_matchup = Matchup(
#                             owner_id=owner_id,
#                             year=int(year),
#                             week=int(week),
#                             score=matchup_results_dict['score'],
#                             opponent=matchup_results_dict['opponent'],
#                             opponent_score=matchup_results_dict['opponent_score'],
#                             result=matchup_results_dict['result']
#                         )                     

#                         db.session.add(new_matchup)

#             db.session.commit()

#         except Exception as e:
#             print(f"Error: {e}")
#             db.session.rollback()

# if __name__ == "__main__":
#     load_new_matchup_data(path_to_json='/Users/kyledisch/Desktop/gov-bowl-app/data_processing/new_owner_weekly_stats_raw.json')




# app = create_app()
# with app.app_context():
#     TempMatchup.__table__drop(db.engine)
#     db.create_all()
#     old_rows = db.session.query(Matchup).all()
#     for row in old_rows:
#         if row is not None:
#             new_row = TempMatchup(
#                 owner_id=row.owner_id,
#                 year=row.year,
#                 week=row.week,
#                 score=row.score,
#                 opponent=row.opponent,
#                 opponent_score=row.opponent_score,
#                 result=row.result
#             )
#             db.session.add(new_row)
#     db.session.commit()


# def load_yearly_owner_data(path_to_json):
#     # load the json data
#     with open(path_to_json, 'r') as f:
#         data = json.load(f)

#     app = create_app()

#     with app.app_context():
#         # create the tables in the database if they don't exist
#         db.create_all()

#         # for each owner in the data
#         for owner_name, owner_data in data.items():
#             print(owner_name)
#             print(owner_data)
#             # fetch the owner from the database
#             owner = Owner.query.filter_by(name=owner_name).first()
#             # if the owner does not exist, skip this iteration
#             if not owner:
#                 continue
            

#             # for each year of matchup data for the owner
#             for year, year_data in owner_data.items():
#                 print(year)
#                 print(year_data)
#                 try:
#                     new_yearly_stats_entry = OwnerYearlyStats(
#                         owner_id = owner.id,
#                         year = year,
#                         wins = year_data['wins'],
#                         losses = year_data['losses'],
#                         ties = year_data['ties'],
#                         points_for = year_data['points_for'],
#                         points_against = year_data['points_against'],
#                         acquisitions = year_data['acquisitions'],
#                         budget_spent = year_data['budget_spent'],
#                         trades = year_data['trades']
#                     )
#                     db.session.add(new_yearly_stats_entry)
#                 except KeyError:
#                     print("No data for this year... Continuing")
#         db.session.commit()

# if __name__ == "__main__":
#     load_yearly_owner_data(path_to_json='/Users/kyledisch/Desktop/gov-bowl-app/gov_bowl_app/data/processed_owner_yearly_stats.json')



# import sys
# import os
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

# from gov_bowl_app import create_app, db
# from gov_bowl_app.models.owner_stat_models import Owner, OwnerStatTotal, AllTimeStatRank
# from gov_bowl_app.db_queries.owners_table import get_owner_name, get_owner_id

# def load_rank_data():

#     app = create_app()

#     with app.app_context():
#         db.create_all()
#         column_names = [column.name for column in OwnerStatTotal.__table__.columns]
#         owner_all_time_stats = {}
#         for column in column_names [1:]:
#             owner_all_time_stats[column] = {}
#         # Query all owners
#         all_time_stats = OwnerStatTotal.query.all()
#         for row in all_time_stats:
#             owner_name = get_owner_name(row.owner_id)

#             for column in column_names[1:]:
#                 owner_all_time_stats[column][owner_name] = getattr(row, column)

#         items_list = list(owner_all_time_stats.items())
#         # Dictionary of owner names as keys and values
#         owner_id_numbers = items_list[0]
#         print(f"First item: {owner_id_numbers}")

#         for stat, owners in items_list[1:]:
#             sorted_stats = sorted(owners.items(), key=lambda x: x[1], reverse=True)
#             for rank, (owner, score) in enumerate(sorted_stats, start=1):
#                 print(f'Rank: {rank}')
#                 print(f'Owner: {owner}')
#                 print(f'Score: {score}')
#                 owner_id = get_owner_id(owner)
#                 rank_entry = AllTimeStatRank(owner_id=owner_id, owner_name=owner, stat_name=stat, rank=rank)
#                 db.session.add(rank_entry)
#         db.session.commit()


#     # for stat, owners in items_list[1:]:
#     #     sorted_stats = sorted(owners.items(), key=lambda x: x[1], reverse=True)
#     #     # print(f"\nRankings for {stat}:")
#     #     for rank, (owner, score) in enumerate(sorted_stats, start=1):
#     #         # print(f"Rank {rank}: {owner} with score {score}")



# if __name__ == "__main__":
#     load_rank_data()








