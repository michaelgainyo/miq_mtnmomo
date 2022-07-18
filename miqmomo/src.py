import time
from pprint import pprint
from uuid import uuid4
import requests
from requests.auth import HTTPBasicAuth

# from .errors import *

SANDBOX_BASEURL = 'https://sandbox.momodeveloper.mtn.com/'
API_USER_URL = SANDBOX_BASEURL + 'v1_0/apiuser'
API_KEY_PATH = 'v1_0/apiuser/{apiuser_id}/apikey'

collection_apiusers = [
    '10ac74f1-2e4c-47c2-93a7-3b9067a6aff8'
]
# apiuser_id = 'a7eadcd7-ff5f-4b27-bb97-9ec60b575166'
apiuser_id = f'{uuid4()}'
apikey = '6a5e4d2d9dd044dea7601a8dc8557f52'
subscription_key = 'e50d0fabb3044afdba48f25815415136'


# ##############################################################################################
#                                          USER
# ##############################################################################################

#
# Create session
#


"""
Creates a new session with Ocp-Apim-Subscription-Key as subscription_key
"""

session = requests.Session()
session.headers.update({
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': subscription_key
})


#
# Create sandbox user
#


print('Creating api user, ', f'apiuser_id: "{apiuser_id}"')


"""
Create an API user in the sandbox target environment.
"""

create_user_data = {"providerCallbackHost": 'call back goes here'}
session.headers.update({'X-Reference-Id': f'{apiuser_id}', })

res = session.post(API_USER_URL, json=create_user_data)
try:
    res.raise_for_status()
except Exception as e:
    print(e)


assert res.status_code == 201


#
# Get sandbox user
#


"""
Get API user information
Sample response
{"providerCallbackHost": "astring","targetEnvironment": "sandbox"}
"""

res = session.get(API_USER_URL + f'/{apiuser_id}')
assert res.status_code == 200


#
# Create a new api key
#

"""
Create an API key for an API user in the sandbox target environment.
Returns a new key by successful request, and the new key invalidates
the previous one.

Sample response
{"apiKey": "46660e338d944c83a6fb18eefa60d4d7"}
"""

r = session.post(API_USER_URL + f'/{apiuser_id}/apikey')
r.raise_for_status()
assert r.status_code == 201
assert 'apiKey' in r.json().keys()

apiKey = r.json().get('apiKey')
print("created apiKey: ", apiKey)


# ##############################################################################################
#                                          COLLECTIONS
# ##############################################################################################


#
# Get new collection token
#

"""

Sample response
{
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSMjU2In0.eyJjbGllbnRJZCI6ImQ2NzliZjZhLWI1NTEtNDZlNS04Mzg2LTZhY2RmY2MxMmJlMiIsImV4cGlyZXMiOiIyMDIyLTA3LTE3VDE5OjI3OjExLjI0OCIsInNlc3Npb25JZCI6IjAxMjBlODczLWUyYTQtNGFlZS1hMDk2LTI3MTYxYTNhNGJjMyJ9.Hy2XkqwDBuJlFdBH4kx_knLlOlx5_brjyS6uM2UaTYghJ3eR5-LyLue8nM_9pxOp1Q6ewWTiRWp5fIIeVvy6Nl6NdliKbCaxSTf2-VhXtF_kfCr49ATFYX5phzk5mA7wVFhHE0Pur305lZ9giohffv9Lg0QsKodnbYyh1nzQJ9viepQuuuZZxVEdCOAFGFYeNh-9JkPgUFo5G92cArY-7t-3J9UdwnVuJ0sKnNXzal5r4YA3_vjPSoQtGJxmX6txoVaNykGZ-zwZPzEoqNtqsmT77BbaDd12tLe2oFoygbrTCkg9MDOnHLUEB-XW1SHKBgZ-o4gFmc54fNuMnENf3A",
    "token_type": "access_token",
    "expires_in": 3600
}
"""

r = session.post(
    'https://sandbox.momodeveloper.mtn.com/collection/token/',
    auth=HTTPBasicAuth(apiuser_id, apiKey)
)
r.raise_for_status()

assert r.status_code == 200
data = r.json()
assert 'access_token' in data.keys()

access_token = data.get('access_token')
print('Creating new collection token: Response')
# pprint(data)
print("access_token: ", access_token)
print("token_type: ", data.get('token_type'))
print("expires_in: ", data.get('expires_in'))


json_data = {
    "amount": "500",
    "currency": "EUR",
    "externalId": "123456789",
    "payer": {
        "partyIdType": "MSISDN",
        "partyId": "250784803644"
    },
    "payerMessage": "Thank you",
    "payeeNote": "note"
}


session.headers.update({
    'Authorization': f'Bearer {access_token}',
    'X-Target-Environment': 'sandbox',
    # 'X-Callback-Url ': callback_url,
})

print('Requesting to pay collection')
time.sleep(2)
r = session.post(
    'https://sandbox.momodeveloper.mtn.com/collection/v1_0/requesttopay',
    json=json_data,
)
r.raise_for_status()
assert r.status_code == 202
print('Collection paid\n')
