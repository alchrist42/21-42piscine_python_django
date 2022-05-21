from django import forms


class HistoryForm(forms.Form):
    data = forms.CharField(label='data', min_length=1)