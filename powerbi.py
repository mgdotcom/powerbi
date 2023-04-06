import requests
import json

# Define the Office 365 API endpoint
api_url = "https://graph.microsoft.com/v1.0"

# Define the API endpoint for retrieving users with Power BI licenses
powerbi_license_url = api_url + "/users?$filter=assignedLicenses/any(x:x/skuId eq 'b05e124f-c7cc-45a0-a6aa-8cf78c946968')&$select=userPrincipalName"

# Define the access token for the API call (you'll need to get this from the Azure portal)
access_token = "YOUR_ACCESS_TOKEN_HERE"

# Define the headers for the API call
headers = {
    "Authorization": "Bearer " + access_token,
    "Accept": "application/json"
}

# Make the API call to retrieve users with Power BI licenses
response = requests.get(powerbi_license_url, headers=headers)

# Parse the JSON response and extract the user principal names
users = json.loads(response.text)
user_principal_names = [user["userPrincipalName"] for user in users["value"]]

# Print the list of user principal names with Power BI licenses
print(user_principal_names)
