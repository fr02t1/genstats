#TODO 
#1. add command line arguments

# WARNING: this is a work in progress and is not yet functional or complete

import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Generate stats for a subreddit')
    parser.add_argument('-s', '--subreddit', type=str, help='subreddit to generate stats for', required=True)
    parser.add_argument('-t', '--timezone', type=str, help='timezone to use for the plot', default='Europe/Zagreb')
    parser.add_argument('-d', '--days', type=int, help='number of days to go back', default=14)
    parser.add_argument('-a', '--all', action='store_true', help='generate stats for comments and posts', default=False)
    parser.add_argument('-v', '--verbose', action='store_true', help='increase output verbosity', default=False)
    parser.add_argument('-l', '--log', action='store_true', help='log output to file', default=False)

args = parser.parse_args()