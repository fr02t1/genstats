import praw
import datetime
import pytz
import logging
import os
import json

from config import creds_path
from config import tz



def tprint(string,end=None):
    global tz
    #tz = pytz.timezone('Europe/Zagreb')
    timestamp = datetime.datetime.now(tz).strftime('%Y:%m:%d %H:%M:%S')

    args = f"{timestamp} [+] {string}"
    print(args, end=end)
    logging.info(args)

def eprint(string,end=None):
    global tz
    timestamp = datetime.datetime.now(tz).strftime('%Y:%m:%d %H:%M:%S')

    args = f"{timestamp} [-] {string}"
    print(args, end=end)
    logging.error(args)
    


def check_dirs():
    tprint("Checking for logs/, plot/ and data/ dirs ")
    if not os.path.exists('logs'):
        eprint("logs/ dir doesn't exist creating it")
        os.makedirs('logs')

    # tprint("Checking for plots/ dir ")
    if not os.path.exists('plots'):
        eprint("plots/ dir doesn't exist creating it")
        os.makedirs('plots')

    # tprint("Checking for data/ dir ")
    if not os.path.exists('data'):
        eprint("data/ dir doesn't exist creating it\n")
        os.makedirs('data')


if not os.path.exists('creds'):
    tprint("creds/ dir doesn't exist creating it")
    os.makedirs('creds', exist_ok=True)

if not os.path.exists(creds_path):
    eprint("creds.json not found please create it")
    exit(1)

creds = json.load(open(creds_path))


r = praw.Reddit(client_id=creds['client_id'],
                client_secret=creds['client_secret'],
                user_agent=creds['user_agent'],
                username=creds['username'],
                password=creds['password'])

