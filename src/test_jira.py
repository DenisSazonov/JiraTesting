import requests
import json
from .data import Data

BASE_URL = 'https://jira.hillel.it'
LOGIN_URL = BASE_URL + '/rest/gadget/1.0/login'
CREATE_ISSUE_URL = BASE_URL + '/rest/api/2/issue'
EDIT_ISSUE_URL = BASE_URL + ':8081/rest/api/2/issue/WEBINAR-10058/comment'


class WorkingWithIssues:
    def get_issue(self, issue_id):
        pass

    def add_issue(self, issue_id):
        pass

    def edit_issue(self, issue_id):
        pass

    def delete_issue(self, issue_id):
        pass


class TestAuthentification(Data):
    def test_authentification(self):
        result = requests.post(LOGIN_URL, json=Data.auth_json)
        print(result.text)
        assert 200 == result.status_code
        print(result.text)

    def test_create_issue(self):
        result = requests.post(LOGIN_URL, json=Data.auth_json)
        cont_type = result.headers['Content-Type']
        cookie = result.headers['cookies']
        headers = {'content-type': cont_type,
                   'cookie': cookie
                   }
        result = requests.post(CREATE_ISSUE_URL, json=Data.create_issue_json,
                               headers=headers)
        print(result.text)
        assert 200 == result.status_code
        print(result.text)
        # assert result.json()

    def test_edit_issue(self):
        result = requests.get('http://jira.hillel.it:8080',
                              auth=('webinar2', 'webinar2'))
        print(result)
        assert 200 == result.status_code
        cookie = {'JSESSIONID': result.cookies.get("JSESSIONID")}

    def test_recreate_issue(self):
        result = requests.get('http://jira.hillel.it:8080',
                              auth=('webinar2', 'webinar2'))
        print(result)
        assert 200 == result.status_code
        cookie = {'JSESSIONID': result.cookies.get("JSESSIONID")}

        json_for_edit_issue = {
            "body": "This is a comment regarding the quality of the response."
        }
        result = requests.post(EDIT_ISSUE_URL,
                               json=json_for_edit_issue,
                               headers={'Content-Type': 'application/json'},
                               cookies=cookie)
        print(result)
        assert 201 == result.status_code
