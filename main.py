# provides ways to access the Operating System and allows us to read the environment variables
import os

from datetime import datetime
from src.extract import extract_transaction_data
from src.transform import identify_and_remove_duplicated_data
from src.load_data_to_s3 import df_to_s3

# import the load_dotenv from the python-dotenv module
from dotenv import load_dotenv
load_dotenv() # take environment variables from .env only for local testing


# import environment variables from .env file
dbname = os.getenv("dbname")
host = os.getenv("host")
port = os.getenv("port")
user = os.getenv("user")
password = os.getenv("password")
aws_access_key_id = os.getenv("aws_access_key_id")
aws_secret_access_key_id = os.getenv("aws_secret_access_key_id")

# this creates a variable that tracks the time we executed the script
start_time = datetime.now()

# make a connection to redshift and extract online transactions data with transformation tasks
print("\nExtracting and transforming data in sql...")
online_trans_cleaned = extract_transaction_data(dbname, host, port, user, password)
print('\nExtraction and transformation in sql completed')

# remove duplicated data
print("\nRemoving duplicated data...")
online_trans_deduped = identify_and_remove_duplicated_data(online_trans_cleaned)
print('\nDuplicated data removed')

# load online_trans_deduped to s3
print("\nLoading data to s3...")
s3_bucket = 'waia-data-dump'
key = 'bootcamp2/etl/dk_online_trans_cleaned.csv'

df_to_s3(online_trans_deduped, key, s3_bucket, aws_access_key_id, aws_secret_access_key_id)
print('\nData loaded to s3')

# this creates a variable that calculates how long it takes to run the script
execution_time = datetime.now() - start_time
print(f"\nTotal execution time (hh:mm:ss.ms) {execution_time}")