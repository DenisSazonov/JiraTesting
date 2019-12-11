import json
import os
import requests

BASE_URL = 'https://jira.hillel.it'
LOGIN_URL = BASE_URL + '/rest/gadget/1.0/login'


class Data:
    current_dir = os.path.abspath(os.path.dirname(__file__))
    with open(current_dir + '\credentials.json', 'r') as f:
        credentials = json.load(f)
    username = (credentials['user']['login'])
    password = (credentials['user']['password'])

    # def __init__(self):
    #     self.headers = {}
    #
    # def get_headers(self):
    #     result = requests.post(LOGIN_URL, json=Data.auth_json)
    #     cont_type = result.headers['Content-Type']
    #     cookie = result.headers['cookie']
    #     self.headers = {'content-type': cont_type,
    #                "cookie": cookie
    #                }
    #     return self.headers

    auth_json = {'username': username, 'password': password}

    create_issue_json = {
            "fields": {
                "project":
                    {
                        "key": "WEBINAR"
                    },
                "summary": "Test Summary",
                "description": "Creating of an issue",
                # "assignee": {"name": "webinar5"},
                "priority": {"name": "High"},
                "issuetype": {"name": "Bug"},
                "reporter": {
                    "name": "webinar5"
                }
            }
        }

#         asd = {
#    "fields":{
#       "project":{
#          "key":"Key"
#       },
#       "summary":"REST EXAMPLE",
#       "description":"Creating an issue via REST API",
#       "issuetype":{
#          "name":"Story"
#       },
#       "reporter":{
#          "self":"http://jiradev/rest/api/2/user?username=name",
#          "name":"name",
#          "emailAddress":"email@email.com",
#          "displayName":"Name",
#          "active":true
#       }
#    }
# }