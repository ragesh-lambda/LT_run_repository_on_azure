import requests
import csv

# Define the URL and other payload data
url = "https://api.lambdatest.com/pdf/upload"
build_name = 'muktesh_7'

# Read the project tokens and other data from the CSV file
with open('project.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        project_token = row['projectToken']
        
        # Define the payload and files for the current project token
        payload = {'projectToken': project_token, 'buildName': build_name}
        files = [('pathToFiles', ('File1709202322476046.pdf', open('sample-pdf.pdf', 'rb'), 'application/pdf'))]
        headers = {}

        # Make the POST request for the current project token
        response = requests.post(url, headers=headers, data=payload, files=files)

        print(f"Project Token: {project_token}")
        print(response.text)
        print()
