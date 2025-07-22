from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import LeadSerializer
from .models import Lead

@api_view(['GET', 'POST'])
def submit_lead(request):
    if request.method == 'POST':
        serializer = LeadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'message': 'Lead saved', 'data': serializer.data}, 
                          status=status.HTTP_201_CREATED)
        return Response({'status': 'error', 'message': serializer.errors}, 
                       status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'GET':
        leads = Lead.objects.all()
        serializer = LeadSerializer(leads, many=True)
        return Response({'status': 'success', 'data': serializer.data}, 
                       status=status.HTTP_200_OK)

@api_view(['GET', 'PUT', 'DELETE'])
def lead_detail(request, pk):
    try:
        lead = Lead.objects.get(pk=pk)
    except Lead.DoesNotExist:
        return Response({'status': 'error', 'message': 'Lead not found'}, 
                       status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LeadSerializer(lead)
        return Response({'status': 'success', 'data': serializer.data}, 
                       status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = LeadSerializer(lead, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'message': 'Lead updated', 'data': serializer.data}, 
                          status=status.HTTP_200_OK)
        return Response({'status': 'error', 'message': serializer.errors}, 
                       status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        lead.delete()
        return Response({'status': 'success', 'message': 'Lead deleted'}, 
                       status=status.HTTP_204_NO_CONTENT)
