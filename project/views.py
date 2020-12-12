from django.shortcuts import render
from.forms import *
def UserViewPost(request):
    posturl="http://127.0.0.1:8000/api/user/"
    resp=request.get(posturl)
    data=resp.json()
    form=UserForm()
    context={'form':form}
    return render(request, 'project/user_form.html', context=context)

def UserView(request):
    geturl="http://127.0.0.1:8000/signup/register"
    resp = request.get(geturl)
    data = resp.json()
    form=SignUpForm()
    context = {'form': form}
    return render(request, 'project/user_form.html', context=context)
# Create your views here.
