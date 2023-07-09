import datetime
import matplotlib.pyplot as plt
import pandas as pd
import pytz
import re

from common import tprint

def plot_comm_day(filenames, timezone):
    # create a figure and axis object
    fig, ax = plt.subplots()

    # iterate over each file
    for filename in filenames:
        # read the CSV file into a pandas DataFrame
        df = pd.read_csv(filename)

        # extract the subreddit name from the filename
        subreddit_name = re.search(r'comments_(.+)-14d.csv', filename).group(1)

        # # look up the subreddit avatar
        # subreddit = reddit.subreddit(subreddit_name)
        # subreddit_icon = subreddit.icon_img

        # add r/ to the subreddit name
        subreddit_name = 'r/' + subreddit_name

        # convert the 'created_utc' column to a datetime object in the specified timezone
        tz = pytz.timezone(timezone)
        df['created_utc'] = pd.to_datetime(df['created_utc'], unit='s').dt.tz_localize('UTC').dt.tz_convert(tz)

        # group the comments by day and count the number of comments per day
        comments_per_day = df.groupby(df['created_utc'].dt.date).size()

        # plot the data as a line graph with a grid
        ax.plot(comments_per_day.index, comments_per_day.values, linewidth=2, marker='.', markersize=20, label=subreddit_name)

        # add the number of comments to each point on the line graph
        for x, y in zip(comments_per_day.index, comments_per_day.values):
            ax.text(x, y, str(y), ha='center', va='bottom')

    # fig size
    fig.set_size_inches(20, 10)
    # set the x-axis label, y-axis label, and title
    ax.set_xlabel('Date')
    ax.set_ylabel('Number of Comments')
    ax.set_title('Number of Comments per Day')

    # add a legend and grid
    ax.legend()
    ax.grid(True)

    # show the plot
    out_filename= datetime.datetime.now().strftime('genstats-img-%Y-%m-%d_%H-%M-%S.png')
    plt.savefig(f"plots/{out_filename}")
    tprint(f"plot saved to plots/{out_filename}")
    #plt.show()