from django.test import TestCase, Client
from forms import SearchForm

from django_webtest import WebTest

class SearchFormTestCase(TestCase):

	# basic test ideas
	# that form does not submit if all fields empty
	# that form is able to login
	# that form is able to query if logged in
	# that form queries if one field given

	def test_init_without_entry(self):
		# should not be a valid test if empty fields
		form = SearchForm()

		self.assertFalse(form.is_valid())

	def test_valid_data(self):
		# valid data is at least 1 input is given

		form = SearchForm({
			'dept_name' : 'Admin'
			})

		self.assertTrue(form.is_valid())
	
	def test_valid_login(self):
		form = SearchForm({
			'dept_name' : 'Admin'
			})

		form.submit()

		response = self.client.get('/')
		self.assertEquals(response.status_code, 200)

		# check that you can login
		# should also return "Administration" to ensure query works

