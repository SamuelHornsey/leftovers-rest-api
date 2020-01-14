'''
API proxy for leftovers application

@author Samuel Hornsey
@email me@samuelhornsey.com
'''
# Modules
import json
import logging
import os

import requests

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)

# Get API key
API_URL = 'https://api.spoonacular.com'
API_KEY = os.environ['API_KEY']

__author__ = 'Samuel Hornsey'


def make_url(path, params):
    '''
    Make the url
    '''
    if not params:
        return f'{API_URL}{path}?apiKey={API_KEY}'

    query = ''

    for key, val in params.items():
        query += f'{key}={val}&'

    return f'{API_URL}{path}?{query}apiKey={API_KEY}'


def handler(*args):
    '''
    Event handler function
    '''
    event = args[0]

    # separate params
    params = event.get('queryStringParameters')
    method = event.get('httpMethod')
    path = event.get('path')

    LOGGER.info(params)

    # get url
    url = make_url(path, params)

    LOGGER.info(url)

    req = requests.request(
        method,
        url
    )

    return {
        "statusCode": req.status_code,
        "body": json.dumps(req.json())
    }
