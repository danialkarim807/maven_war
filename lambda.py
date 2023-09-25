import boto3
import os

# Initialize AWS services
s3 = boto3.client('s3')
ses = boto3.client('ses')

def lambda_handler(event, context):
    # Your Lambda function logic here

    # Example: Download a file from S3
    s3_bucket = 'your-s3-bucket'
    s3_key = 'your-file-key'
    download_path = '/tmp/downloaded_file.txt'
    s3.download_file(s3_bucket, s3_key, download_path)

    # Example: Perform transformations
    with open(download_path, 'r') as file:
        data = file.read()
        # Perform transformations here

    # Example: Send an email through SES
    sender_email = 'your-sender@example.com'
    recipient_email = 'your-recipient@example.com'
    subject = 'Your Subject'
    body = 'Your Email Body'

    ses.send_email(
        Source=sender_email,
        Destination={'ToAddresses': [recipient_email]},
        Message={'Subject': {'Data': subject}, 'Body': {'Text': {'Data': body}}},
    )

    # Clean up temporary files
    os.remove(download_path)

    return {
        'statusCode': 200,
        'body': 'Lambda function executed successfully'
    }
# ........................................................................................


import boto3

def create_lambda_function(function_name, runtime, handler, code, environment_variables):
    # Create a Lambda client
    lambda_client = boto3.client('lambda')

    # Define the function parameters
    function_params = {
        'FunctionName': function_name,
        'Runtime': runtime,
        'Role': 'YOUR_EXECUTION_ROLE_ARN',  # Replace with your execution role ARN
        'Handler': handler,
        'Code': {'ZipFile': code},
        'Environment': {'Variables': environment_variables}
    }

    # Create the Lambda function
    response = lambda_client.create_function(**function_params)

    return response

# Example usage:
function_name = 'MyLambdaFunction'
runtime = 'python3.8'
handler = 'lambda_handler'
code = '''
def lambda_handler(event, context):
    # Your Lambda function code here
    pass
'''
environment_variables = {
    'API_KEY': 'your_api_key',
    'CONFIG_SETTING': 'your_config_setting'
}

create_lambda_function(function_name, runtime, handler, code, environment_variables)

# --------------------------------------------------------------------------------------------------

# list down all the services
import boto3

def list_aws_services(event, context):
    # Initialize a list to store service names
    service_names = []

    # Create a session using the Lambda execution role credentials
    session = boto3.Session()

    # Iterate through available services and append their names to the list
    for service in session.get_available_services():
        service_names.append(service)

    # Return the list of service names
    return {
        'statusCode': 200,
        'body': ', '.join(service_names)
    }
# ------------------------------------create s3 from lambda----------------------------


import json 
import boto3

def lambda_handler(event, contaxt):
    bucket_name='save_data_from_lambda'
    listen001=["this is first list"]
    s3_path_001 = "001"

    s3_client = boto3.client('s3', 'eu-central-1')
    save_to_s3 = s3_client.put_objects(
        key=s3_path_001,
        Bucket= bucket_name,
        body=json.dumps(listen001).encode('UTF-8'))