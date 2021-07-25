from requests import Session
from uuid import uuid4

import requests
from .endpoints import SANDBOX_BASEURL


def create_sb_apiuser_apikey(apiuser_id: str, session: Session, base_url=SANDBOX_BASEURL):
    """
    Create an API key for an API user in the sandbox target environment.
    Returns a new key by successful request, and the new key invalidates
    the previous one.
    """

    base_url += f'v1_0/apiuser/{apiuser_id}/apikey'

    res = session.post(base_url)
    res.raise_for_status()
    return res


def get_sb_apiuser(apiuser_id: str, session: Session, base_url: str = SANDBOX_BASEURL):
    """get API user information"""

    base_url += f'v1_0/apiuser/{apiuser_id}'

    res = session.get(base_url)
    res.raise_for_status()
    return res


def create_sb_apiuser(session: Session, apiuser_id: str = f'{uuid4()}', callback_host: str = 'string', base_url: str = SANDBOX_BASEURL):
    """
    Create an API user in the sandbox target environment.
    """

    print()
    print(f'API User ID: ===> {apiuser_id} <===')
    print()

    base_url += 'v1_0/apiuser'
    data = {"providerCallbackHost": callback_host}

    session.headers.update({'X-Reference-Id': f'{apiuser_id}', })

    res = session.post(base_url, json=data)
    res.raise_for_status()
    return res

    # requests.post(url, headers=headers, params=params, json=data)
