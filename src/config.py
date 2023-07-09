# create a config class to store all the configuration parameters for the project
import json
import datetime
import pytz
import os 

tz = pytz.timezone('Europe/Zagreb')

creds = json.load(open('creds/creds.json'))
end_date = datetime.datetime.utcnow()

subs = ['croatia', 'hrvatska', 'cromunity']