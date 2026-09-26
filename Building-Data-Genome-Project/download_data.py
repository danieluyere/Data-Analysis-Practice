from pathlib import Path
import requests

# define path
data_folder = Path('data') / 'git_data'
data_folder.mkdir(parents=True, exist_ok=True)

# load building meta data, energy consumption and weather data from github
base_url = 'https://media.githubusercontent.com/media/buds-lab/building-data-genome-project-2/refs/heads/master/data'

# sub-urls for files
files = {
    'metadata.csv': f'{base_url}/metadata/metadata.csv',
    'electricity.csv': f'{base_url}/meters/cleaned/electricity_cleaned.csv',
    'weather.csv': f'{base_url}/weather/weather.csv'
        }

for file_name, url in files.items():
    destination = data_folder / file_name

    # only download files if it does not exist
    if not destination.exists():
        try:
            r = requests.get(url)
            r.raise_for_status()
            destination.write_bytes(r.content)
            print(f'{file_name} saved')
        except requests.exceptions.RequestException as err:
            print(f'Request error: {err}')
    else: print(f'{destination.name} exists')