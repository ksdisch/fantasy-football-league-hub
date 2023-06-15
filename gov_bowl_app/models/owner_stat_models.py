# Import necessary modules
import sys
import os

# We need to insert our app's path to sys path for python to find the modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from gov_bowl_app import db  # We're importing the SQLAlchemy instance that we created in __init__.py
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship, backref

# Table - Fantasy players on rosters 
class PlayerT(db.Model):
    __tablename__ = 'players_t'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    position = db.Column(db.String)
    team_name = db.Column(db.String)
    

# Table - Basically a yearly stats table. The team name applies for the whole year.
class OwnerYearlyStatsT(db.Model):
    __tablename__ = 'owner_yearly_stats_t'
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.String, db.ForeignKey('owners_t.owner_id'))  # foreign key to Owner table
    team_name = db.Column(db.String)
    year = db.Column(db.Integer)
    team_abbrev = db.Column(db.String)
    wins = db.Column(db.Integer)
    losses = db.Column(db.Integer)
    # ties = db.Column(db.Integer)
    points_for = db.Column(db.Float)
    points_against = db.Column(db.Float)
    acquisitions = db.Column(db.Integer)
    budget_spent = db.Column(db.Integer)
    trades = db.Column(db.Integer)
    playoff_seed = db.Column(db.Integer)
    final_rank = db.Column(db.Integer)
    projected_rank = db.Column(db.Integer)

class OwnerT(db.Model):
    __tablename__ = 'owners_t'
    owner_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    teams = db.relationship('OwnerYearlyStatsT', backref='ownert', lazy=True)  # relationship to Team table
    # other fields...



    # other fields like wins, losses, points for, points against etc.




class MatchupT(db.Model):
    __tablename__ = 'weekly_matchups_t'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    owner_id = db.Column(db.String, db.ForeignKey('owners_t.owner_id'), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    week = db.Column(db.Integer, nullable=False)
    score = db.Column(db.Float, nullable=False)
    opponent = db.Column(db.String, nullable=False)
    opponent_score = db.Column(db.Float, nullable=False)
    result = db.Column(db.String, nullable=False)
    result_margin = db.Column(db.Float, nullable=False)


# ------------------------------ New above this ------------------------------ # 


class OwnerStatTotalT(db.Model):
    __tablename__ = 'owner_all_time_totals_t'
    id = Column(Integer, primary_key=True)
    owner_id = Column(db.String, ForeignKey('owners_t.owner_id'), nullable=False)
    total_wins = Column(Integer)
    total_losses = Column(Integer)
    ties = Column(Integer)
    total_points_for = Column(Float)
    weekly_avg_points_for = Column(Float)
    total_points_against = Column(Float)
    weekly_avg_points_against = Column(Float)
    total_acquisitions = Column(Integer)
    budget_spent = Column(Integer)
    total_trades = Column(Integer)
    average_playoff_seed = Column(Float)
    average_final_rank = Column(Float)

class AllTimeStatRankT(db.Model):
    __tablename__ = 'all_time_stat_rank_t'
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.String, db.ForeignKey('owners_t.owner_id'), nullable=False)
    owner_name = Column(String)
    stat_name = Column(String)
    rank = Column(Integer)