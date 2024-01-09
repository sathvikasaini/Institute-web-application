from django import views
from django import forms
from django.contrib.auth.models import User
from .models import CommentData

class RegistrationForm(forms.ModelForm):
    first_name=forms.CharField(label="Enter First Name",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'firstname'}))
    last_name=forms.CharField(label="Enter Last Name",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'lastname'}))
    username=forms.CharField(label="Enter User Name",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}))
    email=forms.EmailField(label="Enter your email",widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}))
    password=forms.CharField(label="Enter password",widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'password'}))
    class Meta:
        model=User
        fields=('first_name','last_name','username','email','password')

class CommentForm(forms.ModelForm):
    content=forms.CharField(
       label="",
       widget=forms.Textarea(
          attrs={
            'class':'form-control',
            'placeholder':'Give your Feedback and any suggestions',
            'cols':10,
            'rows':10
          }
       )
    )
    class Meta:
        model=CommentData
        fields=('content',)

class ContactForm(forms.Form):
    full_name=forms.CharField(
       label='full name',
       widget=forms.TextInput(
           attrs={
              'placeholder':'Full name...',
              'class':'form-control'
           }
        )
    )
    courses=forms.CharField(
       label='courses',
       widget=forms.TextInput(
           attrs={
              'class':'form-control',
              'placeholder':'Full name...'
           }
        )
    )
    email=forms.EmailField(
       label='email',
       widget=forms.EmailInput(
           attrs={
              'class':'form-control',
              'placeholder':'email...'
           }
        )
    )
    mobile=forms.IntegerField(
       label='mobile',
       widget=forms.NumberInput(
           attrs={
              'class':'form-control',
              'placeholder':'mobile'
           }
        )
    )
    location=forms.CharField(
       label='location',
       widget=forms.TextInput(
           attrs={
              'class':'form-control',
              'placeholder':'location'
           }
        )
    )
    referred_by=forms.CharField(
       label='referred by',
       widget=forms.TextInput(
           attrs={
              'class':'form-control',
              'placeholder':'referred by'
           }
        )
    )
