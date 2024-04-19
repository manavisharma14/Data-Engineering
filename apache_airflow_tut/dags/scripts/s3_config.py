import boto3
import os

def upload_to_s3(bucket_name, filename, object_name):
    # Initialize a boto3 client
    s3 = boto3.client('s3')

    # Complete path to the file
    base_path = os.environ.get('AIRFLOW_HOME', '')
    full_file_path = os.path.join(base_path, filename)

    # Upload the file
    s3.upload_file(Filename=full_file_path, 
                   Bucket=bucket_name, 
                   Key=object_name)

    print("File uploaded successfully to bucket '{}' with object name '{}'".format(bucket_name, object_name))

if __name__ == "__main__":
    # Default values for testing; replace or parameterize as needed
    bucket_name = 'sourabh-sample-bucket'
    filename = 'dags/data/transformed_loan_data.csv'  # Assuming this path is relative to AIRFLOW_HOME
    object_name = 'dataset/alcohol.csv'

    upload_to_s3(bucket_name, filename, object_name)