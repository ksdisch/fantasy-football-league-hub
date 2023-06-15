import plotly.express as px
import plotly
from gov_bowl_app import db
from gov_bowl_app.models.owner_stat_models import OwnerT, OwnerStatTotalT, MatchupT

import plotly.graph_objects as go
import json

# Points for chart for one owner for a given year
def create_weekly_owner_pf_fig_json(owner_id_arg, year):
    owner = db.session.query(OwnerT).filter(OwnerT.owner_id == owner_id_arg).first().name
    owner_rows = db.session.query(MatchupT).filter(MatchupT.owner_id == owner_id_arg, MatchupT.year == year).all()
    weeks = [row.week for row in owner_rows]
    weekly_scores = [row.score for row in owner_rows]
    opp_weekly_scores = [row.opponent_score for row in owner_rows]
    weekly_opps = [row.opponent for row in owner_rows]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=weeks, y=weekly_scores, mode='lines', name='Points'))
    fig.add_trace(go.Scatter(x=weeks, y=opp_weekly_scores, mode='lines', name='Opponent Points'))

    fig.update_layout(title=f"{owner}'s Weekly Scores - {year}")

    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return fig_json