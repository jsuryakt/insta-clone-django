from django.shortcuts import render,redirect
from django.views.generic import View
from django.http import HttpResponse
from authentication.forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
# Create your views here.

class SignInView(View):
    template_name = 'authentication/signin.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('feed_view')
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        password = request.POST.get('password')
        form = AuthenticationForm(request.POST)

        user = authenticate(request, email = email, password = password)
        if user is None:
            messages.error(request,'Username or Password Invalid')
            return redirect('signin_view')
            # return render(request, self.template_name)

        login(request, user)
        return redirect('feed_view')

class SignUpView(View):
    template_name = 'authentication/signup.html'
    form_class = UserForm

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('feed_view')
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin_view')
        context = {'form':form}
        return render(request, self.template_name, context)

class SignOutView(View):
    def post(self, request):
        logout(request)
        return redirect('signin_view')