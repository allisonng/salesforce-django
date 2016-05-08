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

	template = loader.get_template('salesforce/index.html')
	context = {
		'content': test,
		'form': form_class,
		# 'contact_list': query_contacts['records'],
	}

	if request.method == 'GET':
		print "IN GET METHOD"
		form = form_class(data=request.GET)

		if form.is_valid():
			name = request.GET.get('contact_name')
			context['contact_name'] = name

	# return HttpResponse("Hello World!")
	# return HttpResponse(template.render(context, request))
	return render(request, 'salesforce/index.html', context)

	#https://docs.djangoproject.com/en/1.9/intro/tutorial03/
	# should use render() and get_http_and_404

def contact(request):
    form_class = ContactForm
    
    return render(request, 'salesforce/contact.html', {
        'form': form_class,
    })

def get_name(request):
	if request.method =='POST':
		form = NameForm(request.POST)
		if form.is_valid():
			return HttpResponseDirect('/thanks/')

	else: 
		form = NameForm()

	return render(request, 'salesforce/index.html', {'form': form})

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