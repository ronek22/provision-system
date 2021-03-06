from django.shortcuts import render
from .models import Client
from .serializers import ClientSerializer
from .utils import calculate_profit_from_clients
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from accounts.serializers import UserSerializer
from datetime import datetime

# Create your views here.
class CreateClientView(CreateAPIView):
    model = Client
    permission_classes = [IsAuthenticated]
    serializer_class = ClientSerializer

class UpdateClientView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ClientSerializer

    def get_queryset(self):
        return Client.objects.filter(created_by=self.request.user)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_clients_for_current_month(request):
    user = request.user
    clients = Client.objects.filter(created_by=user, created_on__month=datetime.now().month)
    clients_json = [ClientSerializer(x).data for x in clients]
    return Response(clients_json)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_profit_for_current_month(request):
    user = request.user
    clients = Client.objects.filter(created_by=user, created_on__month=datetime.now().month)
    profit = calculate_profit_from_clients(clients)
    return Response(profit)