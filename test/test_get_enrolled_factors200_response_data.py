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
from openapi_client.models.get_enrolled_factors200_response_data import GetEnrolledFactors200ResponseData  # noqa: E501
from openapi_client.rest import ApiException

class TestGetEnrolledFactors200ResponseData(unittest.TestCase):
    """GetEnrolledFactors200ResponseData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GetEnrolledFactors200ResponseData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetEnrolledFactors200ResponseData`
        """
        model = openapi_client.models.get_enrolled_factors200_response_data.GetEnrolledFactors200ResponseData()  # noqa: E501
        if include_optional :
            return GetEnrolledFactors200ResponseData(
                otp_devices = [
                    openapi_client.models.get_enrolled_factors_200_response_data_otp_devices_inner.getEnrolledFactors_200_response_data_otp_devices_inner(
                        active = True, 
                        default = False, 
                        state_token = 'f2402de2b446abd86ea5aa1f79b3fa72b4befacd', 
                        auth_factor_name = 'Onelogin SMS', 
                        phone_number = '+1xxxxxxxxxx', 
                        type_display_name = 'Onelogin SMS', 
                        needs_trigger = True, 
                        user_display_name = 'Rich's Phone', 
                        id = 525509, )
                    ]
            )
        else :
            return GetEnrolledFactors200ResponseData(
        )
        """

    def testGetEnrolledFactors200ResponseData(self):
        """Test GetEnrolledFactors200ResponseData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()