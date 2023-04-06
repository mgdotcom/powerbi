# powerbi
Connect to Office 365 and get all powerbi License holders

This code first defines the Office 365 API endpoint and the API endpoint for retrieving users with Power BI licenses. It then defines the access token and headers for the API call, which you'll need to obtain from the Azure portal.

The code then makes the API call using the requests library and parses the JSON response to extract the user principal names. Finally, it prints the list of user principal names with Power BI licenses.

Note that you'll need to have the appropriate permissions and authentication set up in order to make this API call successfully. You may also need to adjust the API endpoint URL or the filter criteria depending on your specific requirements.


