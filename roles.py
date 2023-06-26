import os
import json
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

def get_project_roles(domain, auth, projectKey):
    url = f"{domain}/rest/api/latest/project/{projectKey}/role"
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers, auth=auth)
    resp = json.loads(response.text)
    return resp

def get_role_actors(domain, auth, roleId):
    url = f"{domain}/rest/api/latest/role/{roleId}/actors"
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers, auth=auth)
    resp = json.loads(response.text)
    print(resp)
    return resp

def delete_role_actor(domain, auth, projectKey, roleId, group):
    url = f"{domain}/rest/api/latest/project/{projectKey}/role/{roleId}/actors"
    query = {'group': group}
    response = requests.delete(url, params=query, auth=auth)
    print(response.text, response.status_code)

if __name__ == '__main__':
    load_dotenv()
    domain = os.getenv("URL")
    auth = HTTPBasicAuth(os.getenv("EMAIL"), os.getenv("API_TOKEN"))
    
    project_key = "project_keys_MRT.csv"
    roles = get_project_roles(domain, auth, project_key)
    print(roles)

    role_id = 10500
    get_role_actors(domain, auth, role_id)
