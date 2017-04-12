from django.shortcuts import render
from django.http import request,response, HttpResponseRedirect
from .forms import LoginForm


# Create your views here.
def landingPage(request):
    return render(request,template_name='foodBlog/sharecipe_home.html')

def login(request):
    if(request.method == 'POST'):
        import pdb; pdb.set_trace()
        
        submitted_form = LoginForm(request.POST)
        return render(request, template_name='foodblog/sharecipe_home.html')
        #Redirect to A page where user'home page
    else:
        #return HttpResponseRedirect('http://google.co.in')
        return render(request, template_name='foodblog/sharecipe_login.html')


def signup(request):
    return render(request,template_name='foodBlog/sharecipe_signup.html')