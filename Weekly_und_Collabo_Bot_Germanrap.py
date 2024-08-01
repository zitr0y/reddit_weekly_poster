import logging
import os
import connect_to_reddit
import csv_handler
import alle_post_texte

os.chdir(os.path.dirname(os.path.realpath(__file__)))
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', filename='posterscript.log')

post_names = {
        1: "post1_internationale_releases",
        2: "post2_was_hoert_ihr",
        3: "post3_collabothread",
        4: "post4_reflektion_releases",
        5: "post5_versteckter_thread"
    }

def post(reddit, subreddit, title, flairID=None, url=None, text=None):
    reddit.validate_on_submit = True
    subreddit = reddit.subreddit(subreddit)
    
    if not (url or text):
        logging.error(f"Error: You need to provide either selftext or URL to post! Post with title '{title}' was not posted!")
        return None

    try:
        if url:
            logging.info(f'Submitting link post: {title}')
            submission = subreddit.submit(title, url=url, flair_id=flairID)
        else:
            logging.info(f'Submitting text post: {title}')
            submission = subreddit.submit(title, selftext=text, flair_id=flairID)
        
        logging.info(f'Successfully submitted post: {title}')
        return submission
    except Exception as e:
        logging.error(f"Error posting '{title}': {str(e)}")
        return None

def get_post_name(post_nummer):
    """Convert post number to post name."""
    return post_names.get(post_nummer)

def prepare_post_content(post_name):
    """Prepare the title and text for the post."""
    with_link = csv_handler.output_csv_entry(post_name)
    logging.info(f'Preparing text with parameters: with_link: {with_link}')
    return alle_post_texte.get_post_text(post_name, with_link)

def submit_post(reddit, subreddit, title, text, flairID):
    """Submit the post to Reddit."""
    logging.info(f'Attempting to submit post: {title}')
    return post(reddit, subreddit, title, flairID, text=text)

def update_csv(post_name, submissionID):
    """Update the CSV with the new post ID."""
    logging.info(f'Updating CSV with new post ID')
    csv_handler.update_or_append_csv_entry(post_name, submissionID)

def friss_post(post_nummer, subreddit="germanrap", flairID=False):
    """Main function to create and submit a post."""
    logging.info(f'Starting post creation: number {post_nummer}, subreddit {subreddit}, flairID {flairID}')

    post_name = get_post_name(post_nummer)
    if not post_name:
        logging.error(f"Error: Invalid post number. Must be between 1-5. Given: {post_nummer}")
        return

    title, text = prepare_post_content(post_name)
    submissionID = submit_post(reddit, subreddit, title, text, flairID)
    update_csv(post_name, submissionID)

    logging.info(f'Post creation completed for {post_name}')


reddit = connect_to_reddit.connecttoreddit()
