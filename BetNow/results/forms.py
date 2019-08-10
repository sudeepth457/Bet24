from django import forms
from .models import resultsection


class resultform(forms.ModelForm):
    class Meta:
        model = resultsection
        fields = (
            'match',
            'team',
        )

