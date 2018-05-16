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

from sawtooth_intkey.intkey_message_factory import IntkeyMessageFactory
from sawtooth_intkey.client_cli.intkey_workload import do_workload


from sawtooth_sdk.protobuf.batch_pb2 import Batch
from sawtooth_sdk.protobuf.batch_pb2 import BatchList
from sawtooth_sdk.protobuf.batch_pb2 import BatchHeader

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

def test_rest_api_post_batch():
    """Tests that transactions are submitted and committed for
    each block that are created by submitting intkey batches
    """
    LOGGER.info('Starting test for batch post')
    LOGGER.info("Creating batches")
    batches = make_batches('abcd')
    print("++++++++++++++++++POST BATCH TESSSTTTT+++++++++++++++++++")
    LOGGER.info("Submitting batches to the handlers")
    initial_state_length = len(get_state_list())
    
    for i, batch in enumerate(batches):
        response = post_batch(batch)
        block_list = get_blocks()
