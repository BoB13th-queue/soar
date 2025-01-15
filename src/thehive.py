import requests
import json
import warnings
from urllib3.exceptions import InsecureRequestWarning

# Optional: Disable only the single warning from urllib3 (development use only)
warnings.simplefilter('ignore', InsecureRequestWarning)

THEHIVE_URL = "https://localhost/thehive"
API_KEY = "S+v8oDBhWrfFCCAFzhEeAfumsPzLYfOd"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    "X-Organisation": "bob"
}

endpoint = "/api/v1/case"

payload = {
    "title": "string",
    "description": "string",
    "severity": 1,
    "startDate": 1640000000000,
    "endDate": 1640000000000,
    "tags": ["string"],
    "flag": False,
    "tlp": 0,
    "pap": 0,
    "status": "InProgress",
    "summary": "string",
    "assignee": "tomorrow9913@gmail.com",
    "customFields": {
        "property1": None,
        "property2": None
    },
    "caseTemplate": "악성 이메일",
    "tasks": [
        {
            "title": "string",
            "group": "string",
            "description": "string",
            "status": "InProgress",
            "flag": True,
            "startDate": 1640000000000,
            "endDate": 1640000000000,
            "order": 0,
            "dueDate": 1640000000000,
            "assignee": "tomorrow9913@gmail.com",
            "mandatory": True
        }
    ],
    "pages": [
        {
            "title": "string",
            "content": "string",
            "order": 0,
            "category": "string"
        }
    ],
    "sharingParameters": [
        {
            "organisation": "bob",
            "share": True,
            "profile": "analyst",
            "taskRule": "Sharing rule applied on the case",
            "observableRule": "Sharing rule applied on the case"
        }
    ],
    "taskRule": "string",
    "observableRule": "string"
}

# POST to create a new case
response = requests.post(
    f"{THEHIVE_URL}{endpoint}",
    headers=headers,
    json=payload,           # Use 'json' instead of 'data'
    verify=False            # For development only
)

if response.status_code == 201:
    print("Case created successfully!")
    print(response.json())
else:
    print(f"Failed to create case. Status code: {response.status_code}")
    print("Error:", response.text)
