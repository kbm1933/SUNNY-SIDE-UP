from content.models import ContentModel, ContentComment
from django.views.generic import ListView, TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    #로그인이 되어 있다면
    """
    :param request: user
    :return: redirect('content') else redirect('sign-in')
    """
    user = request.user.is_authenticated  # 사용자가 인증을 받았는지 (로그인이 되어있는지)
    if user:
        return redirect('/content')
    else:
        return redirect('/sign-in')

def content(request):
    """

    :param request: [all_tweet -> all_content], [content -> contents], [my_tweet -> my_content]
    :return:
    """
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:#로그인이 되어 있다면
            all_content = ContentModel.objects.all().order_by('-created_at')
            return render(request,'content/home.html',{'content':all_content})
        else:#로그인이 안되어 있다면
            return redirect('/sign-in')

    elif request.method == 'POST':
        user = request.user
        contents = request.POST.get('my-content','')

        if contents == '':
            all_content = ContentModel.objects.all().order_by('-created_at')
            return render(request,'content/home.html',{'error':'글은 공백일 수 없습니다.','content':all_content})
        else:
            my_content = ContentModel.objects.create(author=user,contents=contents)
            my_content.save()
            return redirect('/content')

@login_required
def delete_content(request,id):
    """

    :param request: delete
    :param id: contentModel
    :return: redirect
    """
    my_content = ContentModel.objects.get(id=id)
    my_content.delete()
    return redirect('/content')

@login_required
def detail_content(request,id):
    my_content = ContentModel.objects.get(id=id)
    content_comment = ContentModel.objects.filter(contents = id).order_by('-created_at')
    return render(request,'content/content_detail.html',{'content':my_content,'comment':content_comment})

@login_required
def write_comment(request,id):
    if request.method == 'POST':
        comment = request.POST.get("comment","")
        current_content = ContentModel.objects.get(id=id)

        CC = ContentComment()
        CC.comment = comment
        CC.author = request.user
        CC.contents = current_content
        CC.save()

        return redirect('/content/'+str(id))

@login_required
def delete_comment(request,id):
    comment = ContentComment.objects.get(id=id)
    current_content = comment.contents.id
    comment.delete()
    return redirect('/content/'+str(current_content))

def push_test():
    pass