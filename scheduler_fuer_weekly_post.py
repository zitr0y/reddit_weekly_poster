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
from dotenv import load_dotenv

import Weekly_und_Collabo_Bot_Germanrap
import requests

# Get the directory of the script
dir_path = os.path.dirname(os.path.realpath(__file__))

# Set the current working directory to the directory of the script
os.chdir(dir_path)

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', filename='schedulerscript.log')

try:
    load_dotenv()
    subreddit = os.getenv('SUBREDDIT')
    flairID = os.getenv('FLAIRID')
    webhook_url = os.getenv('WEBHOOK_URL')
    
    logging.info('Loaded .env file successfully.')
except:
    logging.error('Error: Could not load .env file. Please make sure that the file exists and is in the same directory as the script.')
    sys.exit()



# friss_post(post_nummer, subreddit="germanrap", flairID=None)
# post1_internationale_releases
# post2_was_hoert_ihr
# post3_collabothread
# post4_reflektion_releases

def week_of_month(date):
    current_date = datetime.date.today()
    week = current_date.day // 7 + 1
    logging.info(f'Date: {current_date} Week of the Month: {week}')
    return week

def send_discord_message(webhook_url, message):
        data = {
            "content": message
        }
        response = requests.post(webhook_url, json=data)
        if response.status_code == 204:
            print("Discord message sent successfully")
        else:
            print("Failed to send message") 

    
#### 1-5!!!
# 5 Heisst Special Post (anfangs merch-appreciation, später gerne auch anderes!)
try:
    Weekly_und_Collabo_Bot_Germanrap.friss_post(week_of_month(datetime.date), subreddit, flairID)
except:
  send_discord_message(webhook_url, "Es gab einen Fehler beim Posten des Weeklys! Check die Logs @zitr0y")
  logging.error(f'Error in friss_post()')
  print("Error in friss_post()")




#Weekly_und_Collabo_Bot_Germanrap.friss_post(1, subreddit = "germanraptest", flairID="0dc4ec00-0d69-11ec-99e6-f6bad6da933e")
#Weekly_und_Collabo_Bot_Germanrap.friss_post(2, subreddit = "germanraptest", flairID="0dc4ec00-0d69-11ec-99e6-f6bad6da933e")
#Weekly_und_Collabo_Bot_Germanrap.friss_post(3, subreddit = "germanraptest", flairID="0dc4ec00-0d69-11ec-99e6-f6bad6da933e")
#Weekly_und_Collabo_Bot_Germanrap.friss_post(4, subreddit = "germanraptest", flairID="0dc4ec00-0d69-11ec-99e6-f6bad6da933e")
#Weekly_und_Collabo_Bot_Germanrap.friss_post(5, subreddit = "germanraptest", flairID="0dc4ec00-0d69-11ec-99e6-f6bad6da933e")
