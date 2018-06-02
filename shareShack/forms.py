from django import forms
from shareShack.models import Item

class DateInput(forms.DateInput):
    input_type = 'date'

class DonationForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['department', 'writtenId', 'name', 'donor',
        'condition' ]
        widgets = {
            'date_Added': DateInput()
        }

class CheckOutForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['due_Back', 'condition', 'checked_Out_To']
        help_texts = {
            'due_Back': 'Press X for returns',
            'condition': 'i.e. stain on side 10/12/18',
            'checked_Out_To': 'select "-----" for returns',
        }
        widgets = {
            'due_Back': DateInput()
        }
    '''
    class Meta:
        model = CheckOut
        fields = '__all__'
        help_texts = {'items': 'Hold down CTRL to select multiple',
        }
        widgets = {
            'dateIssued': DateInput(),
            'items': forms.SelectMultiple(attrs={'size':'15',
              'style': 'color:blue;width:175px'})
        }
    '''
