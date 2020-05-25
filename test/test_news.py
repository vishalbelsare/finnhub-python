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
from finnhub.models.news import News  # noqa: E501
from finnhub.rest import ApiException

class TestNews(unittest.TestCase):
    """News unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test News
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = finnhub.models.news.News()  # noqa: E501
        if include_optional :
            return News(
                category = '0', 
                datetime = 56, 
                headline = '0', 
                id = 56, 
                image = '0', 
                related = '0', 
                source = '0', 
                summary = '0', 
                url = '0'
            )
        else :
            return News(
        )

    def testNews(self):
        """Test News"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
