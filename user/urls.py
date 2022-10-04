from django.urls import path
from . import views
from user import views

urlpatterns = [
    path('sign-up/', views.sign_up_view, name='sign-up'),
    path('sign-in/', views.sign_in_view, name = 'sign-in'),
    path('logout/',views.logout, name = 'logout'),
    path('user/follow/<int:id>', views.user_follow, name='user-follow'),
    path('user/my-profile', views.my_view, name = 'my-profile'),
    ]
