from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import notesSerializer, userSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Notes



class NotesListCreate(generics.ListCreateAPIView):
    serializer_class = notesSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        return Notes.objects.filter(author=user)
    
    def perform_create(self, serializer):
        if serializer.is_valid():
             serializer.save(author=self.request.user)
        else:
            print(serializer.errors)
            

class NotesDelete(generics.DestroyAPIView):
      serializer_class = notesSerializer
      permission_classes = [IsAuthenticated]
      
      def get_queryset(self):
          user = self.request.user
          return Notes.objects.filter(author=user)               


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = userSerializer
    permission_classes = [AllowAny]