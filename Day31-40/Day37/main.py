import requests

pixela_endpoint = "https://pixe.la/v1/users"

USERNAME = "foxdev"
TOKEN = "asdaskj4kljk8dkj"

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

response = requests.post(graph_endpoint, json=graph_config, headers=headers)
print(response.text)

# Link to the graph: https://pixela.v1/users/foxdev/graphs/graph1.html