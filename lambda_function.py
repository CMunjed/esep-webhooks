import json
import os
import requests

def lambda_handler(event, context):

    slack_url = os.environ['SLACK_URL']
    
    payload = {'text':f"Issue Created: {event['issue']['html_url']}"}
    
    #headers = {"Content-type": "application/json"}
    
    requests.post(url=slack_url, json=payload)
    
    return {
        'statusCode': 200,
        'body': json.dumps('success')
    }