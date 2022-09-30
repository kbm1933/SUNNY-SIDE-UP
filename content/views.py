from django.shortcuts import render, redirect
from .models import ContentModel, ContentComment
from django.contrib.auth.decorators import login_required

# 상세 페이지
@login_required
def detail_tweet(request, id):
    my_content = ContentModel.objects.get(id=id)
    content_comment = ContentComment.objects.filter(content_id=id).order_by('-created_at')
    return render(request, 'content/content_detail.html', {'content': my_content, 'comment': content_comment})

# 댓글 작성
@login_required
def write_comment(request, id):
    if request.method == 'POST':
        comment = request.POST.get("comment", "")
        current_content = ContentModel.objects.get(id=id)

        CC = ContentComment()
        CC.comment = comment
        CC.author = request.user
        CC.content = current_content
        CC.save()

        return redirect('/content/'+str(id))

# 댓글 삭제
@login_required
def delete_comment(request, id):
    comment = ContentComment.objects.get(id=id)
    current_content = comment.content.id
    comment.delete()
    return redirect('/content/'+str(current_content))
