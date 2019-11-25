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

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "passwords do not match"
            )
