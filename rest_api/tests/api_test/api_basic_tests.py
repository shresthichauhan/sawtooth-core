from common import *
import pytest
MAX_BATCH_IN_BLOCK = 100

@pytest.fixture
def module():
    data_gen()
    block_list = get_blocks()
    return block_list

def test_rest_api_check_post_max_batches(module):
    """Tests that allow max post batches in block
    Handled max 100 batches post in block and handle for extra batch
    """
    block_list = module
    for batchcount, _ in enumerate(block_list, start=1):
        if batchcount == MAX_BATCH_IN_BLOCK:
            print("Max 100 Batches are present in Block") 
           

def test_rest_api_check_head_signature(module):
    """Tests that head signature of each batch of the block 
    should be not none 
    """
    block_list = module
    head_signature = [block['batches'][0]['header_signature'] for block in block_list]
    for i, _ in enumerate(block_list):
        head_sig = json.dumps(head_signature[i]).encode('utf8')
        assert head_signature[i] is not None, "Head signature is available for all batches in block"   

def test_rest_api_check_family_version(module):
    """Test batch transaction family version should be present 
    for each transaction header
    """
    block_list = module
    family_version = [block['batches'][0]['transactions'][0]['header']['family_version'] for block in block_list]
    for i, _ in enumerate(block_list):
        assert family_version[i] is not None, "family version present for all batches in block"

def test_rest_api_check_family_name(module):
    """Test batch transaction family name should be present
    for each tansaction header 
    """
    block_list = module
    family_name = [block['batches'][0]['transactions'][0]['header']['family_name'] for block in block_list]
    for i, _ in enumerate(block_list):
        assert family_name[i] == "intkey"

def test_rest_api_get_receipt(module):
    """Tests that get receipt operation with bad request 
    transaction id of batch thats part of block in block list
    """
    block_list = module
    batch_ids = [block['batches'][0]['header']['transaction_ids'] for block in block_list]
    for i, _ in enumerate(module):
        receipt_txn = json.dumps(batch_ids[i]).encode('utf8')
        size_data= post_receipts(receipt_txn)
        try:
            get_receipts()               
        except urllib.error.HTTPError as e:
            errdata = e.file.read().decode('utf8')
            assert (json.loads(errdata)['error']['code'])==83
            assert e.code == 400
        

def test_rest_api_check_input_output_content(module):
    """Test batch input and output content should be same for
    each batch and unique from other
    """
    block_list = module    
    txn_input = [block['batches'][0]['transactions'][0]['header']['inputs'][0] for block in block_list]
    txn_output = [block['batches'][0]['transactions'][0]['header']['outputs'][0] for block in block_list]
    if(txn_input == txn_output):
        return True

def test_rest_api_check_signer_public_key(module):
    """Tests that signer public key is calculated for a block
    properly
    """
    block_list = module    
    signer_public_key = [block['batches'][0]['header']['signer_public_key'] for block in block_list]
    assert signer_public_key is not None, "signer public key is available"

def test_rest_api_get_peer():
    """Tests that nodes will display in listing the peer
    nodes can be static and dynamically peered
    """
    batches = make_batches('&')
    get_peer()

def test_rest_api_post_receipt(module):
    """Tests that post receipt operation works properly with each 
    transaction id of batch thats part of block in block list
    """    
    block_list = module
    batch_ids = [block['batches'][0]['header']['transaction_ids'] for block in block_list]
    for i, _ in enumerate(module):
        receipt_txn = json.dumps(batch_ids[i]).encode('utf8')
        size_data= post_receipts(receipt_txn) 
