from django.shortcuts import redirect,render
from django.contrib.auth import authenticate,logout,login
from django.views import View
from django.contrib import  messages
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

class DashboardView(LoginRequiredMixin, View):
    template_name ='home.html'
    login_url = 'login'
    def get(self,request):
            return render(request,self.template_name)


class SigninView(View):
    template_name = 'login.html'
    def get(self, request):
        return render(request, self.template_name)
    def post(self,request,*args,**kwargs):
        u = request.POST['username']
        p = request.POST['password']
        user = authenticate(username=u,password=p)
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            messages.add_message(request,messages.ERROR,'Your crediantial doesnot match')
            return redirect('login')


class SignupView(View):
    template_name = 'register.html'

    def get(self, request):
        return render(request, self.template_name)
    def post(self,request, *args,**kwargs):
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        username = request.POST['username']
        p1 = request.POST['password1']
        p2 = request.POST['password2']
        if p1 == p2:
            try:
                u = User(username=username,email=email,first_name=fname,last_name=lname)
                u.set_password(p1)
                u.save()
                messages.add_message(request,messages.SUCCESS,'Account created successfully')
                return redirect('login')
            except:
                messages.add_message(request,messages.ERROR,'Username already exist')
                return redirect('signup')
        else:
            messages.add_message(request,messages.ERROR,'Password incorrect')
            return redirect('signup')



def signout(request):
    logout(request)
    return redirect('login')