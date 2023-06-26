import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://alluvium-hq.atlassian.net/rest/api/3/project"

auth = HTTPBasicAuth("adeola@alluvium.net", "ATATT3xFfGF0NFKnwv7J87fT8UtDjqyFSEQgdAvpVDD1Zd5TQYvG1TcBaGlC7V1plLr0vF9Vy1DLDxNBxm49UXc-1_PTzL5NbKQaTNQc5MMuF4erCFtUV--EZoE5gPihLHoPfx4QKRChlWq7oVPJVCX4-ZB3Gkse2FVKWHgTKev6_6hWn7ITCFw=CA77B156")
headers = {
    "Accept": "application/json"
}

response = requests.get(url, headers=headers, auth=auth)

if response.status_code == 200:
    projects = json.loads(response.text)
    for project in projects:
        print(f"Project Key: {project['key']}")
        print(f"Project Name: {project['name']}")
        print("-----------------------------")
else:
    print("Failed to retrieve projects. Error:", response.status_code)
