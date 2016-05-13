# from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader

from collections import OrderedDict

from simple_salesforce import Salesforce
from .forms import SearchForm

import os

def index(request):
	form = SearchForm
	context = {}
	
	if request.method == 'POST':
		form = SearchForm(request.POST)

		if form.is_valid():
			form_fields = OrderedDict()
			form_fields['Department'] = form.cleaned_data['dept_name']
			form_fields['Account'] = form.cleaned_data['account_name']
			form_fields['MailingCity'] = form.cleaned_data['city_name']
			form_fields['MailingCountry'] = form.cleaned_data['country_name']
			form_fields['FirstName'] = form.cleaned_data['first_name']
			form_fields['LastName'] = form.cleaned_data['last_name']

			(is_logged_in, sf_conn) = salesforce_login()
			if is_logged_in:
				query_result = query_salesforce(form_fields, sf_conn)
				if query_result and query_result['totalSize'] > 0:  
					context['contact_list'] = parse_query_result(query_result)
				else: 
					context['error_msg'] = "No results were returned."
			else:
				context['error_msg'] = "Cannot login." 

	context['form'] = form
	return render(request, 'salesforce/index.html', context)

def query_salesforce(form_fields, sf_conn):

	if sf_conn:
		query_select = "Id, Name, Phone, Email, Account.Name"
		query_from = 'Contact'
		query_where = ''
		for key, value in form_fields.items():
			if value:

				if query_where:
					query_where += " AND "

				if key == 'Account':
					query_where += 'Account.Name LIKE \'' + value + '%\''
				else:
					query_where = query_where + key + \
								' LIKE \'' + value + '%\''

		query = "SELECT " + query_select + \
			" FROM " + query_from + \
			" WHERE " + query_where 

		query_result = {}
		try:
			query_result = sf_conn.query_all(query)
		except: 
			print "Salesforce query error."	
		finally:
			return query_result
	else:
		return

def salesforce_login():
	loginInfo = ()
	try: 
		sf = Salesforce(
			username=os.environ['SF_USERNAME'],
			password=os.environ['SF_PASSWORD'],
			security_token=os.environ['SF_SECURITYTOKEN'],
			)
		loginInfo = (True, sf)
	# exception SalesforceAuthenticationFailed doesn't work, need to use wildcard
	except: 
		print "Salesforce login error. Cannot login."
		loginInfo = (False, None)
		raise 
	finally:
		return loginInfo

def parse_query_result(query_result):
	contact_list = []
	if query_result['totalSize'] > 0:
		for obj in query_result['records']:
			contact = OrderedDict()
			contact['Id'] = obj['Id']
			contact['Name'] = obj['Name']
			contact['Email'] = obj['Email']
			contact['AccountName'] = obj['Account']['Name']
			contact_list.append(contact)
		return contact_list
	else: 
		return
