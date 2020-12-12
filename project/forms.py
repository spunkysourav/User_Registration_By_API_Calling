from django import forms
from django.contrib.auth.forms import UserCreationForm, User

class SignUpForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username', 'first_name', 'last_name', 'email']
class UserForm(forms.Form):
    id=forms.IntegerField(label='User Id')
    name = forms.CharField(label='Name')
    college_name = forms.CharField(label='College Name')
    branch = forms.CharField(label='Branch')
    address = forms.CharField(label='Address', widget=forms.Textarea)
    mobile_no = forms.CharField(label='Mobile No')
