import requests
from typing import Any, Dict, List

API_KEY = 'BHcPDHME/P3NrjiGFSXVzA==BdVL2dPvUZZBI54H'



def fetch_data(animal_name: str) -> List[Dict[str, Any]]:
    """
    Fetches the animals data for the animal 'animal_name'.

    Returns:
        List[Dict[str, Any]]: A list of animal dictionaries, each with 'name',
        'taxonomy', 'locations', and 'characteristics' keys.
    """
    api_url = f'https://api.api-ninjas.com/v1/animals?name={animal_name}'
    headers = {'X-Api-Key': API_KEY}
    response = requests.get(api_url, headers=headers)

    if response.status_code == requests.codes.ok:
        data = response.json()
        return data if data else []
    else:
        print("Error:", response.status_code, response.text)
        return []
