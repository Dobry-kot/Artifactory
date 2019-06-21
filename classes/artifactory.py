import requests
import json
import copy

class artifactory():
    DEFAULTS_OPTIONS = { 
                         'headers' :  {
                                        'Content-Type' : 'application/json;charset=UTF-8'
                                       }
                         }   

    def __init__(self):
        self._options = copy.copy(artifactory.DEFAULTS_OPTIONS)
        
    def auth(self, url, **auth_data):
        self._session   = requests.session()
        self.url        = url
        auth_url        = self.url + '/artifactory/ui/auth/login'
   
        self._options['headers']['Content-Type'] = 'application/json'

        try:
            payload = {
                        "user"      :"%s" % auth_data['auth'][0],
                        "password"  :"%s" % auth_data['auth'][1],
                        "type"      :"login"
                        }
       
        except KeyError as error:
            pass
                    
        auth = self._session.post(auth_url, 
                                  headers = self._options['headers'], 
                                  data    = json.dumps(payload)) 

        if auth.status_code == 200:
            return True

        else:
            print(auth.json())

    def user_delete(self, *usernames):
        
        user_delete_url = self.url + '/artifactory/ui/users/userDelete'

        self._options['headers']['Content-Type'] = 'application/json;charset=UTF-8'
        
        try:
            
            payload = {
                    "userNames": usernames[0]
                    }

            user_delete = self._session.post(user_delete_url, 
                                             headers = self._options['headers'], 
                                             data    = json.dumps(payload))
            print(user_delete.json())
            
        except KeyError and TypeError as error:
            print('Error:artifactory.user_delete <%s>' % error) 

    def user_create(self, **account_data):
        user_create_url = self.url + '/artifactory/ui/users'

        try:
            payload  = {"profileUpdatable"  : "true",
                        "name"              : "%s" % account_data['username'],
                        "email"             : "%s" % account_data['email'],
                        "password"          : "%s" % account_data['password'],
                        "retypePassword"    : "%s" % account_data['password'],
                        }
            groupNames = list() 
 
            for groupName in account_data['gropePolicy']:
                groupNames.append({"groupName" : "%s" % groupName, "realm" : "artifactory" } )

            payload['userGroups'] = groupNames
            
        except KeyError and TypeError as error:
            print(error)

        user_create = self._session.post(user_create_url,
                                         headers    =self._options['headers'], 
                                         data       =json.dumps(payload)) 
        if user_create.status_code == 200:
            return True
        
        else:
            print(user_create.json())
