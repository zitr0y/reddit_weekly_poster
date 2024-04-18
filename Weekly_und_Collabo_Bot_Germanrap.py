import praw
import random
import webbrowser
import sys
import socket
import datetime
import schedule
import time
import logging
import os
import csv
import alle_post_texte
from dotenv import load_dotenv





# Get the directory of the script
dir_path = os.path.dirname(os.path.realpath(__file__))

# Set the current working directory to the directory of the script
os.chdir(dir_path)

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', filename='posterscript.log')

try:
    load_dotenv()
    client_id = os.getenv('CLIENT_ID')
    client_secret = os.getenv('CLIENT_SECRET')
    refresh_token = os.getenv('REFRESH_TOKEN')
    user_agent = os.getenv('USER_AGENT')
    logging.info('Loaded .env file successfully.')
except:
    logging.error('Error: Could not load .env file. Please make sure that the file exists and is in the same directory as the script.')
    sys.exit()



def connecttoreddit():
    reddit = praw.Reddit(
        client_id=client_id,
        client_secret=client_secret,
        refresh_token=refresh_token,
        user_agent=user_agent,
    )
    logging.info('Connected to Reddit!')
    return reddit

def post(reddit, subreddit, title, flairID=False, url=False, text=False):
    reddit.validate_on_submit = 1
    subreddit = reddit.subreddit(subreddit)
    if url:
        logging.info(f'URL given. If Selftext was given, it will be disregarded.')
        if flairID:
            submission = subreddit.submit(title, url=url)
            logging.info(f'Submitted link post with title {title}')
        else:
            submission = subreddit.submit(title, url=url, flair_id=flairID)
            logging.info(f'Submitted link post with title {title} and flairID {flairID}')
    elif text:
        logging.info(f'Selftext and no URL given')
        if flairID:
            submission = subreddit.submit(title, selftext=text, flair_id=flairID)
            logging.info(f'Submitted text post with title {title} and flairID {flairID}')
        else:
            submission = subreddit.submit(title, selftext=text)
            logging.info(f'Submitted text post with title {title}')
    else:
        print("Error: You need to provide either selftext or URL to post!")
        logging.error(f"Error: You need to provide either selftext or URL to post! Post with title {title} was not posted!")
    if submission: return submission
    else: return None

def update_or_append_csv_entry(post_Category, post_ID, variation = 200, filename='last_thread_link_list.csv'):
    rows = []
    logging.info(f'attempting to update csv with post_Category, post ID: {post_Category}, {post_ID}.')
    # Read existing data
    try:
        with open(filename, mode='r') as last_thread_file:
            last_thread_reader = csv.reader(last_thread_file)
            rows = list(last_thread_reader)
    except FileNotFoundError:
        logging.info(f'csv did not exist yet, will be newly created.')
        pass  # File doesn't exist yet

    # Check if entry with the same post_Category exists
    entry_exists = False
    for row in rows:
        if len(row) > 0:  # Add check for row[0] existence
            if not row[0].startswith('#'):
                if len(row) > 2 and row[0] == post_Category:
                    logging.info(f'Old entry for {post_Category}, {row[1]}, will be overwritten. Variation was {row[2]}, now {variation}. (200 is placeholder for no variation specified)')
                    row[1] = post_ID  # Update post_ID if post_Category exists
                    if variation != 200:
                        row[2] = variation # Update variation if post_Category exists
                    elif int(row[2]) >= 0: # number of different posts of the same category (currently not in use)
                        row[2] = 0
                        variation = row[2]
                    else: # miese notlösung gerade
                        row[2] = 0
                        variation = row[2]
                    #elif int(row[2]) < 0: # currently not in use
                    #    row[2] = str(int(row[2]) + 1)
                    #    variation = row[2]
                    
                    entry_exists = True
                    logging.info(f'There was already an entry for {post_Category}, overwritten with new entry, {post_ID}')
                    break 

    # If entry doesn't exist, append a new row
    if not entry_exists:
        variation = 0
        rows.append([post_Category, post_ID, variation])
        logging.info(f'There was not already an entry for {post_Category}, category created.')

    # Write data back to the file
    with open(filename, mode='w', newline='') as last_thread_file:
        last_thread_writer = csv.writer(last_thread_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        last_thread_writer.writerows(rows)
        logging.info(f'Writing to csv complete. post_Category, post_ID, variation: {post_Category}, {post_ID}, {variation}')

def output_csv_entry(post_Category, filename='last_thread_link_list.csv'):
    variation_if_no_entry = 0
    rows = []
    logging.info(f'Attempting to read from csv with post_Category: {post_Category}.')
    # Read existing data
    try:
        with open(filename, mode='r') as last_thread_file:
            last_thread_reader = csv.reader(last_thread_file)
            rows = list(last_thread_reader)
    except FileNotFoundError:
        logging.info(f'csv does not exist yet, returning False.')
        return False, variation_if_no_entry

    # Check if entry with the same post_Category exists and return
    for row in rows:
        if len(row) > 0:  # Add check for row[0] existence
            if not row[0].startswith('#'):
                if row and row[0] == post_Category:
                    if len(row) > 2 and row[1] != "" and row[2] != "":  # Add check for row[1] and row[2] existence
                        logging.info(f'Entry found for {post_Category}. Returning post ID: {row[1]}')
                        return row[1], row[2]  # Update post_ID if post_Category exists
                    else: 
                        logging.error(f'Entry found for {post_Category} but it is empty or incomplete. This means that something went wrong in the past and our csv is faulty. Returning False.')
                        return (False, variation_if_no_entry)

    # If entry doesn't exist, return None
    logging.info(f'No entry found for {post_Category}. Returning False.')
    return False, variation_if_no_entry

def post1_internationale_releases(subreddit, flairID):
    with_link, variation = output_csv_entry("post1_internationale_releases")
    logging.info(f'Text wird mit folgenden parametern ausgesucht: with_link, variation: {with_link}, {variation}')
    title, text = alle_post_texte.post1_internationale_releases_text(with_link, variation)
    logging.info(f'Attempting to submit post of kind "post1_internationale_releases"')
    submissionID = post(reddit, subreddit, title, flairID, text=text)
    logging.info(f'Attempting to write ID to csv')
    update_or_append_csv_entry("post1_internationale_releases", submissionID)
    return

def post2_was_hoert_ihr(subreddit, flairID):
    with_link, variation = output_csv_entry("post2_was_hoert_ihr")
    logging.info(f'Text wird mit folgenden parametern ausgesucht: with_link, variation: {with_link}, {variation}')
    title, text = alle_post_texte.post2_was_hoert_ihr_text(with_link, variation)
    logging.info(f'Attempting to submit post of kind "post2_was_hoert_ihr"')
    submissionID = post(reddit, subreddit, title, flairID, text=text)
    logging.info(f'Attempting to write ID to csv')
    update_or_append_csv_entry("post2_was_hoert_ihr", submissionID)
    return

def post3_collabothread(subreddit, flairID):
    with_link, variation = output_csv_entry("post3_collabothread")
    logging.info(f'Text wird mit folgenden parametern ausgesucht: with_link, variation: {with_link}, {variation}')
    title, text = alle_post_texte.post3_collabothread_text(with_link, variation)
    logging.info(f'Attempting to submit post of kind "post3_collabothread"')
    submissionID = post(reddit, subreddit, title, flairID, text=text)
    logging.info(f'Attempting to write ID to csv')
    update_or_append_csv_entry("post3_collabothread", submissionID)
    return

def post4_reflektion_releases(subreddit, flairID):
    with_link, variation = output_csv_entry("post4_reflektion_releases")
    logging.info(f'Text wird mit folgenden parametern ausgesucht: with_link, variation: {with_link}, {variation}')
    title, text = alle_post_texte.post4_reflektion_releases_text(with_link, variation)
    logging.info(f'Attempting to submit post of kind "post4_reflektion_releases"')
    submissionID = post(reddit, subreddit, title, flairID, text=text)
    logging.info(f'Attempting to write ID to csv')
    update_or_append_csv_entry("post4_reflektion_releases", submissionID)
    return

def post5_versteckter_thread(subreddit, flairID):
    with_link, variation = output_csv_entry("post5_versteckter_thread")
    logging.info(f'Text wird mit folgenden parametern ausgesucht: with_link, variation: {with_link}, {variation}')
    title, text = alle_post_texte.post5_versteckter_thread_text(with_link, variation)
    logging.info(f'Attempting to submit post of kind "post5_versteckter_thread"')
    submissionID = post(reddit, subreddit, title, flairID, text=text)
    logging.info(f'Attempting to write ID to csv')
    update_or_append_csv_entry("post5_versteckter_thread", submissionID)
    return



def friss_post(post_nummer, subreddit="germanrap", flairID=False):
    if post_nummer == 1:
        logging.info(f'friss_post given info: post_nummer {post_nummer}, subreddit {subreddit}, flairID {flairID}')
        post1_internationale_releases(subreddit, flairID)
    elif post_nummer == 2:
        logging.info(f'friss_post given info: post_nummer {post_nummer}, subreddit {subreddit}, flairID {flairID}')
        post2_was_hoert_ihr(subreddit, flairID)
    elif post_nummer == 3:
        logging.info(f'friss_post given info: post_nummer {post_nummer}, subreddit {subreddit}, flairID {flairID}')        
        post3_collabothread(subreddit, flairID)
    elif post_nummer == 4:
        logging.info(f'friss_post given info: post_nummer {post_nummer}, subreddit {subreddit}, flairID {flairID}')        
        post4_reflektion_releases(subreddit, flairID)
    elif post_nummer == 5:
        logging.info(f'friss_post given info: post_nummer {post_nummer}, subreddit {subreddit}, flairID {flairID}')        
        post5_versteckter_thread(subreddit, flairID)
    else:
        logging.error(f"Error: Das erste Parameter muss eine Zahl zwischen 1-5 sein, welche mit einem der monatlichen Releases korrespondiert. \nGiven: {post_nummer}")
    return


reddit = connecttoreddit()
