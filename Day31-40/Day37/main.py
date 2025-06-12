import requests

pixela_endpoint = "https://pixe.la/v1/users"

USERNAME = "foxdev"
TOKEN = "adasdas89fd0sdsr"
GRAPH_ID = "graph1"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(pixela_endpoint, json=user_params)
# print(response.text)


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

# response = requests.post(graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# Link to the graph: https://pixe.la/v1/users/foxdev/graphs/graph1.html

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

pixel_data = {
    "date": "20250612",
    "quantity": "1.9",
}

response = requests.post(pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)