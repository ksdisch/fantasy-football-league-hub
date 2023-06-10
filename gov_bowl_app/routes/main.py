import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

import pandas as pd
import json
import plotly
from gov_bowl_app import create_app
from gov_bowl_app.plotly.owner_stat_total_plots import create_wins_fig_json, create_total_points_for_fig_json, create_total_points_against_fig_json
from gov_bowl_app.plotly.weekly_result_plots import create_weekly_owner_pf_fig_json

from gov_bowl_app.db_queries.owners_table import get_owners_list, get_owner_id
from gov_bowl_app.db_queries.owner_totals_table import fetch_owner_totals, fetch_all_totals
from gov_bowl_app.db_queries.owner_yearly_stats_table import fetch_yearly_stats
from gov_bowl_app.db_queries.owner_stat_ranks_table import fetch_owner_stat_ranks
import plotly.express as px
from flask import redirect, url_for
import os
import pprint



# Importing Blueprint for grouping routes, and render_template to generate HTML from templates.
from flask import Blueprint, render_template

# This creates a new blueprint. We will add routes to this blueprint.
main = Blueprint('main', __name__)


# This decorator tells Flask what URL should trigger the function underneath it.
@main.route('/')
# This function will be run when the user visits the URL '/'
# render_template generates HTML from the given template file.
def home():
    wins_fig_json = create_wins_fig_json()
    total_points_for_json = create_total_points_for_fig_json()
    total_points_against_json = create_total_points_against_fig_json()
    kyle_weekly_scores_json = create_weekly_owner_pf_fig_json(owner_id_arg=8, year=2017)
    owner_stat_totals = fetch_all_totals()
    owner_stat_ranks = fetch_owner_stat_ranks()
    # print(owner_stat_totals)
    # print('\n\n')
    # print(owner_stat_ranks)
    # dict_for_table = owner_stat_totals
    # for owner_id, totals_dict in dict_for_table.items():
    #     # print(key)
    #     # print()
    #     # print(value)
    #     for label, total in totals_dict.items():
    #         for key, value in owner_stat_ranks.items():
    #             stat_label = key
    #             owner_ids_and_ranks = value
    #             for id, owner_rank in owner_ids_and_ranks.items():
    #                 print(id)
    #                 print(owner_rank)
    #                 dict_for_table[id][label] = f'{total}({owner_rank})'
    #                 # dict_for_table[id][f'{stat_label}_rank'] = owner_rank


    # pprint.pprint(dict_for_table)

    # for key, value in dict_for_table.items():
    #     print(key)
    #     print(value)
    #     print()
    owners_list = get_owners_list()
    

    return render_template('index.html', 
                           wins_chart=wins_fig_json, 
                           total_points_for_chart=total_points_for_json, 
                           total_points_against_chart=total_points_against_json, 
                           weekly_pf_chart=kyle_weekly_scores_json,
                           owners=owners_list,
                           owner_stat_totals=owner_stat_totals,
                           owner_stat_ranks=owner_stat_ranks,
                           )

# This route is used when no year is specified.
@main.route('/owner/<owner>')
def owner_page_default(owner):
    default_year = 2022  # Set your default year here
    clean_owner = owner.title().replace("  ", " ")
    return redirect(url_for('main.owner_page', owner=owner, owner_name_clean=clean_owner, year=default_year))
  
# This route is used when a year is specified.
@main.route('/owner/<owner>/<int:year>')
def owner_page(owner, year):
    owner_id = get_owner_id(owner=owner)
    clean_owner = owner.title().replace("  ", " ")
    owner_weekly_pf_json = create_weekly_owner_pf_fig_json(owner_id_arg=owner_id, year=year)
    years = range(2016, 2023)  # replace with the range of years you want to include
    owner_stat_totals = fetch_owner_totals(owner)
    owner_yearly_stats = fetch_yearly_stats(owner)
    return render_template('owner.html', owner_name=owner, owner_name_clean=clean_owner, owner_weekly_pf_chart=owner_weekly_pf_json, years=years, stat_totals=owner_stat_totals, yearly_stats=owner_yearly_stats)

