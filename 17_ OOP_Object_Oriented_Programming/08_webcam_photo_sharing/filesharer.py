"""This module defines a FileSharer class that uploads 
a file to a file-sharing service and returns a sharable link."""



import requests
from filestack import Client

class FileSharer:
    def __init__(self, filepath, api_key=None):
        self.filepath = filepath
        self.api_key = api_key

    def share(self):
        """Uploads the file using Filestack and returns the link."""
        try:
            # You'll need to get a free API key from https://www.filestack.com/
            client = Client(self.api_key or "YA8nIgbg1FSjaq233s5xhkz")
            filelink = client.upload(filepath=self.filepath)
            return filelink.url
        except Exception as e:
            print(f"An error occurred with Filestack: {e}")
            # Fallback to tempfile.io
            try:
                with open(self.filepath, 'rb') as f:
                    response = requests.post('https://tempfile.io/upload', files={"file": f})
                
                print(f"Status Code: {response.status_code}")
                print(f"Response Text: {response.text}")
                
                response.raise_for_status()
                return response.json().get('url')
            except (requests.exceptions.HTTPError, requests.exceptions.JSONDecodeError) as e:
                print(f"An error occurred with fallback service: {e}")
                return f"Error: Could not upload file. Status: {response.status_code}"