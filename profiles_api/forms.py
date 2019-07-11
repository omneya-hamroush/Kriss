from django import forms


class UserMessageForm(forms.Form):
    subject=forms.TextField(max_length=3000)
