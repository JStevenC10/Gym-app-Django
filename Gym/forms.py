from datetime import datetime, timedelta

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
        exclude = ('start_date', 'finish_date', 'status', 'check_in')
    
    # METHOD SAVE FOR ALTER DATES OF CLIENT
    def save(self, commit=True):
        client = super().save(commit=False)
        if client.payed:
            client.start_date = datetime.today().date()
            client.finish_date = client.start_date + timedelta(days=31)
        else:
            client.start_date = None
            client.finish_date = None
        client.save()
        return client