# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class GradeRecord(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, subject_name: str=None, grade_number: float=None):  # noqa: E501
        """GradeRecord - a model defined in Swagger

        :param subject_name: The subject_name of this GradeRecord.  # noqa: E501
        :type subject_name: str
        :param grade_number: The grade_number of this GradeRecord.  # noqa: E501
        :type grade_number: float
        """
        self.swagger_types = {
            'subject_name': str,
            'grade_number': float
        }

        self.attribute_map = {
            'subject_name': 'subject_name',
            'grade_number': 'grade_number'
        }
        self._subject_name = subject_name
        self._grade_number = grade_number

    @classmethod
    def from_dict(cls, dikt) -> 'GradeRecord':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The GradeRecord of this GradeRecord.  # noqa: E501
        :rtype: GradeRecord
        """
        return util.deserialize_model(dikt, cls)

    @property
    def subject_name(self) -> str:
        """Gets the subject_name of this GradeRecord.


        :return: The subject_name of this GradeRecord.
        :rtype: str
        """
        return self._subject_name

    @subject_name.setter
    def subject_name(self, subject_name: str):
        """Sets the subject_name of this GradeRecord.


        :param subject_name: The subject_name of this GradeRecord.
        :type subject_name: str
        """
        if subject_name is None:
            raise ValueError("Invalid value for `subject_name`, must not be `None`")  # noqa: E501

        self._subject_name = subject_name

    @property
    def grade_number(self) -> float:
        """Gets the grade_number of this GradeRecord.


        :return: The grade_number of this GradeRecord.
        :rtype: float
        """
        return self._grade_number

    @grade_number.setter
    def grade_number(self, grade_number: float):
        """Sets the grade_number of this GradeRecord.


        :param grade_number: The grade_number of this GradeRecord.
        :type grade_number: float
        """

        self._grade_number = grade_number
