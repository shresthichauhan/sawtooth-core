import pytest
import logging
import json
import urllib.request
import urllib.error
  
from fixtures import setup
from utils import get_state_list
 
from base import RestApiBaseTest
state_address = 70

class TestStateList(RestApiBaseTest):
    """This class tests the state list with different parameters
    """
    def test_api_get_state_data_address_prefix_namespace(self, setup):
        """Tests the state data address with 6 hex characters long 
        namespace prefix
        """   
        try:   
            for state in get_state_list()['data']:
                #Access each address using namespace prefix
                namespace = state['address'][:6]
                get_state_list(address=namespace)
        except urllib.error.HTTPError as error:
            LOGGER.info("Not able to access related state address using namespace prefix")
            
            
    def test_api_get_state_data_address_length(self, setup):
        """Tests the state data address length is 70 hex character long
        with proper prefix namespace
        """   
        try:
            response = get_state_list()   
            for state in get_state_list()['data']:
                #Access each address using of state
                address = len(response['data'][0]['address'])
        except urllib.error.HTTPError as error:
            LOGGER.info("State address is not 70 character long")        
        assert address == state_address
        
        
    def test_api_get_state_data_address_with_odd_hex_value(self, setup):
        """Tests the state data address fail with odd hex character 
        address 
        """   
        try:
            response = get_state_list()   
            for state in get_state_list()['data']:
                #Access each address using of state
                address = len(response['data'][0]['address'])
                if(address%2 == 0):
                    pass
        except urllib.error.HTTPError as error:
            LOGGER.info("Odd state address is not correct")
            
    def test_api_get_state_data_address_with_reduced_length(self, setup):
        """Tests the state data address with reduced even length hex character long 
        """   
        try:
            response = get_state_list()   
            for state in get_state_list()['data']:
                #Access each address using of state
                address = response['data'][0]['address']
                nhex = address[:-4]
                get_state_list(address = nhex)
        except urllib.error.HTTPError as error:
            LOGGER.info("Reduced length data address failed to processed")        
            
                    
    def test_api_get_state_data_address_64_Hex(self, setup):
        """Tests the state data address with 64 hex give empty data 
        """   
        try:
            response = get_state_list()   
            for state in get_state_list()['data']:
                #Access each address using of state
                address = response['data'][0]['address']
                nhex = address[6:70]
                naddress = get_state_list(address = nhex)
                assert naddress['data'] == []
        except urllib.error.HTTPError as error:
            LOGGER.info("state data address with 64 hex characters not processed ")        
                    
                    
    def test_api_get_state_data_address_alter_bytes(self, setup):
        """Tests the state data address with alter bytes give empty data 
        """   
        try:
            response = get_state_list()   
            for state in get_state_list()['data']:
                #Access each address using of state
                address = response['data'][0]['address']
                nhex = address[6:8]
                naddress = get_state_list(address = nhex)
                assert naddress['data'] == []
        except urllib.error.HTTPError as error:
            LOGGER.info("state data address with altered bytes not processed ")        
                            
        
    
             
