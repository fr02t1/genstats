from common import tprint, r
from config import end_date
import pandas as pd
import datetime
import tqdm
import re

def get_date_range(subreddit, days):
    global end_date
    start_date = end_date - datetime.timedelta(days=days)
    print("\n")
    tprint(f"Getting posts ids from r/{subreddit}")
    count = 0
    tprint(f"Start date: {start_date}")
    tprint(f"End date: {end_date}")
    subm_ids = []
    for submission in r.subreddit(subreddit).new(limit=None):
            # if the submission is less than the specified number of days old, add it to the list
      if submission.created_utc > start_date.timestamp():
        count += 1
        print(f"count: {count}", end='\r')
        subm_ids.append(submission.id)
      else:
        continue
    tprint(f"count: {count}", end='\r')

    return subm_ids


def get_comments(subm_id):
    df = pd.DataFrame(columns=['id','subreddit', 'created_utc', 'score', 'body'])
    df_list = []

    current_subreddit = None

    for id in tqdm.tqdm(subm_id, desc='Submissions', leave=False, ncols=80):
        submission = r.submission(id=id)
        submission.comments.replace_more(limit=None)
        for comment in submission.comments.list():
            subreddit_name = comment.subreddit.display_name
            if subreddit_name != current_subreddit:
                # if the subreddit has changed, write the current dataframe to a file
                if current_subreddit is not None:
                    current_filename = f"data/comments_{current_subreddit}-14d.csv"
                    df.to_csv(current_filename, index=False)
                    tprint(f"Wrote {len(df)} comments to {current_filename}")
                # create a new dataframe for the new subreddit
                df = pd.DataFrame(columns=['id','subreddit', 'created_utc', 'score', 'body'])
                current_subreddit = subreddit_name
            df_list.append(pd.DataFrame({'id': comment.id, 
                                         'subreddit': subreddit_name,
                                         'created_utc': comment.created_utc, 
                                         'score': comment.score, 
                                         'body': comment.body}, index=[0]))
    # write the final dataframe to a file
    current_filename = f"data/comments_{current_subreddit}-14d.csv"
    df = pd.concat(df_list, ignore_index=True)
    df.to_csv(current_filename, index=False)
    tprint(f"Wrote {len(df)} comments to {current_filename}")
