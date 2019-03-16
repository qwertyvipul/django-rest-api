from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer
from django.shortcuts import render

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allow users to be edited to deleted
    """
    queryset = User.objects.all().order_by('-data_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allow users to be edited to deleted
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
