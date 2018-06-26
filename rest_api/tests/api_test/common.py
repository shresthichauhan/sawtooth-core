# Copyright 2018 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ------------------------------------------------------------------------------

import pytest
import logging
import json
import urllib.request
import urllib.error
import base64
import argparse
import cbor
import sys

from sawtooth_intkey.intkey_message_factory import IntkeyMessageFactory
from sawtooth_intkey.client_cli.intkey_workload import do_workload


LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)
WAIT = 300


def get_blocks():
    response = query_rest_api('/blocks')
    return response['data']

def get_batches():
    response = query_rest_api('/batches')
    return response['data']

def get_batch(batch_id):
    response = query_rest_api('/batches/%s' % batch_id)
    return response['data']

def get_transactions():
    response = query_rest_api('/transactions')
    return response['data']

def get_transaction(transaction_id):
    response = query_rest_api('/transactions/%s' % transaction_id)
    return response['data']

def get_peer():
    response = query_rest_api('/peers')
    return response

def post_receipts(transaction_id, header=None, resourceid=None):
    headers={'content-type': 'application/json'}
    response = query_rest_api('/receipts', data=transaction_id, headers=headers)

    if resourceid == "NO_RESOURCE":
        #response['link']="http://localhost:8008/batch_statuses?id=d3424"
        #response = submit_request('{}&wait={}'.format(response['link'], WAIT))   
        response = query_rest_api('/receipts', data=transaction_id, headers=headers)
    return response['data']

def get_receipts():
    headers={'content-type': 'application/json'}
    response = query_rest_api('/receipts', headers=headers)
    return response
"""
def get_receipts(transaction_id):
    headers={'content-type': 'application/json'}
    response = query_rest_api('/receipts', data=transaction_id, headers=headers)
    return response
"""
def get_state_list():
    response = query_rest_api('/state')
    return response['data']

def get_state(address):
    response = query_rest_api('/state/%s' % address)
    return response

def post_batch(batch):
    headers = {'Content-Type': 'application/octet-stream'}
    response = query_rest_api(
        '/batches', data=batch, headers=headers)
    print(response)
    response = submit_request('{}&wait={}'.format(response['link'], WAIT))
    return response

def query_rest_api(suffix='', data=None, headers=None):
    if headers is None:
        headers = {}
    url = 'http://localhost:8008' + suffix
    return submit_request(urllib.request.Request(url, data, headers))

def submit_request(request):
    response = urllib.request.urlopen(request).read().decode('utf-8')
    return json.loads(response)

def make_batches(keys):
    imf = IntkeyMessageFactory()
    return [imf.create_batch([('set', k, 0)]) for k in keys]

def data_gen():
    with open("source.txt", mode = "r", encoding = "utf8") as f:
        return f.read()
