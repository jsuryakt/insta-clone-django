from django.shortcuts import render,redirect
from django.views.generic import View
from django.http import HttpResponse
from authentication.forms import UserForm
# Create your views here.
def home(request):
    return HttpResponse("Home")
class SignUpView(View):
    template_name = 'authentication/signup.html'
    form_class = UserForm

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        context = {'form':form}
        return render(request, self.template_name, context)