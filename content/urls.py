from django.urls import path
from . import views

urlpatterns = [
    path('content/<int:id>',views.detail_comment,name='detail-content'), # 해당 번호의 게시글과 댓글들 읽어오기
    path('content/comment/<int:id>',views.write_comment, name='write-comment'), # 해당 id 트윗에 댓글을 작성
    path('content/comment/delete/<int:id>',views.delete_comment, name='delete-comment'), # 해당 번호 댓글 삭제
]