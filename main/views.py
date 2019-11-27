from django.shortcuts import render
from django.views import View
from .forms import RegisterForm, LoginForm
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login

# We will map urls pattern to this view function in 'urls.py' module(file)


def home(request):
    return render(request, 'main/home.html')


def about(request):
    return render(request, 'main/about.html')


def single_list(request):
    return render(request, 'main/single-list.html')


class Register(View):
    form_class = RegisterForm
    template_name = 'main/sign-up.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            register_form = form.save(commit=False)
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            confirm_password = form.cleaned_data.get('confirm_password')
            register_form.set_password(password)
            register_form.save()
            new_user = authenticate(username=username,
                                    password=password,
                                    )
            login(request, new_user)
            # <process form cleaned data>
            return HttpResponseRedirect('/home')

        return render(request, self.template_name, {'form': form})


class Login(View):
    form_class = RegisterForm
    template_name = 'main/login.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():

            return HttpResponseRedirect('/home')

        return render(request, self.template_name, {'form': form})
