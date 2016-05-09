from django import forms

# our new form
class SearchForm(forms.Form):
	# DEPARTMENT = 'DEPT'
	# ACCOUNT = 'ACCT'
	# WAREHOUSE = 'WRHS'
	# GAME = 'GAME'
	# FINANCE = 'FINA'
	# ADMINISTRATION = 'ADMN'

	DEPARTMENT = 'Department'
	ACCOUNT = 'Account'
	MAILING_CITY = 'Mailing_City'
	MAILING_COUNTRY = 'Mailing_Country'
	FIRST_NAME = 'First_Name'
	LAST_NAME = "Last_Name"

 
	FILTER_CHOICES = [
		(DEPARTMENT, 'Department'),
		(ACCOUNT, 'Account'),
		(MAILING_CITY, 'City'),
		(MAILING_COUNTRY, 'Country'),
		(FIRST_NAME, 'First Name'),
		(LAST_NAME, 'Last Name'),
		]
	
	filters = forms.MultipleChoiceField(label='Choose what to filter by', 
										choices=FILTER_CHOICES, 
										widget=forms.CheckboxSelectMultiple,
										required=True)
	
	name = forms.CharField(label='Name of filter (e.g. Department: \'Marketing\')', 
							max_length=100,
 							required=True,
 							initial='')

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