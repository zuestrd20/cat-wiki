import requests
import os
import json

# Notion Config
NOTION_KEY = open(os.path.expanduser("~/.config/notion/api_key")).read().strip()
DATABASE_ID = "df5887002d73458d810ae5597d3f7c66"

def fetch_pending_tasks():
    url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"
    headers = {
        "Authorization": f"Bearer {NOTION_KEY}",
        "Notion-Version": "2025-09-03",
        "Content-Type": "application/json"
    }
    # Filter for status "待處理"
    payload = {
        "filter": {
            "property": "狀態",
            "select": {
                "equals": "待處理"
            }
        }
    }
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        results = response.json().get("results", [])
        tasks = []
        for page in results:
            title_prop = page["properties"]["任務名稱"]["title"]
            if title_prop:
                tasks.append({
                    "id": page["id"],
                    "name": title_prop[0]["plain_text"]
                })
        return tasks
    return []

if __name__ == "__main__":
    pending = fetch_pending_tasks()
    if pending:
        print(f"FOUND_TASKS: {json.dumps(pending)}")
    else:
        print("NO_TASKS")
