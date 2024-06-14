from django.urls import path, include
from .views import *
from . import views

urlpatterns=[
    path('create/', Create.as_view(), name='create'),
    path('detail/<int:pk>/', Details.as_view(), name='details'),
    path('update/<int:pk>/', Update.as_view(), name='update'),
    path('delete/<int:pk>/', Delete.as_view(), name='delete'),
    path('search/<str:Name>/', Search.as_view(), name='search'),

    path('create_travel_details/', views.create_travel_details, name='create-travel-details'),
    path('fetch_travel_details/<int:id>/', views.fetch_travel_details, name='fetch-travel-details'),
    path('update_travel_details/<int:id>/', views.update_travel_details, name='update-travel-details'),
    path('delete_travel_details/<int:id>/', views.delete_travel_details, name='delete-travel-details'),
    path('', views.main, name='main'),
    path('update_details/<int:id>/', views.travel_details_for_update, name='travel-details-for-update'),
    path('user/', views.users, name='users'),
    path('image_view/<int:id>/', views.image_view, name='image-view'),
    path('help_page/', views.help, name='help'),
]