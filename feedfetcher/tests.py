from django.test import TestCase

# Create your tests here.
class MyTest(TestCase):
	def test_firstTest(self):
		self.assertEqual( 1+2, 3)

	def test_second(self):
		self.assertEqual(5-2, 3)