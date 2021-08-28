from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm

from records.models import GoUser, GoCustomerRegistration


# from .models import File


class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label="Password", max_length=20,
                                widget=forms.PasswordInput(
                                    attrs={"class": 'form-control form-control-user'
                                           }
                                )
                                )
    password2 = forms.CharField(label="Confirm Password", max_length=20,
                                widget=forms.PasswordInput(
                                    attrs={"class": 'form-control form-control-user'
                                           }
                                )
                                )

    class Meta:
        model = GoUser
        fields = ('username', 'name', 'email', 'phone', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
            'name': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
            'email': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
            'phone': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
        }


class UserLoginForm(forms.ModelForm):
    password = forms.CharField(label='password', widget=forms.PasswordInput(
        attrs={"class": 'form-control form-control-user'}
    ))
    username = forms.CharField(label='username', widget=forms.TextInput(
        attrs={"class": 'form-control form-control-user'}
    ))

    class Meta:
        model = GoUser
        fields = ('username', 'password')

    def clean(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            password = self.cleaned_data["password"]

            if not authenticate(username=username, password=password):
                raise forms.ValidationError('Invalid Entries')


class GoCustomerRegistrationForm(forms.ModelForm):
    class Meta:
        model = GoCustomerRegistration
        fields = ('name', 'type', 'destination', 'age', 'photo', 'documents')
        TYPE_CHOICES = (
            ('', 'Select a customer type'),
            ('student', 'STUDENT'),
            ('worker', 'WORKER'),
            ('tourist', 'TOURIST'),)
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control w - 30 form-control-user',
                       'placeholder': 'Enter Customer\'s name', },
            ),
            'age': forms.TextInput(
                attrs={'class': 'form-control form-control-user',
                       'placeholder': 'What\'s his age'},
            ),
            'type': forms.Select(
                choices=TYPE_CHOICES,
                attrs={'class': 'form-control form-control-user',
                       'placeholder': 'Which type of Customer is he/she'},
            ),
            'destination': forms.TextInput(
                attrs={'class': 'form-control form-control-user',
                       'placeholder': 'What is his/her Destination'}
            ),
            'photo': forms.ClearableFileInput(
                attrs={'class': 'btn btn-primary d - block btn - user w - 100  m-lg-2',
                       'placeholder': 'Drop his/her` picture', },
            ),
            'documents': forms.ClearableFileInput(
                attrs={'multiple': True, 'class': ' mb-lg-2 btn btn-primary  m-lg-2'
                                                  ' d - block btn - user w - 100',
                       'placeholder': 'Drop his files at once here'},
            ),
        }
