from config import creds
from config import tz

import praw
import datetime
import pytz
import logging
import os

r = praw.Reddit(client_id=creds['client_id'],
                client_secret=creds['client_secret'],
                user_agent=creds['user_agent'],
                username=creds['username'],
                password=creds['password'])


def tprint(string,end=None):
    global tz
    #tz = pytz.timezone('Europe/Zagreb')
    timestamp = datetime.datetime.now(tz).strftime('%Y:%m:%d %H:%M:%S')

    args = f"{timestamp} [+] {string}"
    print(args, end=end)
    logging.info(args)

def check_dirs():
    tprint("Checking for logs/, plot/ and data/ dirs ")
    if not os.path.exists('logs'):
        tprint("logs/ dir doesn't exist creating it")
        os.makedirs('logs')

    # tprint("Checking for plots/ dir ")
    if not os.path.exists('plots'):
        tprint("plots/ dir doesn't exist creating it")
        os.makedirs('plots')

    # tprint("Checking for data/ dir ")
    if not os.path.exists('data'):
        tprint("data/ dir doesn't exist creating it\n")
        os.makedirs('data')