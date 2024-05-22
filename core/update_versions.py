import json
import requests

# Load the current data.json file
with open('data.json', 'r') as file:
    data = json.load(file)

# Function to get the latest version from GitHub
def get_latest_version(repo_url):
    api_url = repo_url.replace('github.com', 'api.github.com/repos').rstrip('.git') + '/releases/latest'
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json().get('tag_name')
    return None

# Update the versions
updated = False
for tool in data.values():
    latest_version = get_latest_version(tool['url'])
    if latest_version and latest_version != tool['version']:
        tool['version'] = latest_version
        updated = True

# Save the updated data.json file if there were any updates
if updated:
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)
