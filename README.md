# GermanRap Subreddit Bot

## Description
This bot automates the creation of weekly discussion threads for the r/GermanRap subreddit. It posts different types of threads on a rotating schedule, including international releases, music recommendations, collaboration opportunities, and subreddit feedback. It can be quite easily adapted to other subreddits and topics by changing the .env and the texts in "all_post_texts.py".

## Features
- Automated weekly post creation
- Rotating topics for each week of the month
- Linking to previous threads
- Error logging and Discord notifications

## Requirements
- Python 3.7+
- PRAW (Python Reddit API Wrapper)
- python-dotenv
- requests

## Setup
1. Clone the repository:
git clone https://github.com/your-username/germanrap-subreddit-bot.git
cd germanrap-subreddit-bot

2. Install the required packages:
pip install -r requirements.txt

3. Create a `.env` file in the project root with the following variables:

CLIENT_ID=your_reddit_client_id
CLIENT_SECRET=your_reddit_client_secret
REFRESH_TOKEN=your_reddit_refresh_token
USER_AGENT=your_user_agent
SUBREDDIT=your_subreddit
FLAIRID=your_flair_id
WEBHOOK_URL=your_discord_webhook_url

Replace the placeholder values with your actual Reddit API credentials, data and Discord webhook URL.

## Usage
To run the bot, execute the main script:
python main.py
The bot will automatically determine which weekly thread to post based on the current week of the month.

## File Structure
- `main.py`: The entry point of the application
- `Weekly_und_Collabo_Bot_Germanrap.py`: Contains the main logic for creating and submitting posts
- `alle_post_texte.py`: Stores the text content for different types of posts
- `connect_to_reddit.py`: Handles the Reddit API connection
- `csv_handler.py`: Manages the CSV file for tracking previous threads

## Logging
The bot logs its activities to various log files:
- `main_script.log`
- `posterscript.log`
- `schedulerscript.log`

Check these files for debugging information and error messages.

## Contributing
It's a personal hobby project but contributions are welcome! Please feel free to submit a Pull Request.

## License
This project is licensed under the GNU General Public License v3.0 (GPLv3). See the [LICENSE](LICENSE) file for details.

## Contact
For any queries or issues, please open an issue on this GitHub repository.
