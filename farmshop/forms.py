from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NewUserForm(UserCreationForm):
    # fname = forms.CharField(label="First name", required=True),
    # lname = forms.CharField(label="Last name", required=True),
    email = forms.EmailField(required=True)


class Meta:
	model = User
	fields = ("username", "email", "password1", "password2")


def save(self, commit=True):
	user = super(NewUserForm, self).save(commit=False)
	user.email = self.cleaned_data['email']
	# user.fname = self.cleaned_data['fname']
	# user.lname = self.cleaned_data['lname']
	if commit:
		user.save()
	return user
