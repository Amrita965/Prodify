
from django import forms

class RegistrationForm(forms.Form):
    
    name = forms.CharField(
        label="Name",
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter Your Name'
            }
        )
    )
    email = forms.EmailField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Enter Your Email'
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Enter Your Password'
        }
    ))
