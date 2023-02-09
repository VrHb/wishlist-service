from django import forms 


class WishlistForm(forms.Form):
    wishlist = forms.CharField(max_length=150)

class WishForm(forms.Form):
    wish = forms.CharField(required=True, max_length=100)
    link = forms.URLField(required=False)
    price = forms.FloatField(min_value=0, required=False)

