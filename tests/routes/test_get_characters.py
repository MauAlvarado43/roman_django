"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

import json

from rest_framework import status
from rest_framework.test import APITestCase
from app.models import User, Process

from seed.tests.util_test import fill_test_database

class TestRest(APITestCase):

    def setUp(self):
        fill_test_database()

        user = User.objects.get(id=1)
        process = Process(decimal=10, result="X", user_id=user)
        process.save()

    def test_decimal_to_roman(self):

      response = self.client.get('/api/processes/2/characters/')
      self.assertEqual(response.status_code, status.HTTP_200_OK)
      self.assertEqual(response.data, {"characters": ["X"]})