import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from gov_bowl_app import db  # We're importing the SQLAlchemy instance that we created in __init__.py
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship, backref

# We're defining a new class 'Owner' that inherits from db.Model
# Each class that inherits from db.Model corresponds to a table in the database.
class Owner(db.Model):
    __tablename__ = 'owners'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    weekly_matchups = relationship('Matchup', backref='owner')
    stattotals = relationship('OwnerStatTotal', backref='owner')
    yearly_stats = relationship('OwnerYearlyStats', backref='owner')
    all_time_ranks = relationship('AllTimeStatRank', backref='owner')


class OwnerStatTotal(db.Model):
    __tablename__ = 'owner_all_time_totals'
    id = Column(Integer, primary_key=True)
    owner_id = Column(Integer, ForeignKey('owners.id'), nullable=False)
    total_wins = Column(Integer)
    avg_wins = Column(Float)
    total_losses = Column(Integer)
    avg_losses = Column(Float)
    ties = Column(Integer)
    total_points_for = Column(Float)
    yearly_avg_points_for = Column(Float)
    weekly_avg_points_for = Column(Float)
    total_points_against = Column(Float)
    yearly_avg_points_against = Column(Float)
    weekly_avg_points_against = Column(Float)
    total_acquisitions = Column(Integer)
    budget_spent = Column(Integer)
    total_trades = Column(Integer)
    average_playoff_seed = Column(Float)
    average_final_rank = Column(Float)

class Matchup(db.Model):
    __tablename__ = 'weekly_matchups'
    id = Column(db.Integer, primary_key=True, autoincrement=True)
    owner_id = Column(Integer, ForeignKey('owners.id'), nullable=False)
    year = Column(Integer, nullable=False)
    week = Column(Integer, nullable=False)
    score = Column(Float, nullable=False)
    opponent = Column(String, nullable=False)
    opponent_score = Column(Float, nullable=False)
    result = Column(String, nullable=False)

class TempMatchup(db.Model):
    __tablename__ = 'temp_weekly_matchups'
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('owners.id'), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    week = db.Column(db.Integer, nullable=False)
    score = db.Column(db.Float, nullable=False)
    opponent = db.Column(db.String, nullable=False)
    opponent_score = db.Column(db.Float, nullable=False)
    result = db.Column(db.String, nullable=False)


class OwnerYearlyStats(db.Model):
    __tablename__ = 'yearly_stats'
    id = Column(Integer, primary_key=True, autoincrement=True)
    owner_id = Column(Integer, ForeignKey('owners.id'), nullable=False)
    year = Column(Integer, nullable=False)
    wins = Column(Integer)
    losses = Column(Integer)
    ties = Column(Integer)
    points_for = Column(Float)
    points_against = Column(Float)
    acquisitions = Column(Integer)
    budget_spent = Column(Integer)
    trades = Column(Integer)
    playoff_seed = Column(Integer)
    final_rank = Column(Integer)

class AllTimeStatRank(db.Model):
    __tablename__ = 'all_time_stat_ranks'
    id = Column(Integer, primary_key=True)
    owner_id = Column(Integer, ForeignKey('owners.id'), nullable=False)
    owner_name = Column(String)
    stat_name = Column(String)
    rank = Column(Integer)




