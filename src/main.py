from common import tprint, r, check_dirs
from getData import get_date_range, get_comments
from config import subs, tz, plot_data
from plot import plot_comm_day

import datetime
import logging
import os
import pytz


def main():
    # check if logs/,plots and data/ dirs exist
    check_dirs()

    # set up logging
    log_filename = datetime.datetime.now().strftime('gs-log_%Y-%m-%d_%H-%M-%S.log')
    logging.basicConfig(filename=f"logs/{log_filename}", level=logging.INFO)


    tprint(f"Authenticated as /u/{r.user.me()}")
    tprint(f"Starting at: {datetime.datetime.now(tz).strftime('%Y:%m:%d %H:%M:%S')}")
    tprint(f"Timezone: {tz}")
    tprint(f"Subreddits: {subs}")

    # for sub in subs:
    #     sub_ = get_date_range(sub, 14)
    #     get_comments(sub_)

    plot_comm_day(plot_data, str(tz))

if __name__ == '__main__':
    main()
    #
