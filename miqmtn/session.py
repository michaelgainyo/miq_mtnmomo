import requests


def create_session(subscription_key=''):
    """
    Creates a new session with Ocp-Apim-Subscription-Key as subscription_key
    """

    session = requests.Session()
    session.headers.update({
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': subscription_key
    })
    return session
