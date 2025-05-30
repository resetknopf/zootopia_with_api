import requests

name = 'baum'
api_url = 'https://api.api-ninjas.com/v1/animals?name={}'.format(name)
response = requests.get(api_url, headers={'X-Api-Key': 'BHcPDHME/P3NrjiGFSXVzA==BdVL2dPvUZZBI54H'})
if response.status_code == requests.codes.ok:
    print(response.json())
else:
    print("Error:", response.status_code, response.text)