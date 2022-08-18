from django import forms
from accounts.models import CustomUser
from accounts.forms import CustomUserCreationForm

# Sign Up Form
class SignUpForm(CustomUserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')

    class Meta:
        model = CustomUser
        fields = [
            'username', 
            'email', 
            'password1', 
            'password2', 
            ]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None
        self.fields['email'].help_text = None
        self.fields['username'].help_text = None