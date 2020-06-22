from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from collections import Counter


@api_view(['POST'])
def lambda_function(request):
    if request.method == 'POST':
        data = request.data.get('question')
        counter = list(Counter(data).elements())
        response = sorted(counter, key=counter.count, reverse=True)
        return Response({'solution': response}, status=status.HTTP_200_OK)
