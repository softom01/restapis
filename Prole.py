import requests
import json

url = "https://your-domain.atlassian.net/rest/api/3/project/{projectIdOrKey}/role"
email = "email@example.com"
api_token = "<api_token>"

headers = {
    "Accept": "application/json"
}

response = requests.get(url, headers=headers, auth=(email, api_token))

if response.status_code == 200:
    roles = response.json()
    formatted_roles = json.dumps(roles, sort_keys=True, indent=4, separators=(",", ": "))
    print(formatted_roles)
else:
    print("Failed to retrieve project roles. Error:", response.status_code)
