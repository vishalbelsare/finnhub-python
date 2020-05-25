# coding: utf-8

"""
    Finnhub API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import finnhub
from finnhub.models.merger_country import MergerCountry  # noqa: E501
from finnhub.rest import ApiException

class TestMergerCountry(unittest.TestCase):
    """MergerCountry unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test MergerCountry
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = finnhub.models.merger_country.MergerCountry()  # noqa: E501
        if include_optional :
            return MergerCountry(
                announcement_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                deal_size = 1.337, 
                status = '0', 
                target_name = '0', 
                target_nation = '0', 
                acquirer_name = '0', 
                acquirer_nation = '0', 
                form = '0', 
                target_industry = '0', 
                acquirer_industry = '0', 
                target_description = '0', 
                acquirer_description = '0', 
                target_region = '0', 
                acquirer_region = '0', 
                target_public_status = '0', 
                acquirer_public_status = '0', 
                deal_attitude = '0', 
                netincome_multiple = 1.337, 
                percent_acquired = 1.337
            )
        else :
            return MergerCountry(
        )

    def testMergerCountry(self):
        """Test MergerCountry"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
