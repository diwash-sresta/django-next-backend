from django import forms
from .models import WaitlistEntry
from django.utils import timezone

class WaitlistEntryCreateForm(forms.ModelForm):
  #email = forms.EmailField()
  class Meta:
    model = WaitlistEntry
    fields = ['email']

  def clean_email(self):
    email = self.cleaned_data.get("email")
    today = timezone.now().day
    qs = WaitlistEntry.objects.filter(
      email=email,
      timestamp__day = today
    )
    if qs.count() >=5:
      raise forms.ValidationError("Cannot enter this email again today.")
    # if email.endswith('@gmail.com'):
    #   raise forms.ValidationError('Cannot use gmail')
    return email