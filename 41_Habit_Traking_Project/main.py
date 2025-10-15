import requests
import os
from dotenv import load_dotenv
from datetime import datetime
load_dotenv()


pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": os.getenv("PIXELA_API_TOKEN"),
    "username": os.getenv("PIXELA_USERNAME"),
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}


# response = requests.post(pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{os.getenv('PIXELA_USERNAME')}/graphs"

graph_config = {
    "id": os.getenv("PIXELA_GRAPH_ID"),
    "name": "Python daily coding",
    "unit": "days",
    "type": "int",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": os.getenv("PIXELA_API_TOKEN")
}

# First, let's create the user account (if it doesn't exist)
print("Creating user account...")
response = requests.post(pixela_endpoint, json=user_params)
print(f"User creation response: {response.status_code} - {response.text}")

# Then create/update the graph
print("\nCreating/updating graph...")
response = requests.post(graph_endpoint, json=graph_config, headers=headers)
print(f"Graph creation response: {response.status_code} - {response.text}")

# If graph already exists, update it instead
if response.status_code == 409:  # Conflict - graph already exists
    print("\nGraph already exists, updating instead...")
    update_graph_endpoint = f"{pixela_endpoint}/{os.getenv('PIXELA_USERNAME')}/graphs/{os.getenv('PIXELA_GRAPH_ID')}"
    
    # Retry logic for 503 errors (rate limiting)
    max_retries = 3
    for attempt in range(max_retries):
        response = requests.put(update_graph_endpoint, json=graph_config, headers=headers)
        print(f"Graph update attempt {attempt + 1}: {response.status_code} - {response.text}")
        
        if response.status_code == 503:
            print(f"Rate limited (503), retrying in 2 seconds... (attempt {attempt + 1}/{max_retries})")
            import time
            time.sleep(2)
        else:
            break
    else:
        print("Failed to update after all retries due to rate limiting.")

# Let's also check if we can retrieve the graph
print("\nChecking if graph exists...")
get_graph_endpoint = f"{pixela_endpoint}/{os.getenv('PIXELA_USERNAME')}/graphs/{os.getenv('PIXELA_GRAPH_ID')}"
response = requests.get(get_graph_endpoint, headers=headers)
print(f"Graph retrieval response: {response.status_code} - {response.text}")

# Print the URL that should work
print(f"\nYour graph should be viewable at: https://pixe.la/v1/users/{os.getenv('PIXELA_USERNAME')}/graphs/{os.getenv('PIXELA_GRAPH_ID')}.html")

# Update today's pixel

pixel_configuration = {
    "date": datetime.now().strftime("%Y%m%d"),
    "quantity": input("How many lines you coded today?")  # e.g., "1" for one day
}

header_pixel = {
    "X-USER-TOKEN": os.getenv("PIXELA_API_TOKEN")
}

update_pixel_endpoint = f"{pixela_endpoint}/{os.getenv('PIXELA_USERNAME')}/graphs/{os.getenv('PIXELA_GRAPH_ID')}"
response = requests.post(update_pixel_endpoint, json=pixel_configuration, headers=header_pixel)
print(f"\nPixel update response: {response.status_code} - {response.text}")

#Update a specific day
date = "20250615"
update_pixel_configuration = {
    "quantity": "10"
}       
update_specific_pixel_endpoint = f"{pixela_endpoint}/{os.getenv('PIXELA_USERNAME')}/graphs/{os.getenv('PIXELA_GRAPH_ID')}/{date}"
response = requests.put(update_specific_pixel_endpoint, json=update_pixel_configuration, headers=header_pixel)
print(f"\nSpecific Pixel update response: {response.status_code} - {response.text}")

# #Delete a specific day
# date = "20251013"
# delete_specific_pixel_endpoint = f"{pixela_endpoint}/{os.getenv('PIXELA_USERNAME')}/graphs/{os.getenv('PIXELA_GRAPH_ID')}/{date}"   
# response = requests.delete(delete_specific_pixel_endpoint, headers=header_pixel)
# print(f"\nSpecific Pixel deletion response: {response.status_code} - {response.text}")

