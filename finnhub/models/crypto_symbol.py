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


class CryptoSymbol(object):
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
        'description': 'str',
        'display_symbol': 'str',
        'symbol': 'str'
    }

    attribute_map = {
        'description': 'description',
        'display_symbol': 'displaySymbol',
        'symbol': 'symbol'
    }

    def __init__(self, description=None, display_symbol=None, symbol=None, local_vars_configuration=None):  # noqa: E501
        """CryptoSymbol - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._description = None
        self._display_symbol = None
        self._symbol = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if display_symbol is not None:
            self.display_symbol = display_symbol
        if symbol is not None:
            self.symbol = symbol

    @property
    def description(self):
        """Gets the description of this CryptoSymbol.  # noqa: E501

        Symbol description  # noqa: E501

        :return: The description of this CryptoSymbol.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CryptoSymbol.

        Symbol description  # noqa: E501

        :param description: The description of this CryptoSymbol.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def display_symbol(self):
        """Gets the display_symbol of this CryptoSymbol.  # noqa: E501

        Display symbol name.  # noqa: E501

        :return: The display_symbol of this CryptoSymbol.  # noqa: E501
        :rtype: str
        """
        return self._display_symbol

    @display_symbol.setter
    def display_symbol(self, display_symbol):
        """Sets the display_symbol of this CryptoSymbol.

        Display symbol name.  # noqa: E501

        :param display_symbol: The display_symbol of this CryptoSymbol.  # noqa: E501
        :type: str
        """

        self._display_symbol = display_symbol

    @property
    def symbol(self):
        """Gets the symbol of this CryptoSymbol.  # noqa: E501

        Unique symbol used to identify this symbol used in <code>/crypto/candle</code> endpoint.  # noqa: E501

        :return: The symbol of this CryptoSymbol.  # noqa: E501
        :rtype: str
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        """Sets the symbol of this CryptoSymbol.

        Unique symbol used to identify this symbol used in <code>/crypto/candle</code> endpoint.  # noqa: E501

        :param symbol: The symbol of this CryptoSymbol.  # noqa: E501
        :type: str
        """

        self._symbol = symbol

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
        if not isinstance(other, CryptoSymbol):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CryptoSymbol):
            return True

        return self.to_dict() != other.to_dict()
