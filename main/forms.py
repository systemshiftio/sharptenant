from django import forms 
from django.forms import widgets
import main.models as mm
from django.forms import formset_factory



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

LOCATION = (
    ('ikeja', 'Ikeja'),
    ('yaba', 'Yaba'),
    ('iyana-ipaja', 'Iyana-Ipaja'),
    ('oworonsoki', 'Oworonsoki')
)

STATE = (
    ('lagos', 'Lagos'),
    # ('imo', 'Imo'),
    # ('abuja', 'Abuja'),
    # ('port-hacourt', 'Port-hacourt'),
)

class SearchForm(forms.Form):
    address = forms.CharField(label='Address', max_length=200, required=False)
    location = forms.ChoiceField(label='Location', choices=LOCATION)
    state = forms.ChoiceField(label='state', choices=STATE)

    state.widget.attrs.update({'placeholder': 'state'})
    address.widget.attrs.update({'placeholder': 'Enter a street name, address number or keyword'})
    location.widget.attrs.update({'placeholder': 'Area/state'})


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = mm.AppUser
        fields = ('username',)

    username.widget.attrs.update({'class': 'form-control', 
                               'placeholder': 'username'})
    password.widget.attrs.update({'class': 'form-control',
                                  'placeholder': 'password'})


class ReviewForm(forms.ModelForm):
    title = forms.CharField(label='Title', max_length=200, required=True)
    street_name = forms.CharField(label='Address', max_length=200, required=True)
    location = forms.ChoiceField(label='Location', choices=LOCATION)
    state = forms.ChoiceField(label='State', choices=STATE)
    house_alias = forms.CharField(label='House alias', max_length=100, required=False)
    landlord = forms.CharField(label='Landlord Name', max_length=100, required=False)
    content = forms.CharField( required= True, widget=forms.Textarea)

    image1 = forms.FileField(label='image1', required=False)
    image2 = forms.FileField(label='image2', required=False)
    image3 = forms.FileField(label='image3', required=False)
    image4 = forms.FileField(label='image4', required=False)

    class Meta:
        model = mm.Review
        fields = ('title', 'street_name', 'location', 'state', 'house_alias', 'landlord', 'content', )
        exclude = ('owner', 'images', 'review_id')
        
    title.widget.attrs.update({'placeholder': 'Review Title e.g Not a place fit for human'})
    street_name.widget.attrs.update({'placeholder': 'Address e.g No 57 Okemu street oworonsoki'})
    house_alias.widget.attrs.update({'placeholder': 'House Alias e.g Akindele house, Nikadel estate'})
    landlord.widget.attrs.update({'placeholder': 'Landlord Name: e.g Akindele ileeru'})
    location.widget.attrs.update({'class':'custom-select form-control mb-2 mr-sm-2'})
    state.widget.attrs.update({'class':'custom-select form-control mb-2 mr-sm-2'})
    image1.widget.attrs.update({'class': 'custom-file', 'accept':'image/*'})
    image2.widget.attrs.update({'class': 'custom-file', 'accept':'image/*'})
    image3.widget.attrs.update({'class': 'custom-file', 'accept':'image/*'})
    image4.widget.attrs.update({'class': 'custom-file', 'accept':'image/*'})