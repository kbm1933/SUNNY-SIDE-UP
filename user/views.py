from django.shortcuts import render,redirect
from django.contrib import auth
# Create your views here.

def sign_in_view(request):
    if request.method == "GET":

        user = request.user.is_authenticated

        if user:
            return redirect('/')
        else:
            return render(request,'user/signin.html')
    
    elif request.method == "POST":
        username = request.POST.get('username','')
        password = request.POST.get('password','')

        me = auth.authenticate(request, username=username, password=password)

        if me is not None:
            auth.login(request,me)
            return redirect('/')
        else:
            msg = {'error' : '유저이름 혹은 패스워드를 확인 해 주세요'}
            return render(request,'user/signin.html', msg)