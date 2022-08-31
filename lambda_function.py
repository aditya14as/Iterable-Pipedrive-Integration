from asyncio import events
import json
from jwt import getJWT
from getContactType import getContactType
from getMarketingOptIn import getMarketingOptIn
from getProgramAttended import getProgramAttended
from getProgramInterestedIn import getProgramInterestedIn
import requests 
import os

pipedrive_api = os.environ['PIPEDRIVE_API']
iterable_api_key = os.environ['ITERABLE_API']
secret_jwt = os.environ['ITERABLE_SECRET_JWT']

def lambda_handler(event, context):
    events =  json.loads(event['body'])
    
    first_name = events["current"]["first_name"]
    last_name = events["current"]["last_name"]
    company = events["current"]["org_name"]
    job_title = events["current"]["b4a786a6de407992879deb06762f2d7b293daebd"]
    email = events["current"]["email"][0]["value"]
    contact_type = getContactType(events["current"]["0c00cb4578a2b32725c455869548899df69a3fb3"],pipedrive_api)
    program_interested_in = getProgramInterestedIn(events["current"]["c166ae40ccfde037d9cbaf0722c380511aea9c85"],pipedrive_api)
    marketing_opt_in = getMarketingOptIn(events["current"]["f5257f743ab8c87c2a67dac9413058ce8ac18951"],pipedrive_api)
    program_attended = getProgramAttended(events["current"]["15cecbf33424293b1c095ebe2bd1457447f74f63"],pipedrive_api)
    
    request_body = {
            "email" : email,
            "dataFields": {
                "first_name": first_name,
                "last_name": last_name,
                "company": company,
                "email": email,
                "job_title": job_title,
                "contact_type":contact_type,
                "program_interested_in":program_interested_in,
                "marketing_opt_in": marketing_opt_in,
                "program_attended":program_attended
                }
            }
    
    
    req = json.dumps(request_body)
    iterable_jwt = getJWT(secret_jwt,email)
    iterable_headers = {
            "Authorization": "Bearer"+" "+iterable_jwt,
            "Api-Key": iterable_api_key,
            "Content-Type": "application/json"
            }

    iterable_url = "https://api.iterable.com/api/users/update"

    createdUpdated = requests.post(url=iterable_url, data=req,headers=iterable_headers) 
    print(createdUpdated.text)

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
