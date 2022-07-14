from django.forms import ModelForm
from .models import Messaging

class MessagingForm(ModelForm):
  class Meta:
    model = Messaging
    fields = ['date', 'message']
    