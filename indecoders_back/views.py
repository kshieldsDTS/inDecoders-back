from django.shortcuts import render
from rest_framework import generics, permissions
from .models import LFHelp, LFWork
from .serializers import LFHelpSerializer, LFWorkSerializer
from .permissions import IsOwnerOrReadOnly
# Create your views here.

class LFWorkList(generics.ListCreateAPIView):
    queryset = LFWork.objects.all()
    serializer_class = LFWorkSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class LFWorkDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LFWork.objects.all()
    serializer_class = LFWorkSerializer
    permission_classes = [IsOwnerOrReadOnly]

class LFHelpList(generics.ListCreateAPIView):
    queryset = LFHelp.objects.all()
    serializer_class = LFHelpSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class LFHelpDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LFHelp.objects.all()
    serializer_class = LFHelpSerializer
    permission_classes = [IsOwnerOrReadOnly]