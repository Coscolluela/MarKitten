from ast import Pass
from tkinter import DISABLED
from django.forms import ModelForm, TextInput, PasswordInput, CharField, EmailInput, HiddenInput, NumberInput, widgets
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, PasswordResetForm

from django.contrib.auth.models import User
from .models import *
from django import forms

class UserForm(UserCreationForm):
    attrs = { 'class' : 'form-control', 'id' : 'floating-input', 'placeholder' : 'Enter Password', 'required' : True ,}
    password1 = CharField(widget=PasswordInput(attrs=attrs))
    password2 = CharField(widget=PasswordInput(attrs=attrs))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        widgets = {
            'first_name' : TextInput(attrs = { 'class' : 'form-control', 'id' : 'floating-input', 'placeholder' : 'Enter First Name', 'required' : True ,}),
            'last_name' : TextInput(attrs = { 'class' : 'form-control', 'id' : 'floating-input', 'placeholder' : 'Enter Last Name', 'required' : True ,}),
            'username' : TextInput(attrs = { 'class' : 'form-control', 'id' : 'floating-input', 'name' : 'username', 'placeholder' : 'Enter Username', 'required' : True ,}),
            'email' : TextInput(attrs = { 'type' : 'email' , 'class' : 'form-control', 'id' : 'floating-input', 'name' : 'email', 'placeholder' : 'Enter Email', 'required' : True ,})
            }

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']
        widgets = {
            'first_name' : TextInput(attrs = { 'class' : 'form-control', 'id' : 'floating-input', 'placeholder' : 'Enter First Name', 'required' : True ,}),
            'last_name' : TextInput(attrs = { 'class' : 'form-control', 'id' : 'floating-input', 'placeholder' : 'Enter Last Name', 'required' : True ,}),
            'username' : TextInput(attrs = { 'class' : 'form-control', 'id' : 'floating-input', 'name' : 'username', 'placeholder' : 'Enter Username', 'required' : True ,}),
            'email' : TextInput(attrs = { 'type' : 'email' , 'class' : 'form-control', 'id' : 'floating-input', 'name' : 'email', 'placeholder' : 'Enter Email', 'required' : True ,})
            }

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'sex', 'birthday', 'nationality', 'citizenship', 'office_email', 'personal_email',
                'present_address', 'billing_address', 'permanent_address','shopping_address', 'office_address',
                'mobile_number', 'landline_number', 'office_number', 'is_subscribed']
        widgets = {
            'sex' : TextInput(attrs = { 'class' : 'form-control', 'id' : 'floating-input', 'placeholder' : 'Male/Female', 'required' : True ,}),
            'birthday' : TextInput(attrs = { 'class' : 'form-control', 'id' : 'floating-input', 'placeholder' : 'Birthday', 'required' : True ,}),
            'nationality' : TextInput(attrs = { 'class' : 'form-control', 'id' : 'floating-input', 'name' : 'nationality', 'placeholder' : 'Filipino', 'required' : True ,}),
            'citizenship' : TextInput(attrs = { 'class' : 'form-control', 'id' : 'floating-input', 'name' : 'citizenship', 'placeholder' : 'Filipino', 'required' : True ,}),
            'personal_email' : TextInput(attrs = { 'class' : 'form-control', 'id' : 'floating-input', 'name' : 'personal_email', 'placeholder' : 'abcd@gmail.com', 'required' : True ,}),
            'office_email' : TextInput(attrs = { 'class' : 'form-control', 'id' : 'floating-input', 'name' : 'office_email', 'placeholder' : 'abcd@gmail.com', 'required' : True ,}),
            'present_address' : TextInput(attrs = { 'class' : 'form-control', 'id' : 'floating-input', 'name' : 'present_address', 'placeholder' : 'Address', 'required' : True ,}),
            'billing_address' : TextInput(attrs = { 'class' : 'form-control', 'id' : 'floating-input', 'name' : 'billing_address', 'placeholder' : 'Address', 'required' : True ,}),
            'permanent_address' : TextInput(attrs = { 'class' : 'form-control', 'id' : 'floating-input', 'name' : 'permanent_address', 'placeholder' : 'Address',}),
            'shopping_address' : TextInput(attrs = { 'class' : 'form-control', 'id' : 'floating-input', 'name' : 'shopping_address', 'placeholder' : 'Address', 'required' : True ,}),
            'office_address' : TextInput(attrs = { 'class' : 'form-control', 'id' : 'floating-input', 'name' : 'office_address', 'placeholder' : 'Address', 'required' : True ,}),
            'mobile_number' : TextInput(attrs = { 'class' : 'form-control', 'id' : 'floating-input', 'name' : 'mobile_number', 'placeholder' : 'Number', 'required' : True ,}),
            'landline_number' : TextInput(attrs = { 'class' : 'form-control', 'id' : 'floating-input', 'name' : 'landline_number', 'placeholder' : 'Number', 'required' : True ,}),
            'office_number' : TextInput(attrs = { 'class' : 'form-control', 'id' : 'floating-input', 'name' : 'office_number', 'placeholder' : 'Number', 'required' : True ,})
            }
class MyPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        attrs = { 'class' : 'form-control', 'id' : 'floating-input', 'required' : True ,}
        
        for fieldname in ['old_password', 'new_password1', 'new_password2']:
            self.fields[fieldname].widget=PasswordInput(attrs=attrs)

class MyPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        attrs = { 'class' : 'form-control', 'id' : 'floating-input', 'required' : True ,}
        
        for fieldname in ['email']:
            self.fields[fieldname].widget=EmailInput(attrs=attrs)
            
class MyPasswordSentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        attrs = { 'class' : 'form-control', 'id' : 'floating-input', 'required' : True ,}
        
        for fieldname in ['new_password1', 'new_password2']:
            self.fields[fieldname].widget=PasswordInput(attrs=attrs)
      
