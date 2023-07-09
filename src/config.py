import json
import datetime
import pytz

tz = pytz.timezone('Europe/Zagreb')

creds_path = 'creds/creds.json'

end_date = datetime.datetime.utcnow()

subs = ['croatia', 'hrvatska', 'cromunity']

plot_data = ['data/comments_croatia-14d.csv', 
             'data/comments_hrvatska-14d.csv',
             'data/comments_cromunity-14d.csv']