from django.urls import path
from .import views

urlpatterns = [
    path('notes/', views.NotesListCreate.as_view(), name='notes-list'),
    path('notes/<int:pk>/', views.NotesDelete.as_view(), name='delete-notes'), 
]