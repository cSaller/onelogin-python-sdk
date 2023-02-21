# coding: utf-8

"""
    OneLogin API

    OpenAPI Specification for OneLogin  # noqa: E501

    The version of the OpenAPI document: 3.1.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.models.get_event_types200_response import GetEventTypes200Response  # noqa: E501
from openapi_client.rest import ApiException

class TestGetEventTypes200Response(unittest.TestCase):
    """GetEventTypes200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GetEventTypes200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetEventTypes200Response`
        """
        model = openapi_client.models.get_event_types200_response.GetEventTypes200Response()  # noqa: E501
        if include_optional :
            return GetEventTypes200Response(
                status = openapi_client.models.generate_token_400_response.generateToken_400_response(
                    error = False, 
                    code = 200, 
                    type = 'Success', 
                    message = 'Success', ), 
                data = [
                    openapi_client.models.get_event_types_200_response_data_inner.getEventTypes_200_response_data_inner(
                        name = 'APP_REMOVED_FROM_ROLE', 
                        description = 'App %app% removed from role %role%', 
                        id = 2, )
                    ]
            )
        else :
            return GetEventTypes200Response(
        )
        """

    def testGetEventTypes200Response(self):
        """Test GetEventTypes200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()