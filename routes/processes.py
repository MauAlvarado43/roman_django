"""
__Seed builder__
  Extended module
"""

import seed.routes.processes as SeedRoute
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from django.shortcuts import get_object_or_404
from seed.util.request_util import has_fields_or_400
from app.serializers import ProcessSerializer
from domain.get_roman import get_roman
from domain.get_characters import get_characters

class ProcessViewSet(SeedRoute.ProcessViewSet):

  """ POST /api/processes/decimal_to_roman """
  @action(detail=False, methods=["POST"])
  def decimal_to_roman(self, request):
    
    #has_fields_or_400(request.data, "decimal", "user_id")

    decimal = int(request.data["decimal"])
    user_id = int(request.data["user_id"])
    roman = get_roman(decimal, user_id)

    return Response(roman)

  """ GET /api/processes/{process_id}/characters """
  @action(detail=True, methods=["GET"])
  def characters(self, request, pk):

    characters = get_characters(pk)
    
    return Response(characters)