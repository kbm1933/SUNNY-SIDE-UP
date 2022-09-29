from django.urls import path
from user import views

urlpatterns = [
    path('sign-in/', views.sign_in_view, name = 'sign-in')
]
