import requests
import json

web_hook_url =  "https://hooks.slack.com/services/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"

def Inputs(id, Time, status):
	slack_msg = 'Alert ' + id + ' status is ' + status +' at time stamp ' + Time
	return slack_msg
	
Inputs('NewEdge', '3:00', 'Failed')

slack_msg = {'text':  Inputs('NewEdge', '3:00', 'Failed')}

requests.post(web_hook_url, data = json.dumps(slack_msg))