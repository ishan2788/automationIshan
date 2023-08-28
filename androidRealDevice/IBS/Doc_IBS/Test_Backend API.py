import requests


GHOST_TOKEN = '6d86763b067ec953a49ddbd950e3c6a4'


url = "https://eu-prod.cara.care/v1/clinical-trials/qa-access-code/"
url_stg = "https://eu-staging.cara.care/v1/clinical-trials/qa-access-code/"

json_body = {"study_name": "Test doctors – IBS"}
response = requests.post(url, headers={'Ghost-Token': GHOST_TOKEN}, json=json_body).json()
access_code = response['access_code']
print(access_code)

# json_body = {"access_token": "6d86763b067ec953a49ddbd950e3c6a4", "study_name": "Test doctors – IBS"}
# response = requests.post(url_stg, json=json_body).json()
# access_code = response['access_code']
# print(access_code)
