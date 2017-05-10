from django import forms


FILTER_CHOICES = (
    ("all", "All"),
    ("person", "Person"),
    ("title", "Title"),
    ("company", "Company"),
    ("industry", "Industry"),
    ("geography", "Geography"),
)


class SearchForm(forms.Form):
    search_filter = forms.CharField(max_length=20, widget=forms.Select(choices=FILTER_CHOICES, attrs={'class':"selectpicker"}), label='')
    search_text = forms.CharField(max_length=1000,error_messages=None, label='')


