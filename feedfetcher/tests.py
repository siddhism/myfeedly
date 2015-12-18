from django.test import TestCase

# Create your tests here.
class MyTest(TestCase):
	def firstTest(self):
		self.assertEqual( 1+2, 3)