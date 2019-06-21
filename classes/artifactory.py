import requests
import json

class artifactory():
    
    def __init__(self):
        pass
        
    def auth(self, url, **auth_data):
        self._session    = requests.session()
        self.url        = url
        auth_url        = self.url + '/artifactory/ui/auth/login'
   
        headers = {
                    'Content-Type': 'application/json',
                    } 
        try:
            payload = {
                        "user"      :"%s" % auth_data['auth'][0],
                        "password"  :"%s" % auth_data['auth'][1],
                        "type"      :"login"
                        }
       
        except KeyError as error:
            pass
                    
        auth = self._session.post(auth_url, headers=headers, data=json.dumps(payload)) 
        print(auth.json())

    def user_delete(self, username):

        user_delete_url = self.url + '/artifactory/ui/users/userDelete'

        headers = {
                    'Content-Type': 'application/json;charset=UTF-8',
                    }
        payload = {
                    "userNames":["%s" % username]
                    }

        user_delete = self._session.post(user_delete_url, headers=headers, data=json.dumps(payload)) 
        print(user_delete.json())

    def user_create(self, **account_data, *policy_data):

        user_create_url = self.url + '/artifactory/ui/users'
        headers = {
                    'Content-Type': 'application/json;charset=UTF-8',
                    }
        try:
            payload  = {"profileUpdatable"  : 'true',
                        "name"              : "%s" % account_data['username'],
                        "email"             : "%s" % account_data['email'],
                        "password"          : "%s" % account_data['password'],
                        "retypePassword"    : "%s" % account_data['password'],
                        }
            groupeNames = list() 

            for groupName in policy_data:
                groupeNames.append('{"groupName" : "%s", "realm" : "artifactory"}' % groupeNames)

            payload.update['userGroups'] = groupName

        except KeyError as error:
            pass

        user_create = self._session.post(user_create_url, headers=headers, data=json.dumps(payload)) 
        print(user_create.json())
