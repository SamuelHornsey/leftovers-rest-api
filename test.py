# modules
import unittest
import json
from unittest.mock import patch

# handler
from main import handler, make_url

# data
EVENT = {
  'queryStringParameters': {
    'ingredients': 'avocado,sugar'
  },
  'path': '/test',
  'method': 'GET'
}

CONTEXT = {}

class TestHandler(unittest.TestCase):
  def setUp (self):
    '''
    Setup test case
    '''
    self.evt = EVENT
    self.cxt = CONTEXT

  def test_make_url (self):
    '''
    Test making the url
    '''
    path = '/test'
    params = {
      'ingredients': 'avocado,sugar',
      'query': 'value'
    }
    url = make_url(path, params)

    self.assertEqual(url, 'https://api.spoonacular.com/test?ingredients=avocado,sugar&query=value&apiKey=DUMMY_KEY')

    # None params
    params = None
    url = make_url(path, params)

    self.assertEqual(url, 'https://api.spoonacular.com/test?apiKey=DUMMY_KEY')

    # Empty params
    params = {}
    url = make_url(path, params)

    self.assertEqual(url, 'https://api.spoonacular.com/test?apiKey=DUMMY_KEY')

  @patch('main.requests.request')
  def test_handler (self, mock):
    '''
    Test the request handler
    '''
    mock.return_value.status_code = 200
    mock.return_value.json.return_value = {}

    res = handler(self.evt, self.cxt)

    self.assertEqual(res['statusCode'], 200)
    self.assertEqual(res['body'], json.dumps({}))

  @patch('main.requests.request')
  def test_err (self, mock):
    '''
    Test request error handling
    '''
    mock.stats_code = 500
    mock.return_value.json.return_value = {}

    res = handler({}, self.cxt)