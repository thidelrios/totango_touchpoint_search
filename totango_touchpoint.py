import requests
import json
import time


#Creating all variables
API_TOKEN = "<Totango-Token>"
account_id = '<Totango-account-ID>'
success_flow = '<Totango-SuccessFlow>'

headers = {
    'app-token': API_TOKEN,
}

params = (
    ('account_id', account_id),
)


#Getting all touchpoints and tasks (from 'account_id' Timeline )
touchpoint = requests.get('https://app.totango.com/api/v2/events', headers=headers, params=params)
touchpoint_data = json.loads(touchpoint.content)

#Searching each individual Touchpoint and Task until the first defined 'success_flow' is found
for timeline_event in touchpoint_data:
    if timeline_event['properties']['activity_type_id'] == success_flow:
        #Gathers all notes from Touchpoint/Tasks, plus the epoch time (which is then converted to MM/DD/YYY)
        notes = timeline_event['note_content']['text']
        epoch = timeline_event['timestamp']
        date = time.strftime('%m-%d-%Y', time.localtime(epoch/1000))
        break
