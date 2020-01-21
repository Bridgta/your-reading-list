from django.forms import ModelForm
from .models import Read

class ReadForm(ModelForm):
    class Meta:
        model = Read
        fields = ['date', 'chapter']