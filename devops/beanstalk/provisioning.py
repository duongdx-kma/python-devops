import boto3
from function import check_application_status

# define session
session = boto3.session.Session(profile_name='duongdinhxuan_duong-admin')

# Create an Elastic Beanstalk client
beanstalk = session.client('elasticbeanstalk')

# Define the parameters for the application
params = {
    'ApplicationName': 'testing-beanstalk',
    'Description': 'testing testing-beanstalk with boto3',
}

# Create the Elastic Beanstalk environment

application_check = check_application_status(beanstalk, [
    'testing-beanstalk',
])

if not application_check:
    response = beanstalk.create_application(**params)
    print(response)
else:
    print("application already exist")
