from django import forms 


class WishForm(forms.Form):
    wish = forms.CharField(required=True)
    link = forms.URLField(required=False)
    price = forms.FloatField(min_value=0, required=False)

