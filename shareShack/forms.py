from django import forms
from shareShack.models import Item

class DateInput(forms.DateInput):
    input_type = 'date'

class DonationForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['department', 'writtenId', 'name', 'donor', 'date_Added',
        'condition' ]
        widgets = {
            'date_Added': DateInput()
        }
