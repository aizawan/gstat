from django.forms import ModelForm
from cms.models import Resource


class ResourceForm(ModelForm):
    class Meta:
        model = Resource
        fields = ("hostname", 'is_available', 'locking_user')

    def clean_locking_user(self):
        is_available = self.cleaned_data['is_available']
        if is_available:
            locking_user = ''
        else:
            locking_user = self.cleaned_data['locking_user']
        return locking_user
