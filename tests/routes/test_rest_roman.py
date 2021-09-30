"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

import json

from rest_framework import status
from rest_framework.test import APITestCase

from seed.tests.util_test import fill_test_database

class TestRest(APITestCase):

    def setUp(self):
        fill_test_database()

    def test_decimal_to_roman(self):

      data = {
        "decimal": 10,
        "user_id": 1
      }

      response = self.client.post('/api/processes/decimal_to_roman/', data)
      self.assertEqual(response.status_code, status.HTTP_200_OK)
      self.assertEqual(response.data, "X")

      data = {
        "decimal": 109,
        "user_id": 1
      }

      response = self.client.post('/api/processes/decimal_to_roman/', data)
      self.assertEqual(response.status_code, status.HTTP_200_OK)
      self.assertEqual(response.data, "CIX")

      data = {
        "decimal": 3779,
        "user_id": 1
      }

      response = self.client.post('/api/processes/decimal_to_roman/', data)
      self.assertEqual(response.status_code, status.HTTP_200_OK)
      self.assertEqual(response.data, "MMMDCCLXXIX")

      data = {
        "decimal": 1,
        "user_id": 1
      }

      response = self.client.post('/api/processes/decimal_to_roman/', data)
      self.assertEqual(response.status_code, status.HTTP_200_OK)
      self.assertEqual(response.data, "I")