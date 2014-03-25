from django.forms import ModelForm
from .models import Contact, Post
# for registeration
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ContactForm(ModelForm):
    class Meta:
        model = Contact

class MyRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(MyRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields =('title', 'body', 'published', 'thumbnail')