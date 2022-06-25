from django import forms

from adverts.models import Adverts


class AdvertsForm(forms.ModelForm):

    class Meta:
        model = Adverts
        fields = ['title', ]


class SearchForm(forms.Form):
    search = forms.CharField(
        max_length=30,
        required=False,
        label='Найти',
        widget=forms.TextInput(
            attrs={'class': 'search_field'}
        )
    )
