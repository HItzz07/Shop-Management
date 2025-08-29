from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from .serializers import BillSerializer
import json

@api_view(['POST'])
# @parser_classes([JSONParser])
def create_bill(request):
    print(request.data)
    serializer = BillSerializer(data=request.data)
    if serializer.is_valid():
        bill = serializer.save()
        return Response(BillSerializer(bill).data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def edit_bill(request):
    pass