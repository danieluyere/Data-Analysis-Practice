import requests
from pathlib import Path

def download_files(base_url: str, files_list: list[str], directory: Path) -> list[Path]:
    '''
    Download file from github if not already cached locally
    '''
    directory.mkdir(parents=True, exist_ok=True)
    
    file_paths = [] # the return object

    for file_name in files_list:
        destination = directory / file_name
        # strip / to eliminate inconsistent input
        url = f'{base_url.rstrip("/")}/{file_name}' 

        # only download file if file does not exist
        if not destination.exists():
            try:
                print(f'downloading {file_name}...')
                
                with requests.get(url, stream=True) as r:
                    r.raise_for_status() # check for HTTP errors
                    with open(destination, 'wb') as f:
                        # read and write the data in 1mb chunks
                        for chunk in r.iter_content(chunk_size=1024 * 1024):
                            f.write(chunk)
                print(f'{file_name} saved')
            except requests.exceptions.RequestException as err:
                print(f'failed to download {file_name}: {err}')
                continue
        else: print (f'{file_name} already exist')

        file_paths.append(destination)

    return file_paths