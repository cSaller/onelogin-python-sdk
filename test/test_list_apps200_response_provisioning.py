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
from openapi_client.models.list_apps200_response_provisioning import ListApps200ResponseProvisioning  # noqa: E501
from openapi_client.rest import ApiException

class TestListApps200ResponseProvisioning(unittest.TestCase):
    """ListApps200ResponseProvisioning unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ListApps200ResponseProvisioning
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListApps200ResponseProvisioning`
        """
        model = openapi_client.models.list_apps200_response_provisioning.ListApps200ResponseProvisioning()  # noqa: E501
        if include_optional :
            return ListApps200ResponseProvisioning(
                enabled = True
            )
        else :
            return ListApps200ResponseProvisioning(
        )
        """

    def testListApps200ResponseProvisioning(self):
        """Test ListApps200ResponseProvisioning"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()