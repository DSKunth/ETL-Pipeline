import boto3
from io import StringIO


def connect_to_s3(aws_access_key_id, aws_secret_access_key):
    """Method that connects to s3"""

    s3_client = boto3.client(
        "s3",
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key
    )

    return s3_client


def df_to_s3(df, key, s3_bucket, aws_access_key_id, aws_secret_access_key):
    """Function that writes a data frame as a .csv file to an s3 bucket"""

    csv_buffer = StringIO()  # create buffer to temporarily store the Data Frame

    df.to_csv(csv_buffer, index=False)  # code to write the data frame as csv file

    s3_client = connect_to_s3(aws_access_key_id, aws_secret_access_key)

    s3_client.put_object(
        Bucket=s3_bucket, Key=key, Body=csv_buffer.getvalue()
    )  # this code writes the temp stored csv file and writes to s3

    print(f"The transformed data is saved as CSV in the following location s3://{s3_bucket}/{key}")