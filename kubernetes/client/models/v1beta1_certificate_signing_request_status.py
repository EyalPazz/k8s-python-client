# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: release-1.17
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from kubernetes.client.configuration import Configuration


class V1beta1CertificateSigningRequestStatus(object):
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
        'certificate': 'str',
        'conditions': 'list[V1beta1CertificateSigningRequestCondition]'
    }

    attribute_map = {
        'certificate': 'certificate',
        'conditions': 'conditions'
    }

    def __init__(self, certificate=None, conditions=None, local_vars_configuration=None):  # noqa: E501
        """V1beta1CertificateSigningRequestStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._certificate = None
        self._conditions = None
        self.discriminator = None

        if certificate is not None:
            self.certificate = certificate
        if conditions is not None:
            self.conditions = conditions

    @property
    def certificate(self):
        """Gets the certificate of this V1beta1CertificateSigningRequestStatus.  # noqa: E501

        If request was approved, the controller will place the issued certificate here.  # noqa: E501

        :return: The certificate of this V1beta1CertificateSigningRequestStatus.  # noqa: E501
        :rtype: str
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        """Sets the certificate of this V1beta1CertificateSigningRequestStatus.

        If request was approved, the controller will place the issued certificate here.  # noqa: E501

        :param certificate: The certificate of this V1beta1CertificateSigningRequestStatus.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                certificate is not None and not re.search(r'^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$', certificate)):  # noqa: E501
            raise ValueError(r"Invalid value for `certificate`, must be a follow pattern or equal to `/^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/`")  # noqa: E501

        self._certificate = certificate

    @property
    def conditions(self):
        """Gets the conditions of this V1beta1CertificateSigningRequestStatus.  # noqa: E501

        Conditions applied to the request, such as approval or denial.  # noqa: E501

        :return: The conditions of this V1beta1CertificateSigningRequestStatus.  # noqa: E501
        :rtype: list[V1beta1CertificateSigningRequestCondition]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this V1beta1CertificateSigningRequestStatus.

        Conditions applied to the request, such as approval or denial.  # noqa: E501

        :param conditions: The conditions of this V1beta1CertificateSigningRequestStatus.  # noqa: E501
        :type: list[V1beta1CertificateSigningRequestCondition]
        """

        self._conditions = conditions

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
        if not isinstance(other, V1beta1CertificateSigningRequestStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1beta1CertificateSigningRequestStatus):
            return True

        return self.to_dict() != other.to_dict()
