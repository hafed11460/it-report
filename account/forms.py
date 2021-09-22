
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from account.models import Account
from django.contrib.auth import get_user_model


# User Registration
class RegistrationForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ('email', 'first_name','last_name', 'password1', 'password2',)

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        try:
            account = Account.objects.get(email=email)
        except Exception as e:
            return email
        raise forms.ValidationError(f'Email {email} is already in use.')



# vendor Registration
class VendorRegistrationForm(UserCreationForm):

    class Meta:
        model = Account
        fields = ['email', 'first_name', 'last_name','password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            vendor = Account.objects.get(email=email)
        except Exception as e:
            return email
        raise forms.ValidationError(f'Email {email} is already in use.')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.account_type = 1
        if commit:
            user.save()
        return user


class BuyerRegistrationForm(UserCreationForm):

    class Meta:
        model = Account
        fields = ['email', 'first_name', 'last_name','password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            vendor = Account.objects.get(email=email)
        except Exception as e:
            return email
        raise forms.ValidationError(f'Email {email} is already in use.')

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.account_type = 2
        if commit:
            user.save()
        return user



class AccountAuthenticationForm(forms.ModelForm):

	# password = forms.CharField(label='Password', widget=forms.PasswordInput)

	class Meta:
		model = Account
		fields = ('email', 'password')

	def clean(self):
		if self.is_valid():
			email = self.cleaned_data['email']
			password = self.cleaned_data['password']
			if not authenticate(email=email, password=password):
				raise forms.ValidationError("Invalid login")
