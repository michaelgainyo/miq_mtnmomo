
from uuid import uuid4
import requests
from requests.auth import HTTPBasicAuth
from .endpoints import SANDBOX_BASEURL


SUB_PRIMARY_KEY = 'e50d0fabb3044afdba48f25815415136'
SUB_SEC_KEY = '31b3840f16f140b8ab10403af94ef732'

base_headers = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': SUB_PRIMARY_KEY,
}


"""
REF that worked
84f47572-4e61-48c0-86d1-13ab4023a2fb
0da9f9dc-b413-41f5-87aa-55fa02c30237
"""


def request_to_pay_collection(
        apiuser_id: str, collection_token: str,
        data: dict,  session: requests.Session,
        transaction_id=f'{uuid4()}',
        callback_url='', env='sandbox',
        base_url=SANDBOX_BASEURL):
    """
    """

    base_url += f'collection/v1_0/requesttopay'
    session.headers.update({
        'Authorization': 'Bearer ' + collection_token,
        'X-Reference-Id': transaction_id,
        # 'X-Reference-Id': apiuser_id,
        # 'X-Callback-Url ': callback_url,
        'X-Target-Environment': env,
        # 'Content-Type': 'application/x-www-form-urlencoded'
    })
    del session.headers['user-agent']
    # session.auth = HTTPBasicAuth(apiuser_id, collection_token)

    res = session.post(
        base_url,
        # json=data,
        data=data,
        # data=json.dumps(data).encode('ascii')
        # auth=HTTPBasicAuth(apiuser_id, collection_token)
    )
    print()
    print(session.headers.__dict__)
    print()
    print(res.__dict__)
    print()

    res.raise_for_status()
    return res


def get_collection_token(
        user_id: str, api_key: str, session: requests.Session,
        base_url=SANDBOX_BASEURL):
    """
    Valid 1 hour in sandbox
    """

    base_url += 'collection/token/'

    res = session.post(base_url, auth=HTTPBasicAuth(user_id, api_key))
    res.raise_for_status()
    return res


#
# OAUTH2
#


def get_user_info_oauth2(token):
    """
    """

    url = f'collection/oauth2/v1_0/userinfo'
    headers = {
        **base_headers,
        'Authorization': f'Bearer {token}',
        'X-Target-Environment': 'sandbox'
    }

    res = requests.get(url, headers=headers)
    res.raise_for_status()
    return res


def get_token_oauth2(user_id, api_key):
    """
    """

    url = f'collection/oauth2/token/'
    headers = {
        **base_headers,
        'Content-Type': 'application/x-www-form-urlencoded',
        'X-Target-Environment': 'sandbox'
    }
    data = 'grant_type=urn:openid:params:grant-type:ciba&auth_req_id={auth_req_id}'
    res = requests.post(
        url, data=data, headers=headers,
        auth=(user_id, api_key)
    )
    res.raise_for_status()
    return res


def login_oauth2(user_id, api_key):
    """
    """

    url = f'collection/v1_0/bc-authorize'
    headers = {
        **base_headers,
        'Content-Type': 'application/x-www-form-urlencoded',
        'X-Target-Environment': 'sandbox'
    }
    data = 'grant_type=urn:openid:params:grant-type:ciba&auth_req_id={auth_req_id}'
    res = requests.post(
        url, data=data, headers=headers,
        auth=(user_id, api_key)
    )
    res.raise_for_status()
    return res


#
#
#
