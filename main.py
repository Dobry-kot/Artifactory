from classes.artifactory import user*
import os, yaml

if __name__ == "__main__":
    
    PWD = os.getenv("HOME")
  
    with open("%s/.python_auth_cfg.yml" % PWD, 'r') as auth:

        auth_conf = yaml.load(auth, Loader=yaml.FullLoader)

    artifactory_conf            = auth_conf['artifactory']
    artifactory_admin_user      = artifactory_conf['admin_user']
    artifactory_admin_password  = artifactory_conf['admin_password']
    artifactory_basic_url       = artifactory_conf['artifactory_url']

    """gropePolicy = ['read', 'writhe']"""
    username    = ''
    email       = ''
    password    = ''
    gropePolicy = ['']

    artifactory = artifactory()
    artifactory.auth(artifactory_basic_url, auth=(artifactory_admin_user, artifactory_admin_password))
    artifactory.user_create(username = username, email = email, password = password)