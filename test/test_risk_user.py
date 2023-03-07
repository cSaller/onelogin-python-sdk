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

import onelogin
from onelogin.models.risk_user import RiskUser  # noqa: E501
from onelogin.rest import ApiException

class TestRiskUser(unittest.TestCase):
    """RiskUser unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RiskUser
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RiskUser`
        """
        model = onelogin.models.risk_user.RiskUser()  # noqa: E501
        if include_optional :
            return RiskUser(
                id = '', 
                name = '', 
                authenticated = True
            )
        else :
            return RiskUser(
                id = '',
        )
        """

    def testRiskUser(self):
        """Test RiskUser"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()