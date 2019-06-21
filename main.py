import os, yaml

from classes.artifactory import artifactory


if __name__ == "__main__":
    
    PWD = os.getenv("HOME")
  
    with open("%s/.python_auth_cfg.yml" % PWD, 'r') as auth:

        auth_conf = yaml.load(auth, Loader=yaml.FullLoader)

    artifactory_conf            = auth_conf['artifactory']
    artifactory_admin_user      = artifactory_conf['admin_user']
    artifactory_admin_password  = artifactory_conf['admin_password']
    artifactory_basic_url       = artifactory_conf['artifactory_url']

    """gropePolicy = ['read', 'writhe']"""
    usernames_delete    = ['ttestovich' , 'ttestov'] # for delete user(s) variable is list
    gropePolicy         = ['readers', 'writers']   
    username_create     = 'ttestovich'               # for create user variable is str
    email               = 'ttestovich@mail.ru'
    password            = 't4too7a'
    
    # init artifactory
    artifactory = artifactory()
    # authorization in artifactory
    artifactory.auth(artifactory_basic_url, auth=(artifactory_admin_user, artifactory_admin_password))
    # create new user
    artifactory.user_create(username = username_create, email = email, password = password, gropePolicy = gropePolicy)
    # delete old user(s)
    # artifactory.user_delete(usernames_delete)