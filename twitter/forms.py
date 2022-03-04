from django.forms import ModelForm
from .models import posts


class renew(ModelForm):
    class Meta:
        model = posts
        fields=['content']