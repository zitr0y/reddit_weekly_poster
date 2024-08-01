import csv
import logging

def update_or_append_csv_entry(post_Category, post_ID, filename='last_thread_link_list.csv'):
    rows = []
    logging.info(f'Attempting to update csv with post_Category, post ID: {post_Category}, {post_ID}.')
   
    # Read existing data
    try:
        with open(filename, mode='r') as last_thread_file:
            last_thread_reader = csv.reader(last_thread_file)
            rows = list(last_thread_reader)
    except FileNotFoundError:
        logging.info(f'CSV did not exist yet, will be newly created.')
   
    # Check if entry with the same post_Category exists
    entry_exists = False
    for i, row in enumerate(rows):
        if row and not row[0].startswith('#'):
            if row[0] == post_Category:
                logging.info(f'Old entry for {post_Category} will be overwritten. New post ID: {post_ID}')
                if len(row) > 1:
                    row[1] = post_ID
                else:
                    rows[i] = [post_Category, post_ID]
                entry_exists = True
                logging.info(f'There was already an entry for {post_Category}, overwritten with new entry, {post_ID}')
                break
   
    # If entry doesn't exist, append a new row
    if not entry_exists:
        rows.append([post_Category, post_ID])
        logging.info(f'There was not already an entry for {post_Category}, category created.')
   
    # Write data back to the file
    with open(filename, mode='w', newline='') as last_thread_file:
        last_thread_writer = csv.writer(last_thread_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        last_thread_writer.writerows(rows)
        logging.info(f'Writing to csv complete. post_Category, post_ID: {post_Category}, {post_ID}')

def output_csv_entry(post_Category, filename='last_thread_link_list.csv'):
    logging.info(f'Attempting to read from csv with post_Category: {post_Category}.')
   
    # Read existing data
    try:
        with open(filename, mode='r') as last_thread_file:
            last_thread_reader = csv.reader(last_thread_file)
            for row in last_thread_reader:
                if row and not row[0].startswith('#'):
                    if row[0] == post_Category:
                        if len(row) > 1 and row[1]:
                            logging.info(f'Entry found for {post_Category}. Returning post ID: {row[1]}')
                            return row[1]
                        else:
                            logging.error(f'Entry found for {post_Category} but it is incomplete. Returning False.')
                            return False
    except FileNotFoundError:
        logging.info(f'CSV does not exist yet, returning False.')
        return False
   
    # If entry doesn't exist, return False
    logging.info(f'No entry found for {post_Category}. Returning False.')
    return False