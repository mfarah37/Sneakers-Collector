from django.forms import ModelForm
from .models import Resale

class ResaleForm(ModelForm):
  class Meta:
    model = Resale
    fields = ['date', 'price']