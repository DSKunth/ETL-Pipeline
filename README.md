# ETL Pipeline Project
This repository contains tasks on how to build an ETL pipeline.
ETL (Extract, Transform, Load) is a data pipeline used to collect data from various sources, transforms the data according to business requirements, and loads the data into a destination data storage.

This project contains the following python files:
- extract.py - contains functions to connect to Amazon Redshift data warehouse and to extract online transactions data with transformations tasks using SQL
- transform.py - contains function to remove duplicated records
- load_data_to_s3.py - contains functions to connect to Amazon S3 cloud object storage and to write the cleaned data as a CSV file into an S3 bucket
- main.py - contains all instructions to extract, transform, and load the transformed data using the functions from extract.py, transform.py, and load_data_to_s3.py.
# ETL-Pipeline-Project
