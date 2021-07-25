from uuid import uuid4

from miqmtn.session import create_session
from miqmtn.sandbox_user import (
    create_sb_apiuser_apikey, get_sb_apiuser,
    create_sb_apiuser
)
from miqmtn.collections import (
    request_to_pay_collection, get_collection_token
)


collection_apiusers = [
    '10ac74f1-2e4c-47c2-93a7-3b9067a6aff8'
]
apiuser_id = 'a7eadcd7-ff5f-4b27-bb97-9ec60b575166'
apikey = '6a5e4d2d9dd044dea7601a8dc8557f52'
subscription_key = 'e50d0fabb3044afdba48f25815415136'
session = create_session(subscription_key=subscription_key)


def test_request_to_pay_collection():
    # r = get_collection_token(.apiuser_id, .apikey, .session)
    # collection_token = r.json()['access_token']
    collection_token = (
        'eyJ0eXAiOiJKV1QiLCJhbGciOiJSMjU2In0.eyJjbGllbnRJZCI6ImE3ZWFkY2'
        'Q3LWZmNWYtNGIyNy1iYjk3LTllYzYwYjU3NTE2NiIsIm'
        'V4cGlyZXMiOiIyMDIxLTA3LTIxVDEyOjQ4OjQ'
        '4Ljk4OSIsInNlc3Npb25JZCI6IjEzNmU1MzgzL'
        'WU3M2QtNDlhOC1hN2QzLWM4ZTdhZWMyODQyMCJ9.'
        'T8NrlNkppOmT1U0uJfTpTqwcuNlCgvyUeYq'
        's8xJEGPxQyq8qxENgckN5WI1dwN546sdij9A'
        'o-qVZ2XxWO7KA-E58ac_uU5on4rGVDNwaG13l04'
        '8OJZia732ZrtzVj1tDZCMmW7y-8mB9dvkY2USRvLQZqt5VC7MCbmKw9_jc-WtVYWQK'
        'obD2q-i5WKUtr5MJBi98outEG1RshUbBwIHwFzqzqn3cuxF3FpV07ZpiV4-_'
        '3hOxTo0RC_70s-GOYkyns05NU1WDDy-WZt5QCdunry5YWUgfVyKTTklRvHEr'
        'C255Kp1KXAJnZ7QBUA_OkecWooSLEYQhT-PA_wDwGq83Tg')

    data = {
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

    transaction_id = f'{uuid4()}'

    r = request_to_pay_collection(
        apiuser_id, collection_token, data,
        session, transaction_id=transaction_id)

    assert r.status_code == 202
    # data = r.json()

    print(data)


def test_get_collection_token():
    r = get_collection_token(apiuser_id, apikey, session)
    assert r.status_code == 200
    data = r.json()
    assert 'access_token' in data.keys()
    print("access_token", data.get('access_token'))
    print(data)


def test_create_sb_apiuser_apikey():
    r = create_sb_apiuser_apikey(apiuser_id, session)
    assert r.status_code == 201
    assert 'apiKey' in r.json().keys()
    print("apiKey", r.json().get('apiKey'))


def test_get_sb_apiuser():
    # {'providerCallbackHost': 'string', 'targetEnvironment': 'sandbox'}

    r = get_sb_apiuser(apiuser_id, session)
    assert r.status_code == 200


def test_create_sb_apiuser():
    r = create_sb_apiuser(session)
    assert r.status_code == 201
