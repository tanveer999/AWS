import boto3
import json
# from datetime import datetime, timedelta

# Initialize a boto3 client for Cost Explorer
cost_explorer = boto3.client('ce')

# Define the time period for the query
# end_date = datetime.today().strftime('%Y-%m-%d')
# start_date = (datetime.today() - timedelta(days=30)).strftime('%Y-%m-%d')

start_date = '2024-01-01'
end_date = '2024-02-29'

# Define the tag key you want to filter by
# tag_key = 'YourTagKey'  # Replace with your tag key

# Get cost details based on the tag key
response = cost_explorer.get_cost_and_usage(
    TimePeriod={
        'Start': start_date,
        'End': end_date
    },
    Granularity='MONTHLY',
    # Filter={
    #     'Tags': {
    #         'Key': tag_key,
    #         'Values': ['*']
    #     }
    # },
    Metrics=['UnblendedCost']
)

# Print the response
print(json.dumps(response, indent=2))