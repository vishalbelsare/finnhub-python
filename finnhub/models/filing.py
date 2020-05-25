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


class Filing(object):
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
        'access_number': 'str',
        'symbol': 'str',
        'cik': 'str',
        'form': 'str',
        'filed_date': 'datetime',
        'accepted_date': 'datetime',
        'report_url': 'str',
        'filing_url': 'str'
    }

    attribute_map = {
        'access_number': 'accessNumber',
        'symbol': 'symbol',
        'cik': 'cik',
        'form': 'form',
        'filed_date': 'filedDate',
        'accepted_date': 'acceptedDate',
        'report_url': 'reportUrl',
        'filing_url': 'filingUrl'
    }

    def __init__(self, access_number=None, symbol=None, cik=None, form=None, filed_date=None, accepted_date=None, report_url=None, filing_url=None, local_vars_configuration=None):  # noqa: E501
        """Filing - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._access_number = None
        self._symbol = None
        self._cik = None
        self._form = None
        self._filed_date = None
        self._accepted_date = None
        self._report_url = None
        self._filing_url = None
        self.discriminator = None

        if access_number is not None:
            self.access_number = access_number
        if symbol is not None:
            self.symbol = symbol
        if cik is not None:
            self.cik = cik
        if form is not None:
            self.form = form
        if filed_date is not None:
            self.filed_date = filed_date
        if accepted_date is not None:
            self.accepted_date = accepted_date
        if report_url is not None:
            self.report_url = report_url
        if filing_url is not None:
            self.filing_url = filing_url

    @property
    def access_number(self):
        """Gets the access_number of this Filing.  # noqa: E501

        Access number.  # noqa: E501

        :return: The access_number of this Filing.  # noqa: E501
        :rtype: str
        """
        return self._access_number

    @access_number.setter
    def access_number(self, access_number):
        """Sets the access_number of this Filing.

        Access number.  # noqa: E501

        :param access_number: The access_number of this Filing.  # noqa: E501
        :type: str
        """

        self._access_number = access_number

    @property
    def symbol(self):
        """Gets the symbol of this Filing.  # noqa: E501

        Symbol.  # noqa: E501

        :return: The symbol of this Filing.  # noqa: E501
        :rtype: str
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        """Sets the symbol of this Filing.

        Symbol.  # noqa: E501

        :param symbol: The symbol of this Filing.  # noqa: E501
        :type: str
        """

        self._symbol = symbol

    @property
    def cik(self):
        """Gets the cik of this Filing.  # noqa: E501

        CIK.  # noqa: E501

        :return: The cik of this Filing.  # noqa: E501
        :rtype: str
        """
        return self._cik

    @cik.setter
    def cik(self, cik):
        """Sets the cik of this Filing.

        CIK.  # noqa: E501

        :param cik: The cik of this Filing.  # noqa: E501
        :type: str
        """

        self._cik = cik

    @property
    def form(self):
        """Gets the form of this Filing.  # noqa: E501

        Form type.  # noqa: E501

        :return: The form of this Filing.  # noqa: E501
        :rtype: str
        """
        return self._form

    @form.setter
    def form(self, form):
        """Sets the form of this Filing.

        Form type.  # noqa: E501

        :param form: The form of this Filing.  # noqa: E501
        :type: str
        """

        self._form = form

    @property
    def filed_date(self):
        """Gets the filed_date of this Filing.  # noqa: E501

        Filed date <code>%Y-%m-%d %H:%M:%S</code>.  # noqa: E501

        :return: The filed_date of this Filing.  # noqa: E501
        :rtype: datetime
        """
        return self._filed_date

    @filed_date.setter
    def filed_date(self, filed_date):
        """Sets the filed_date of this Filing.

        Filed date <code>%Y-%m-%d %H:%M:%S</code>.  # noqa: E501

        :param filed_date: The filed_date of this Filing.  # noqa: E501
        :type: datetime
        """

        self._filed_date = filed_date

    @property
    def accepted_date(self):
        """Gets the accepted_date of this Filing.  # noqa: E501

        Accepted date <code>%Y-%m-%d %H:%M:%S</code>.  # noqa: E501

        :return: The accepted_date of this Filing.  # noqa: E501
        :rtype: datetime
        """
        return self._accepted_date

    @accepted_date.setter
    def accepted_date(self, accepted_date):
        """Sets the accepted_date of this Filing.

        Accepted date <code>%Y-%m-%d %H:%M:%S</code>.  # noqa: E501

        :param accepted_date: The accepted_date of this Filing.  # noqa: E501
        :type: datetime
        """

        self._accepted_date = accepted_date

    @property
    def report_url(self):
        """Gets the report_url of this Filing.  # noqa: E501

        Report's URL.  # noqa: E501

        :return: The report_url of this Filing.  # noqa: E501
        :rtype: str
        """
        return self._report_url

    @report_url.setter
    def report_url(self, report_url):
        """Sets the report_url of this Filing.

        Report's URL.  # noqa: E501

        :param report_url: The report_url of this Filing.  # noqa: E501
        :type: str
        """

        self._report_url = report_url

    @property
    def filing_url(self):
        """Gets the filing_url of this Filing.  # noqa: E501

        Filing's URL.  # noqa: E501

        :return: The filing_url of this Filing.  # noqa: E501
        :rtype: str
        """
        return self._filing_url

    @filing_url.setter
    def filing_url(self, filing_url):
        """Sets the filing_url of this Filing.

        Filing's URL.  # noqa: E501

        :param filing_url: The filing_url of this Filing.  # noqa: E501
        :type: str
        """

        self._filing_url = filing_url

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
        if not isinstance(other, Filing):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Filing):
            return True

        return self.to_dict() != other.to_dict()
