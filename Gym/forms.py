from django import forms

from .models import ClientGym

# SEE CLIENT GYM FORM
class LoginForm(forms.ModelForm):
    class Meta:
        model = ClientGym
        fields = ('cc',)

# REGISTER NEW CLIENT GYM
class ClientGymForm(forms.ModelForm):
    class Meta:
        model = ClientGym
        exclude = ('start_date', 'finish_date')

