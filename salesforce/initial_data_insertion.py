# insert data that will later be pulled :)

from simple_salesforce import Salesforce
import config

sf = Salesforce(
	username=config.username, 
	password=config.password,
	security_token=config.security_token
	)

# create some mock contacts broh
'''
sf.Contact.create({
	'LastName':'Smith',
	'FirstName':'John',
	'Email':'jonsthebomb@gmail.com'
	})

sf.Contact.create({
	'LastName':'Bob',
	'FirstName':'Jim',
	'Email':'jim@bobs.com'
	})

sf.Contact.create({
	'LastName':'Fenix',
	'FirstName':'Marcus',
	'Email':'MarcusFenix@gearsofwar.com'
	})

'''