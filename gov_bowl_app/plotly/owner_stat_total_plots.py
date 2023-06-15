import plotly.express as px
import plotly
from gov_bowl_app import db
from gov_bowl_app.models.owner_stat_models import OwnerT, OwnerStatTotalT

import plotly.graph_objects as go
import json

def create_wins_fig_json():
    # Suppose we have some data
    owners = db.session.query(OwnerT).all()
    stats = db.session.query(OwnerStatTotalT).all()
    names = [owner.name for owner in owners]
    wins = [stat.total_wins for stat in stats]

    # Create a bar graph
    fig = go.Figure(data=go.Bar(x=names, y=wins))

    # Convert the figure to JSON
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    
    return fig_json

# All-time total points for by governor chart
def create_total_points_for_fig_json():
    # Suppose we have some data
    owners = db.session.query(OwnerT).all()
    stats = db.session.query(OwnerStatTotalT).all()
    names = [owner.name for owner in owners]
    points_for = [stat.total_points_for for stat in stats]

    # Create a bar graph
    fig = go.Figure(data=go.Bar(x=names, y=points_for))

    # Convert the figure to JSON
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    
    return fig_json

# All-time total points for by governor chart
def create_total_points_against_fig_json():
    # Suppose we have some data
    owners = db.session.query(OwnerT).all()
    stats = db.session.query(OwnerStatTotalT).all()
    names = [owner.name for owner in owners]
    points_against = [stat.total_points_against for stat in stats]

    # Create a bar graph
    fig = go.Figure(data=go.Bar(x=names, y=points_against))

    # Convert the figure to JSON
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    
    return fig_json