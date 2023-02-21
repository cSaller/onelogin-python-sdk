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
from openapi_client.models.get_invite_link200_response import GetInviteLink200Response  # noqa: E501
from openapi_client.rest import ApiException

class TestGetInviteLink200Response(unittest.TestCase):
    """GetInviteLink200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GetInviteLink200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetInviteLink200Response`
        """
        model = openapi_client.models.get_invite_link200_response.GetInviteLink200Response()  # noqa: E501
        if include_optional :
            return GetInviteLink200Response(
                status = openapi_client.models.generate_token_400_response.generateToken_400_response(
                    error = False, 
                    code = 200, 
                    type = 'Success', 
                    message = 'Success', ), 
                data = [
                    ''
                    ]
            )
        else :
            return GetInviteLink200Response(
        )
        """

    def testGetInviteLink200Response(self):
        """Test GetInviteLink200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()