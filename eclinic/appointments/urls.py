from django.urls import path
from . import views

urlpatterns = [
    path('appointments', views.appointment_list_view, name='appointment_list'),
    path('book/', views.appointment_create_view, name='appointment_create'),
    path('cancel/<int:pk>/', views.appointment_cancel_view, name='appointment_cancel'),
]
