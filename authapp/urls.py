from django.urls import path
from . import views
urlpatterns=[

    path('userregister/', views.registration, name='register'),
    path('userlogIn/', views.login, name='login'),
    path('userlogOut/', views.logout, name='logout'),
    path('profilepage/', views.profile_page, name='profile'),

]