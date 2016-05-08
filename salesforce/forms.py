from django import forms

# our new form
class SearchForm(forms.Form):
	contact_name = forms.CharField(label="name here", required=True)

class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(
        required=True,
        widget=forms.Textarea
    )