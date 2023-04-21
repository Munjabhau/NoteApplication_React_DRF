from django.urls import path
from .import views

urlpatterns = [
    path('', views.getRoutes, name='getRoutes'),
    path('notes/', views.getNotes, name='notes'),
    path('note/<str:pk>/update/', views.updateNote, name='update-note'),

    path('note/<str:pk>/', views.getNote, name='note'),
]
