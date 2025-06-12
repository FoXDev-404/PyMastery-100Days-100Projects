import requests
from datetime import datetime

# -------------------- Pixela API Setup --------------------
pixela_endpoint = "https://pixe.la/v1/users"

USERNAME = "foxdev"  # Your Pixela username
TOKEN = "amnmfdasf5makodold"  # Your Pixela token
GRAPH_ID = "graph1"  # Graph ID to use

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# Uncomment to create a new user
# response = requests.post(pixela_endpoint, json=user_params)
# print(response.text)

# -------------------- Graph Setup --------------------
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "hours",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# Uncomment to create a new graph
# response = requests.post(graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# Link to the graph: https://pixe.la/v1/users/foxdev/graphs/graph1.html

# -------------------- Pixel Creation --------------------
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

# Take user input for date and quantity
print("Enter the date for the pixel (YYYYMMDD). Leave blank for today.")
input_date = input("Date: ").strip()
if not input_date:
    today = datetime.now()
    date_str = today.strftime("%Y%m%d")
else:
    date_str = input_date

quantity = input("Enter the number of hours coded today (e.g., 2.5): ").strip()

pixel_data = {
    "date": date_str,
    "quantity": quantity,
}

# Uncomment to create a new pixel
# response = requests.post(pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)

# -------------------- Pixel Update --------------------
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date_str}"

new_pixel_data = {
    "quantity": quantity  # Use the same input for update
}

# Uncomment to update a pixel
response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
print(response.text)

# -------------------- Pixel Delete --------------------
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date_str}"

# Uncomment to delete a pixel
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)