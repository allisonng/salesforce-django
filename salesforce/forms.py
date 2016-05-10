from django import forms
from collections import OrderedDict

# our new form
class SearchForm(forms.Form):
	# DEPARTMENT = 'DEPT'
	# Account = 'ACCT'
	# WAREHOUSE = 'WRHS'
	# GAME = 'GAME'
	# FINANCE = 'FINA'
	# ADMINISTRATION = 'ADMN'

	field_choices = OrderedDict()
	field_choices['Department'] = 'Department'
	field_choices['Account'] = 'Account'
	field_choices['MailingCity'] = 'Mailing City'
	field_choices['MailingCountry'] = 'Mailing Country'
	field_choices['FirstName'] = 'First Name'
	field_choices['LastName'] = "Last Name"


	# FILTER_CHOICES = [
	# 	(Department, 'Department'),
	# 	(Account, 'Account'),
	# 	(MailingCity, 'City'),
	# 	(MAILING_COUNTRY, 'Country'),
	# 	(FirstName, 'First Name'),
	# 	(LastName, 'Last Name'),
	# 	]
	
	# filters = forms.MultipleChoiceField(label='Choose what to filter by', 
	# 									choices=FILTER_CHOICES, 
	# 									widget=forms.CheckboxSelectMultiple,
	# 									required=True)
	
	dept_name = forms.CharField(label=field_choices['Department'], 
							max_length=100,
 							required=False,
 							)
	account_name = forms.CharField(label=field_choices['Account'],
							max_length=100,
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
							max_length=100,
 							required=False,
 							)
	last_name = forms.CharField(label=field_choices['LastName'], 
							max_length=100,
 							required=False,
 							)	

	# TODO 
	# http://stackoverflow.com/questions/25457695/django-must-have-at-least-one-form-field-filled-in
	'''
	def clean_filters(self):
		if len(self.cleaned_data['filters']) < 1:
			raise forms.ValidationError('Please select at least 1')
		return self.cleaned_data['filters']
	'''

class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(
        required=True,
        widget=forms.Textarea
    )