# Import the necessary libraries and functions
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))


# Create plot functions
from gov_bowl_app.plotly.owner_stat_total_plots import create_wins_fig_json, create_total_points_for_fig_json, create_total_points_against_fig_json
from gov_bowl_app.plotly.weekly_result_plots import create_weekly_owner_pf_fig_json

# Database queries ("fetch data functions")
from gov_bowl_app.db_queries.owners_table import fetch_owners_list, fetch_owner_id
from gov_bowl_app.db_queries.owner_totals_table import fetch_season_recap_data, calc_all_totals, fetch_reg_seas_stat_totals_and_ranks, fetch_yearly_totals

from flask import redirect, url_for
import os
import pprint



# Importing Blueprint for grouping routes, and render_template to generate HTML from templates.
from flask import Blueprint, render_template

# This creates a new blueprint. We will add routes to this blueprint.
main = Blueprint('main', __name__)


@main.route('/season_recap/<int:year>')
def season_recap(year):

    seas_recap_data, seas_recap_labels, superlatives_dict = fetch_season_recap_data(year)

    first_dict_key, first_dict_values = next(iter(seas_recap_data.items()))
    seas_recap_labels = first_dict_values.keys()

    return render_template(
        'season_recaps.html',
        year=year,
        seas_recap_data=seas_recap_data,
        seas_recap_labels=seas_recap_labels,
        superlatives_dict=superlatives_dict
        )






# This decorator tells Flask what URL should trigger the function underneath it.
@main.route('/')
def home():
    years = range(2016, 2023)
    wins_fig_json = create_wins_fig_json()
    total_points_for_json = create_total_points_for_fig_json()
    total_points_against_json = create_total_points_against_fig_json()
    kyle_weekly_scores_json = create_weekly_owner_pf_fig_json(owner_id_arg=8, year=2017)


    owner_stats_w_ranks, alltime_stat_labels = fetch_reg_seas_stat_totals_and_ranks(calc_all_totals())
 
    owners_list = fetch_owners_list()
    fetch_yearly_totals(2016, 2022)
    

    return render_template('index.html', 
                           wins_chart=wins_fig_json, 
                           alltime_stat_labels=alltime_stat_labels,
                           years=years,
                           total_points_for_chart=total_points_for_json, 
                           total_points_against_chart=total_points_against_json, 
                           weekly_pf_chart=kyle_weekly_scores_json,
                           owners=owners_list,
                           owner_stats_w_ranks=owner_stats_w_ranks,
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
    year = int(year)

    owner_stats_w_ranks, alltime_stat_labels = fetch_reg_seas_stat_totals_and_ranks(calc_all_totals())

    owner_alltime_totals = owner_stats_w_ranks[owner] # DONE WORKING WELL
    del owner_alltime_totals['owner_name']
    del owner_alltime_totals['team_name']




    all_yearly_stats, stat_labels = fetch_yearly_totals(2016, 2022) # ******
    if owner in all_yearly_stats:
        owner_yearly_stats = all_yearly_stats[owner]


    owner_id = fetch_owner_id(owner=owner)
    clean_owner = owner.title().replace("  ", " ")


    return render_template('owner.html', 
                           owner_name=owner, 
                           stat_labels=stat_labels,
                           owner_name_clean=clean_owner,
                        #    owner_weekly_pf_chart=owner_weekly_pf_json,
                           owner_yearly_stats=owner_yearly_stats,
                           years=range(2016, 2023), 
                        #    owner_yearly_stats=owner_yearly_stats,
                           owner_alltime_totals=owner_alltime_totals,
                           alltime_stat_labels=alltime_stat_labels

                        )
