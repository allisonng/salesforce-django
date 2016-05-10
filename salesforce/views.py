# from django.shortcuts import render
from django.shortcuts import render
from .forms import ContactForm, SearchForm

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from simple_salesforce import Salesforce

from collections import OrderedDict
import config # holds confidential login infoo


# Create your views here.
def index(request):
	# query_contacts = query_salesforce()
	form_class = SearchForm

	context = {
		'form': form_class,
	}

	# TODO show errors if not valid
	# show error messages
	if request.method == 'POST':
		print "IN POST METHOD"
		form = form_class(request.POST)

		if form.is_valid():
			print "form is valid!"

			form_fields = OrderedDict()
			print "dept name" + form.cleaned_data['dept_name']
			form_fields['Department'] = form.cleaned_data['dept_name']
			form_fields['Account'] = form.cleaned_data['account_name']
			form_fields['MailingCity'] = form.cleaned_data['city_name']
			form_fields['MailingCountry'] = form.cleaned_data['country_name']
			form_fields['FirstName'] = form.cleaned_data['first_name']
			form_fields['LastName'] = form.cleaned_data['last_name']


			# print "filters chosen:"
			# print 'Department ' + form_fields['Department']
			# print 'Account: ' + form_fields['Account'] 
			# print 'MailingCity: ' + form_fields['MailingCity']
			# print 'MailingCountry ' + form_fields['MailingCountry']
			# print 'FirstName ' + form_fields['FirstName']
			# print 'LastName ' + form_fields['LastName']

			query_result = query_salesforce(form_fields)
			contact_list = []
			if query_result['totalSize'] > 0: 
				context['contact_list'] = parse_query_result(query_result)
				print 'contact list ', context['contact_list']
			else: 
				context['no_query_result_msg'] = "No results were returned."


		else:
			print "ERRORS in form: "
			print form.errors
	return render(request, 'salesforce/index.html', context)

	#https://docs.djangoproject.com/en/1.9/intro/tutorial03/
	# should use render() and get_http_and_404

def query_salesforce(form_fields):
	# sf being the salesforce connection
	(isLoggedIn, sf) = salesforce_login()

	if isLoggedIn:
		print "Grabbing salesforce data"
		query_select = "Id, Name, Email, Account.Name"
		query_from = 'Contact'
		query_where = ''
		for key, value in form_fields.items():
			# print '\nkey ' + key + ' value ' + value
			if value:
				#if query_where already has value in it

				if query_where:
					query_where += " AND "

				if key == 'Account':
					query_where += 'Account.Name=\'' + value + '\''
				else:
					query_where = query_where + key + \
								'=\'' + value + '\''
		print "query where" + query_where

		query = "SELECT " + query_select + \
			" FROM " + query_from + \
			" WHERE " + query_where 
		print 'query is:\n' + query

		query_result = sf.query_all(query)
		print "query result: ", query_result
		return query_result

def salesforce_login():
	try: 
		sf = Salesforce(
			username=config.username, 
			password=config.password,
			security_token=config.security_token
			)
		print "\nLogged in\n"
		return (True, sf)
	# exception SalesforceAuthenticationFailed doesn't work, need to use wildcard
	except: 
		print "\nError logging into Salesforce\n"

def parse_query_result(query_result):
	contact_list = []
	if query_result['totalSize'] > 0:
		for obj in query_result['records']:
			contact = OrderedDict()
			contact['Id'] = obj['Id']
			contact['Name'] = obj['Name']
			contact['Email'] = obj['Email']
			contact['AccountName'] = obj['Account']['Name']
			print "\ncontact: ", contact
			contact_list.append(contact)
		return contact_list
	else:
		return False


'''

	To get First name of first contact:
	name = query['records'][0]['firstName'] (inner ordereddict is a list)
	[0] being first contact in list
	[1] being 2nd...

	each item in query['records'] is a contact dict (first name being an attr)

	OrderedDict(
	[(u'totalSize', 2),
	(u'done', True),
	(u'records', [OrderedDict([
		(u'attributes', OrderedDict([(u'type', u'Contact'), (u'url', u'/services/data/v29.0/sobjects/Contact/0033600000DAcYGAA1')])), 
		(u'Id', u'0033600000DAcYGAA1'), 
		(u'Name', u'Olivia Wilde'), 
		(u'Email', u'oliviawilde@eagames.ca'), 
		(u'Account', OrderedDict([(u'attributes', OrderedDict([(u'type', u'Account'), (u'url', u'/services/data/v29.0/sobjects/Account/0013600000JDa19AAD')])), (u'Name', u'EA Games')])
	  	)]), 
		OrderedDict([
			(u'attributes', OrderedDict([(u'type', u'Contact'), (u'url', u'/services/data/v29.0/sobjects/Contact/0033600000CaRlaAAF')])), 
			(u'Id', u'0033600000CaRlaAAF'), 
			(u'Name', u'John Smith'), 
			(u'Email', u'jonsthebomb@gmail.com'), 
			(u'Account', OrderedDict([(u'attributes', OrderedDict([(u'type', u'Account'), (u'url', u'/services/data/v29.0/sobjects/Account/0013600000JDa19AAD')])), (u'Name', u'EA Games')]))])
		]
	)]

	)


'''