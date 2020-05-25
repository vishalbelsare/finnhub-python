# coding: utf-8

"""
    Finnhub API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from finnhub.configuration import Configuration


class Forexrates(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'base': 'str',
        'quote': 'object'
    }

    attribute_map = {
        'base': 'base',
        'quote': 'quote'
    }

    def __init__(self, base=None, quote=None, local_vars_configuration=None):  # noqa: E501
        """Forexrates - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._base = None
        self._quote = None
        self.discriminator = None

        if base is not None:
            self.base = base
        if quote is not None:
            self.quote = quote

    @property
    def base(self):
        """Gets the base of this Forexrates.  # noqa: E501

        Base currency.  # noqa: E501

        :return: The base of this Forexrates.  # noqa: E501
        :rtype: str
        """
        return self._base

    @base.setter
    def base(self, base):
        """Sets the base of this Forexrates.

        Base currency.  # noqa: E501

        :param base: The base of this Forexrates.  # noqa: E501
        :type: str
        """

        self._base = base

    @property
    def quote(self):
        """Gets the quote of this Forexrates.  # noqa: E501


        :return: The quote of this Forexrates.  # noqa: E501
        :rtype: object
        """
        return self._quote

    @quote.setter
    def quote(self, quote):
        """Sets the quote of this Forexrates.


        :param quote: The quote of this Forexrates.  # noqa: E501
        :type: object
        """

        self._quote = quote

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Forexrates):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Forexrates):
            return True

        return self.to_dict() != other.to_dict()
