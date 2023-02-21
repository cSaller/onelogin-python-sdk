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
from openapi_client.models.create_brand201_response_background import CreateBrand201ResponseBackground  # noqa: E501
from openapi_client.rest import ApiException

class TestCreateBrand201ResponseBackground(unittest.TestCase):
    """CreateBrand201ResponseBackground unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CreateBrand201ResponseBackground
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateBrand201ResponseBackground`
        """
        model = openapi_client.models.create_brand201_response_background.CreateBrand201ResponseBackground()  # noqa: E501
        if include_optional :
            return CreateBrand201ResponseBackground(
                urls = openapi_client.models.create_brand_201_response_background_urls.createBrand_201_response_background_urls(
                    original = '', 
                    login = '', 
                    branding = '', ), 
                file_size = 56, 
                updated_at = '', 
                content_type = ''
            )
        else :
            return CreateBrand201ResponseBackground(
                urls = openapi_client.models.create_brand_201_response_background_urls.createBrand_201_response_background_urls(
                    original = '', 
                    login = '', 
                    branding = '', ),
                file_size = 56,
                updated_at = '',
                content_type = '',
        )
        """

    def testCreateBrand201ResponseBackground(self):
        """Test CreateBrand201ResponseBackground"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()