# from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from simple_salesforce import Salesforce
import config # holds confidential login infoo


# Create your views here.
def index(request):
	test = "Hello creator"
	template = loader.get_template('salesforce/index.html')
	query_contacts = get_salesforce_data()

	context = {
		'content': test,
		'contact_list': query_contacts['records'],
	}

	# return HttpResponse("Hello World!")
	return HttpResponse(template.render(context, request))

	#https://docs.djangoproject.com/en/1.9/intro/tutorial03/
	# should use render() and get_http_and_404

def get_salesforce_data():
	print "username " + config.username

	#login
	sf = Salesforce(
		username=config.username, 
		password=config.password,
		security_token=config.security_token
		)
	print "connected"

	return sf.query_all("SELECT id, FirstName, LastName, Email FROM Contact")
	

'''
OrderedDict(
	[(u'totalSize', 1), (u'done', True), 
		(u'records',
			[OrderedDict([
				(u'attributes', OrderedDict([
					(u'type', u'Contact'), (u'url',
u'/services/data/v29.0/sobjects/Contact/0033600000CaRlaAAF')]
					)), 
				(u'Id', u'0033600000CaRlaAAF'), 
				(u'FirstName', u'John')])
			])
	])

	to get first name
	name = query['records'][0]['firstName'] (inner ordereddict is a list)

	each item in query['records'] is a contact OBJECT (first name being an attr)


'''