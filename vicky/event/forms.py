from django import forms

class ChangeUsernamePasswordForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput(), required=True)
    new_username = forms.CharField(max_length=100, required=True)
    new_password = forms.CharField(widget=forms.PasswordInput(), required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput(), required=True)
