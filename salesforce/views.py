# from django.shortcuts import render
from django.shortcuts import render
from .forms import ContactForm, SearchForm

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from simple_salesforce import Salesforce
import config # holds confidential login infoo


# Create your views here.
def index(request):
	# query_contacts = get_salesforce_data()
	form_class = SearchForm
	test = "Hello creator"

	context = {
		'content': test,
		'form': form_class,
		# 'contact_list': query_contacts['records'],
	}

	# TODO show errors if not valid
	# show error messages
	if request.method == 'POST':
		print "IN POST METHOD"
		form = form_class(request.POST)

		if form.is_valid():
			print "form is valid!"
			context['filters'] = request.POST.get('filters')
			context['name'] = request.POST.get('name')
			print "filters chosen:"
			print request.POST.getlist('filters')

			return HttpResponseRedirect('/')
		else:
			print "errors: "
			print form.errors
	# return HttpResponse("Hello World!")
	# return HttpResponse(template.render(context, request))
	return render(request, 'salesforce/index.html', context)

	#https://docs.djangoproject.com/en/1.9/intro/tutorial03/
	# should use render() and get_http_and_404

def contact(request):
    form_class = ContactForm

    print "Trying to login"
    (isLoggedIn, sf) = salesforce_login()
    if isLoggedIn:
    	print "hurrah logged in check passes"
    
    return render(request, 'salesforce/contact.html', {
        'form': form_class,
    })

def salesforce_login(filters):
	try: 
		sf = Salesforce(
			username=config.username, 
			# password=config.password,
			password=config.username,
			security_token=config.security_token
			)
		print "\nLogged in\n"
		return (True, sf)
	# except SalesforceAuthenticationFailed: 
	# 	print "Error logging into Salesforce"
	# exception SalesforceAuthenticationFailed doesn't work, need to use wildcard
	except: 
		print "\nError logging into Salesforce\n"


def get_salesforce_data(filters):
	# need filter and name of filters 
	print "username " + config.username

	#

	print "connected"
	query_select = "id, FirstName, LastName, Email"
	query_from = 'Contact'
	query_where = 
	for filter in filters:
		if filter = 
	query = "SELECT " + query_select + \
		" FROM " + query_from + \
		" WHERE " + query_where 
	print 'query is:\n' + query

	# return sf.query_all("SELECT id, FirstName, LastName, Email FROM Contact")
	

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