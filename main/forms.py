from django import forms
from django.forms import widgets
import main.models as mm


class RegisterForm(forms.ModelForm):
    email = forms.EmailField()
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = mm.AppUser
        fields = ('username', 'email', 'password', )

    username.widget.attrs.update({'class': 'form-control',
                                  'placeholder': 'username'})
    email.widget.attrs.update({'class': 'form-control',
                               'placeholder': 'email'})
    password.widget.attrs.update({'class': 'form-control',
                                  'placeholder': 'password'})
    confirm_password.widget.attrs.update({'class': 'form-control',

                                          'placeholder': 'Re-type password'})


class LoginForm(forms.ModelForm):
    email = forms.EmailField()

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = mm.AppUser
        fields = ('email', 'password',)

    email.widget.attrs.update({'class': 'form-control',
                               'placeholder': 'email'})
    password.widget.attrs.update({'class': 'form-control',
                                  'placeholder': 'password'})
                                 

   
