from django import forms
from .models import Email, Projects, Other, Certification, Blog, User
from django.contrib.auth.forms import AuthenticationForm

class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ['sender', 'subject', 'message', 'date']

    # You can customize the form widgets or add validation if needed
    widgets = {
        'message': forms.Textarea(attrs={'rows': 4}),
        'date': forms.DateInput(attrs={'type': 'date'}),
    }

class ProjectsForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ['name', 'image', 'coding', 'details', 'category']

class OtherForm(forms.ModelForm):
    class Meta:
        model = Other
        fields = ['name', 'image', 'details', 'category']

class CertificationForm(forms.ModelForm):
    class Meta:
        model = Certification
        fields = ['name', 'Institution', 'certificate', 'syllabus']

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['name', 'date', 'article', 'signed', 'category']

 
class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)