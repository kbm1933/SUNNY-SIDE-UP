# tweet/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('content/', views.content, name='content'), # 127.0.0.1:8000/content 과 views.py 폴더의 content 함수 연결
    path('content/delete/<int:id>',views.delete_content,name = 'delete-content'),
    path('content/<int:id>',views.detail_content,name='detail-content'),
    path('content/comment/<int:id>',views.write_comment,name='write-comment'),
    path('content/comment/delete/<int:id>',views.delete_comment,name='delete-comment')

]