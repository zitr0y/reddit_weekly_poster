import os
import sys
import logging
import datetime
from dotenv import load_dotenv
import Weekly_und_Collabo_Bot_Germanrap
import requests

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename='main_script.log')

def load_environment_variables():
    """Load environment variables from .env file."""
    try:
        load_dotenv()
        subreddit = os.getenv('SUBREDDIT')
        flairID = os.getenv('FLAIRID')
        webhook_url = os.getenv('WEBHOOK_URL')
        
        if not all([subreddit, flairID, webhook_url]):
            raise ValueError("One or more required environment variables are missing.")
        
        logging.info('Loaded .env file successfully.')
        return subreddit, flairID, webhook_url
    except Exception as e:
        logging.error(f'Error loading .env file: {str(e)}')
        sys.exit(1)

def week_of_month(date):
    """Calculate the week of the month."""
    return date.day // 7 + 1

def send_discord_message(webhook_url, message):
        data = {
            "content": message
        }
        response = requests.post(webhook_url, json=data)
        if response.status_code == 204:
            return True
        else:
            return False

def post_weekly_thread(subreddit, flairID, webhook_url):
    """Post the weekly thread and handle any errors."""
    try:
        current_week = week_of_month(datetime.date.today())
        Weekly_und_Collabo_Bot_Germanrap.friss_post(current_week, subreddit, flairID)
        logging.info(f'Successfully posted weekly thread for week {current_week}')
    except Exception as e:
        error_message = f"Error posting weekly thread: {str(e)}"
        logging.error(error_message)
        if not send_discord_message(webhook_url, f"Error posting weekly thread. Alert @zitr0y. \n{error_message}"):
            logging.error("Error sending error message to Discord.")
        logging.error(error_message)

def main():
    """Main function to run the script."""
    subreddit, flairID, webhook_url = load_environment_variables()
    #post_weekly_thread(subreddit, flairID, webhook_url)

if __name__ == "__main__":
    main()







# For testing purposes

#Weekly_und_Collabo_Bot_Germanrap.friss_post(1, subreddit = "germanraptest", flairID="0dc4ec00-0d69-11ec-99e6-f6bad6da933e")
#Weekly_und_Collabo_Bot_Germanrap.friss_post(2, subreddit = "germanraptest", flairID="0dc4ec00-0d69-11ec-99e6-f6bad6da933e")
#Weekly_und_Collabo_Bot_Germanrap.friss_post(3, subreddit = "germanraptest", flairID="0dc4ec00-0d69-11ec-99e6-f6bad6da933e")
#Weekly_und_Collabo_Bot_Germanrap.friss_post(4, subreddit = "germanraptest", flairID="0dc4ec00-0d69-11ec-99e6-f6bad6da933e")
#Weekly_und_Collabo_Bot_Germanrap.friss_post(5, subreddit = "germanraptest", flairID="0dc4ec00-0d69-11ec-99e6-f6bad6da933e")
