from django import forms
from .models import Sport

SPORTS_LIST = (
    ('select', '-- SELECT SPORT (Hold Ctrl key to select multiple items) --'),
    ('cricket', 'CRICKET'),
    ('rugby', 'RUGBY'),
    ('tennis', 'TENNIS'),
    ('football', 'FOOTBALL'),
    ('running', 'RUNNING'),
)


class SportInsertForm(forms.ModelForm):
    sportnames = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'readonly': True
        }
    ))

    class Meta:
        model = Sport
        fields = '__all__'
        widgets = {
            'name': forms.SelectMultiple(
                attrs={
                    'class': 'custom-select',
                    'size': 7,
                },
                choices=SPORTS_LIST
            )
        }
