# Create your views here.
from django.shortcuts import render_to_response
from django.http  import HttpResponse ,HttpResponseRedirect
from django.utils.safestring import mark_safe
#from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from models import *
from forms  import *
from django.contrib.auth.views import logout  , login


# Seul l' administraeur saer Dial , a le droit
# de  voir cetrain chose  , les ccx nons
disable_for_user =  False
@login_required
def dashboad(request):
     template_name = "canal/dashboard.html"
     if request.user.username  == 'saer':
          global disable_for_user
          disable_for_user = True
     else :
          disable_for_user =False
     return render_to_response(template_name ,{'disable_for_user' :disable_for_user })
     

@login_required
def rbon_check(request ,template_name):
    print request.user
    date_for_user, data_for_the_best =ConseillerCommercial.rbon_check(request.user)
    return render_to_response(template_name ,{'data' :[date_for_user,data_for_the_best ] })


def login_view(request , template_name):
         return login(request, template_name)
 
def  register(request,template_name):
        if request.method =='POST':
             user, email, password = request.POST ['username'],'', request.POST['password']
             u =User.objects.create_user(user , '',  password)
             u.is_active = True
             u.save()
             #Redirect to dashaboard, need probaly to be logged in
             return HttpResponseRedirect('/dashboard')
        else:
             return render_to_response (
                  template_name, {'form': ConseillerCommercialForm() }
                  )

def logout_view(request,template_name):
    return  logout(request, template_name)

