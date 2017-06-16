import os
from flask import Flask, jsonify
import sqlalchemy
import yaml

# configurations
with open(os.path.join(os.path.dirname(__file__), 'config.yml')) as f:
    config = yaml.load(f)

# web app
app = Flask(__name__)

# database engine
engine = sqlalchemy.create_engine(config['sql'])


@app.route('/')
def index():
    return 'Welcome to EQ Works 😎'


@app.route('/events/hourly')
def events_hourly():
    with engine.connect() as conn:
        result = conn.execute('''
            SELECT date, hour, events
            FROM public.hourly_events
            GROUP BY date, hour
            ORDER BY date, hour
            LIMIT 168;
        ''').fetchall()
        r = [dict(row.items()) for row in result]
        return jsonify(r)


@app.route('/events/daily')
def events_daily():
    with engine.connect() as conn:
        result = conn.execute('''
            SELECT date, events
            FROM public.hourly_events
            GROUP BY date
            ORDER BY date
            LIMIT 7;
        ''').fetchall()
        r = [dict(row.items()) for row in result]
        return jsonify(r)


@app.route('/stats/hourly')
def stats_hourly():
    with engine.connect() as conn:
        result = conn.execute('''
            SELECT date, hour,
                SUM(impressions) AS impressions,
                SUM(clicks) AS clicks,
                SUM(revenue) AS revenue
            FROM public.hourly_stats
            GROUP BY date, hour
            ORDER BY date, hour
            LIMIT 168;
        ''').fetchall()
        r = [dict(row.items()) for row in result]
        return jsonify(r)


@app.route('/stats/daily')
def stats_daily():
    with engine.connect() as conn:
        result = conn.execute('''
            SELECT date,
                SUM(impressions) AS impressions,
                SUM(clicks) AS clicks,
                SUM(revenue) AS revenue
            FROM public.hourly_stats
            GROUP BY date
            ORDER BY date
            LIMIT 7;
        ''').fetchall()
        r = [dict(row.items()) for row in result]
        return jsonify(r)
