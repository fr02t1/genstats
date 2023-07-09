# create a config class to store all the configuration parameters for the project
import json
import datetime
import pytz


tz = pytz.timezone('Europe/Zagreb')

creds = json.load(open('creds/creds.json'))
end_date = datetime.datetime.utcnow()

subs = ['croatia', 'hrvatska', 'cromunity']

plot_data = ['data/comments_croatia-14d.csv', 
             'data/comments_hrvatska-14d.csv',
             'data/comments_cromunity-14d.csv']