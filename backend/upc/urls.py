from django.urls import path
from .views import CreateClientView, get_user_clients_for_current_month

urlpatterns = [
    path('create', CreateClientView.as_view(), name='create_client'),
    path('list', get_user_clients_for_current_month, name='list_clients')
]