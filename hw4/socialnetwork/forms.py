from django import forms



from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class LoginForm(forms.Form):
    # may need to be named as id_username
    
    username = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'id': 'id_username'}))
    password = forms.CharField(max_length=200, widget = forms.PasswordInput())

    def clean(self):
        
        cleaned_data = super().clean()
        
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")
        user = authenticate(username = username, password = password)
        if not user:
            raise forms.ValidationError("Invalid username/password")
        return cleaned_data

class RegisterForm(forms.Form):
    username   = forms.CharField(max_length=20)
    password  = forms.CharField(max_length=200, label = 'Password', widget=forms.PasswordInput())
    confirm_password  = forms.CharField(max_length=200, label = 'Confirm', widget=forms.PasswordInput())
    email      = forms.CharField(max_length=50, widget=forms.EmailInput())
    first_name = forms.CharField(max_length=20)
    last_name  = forms.CharField(max_length=20)

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password1 = cleaned_data.get('password')
        password2 = cleaned_data.get('confirm_password')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Password did not match.")
        return cleaned_data

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username__exact = username):
            raise forms.ValidationError("username is already taken.")

        return username



class EditForm(forms.Form):
    username   = forms.CharField(max_length=20)
    last_name  = forms.CharField(max_length=20)
    first_name = forms.CharField(max_length=20)
    email      = forms.CharField(max_length=50, widget=forms.EmailInput())







