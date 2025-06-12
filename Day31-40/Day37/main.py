import requests

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "iskdopgsbr48dm",
    "username": "foxdev",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(pixela_endpoint, json=user_params)
# print(response.text)