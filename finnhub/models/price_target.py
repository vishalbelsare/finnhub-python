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


class PriceTarget(object):
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
        'symbol': 'str',
        'target_high': 'float',
        'target_low': 'float',
        'target_mean': 'float',
        'target_median': 'float',
        'last_updated': 'datetime'
    }

    attribute_map = {
        'symbol': 'symbol',
        'target_high': 'targetHigh',
        'target_low': 'targetLow',
        'target_mean': 'targetMean',
        'target_median': 'targetMedian',
        'last_updated': 'lastUpdated'
    }

    def __init__(self, symbol=None, target_high=None, target_low=None, target_mean=None, target_median=None, last_updated=None, local_vars_configuration=None):  # noqa: E501
        """PriceTarget - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._symbol = None
        self._target_high = None
        self._target_low = None
        self._target_mean = None
        self._target_median = None
        self._last_updated = None
        self.discriminator = None

        if symbol is not None:
            self.symbol = symbol
        if target_high is not None:
            self.target_high = target_high
        if target_low is not None:
            self.target_low = target_low
        if target_mean is not None:
            self.target_mean = target_mean
        if target_median is not None:
            self.target_median = target_median
        if last_updated is not None:
            self.last_updated = last_updated

    @property
    def symbol(self):
        """Gets the symbol of this PriceTarget.  # noqa: E501

        Company symbol.  # noqa: E501

        :return: The symbol of this PriceTarget.  # noqa: E501
        :rtype: str
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        """Sets the symbol of this PriceTarget.

        Company symbol.  # noqa: E501

        :param symbol: The symbol of this PriceTarget.  # noqa: E501
        :type: str
        """

        self._symbol = symbol

    @property
    def target_high(self):
        """Gets the target_high of this PriceTarget.  # noqa: E501

        Highes analysts' target.  # noqa: E501

        :return: The target_high of this PriceTarget.  # noqa: E501
        :rtype: float
        """
        return self._target_high

    @target_high.setter
    def target_high(self, target_high):
        """Sets the target_high of this PriceTarget.

        Highes analysts' target.  # noqa: E501

        :param target_high: The target_high of this PriceTarget.  # noqa: E501
        :type: float
        """

        self._target_high = target_high

    @property
    def target_low(self):
        """Gets the target_low of this PriceTarget.  # noqa: E501

        Lowest analysts' target.  # noqa: E501

        :return: The target_low of this PriceTarget.  # noqa: E501
        :rtype: float
        """
        return self._target_low

    @target_low.setter
    def target_low(self, target_low):
        """Sets the target_low of this PriceTarget.

        Lowest analysts' target.  # noqa: E501

        :param target_low: The target_low of this PriceTarget.  # noqa: E501
        :type: float
        """

        self._target_low = target_low

    @property
    def target_mean(self):
        """Gets the target_mean of this PriceTarget.  # noqa: E501

        Mean of all analysts' targets.  # noqa: E501

        :return: The target_mean of this PriceTarget.  # noqa: E501
        :rtype: float
        """
        return self._target_mean

    @target_mean.setter
    def target_mean(self, target_mean):
        """Sets the target_mean of this PriceTarget.

        Mean of all analysts' targets.  # noqa: E501

        :param target_mean: The target_mean of this PriceTarget.  # noqa: E501
        :type: float
        """

        self._target_mean = target_mean

    @property
    def target_median(self):
        """Gets the target_median of this PriceTarget.  # noqa: E501

        Median of all analysts' targets.  # noqa: E501

        :return: The target_median of this PriceTarget.  # noqa: E501
        :rtype: float
        """
        return self._target_median

    @target_median.setter
    def target_median(self, target_median):
        """Sets the target_median of this PriceTarget.

        Median of all analysts' targets.  # noqa: E501

        :param target_median: The target_median of this PriceTarget.  # noqa: E501
        :type: float
        """

        self._target_median = target_median

    @property
    def last_updated(self):
        """Gets the last_updated of this PriceTarget.  # noqa: E501

        Updated time of the data  # noqa: E501

        :return: The last_updated of this PriceTarget.  # noqa: E501
        :rtype: datetime
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """Sets the last_updated of this PriceTarget.

        Updated time of the data  # noqa: E501

        :param last_updated: The last_updated of this PriceTarget.  # noqa: E501
        :type: datetime
        """

        self._last_updated = last_updated

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
        if not isinstance(other, PriceTarget):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PriceTarget):
            return True

        return self.to_dict() != other.to_dict()
