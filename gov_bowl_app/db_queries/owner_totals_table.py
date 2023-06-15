import plotly.express as px
import plotly
import pandas as pd
from gov_bowl_app import db
from sqlalchemy import func
from gov_bowl_app.models.owner_stat_models import OwnerT, OwnerStatTotalT, OwnerYearlyStatsT
from gov_bowl_app.db_queries.owners_table import fetch_owner_id, get_owner_name, fetch_owners_list
from sqlalchemy import and_

import pprint

full_column_names = [column.key for column in OwnerYearlyStatsT.__table__.columns]
data_column_names = full_column_names[2:]

non_number_labels = ['id', 'owner_id', 'year', 'team_abbrev']
weekly_stats_to_avg = ['Pts/Wk', 'Opp Pts/Wk']
yearly_stats_to_avg = ['average_playoff_seed', 'average_final_rank']





def fetch_season_recap_data(year):
    superlatives_dict = {} # champ, sacko, scoring_champ, scoring_potato, most_trades, most_acquisitions, etc...
    seas_recap_stat_labels = [column.key for column in OwnerYearlyStatsT.__table__.columns if column.key not in non_number_labels]
    owner_ids = [fetch_owner_id(owner_name) for owner_name in fetch_owners_list()]
    
    seas_recap_dict = {}

    # Query owner_yearly_stats_t table filtering by year
    yearly_stat_rows = db.session.query(OwnerYearlyStatsT).filter(OwnerYearlyStatsT.year == year).all()




    for row in yearly_stat_rows:
        for id in owner_ids:
            # print(id)
            # owner_name =
            seas_recap_dict[id] = {'governor': get_owner_name(id)}
        for label in seas_recap_stat_labels:
            seas_recap_dict[id][label] = getattr(row, label)



    for id in owner_ids:
        seas_recap_dict[id] = {'governor': get_owner_name(id)}

        owner_row = db.session.query(OwnerYearlyStatsT).filter(and_(OwnerYearlyStatsT.owner_id == id, OwnerYearlyStatsT.year == year)).first()
        if owner_row:
            for label in seas_recap_stat_labels:
                seas_recap_dict[id][label] = getattr(owner_row, label)
            if getattr(owner_row, 'final_rank') == 1:

                superlatives_dict['champ'] = {
                    'owner': get_owner_name(id),
                    'team_name': getattr(owner_row, 'team_name'),
                    'reg_seas_record': f"({getattr(owner_row, 'wins')}-{getattr(owner_row, 'losses')})"
                    }
                
            elif getattr(owner_row, 'final_rank') == 12:
                superlatives_dict['sacko'] = {
                    'owner': get_owner_name(id),
                    'team_name': getattr(owner_row, 'team_name'),
                    'reg_seas_record': f"({getattr(owner_row, 'wins')}-{getattr(owner_row, 'losses')})"
                    }

    pprint.pprint(superlatives_dict, sort_dicts=False)
    return (seas_recap_dict, seas_recap_stat_labels, superlatives_dict)











def calc_all_totals():
    # Get a list of owners
    owners_query = db.session.query(OwnerT).all()
    reg_seas_stats_dict = {}
    # Loop through each owner
    for owner in owners_query:
        # Get owner_id
        owner_id = owner.owner_id
        owner_name = get_owner_name(owner_id)
        # Make dictionary for owner in reg_seas_stats_dict
        reg_seas_stats_dict[owner_name] = {'owner_name': owner_name}
        stat_labels = [column.key for column in OwnerYearlyStatsT.__table__.columns if column.key not in non_number_labels]

        stat_labels.insert(3, 'Pts/Wk')
        stat_labels.insert(5, 'Opp Pts/Wk')
        for label in stat_labels:
            reg_seas_stats_dict[owner_name][label] = ''

        for label in stat_labels:
            if label not in weekly_stats_to_avg and label not in yearly_stats_to_avg:
                result = db.session.query(func.sum(getattr(OwnerYearlyStatsT, label))).filter(OwnerYearlyStatsT.owner_id == owner_id).scalar()
                reg_seas_stats_dict[owner_name][label] = result
        
        reg_seas_stats_dict[owner_name]['Pts/Wk'] = (reg_seas_stats_dict[owner_name]['points_for']) / (reg_seas_stats_dict[owner_name]['wins'] + reg_seas_stats_dict[owner_name]['losses'])
        reg_seas_stats_dict[owner_name]['Opp Pts/Wk'] = (reg_seas_stats_dict[owner_name]['points_against']) / (reg_seas_stats_dict[owner_name]['wins'] + reg_seas_stats_dict[owner_name]['losses'])

        years_of_league = 7 # Need to eventually change this to owner_years_in_league to ensure accuracy for those who have not had their own team the whole time the league has been in existence
        reg_seas_stats_dict[owner_name]['playoff_seed'] = (reg_seas_stats_dict[owner_name]['playoff_seed']) / (years_of_league)
        reg_seas_stats_dict[owner_name]['final_rank'] = (reg_seas_stats_dict[owner_name]['final_rank']) / (years_of_league)
        reg_seas_stats_dict[owner_name]['projected_rank'] = (reg_seas_stats_dict[owner_name]['projected_rank']) / (years_of_league)


            

        stat_labels.insert(0, 'governor')

    return(reg_seas_stats_dict)


def fetch_reg_seas_stat_totals_and_ranks(stat_totals_dict):
    stat_labels = [column.key for column in OwnerYearlyStatsT.__table__.columns if column.key not in non_number_labels]

    stat_labels.insert(3, 'Pts/Wk')
    stat_labels.insert(5, 'Opp Pts/Wk')
    stat_labels.insert(0, 'Governor')


    stats_ranks_dict = {}

    for owner in fetch_owners_list():
        stats_ranks_dict[owner] = {'owner_name': owner}

    totals_df = pd.DataFrame.from_dict(stat_totals_dict, orient='index')
    totals_df = totals_df.round(2)
    ascending_columns = ['final_rank', 'playoff_seed', 'projected_rank']
    # Loop through each column
    for col in totals_df.columns[1:]:
        rank = 1
        if col in ascending_columns:
            col_series = totals_df[col]
            col_sorted = col_series.sort_values()
            # print("\nSorted column:")
            # print(col_sorted)
            owner_names = col_sorted.index
            # print("\nIndex values after sorting:")
            # print(owner_names)
            for owner_name in owner_names:
                stat_val_w_rank = f'{col_sorted[owner_name]} ({rank})'
                stats_ranks_dict[owner_name][col] = stat_val_w_rank
                rank += 1


        else:
            col_series = totals_df[col]
            col_sorted = col_series.sort_values(ascending=False)

            # print("\nSorted column:")
            # print(col_sorted)
            owner_names = col_sorted.index
            # print("\nIndex values after sorting:")
            # print(owner_names)
            for owner_name in owner_names:
                stat_val_w_rank = f'{col_sorted[owner_name]} ({rank})'
                stats_ranks_dict[owner_name][col] = stat_val_w_rank
                rank += 1

    for owner, owner_data in stats_ranks_dict.items():
        del owner_data['team_name']
    stat_labels.remove('team_name')

    return(stats_ranks_dict, stat_labels)


def fetch_yearly_totals(start_year, end_year):
    owners_query = db.session.query(OwnerT).all()
    yearly_totals_dict = {}
    stat_labels = [column.key for column in OwnerYearlyStatsT.__table__.columns if column.key not in non_number_labels]

    for owner in owners_query:
        # Get owner_id
        owner_id = owner.owner_id
        owner_name = get_owner_name(owner_id)
        # Make dictionary for owner in reg_seas_stats_dict
        yearly_totals_dict[owner_name] = {}
        for year in range(start_year, end_year + 1):
            yearly_totals_dict[owner_name][year] = {}

            result_rows = db.session.query(OwnerYearlyStatsT).filter(and_(OwnerYearlyStatsT.owner_id == owner_id, OwnerYearlyStatsT.year == year)).all()
            for row in result_rows:
                if row:
                    for label in stat_labels:
                        yearly_totals_dict[owner_name][year][label] = getattr(row, label)


    return(yearly_totals_dict, stat_labels)










