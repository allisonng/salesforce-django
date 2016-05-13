from django import forms
from collections import OrderedDict
import re

class SearchForm(forms.Form):

	field_choices = OrderedDict()
	field_choices['Department'] = 'Department'
	field_choices['Account'] = 'Account'
	field_choices['MailingCity'] = 'Mailing City'
	field_choices['MailingCountry'] = 'Mailing Country'
	field_choices['FirstName'] = 'First Name'
	field_choices['LastName'] = "Last Name"

	
	dept_name = forms.CharField(label=field_choices['Department'], 
							max_length=100,
 							required=False,
 							)
	account_name = forms.CharField(label=field_choices['Account'],
							max_length=150,
 							required=False,
 							)
	city_name = forms.CharField(label=field_choices['MailingCity'],
							max_length=100,
							required=False,
							)
	country_name = forms.CharField(label=field_choices['MailingCountry'], 
							max_length=100,
 							required=False,
 							)
	first_name = forms.CharField(label=field_choices['FirstName'], 
							max_length=60,
 							required=False,
 							)
	last_name = forms.CharField(label=field_choices['LastName'], 
							max_length=60,
 							required=False,
 							)	

	def clean(self):
		isFormEmpty = True
		cleaned_data = super(SearchForm, self).clean()

		for field_value in cleaned_data.itervalues():
			if field_value:
				re.sub(r'([^\s\w]|_)+', '', field_value)
				# re.sub(r'[^a-zA-Z\s]+','', field_value)
				# re.sub(r'[\W_]+', '', field_value, flags=re.LOCALE)
				isFormEmpty = False
		if isFormEmpty:
			raise forms.ValidationError('You must input at least one value', code='invalid')
		return cleaned_data